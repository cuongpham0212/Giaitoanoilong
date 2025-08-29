const PostPreview = ({ entry, widgetFor }) => {
  return (
    <div style={{ padding: "1rem", fontFamily: "sans-serif" }}>
      <h1>{entry.getIn(["data", "title"])}</h1>
      <div>{widgetFor("body")}</div>
    </div>
  );
};

CMS.registerPreviewTemplate("tamsu", "dautu", "pages", "categories", PostPreview);
