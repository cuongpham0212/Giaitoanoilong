document.addEventListener("DOMContentLoaded", function () {
  // Toggle menu
  const toggleBtn = document.getElementById("menu-btn");
  const siteMenu = document.getElementById("site-menu");

  if (toggleBtn && siteMenu) {
    toggleBtn.addEventListener("click", () => {
      siteMenu.classList.toggle("hidden");
      const expanded = toggleBtn.getAttribute("aria-expanded") === "true" || false;
      toggleBtn.setAttribute("aria-expanded", !expanded);
    });
  }

  // Back to top
  const backToTop = document.getElementById("backToTop");
  if (backToTop) {
    window.addEventListener("scroll", () => {
      if (window.scrollY > 300) {
        backToTop.classList.remove("hidden");
      } else {
        backToTop.classList.add("hidden");
      }
    });

    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
});
