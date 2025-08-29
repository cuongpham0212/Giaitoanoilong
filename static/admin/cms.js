(function () {
  // Inject CSS fix caret + editor
  function injectFixCss() {
    if (document.getElementById("nc-ltr-fix")) return;
    var css = `
      /* Các input/textarea thường */
      .nc-controlPane textarea, 
      .nc-controlPane input {
        direction: ltr !important;
        unicode-bidi: plaintext !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        caret-color: auto !important;
      }

      /* Khung editor chính của Netlify CMS (Draft.js) */
      .public-DraftEditor-content {
        direction: ltr !important;
        unicode-bidi: isolate !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        white-space: pre-wrap !important;
        word-break: break-word !important;
        caret-color: black !important;
      }

      /* Placeholder trong editor */
      .public-DraftEditorPlaceholder-root {
        direction: ltr !important;
        unicode-bidi: isolate !important;
        font-family: inherit !important;
        opacity: 0.6 !important;
      }

      /* CodeMirror khi chỉnh Markdown trực tiếp */
      .CodeMirror {
        direction: ltr !important;
        unicode-bidi: isolate !important;
        font-family: monospace !important;
        caret-color: black !important;
      }
    `;
    var style = document.createElement("style");
    style.id = "nc-ltr-fix";
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
  }

  // Preview chỉ hiện Title + Body
  function PostPreview(props) {
    var entry = props.entry;
    var title = entry.getIn(["data", "title"]) || "";
    var body = props.widgetFor("body");

    return React.createElement(
      "div",
      { style: { fontFamily: "sans-serif", padding: "1rem" } },
      React.createElement("h1", null, title),
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
