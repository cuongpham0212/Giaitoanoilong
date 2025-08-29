(function () {
  function injectFixCss() {
    if (document.getElementById("nc-ltr-fix")) return;
    var css = `
      .nc-controlPane textarea, 
      .nc-controlPane input, 
      .public-DraftEditor-content, 
      .CodeMirror {
        direction: ltr !important;
        unicode-bidi: plaintext !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        caret-color: auto !important;
      }
    `;
    var style = document.createElement("style");
    style.id = "nc-ltr-fix";
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
  }

  function PostPreview(props) {
    var entry = props.entry;
    var title = entry.getIn(["data", "title"]) || "";
    var description = entry.getIn(["data", "description"]) || "";
    var body = props.widgetFor("body");

    return window.React.createElement(
      "div",
      { style: { fontFamily: "sans-serif", padding: "1rem" } },
      window.React.createElement("h1", null, title),
      description
        ? window.React.createElement("p", null, window.React.createElement("em", null, description))
        : null,
      body
    );
  }

  function registerTemplates() {
    injectFixCss();
    ["tamsu", "dautu", "pages", "categories"].forEach(function (col) {
      window.CMS.registerPreviewTemplate(col, PostPreview);
    });
    console.log("✅ Preview templates đã đăng ký");
  }

  function waitForCMS() {
    if (window.CMS && window.React) {
      registerTemplates();
      return true;
    }
    return false;
  }

  // thử ngay khi DOM ready
  document.addEventListener("DOMContentLoaded", function () {
    if (!waitForCMS()) {
      console.warn("⏳ CMS chưa sẵn sàng, thử lại bằng interval...");
      var i = setInterval(function () {
        if (waitForCMS()) {
          clearInterval(i);
        }
      }, 200);
    }
  });
})();
