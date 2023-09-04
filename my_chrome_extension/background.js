chrome.tabs.onUpdated.addListener((tabId, tab) => {
  console.log('Tab object:', tab);
  if (tab.url && tab.url.includes("youtube.com/watch")) {
    const queryParameters = tab.url.split("?")[1];
    const urlParameters = new URLSearchParams(queryParameters);

    chrome.tabs.sendMessage(tabId, {
      type: "NEW",
      videoLink: urlParameters.get("v"),
    }, (response) => {
      });
  }
});
