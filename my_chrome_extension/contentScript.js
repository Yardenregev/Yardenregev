// import { fetchVideoId,  fetchBookmarks} from "./utils.js";
const serverUrl = "http://localhost:3000";

(() => {
  let youtubeLeftControls, youtubePlayer;
  let currentVideo = "";
  let currentVideoBookmarks = [];


  const fetchVideo = () => {
    return new Promise((resolve) => {
      console.log(currentVideo);
      let request = serverUrl + "/videos/" + currentVideo;
      console.log("sending requset:" + request);
      fetch(request).then(response => response.json())
      .then(videoData => {
        resolve(videoData)
      });
    });
  };

  const createNewVideo = () => {
    return new Promise((resolve) => {
    console.log("creating new video ", currentVideo);
    let requestBody = {
      video_link : currentVideo
    }
    console.log(requestBody);
    let request = serverUrl + "/videos/";
    fetch(request,{
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(requestBody)
    }).then(response => {
      if (!response.ok) {
        throw new Error('Request failed:', response.status, response.statusText);
      }
      return response.json();
    }).then(responseData => {
      console.log(responseData);
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
  }
  
  const fetchBookmarks = (videoId) => {
    return new Promise((resolve) => {
        request = serverUrl + "/bookmarks/" + videoId
        fetch(request).then(response => response.json()).then(videoBookMarksData => {
          console.log("video bookmark data received: ",videoBookMarksData);
          currentVideoBookmarks = videoBookMarksData
          resolve(currentVideoBookmarks)
        });
      });
  };

  const deleteBookmark = async (givenBookmarkTime) => {
    let currentVideoObj = await fetchVideo();
    let bookMarkToDelete = null;
    console.log("current video is " + currentVideoObj.video_id);
    currentVideoBookmarks = await fetchBookmarks(currentVideoObj.video_id);
    console.log("current video bookmarks are " + currentVideoBookmarks);

    for (let i = 0; i < currentVideoBookmarks.length; i++) {
      if (currentVideoBookmarks[i].bookmark_time == givenBookmarkTime){
        bookMarkToDelete = currentVideoBookmarks[i];
      }
    }
    if (bookMarkToDelete == null){
      return;
    }
    let request = serverUrl + "/bookmarks/" + bookMarkToDelete.bookmark_id;
    console.log(request);
    fetch(request, {
      method: "DELETE"
    }).then(response => {
      if (!response.ok) {
        throw new Error('Request failed:', response.status, response.statusText);
      }
      return response.json();
    }).then(responseData => {
      console.log(responseData);
    })
    .catch(error => {
      console.error('Error:', error);
    });

  }

  const addNewBookmarkEventHandler = async () => {
    let currentTime = youtubePlayer.currentTime;
    console.log("HERE")
    let currentVideoObj = await fetchVideo();
    if (currentVideoObj.video_id == undefined) {
      await createNewVideo();
      currentVideoObj = await fetchVideo();
    }
    console.log("current video is " + currentVideoObj.video_id +", "+ currentVideoObj.video_link)
    currentTime = getTime(currentTime);
    const newBookmark = {
      video_id: currentVideoObj.video_id,
      bookmark_time: currentTime,
      description: "Bookmark at " + currentTime,
    };
    currentVideoBookmarks = await fetchBookmarks(currentVideoObj.video_id);

    // Concatinate the bookmarks received from the database with the new bookmark and sort them
    // let newBookmarks = JSON.stringify([...currentVideoBookmarks, newBookmark].sort((a, b) => a.bookmark_time - b.bookmark_time))
    console.log(newBookmark);
    request_body = JSON.stringify(newBookmark);
    // Make a post request to change the bookmarks at the database
    request = serverUrl + "/bookmarks"
    fetch(request,{
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: request_body
    }).then(response => {
      if (!response.ok) {
        throw new Error('Request failed:', response.status, response.statusText);
      }
      return response.json();
    }).then(responseData => {
      console.log(responseData);
    })
    .catch(error => {
      console.error('Error:', error);
    });


  };

  const newVideoLoaded = async () => {
    const bookmarkBtnExists = document.getElementsByClassName("bookmark-btn")[0];
    let currentVideo = await fetchVideo();
    let currentVideoId = currentVideo.videoId;
    currentVideoBookmarks = await fetchBookmarks(currentVideoId);
    console.log("IM HERE")
    console.log(bookmarkBtnExists);

    if (bookmarkBtnExists == undefined) {
      const bookmarkBtn = document.createElement("img");

      bookmarkBtn.src = chrome.runtime.getURL("assets/bookmark.png");
      bookmarkBtn.className = "ytp-button " + "bookmark-btn";
      bookmarkBtn.title = "Click to bookmark current timestamp";

      youtubeLeftControls = document.getElementsByClassName("ytp-left-controls")[0];
      youtubePlayer = document.getElementsByClassName('video-stream')[0];

      youtubeLeftControls.appendChild(bookmarkBtn);
      bookmarkBtn.addEventListener("click", addNewBookmarkEventHandler);
    }
  };

  chrome.runtime.onMessage.addListener((obj, sender, response) => {
    const { type, value, videoLink } = obj;
    console.log("type, value, videoLink", type, value, videoLink);
    if (type === "NEW") {
      currentVideo = videoLink;
      newVideoLoaded();
    }
    else if (type === "PLAY"){
      youtubePlayer.currentTime = value;
    }
    else if (type === "DELETE"){
      deleteBookmark(value);
    }
  });

  // newVideoLoaded();
  
let trail="&ytExt=ON";
if(!window.location.href.includes(trail)&&!window.location.href.includes("ab_channel")
     && window.location.href.includes("youtube.com/watch")){
        window.location.href+=trail;
   }

})();

const getTime = t => {
  var date = new Date(0);
  date.setSeconds(t);

  return date.toISOString().substr(11, 8);
};
