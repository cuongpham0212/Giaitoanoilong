const PostPreview = ({ entry, widgetFor }) => {
  // Lấy dữ liệu từ entry
  const title = entry.getIn(["data", "title"]);
  const description = entry.getIn(["data", "description"]);
  const body = widgetFor("body");

  return (
    <div style={{ fontFamily: "sans-serif", padding: "1rem" }}>
      <h1>{title}</h1>
      {description && <p><em>{description}</em></p>}
      <div>{body}</div>
    </div>
  );
};

CMS.registerPreviewTemplate("tamsu", "dautu", "pages", "categories", PostPreview);
