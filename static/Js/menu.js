document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("menu-btn");
  const siteMenu = document.getElementById("site-menu");
  const backdrop = document.getElementById("menu-backdrop");

  if (!menuBtn || !siteMenu || !backdrop) return;

  // Mở menu chính
  function openMenu() {
    siteMenu.classList.remove("hidden");
    backdrop.classList.remove("hidden");
    menuBtn.setAttribute("aria-expanded", "true");
  }

  // Đóng menu chính
  function closeMenu() {
    siteMenu.classList.add("hidden");
    backdrop.classList.add("hidden");
    menuBtn.setAttribute("aria-expanded", "false");
    // đóng tất cả submenu
    siteMenu.querySelectorAll(".submenu").forEach(sm => sm.classList.add("hidden"));
    siteMenu.querySelectorAll(".submenu-btn").forEach(b => b.setAttribute("aria-expanded","false"));
  }

  // Toggle menu chính
  menuBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    if (siteMenu.classList.contains("hidden")) openMenu(); else closeMenu();
  });

  // Ngăn click trong menu làm đóng ngoài ý muốn
  siteMenu.addEventListener("click", (e) => e.stopPropagation());

  // Submenu: click để mở/đóng
  siteMenu.querySelectorAll(".submenu-btn").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.stopPropagation();
      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      const isHidden = panel.classList.contains("hidden");

      // Đóng tất cả submenu khác
      siteMenu.querySelectorAll(".submenu").forEach(sm => { if (sm !== panel) sm.classList.add("hidden"); });
      siteMenu.querySelectorAll(".submenu-btn").forEach(b => { if (b !== btn) b.setAttribute("aria-expanded","false"); });

      // Toggle submenu hiện tại
      panel.classList.toggle("hidden", !isHidden ? true : false);
      btn.setAttribute("aria-expanded", isHidden ? "true" : "false");
    });
  });

  // Click ra ngoài hoặc ESC để đóng menu
  document.addEventListener("click", (e) => {
    if (!siteMenu.classList.contains("hidden") && !siteMenu.contains(e.target) && !menuBtn.contains(e.target)) {
      closeMenu();
    }
  });
  backdrop.addEventListener("click", closeMenu);
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeMenu();
  });
});
