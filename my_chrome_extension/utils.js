export async function getActiveTabURL() { // return the first tab
    const tabs = await chrome.tabs.query({
        currentWindow: true,
        active: true
    });
  
    return tabs[0];
}
// const serverUrl = "http://localhost:3000";

// export const fetchVideoId = (currentVideo) => {
//     return new Promise((resolve) => {
//       console.log(currentVideo);
//       let request = serverUrl + "/videos/" + currentVideo;
//       console.log("sending requset:" + request);
//       fetch(request).then(response => response.json())
//       .then(videoData => {
//         videoId = videoData.video_id;
//         response(videoId)
//       });
//     });
//   };
  
// export const fetchBookmarks = (videoId) => {
//     return new Promise((resolve) => {
//         request = serverUrl + "/bookmarks/" + videoId
//         fetch(request).then(response => response.json()).then(videoBookMarksData => {
//           console.log("video bookmark data received: ",videoBookMarksData);
//           currentVideoBookmarks = videoBookMarksData
//           response(currentVideoBookmarks)
//         });
//       });
//   };

