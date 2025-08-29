(function () {
  // Thêm CSS fix caret + font
  function injectFixCss() {
    if (document.getElementById("nc-ltr-fix")) return;
    var css = `
      /* ép hiển thị LTR + caret di chuyển mượt */
      .nc-controlPane textarea,
      .nc-controlPane input,
      .public-DraftEditor-content,
      .CodeMirror {
        direction: ltr !important;
        unicode-bidi: isolate !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
        caret-color: black !important;
      }

      /* tránh caret bị nhảy */
      .public-DraftEditor-content {
        white-space: pre-wrap !important;
      }
    `;
    var style = document.createElement("style");
    style.id = "nc-ltr-fix";
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
  }

  // Component Preview cho bài viết
  function PostPreview(props) {
    var entry = props.entry;
    var title = entry.getIn(["data", "title"]) || "";
    var description = entry.getIn(["data", "description"]) || "";
    var body = props.widgetFor("body");

    return window.React.createElement(
      "div",
      { style: { fontFamily: "sans-serif", padding: "1rem", lineHeight: "1.6" } },
      window.React.createElement("h1", null, title),
      description
        ? window.React.createElement("p", { style: { fontStyle: "italic" } }, description)
        : null,
      body
    );
  }

  // Đăng ký preview template
  function registerTemplates() {
    if (!window.CMS) return;
    injectFixCss();

    ["tamsu", "dautu", "pages", "categories"].forEach(function (col) {
      window.CMS.registerPreviewTemplate(col, PostPreview);
    });
  }

  // Chờ CMS load xong
  var i = setInterval(function () {
    if (window.CMS && window.React) {
      clearInterval(i);
      registerTemplates();
    }
  }, 100);
})();
