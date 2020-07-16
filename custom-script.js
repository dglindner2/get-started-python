window.watsonAssistantChatOptions = {
  integrationID: "", // The ID of this integration.
  region: "us-south", // The region your integration is hosted in.
  serviceInstanceID: "", // The ID of your service instance.
  onLoad: function (instance) {
    instance.render();
  },
};
setTimeout(function () {
  const t = document.createElement("script");
  t.src =
    "https://web-chat.global.assistant.watson.appdomain.cloud/loadWatsonAssistantChat.js";
  document.head.appendChild(t);
});
