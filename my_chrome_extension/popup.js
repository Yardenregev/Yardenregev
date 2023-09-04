import { getActiveTabURL } from "./utils.js";
const serverUrl = "http://localhost:3000";


const fetchVideoId = (currentVideo) => {
  return new Promise((resolve) => {
    let request = serverUrl + "/videos/" + currentVideo;
    console.log("sending requset:" + request);
    fetch(request).then(response => response.json())
    .then(videoData => {
      console.log("popup.js got video data:", videoData);
      resolve(videoData.video_id);
    });
  });
};

const fetchBookmarks = (videoId) => {
  return new Promise((resolve) => {
      let request = serverUrl + "/bookmarks/" + videoId
      fetch(request).then(response => response.json()).then(videoBookMarksData => {
        console.log("popup.js video bookmark data received: ",videoBookMarksData);
        let currentVideoBookmarks = videoBookMarksData
        resolve(currentVideoBookmarks)
      });
    });
};

const addNewBookmark = (bookmarks, bookmark) => {
  const bookmarkTitleElement = document.createElement("div");
  const controlsElement = document.createElement("div");
  const newBookmarkElement = document.createElement("div");

  bookmarkTitleElement.textContent = bookmark.description;
  bookmarkTitleElement.className = "bookmark-title";
  controlsElement.className = "bookmark-controls";

  setBookmarkAttributes("play", onPlay, controlsElement);
  setBookmarkAttributes("delete", onDelete, controlsElement);

  newBookmarkElement.id = "bookmark-" + bookmark.bookmark_time;
  newBookmarkElement.className = "bookmark";
  newBookmarkElement.setAttribute("timestamp", bookmark.bookmark_time);

  newBookmarkElement.appendChild(bookmarkTitleElement);
  newBookmarkElement.appendChild(controlsElement);
  bookmarks.appendChild(newBookmarkElement);
};

const viewBookmarks = (currentBookmarks=[]) => {
  console.log("In viewBookmarks", currentBookmarks)
  const bookmarksElement = document.getElementById("bookmarks");
  bookmarksElement.innerHTML = "";

  if (currentBookmarks.length > 0) {
    for (let i = 0; i < currentBookmarks.length; i++) {
      const bookmark = currentBookmarks[i];
      addNewBookmark(bookmarksElement, bookmark);
    }
  } else {
    bookmarksElement.innerHTML = '<i class="row">No bookmarks to show</i>';
  }

  return;
};

const translateBookmarkTimeToSeconds = (bookmarkTime) => {
  const timeParts = bookmarkTime.split(':');
  const hours = parseInt(timeParts[0], 10);
  const minutes = parseInt(timeParts[1], 10);
  const seconds = parseInt(timeParts[2], 10);

  // Calculate the total time in seconds
  const bookmarkTimeInSeconds = hours * 3600 + minutes * 60 + seconds;

  return bookmarkTimeInSeconds;
}

const onPlay = async e => {
  const bookmarkTime = e.target.parentNode.parentNode.getAttribute("timestamp");
  const activeTab = await getActiveTabURL();
  const bookmarkTimeInSeconds = translateBookmarkTimeToSeconds(bookmarkTime);

  chrome.tabs.sendMessage(activeTab.id, {
    type: "PLAY",
    value: bookmarkTimeInSeconds,
  });
};

const onDelete = async e => {
  const activeTab = await getActiveTabURL();
  const bookmarkTime = e.target.parentNode.parentNode.getAttribute("timestamp");
  const bookmarkElementToDelete = document.getElementById(
    "bookmark-" + bookmarkTime
  );


  bookmarkElementToDelete.parentNode.removeChild(bookmarkElementToDelete);

  chrome.tabs.sendMessage(activeTab.id, {
    type: "DELETE",
    value: bookmarkTime,
  }, viewBookmarks);
};

const setBookmarkAttributes =  (src, eventListener, controlParentElement) => {
  const controlElement = document.createElement("img");

  controlElement.src = "assets/" + src + ".png";
  controlElement.title = src;
  controlElement.addEventListener("click", eventListener);
  controlParentElement.appendChild(controlElement);
};

document.addEventListener("DOMContentLoaded", async () => {
  const activeTab = await getActiveTabURL();
  const queryParameters = activeTab.url.split("?")[1];
  const urlParameters = new URLSearchParams(queryParameters);

  const currentVideo = urlParameters.get("v");

  if (activeTab.url.includes("youtube.com/watch") && currentVideo) {
    let videoId = await fetchVideoId(currentVideo);
    console.log("videoId: " + videoId);
    let currentVideoBookmarks = []
    if (videoId != undefined) {
       currentVideoBookmarks = await fetchBookmarks(videoId);
    }
    viewBookmarks(currentVideoBookmarks);

  } else {
    const container = document.getElementsByClassName("container")[0];

    container.innerHTML = '<div class="title">This is not a youtube video page.</div>';
  }
});

