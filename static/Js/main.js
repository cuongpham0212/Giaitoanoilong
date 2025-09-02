document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("menu-btn");
  const siteMenu = document.getElementById("site-menu");
  const backdrop = document.getElementById("menu-backdrop");

  const openMenu = () => {
    siteMenu.classList.remove("hidden");
    backdrop?.classList.remove("hidden");
    menuBtn?.setAttribute("aria-expanded", "true");
  };

  const closeMenu = () => {
    siteMenu.classList.add("hidden");
    backdrop?.classList.add("hidden");
    menuBtn?.setAttribute("aria-expanded", "false");
    siteMenu.querySelectorAll(".submenu").forEach(sm => sm.classList.add("hidden"));
    siteMenu.querySelectorAll(".submenu-toggle").forEach(b => b.setAttribute("aria-expanded","false"));
  };

  // Toggle menu chính
  menuBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    siteMenu.classList.contains("hidden") ? openMenu() : closeMenu();
  });

  // Toggle submenu bằng nút mũi tên (không chặn click vào link cha)
  siteMenu?.querySelectorAll(".submenu-toggle").forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      e.stopPropagation();

      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      const isHidden = panel.classList.contains("hidden");

      // Đóng các submenu khác
      siteMenu.querySelectorAll(".submenu").forEach(sm => { if (sm !== panel) sm.classList.add("hidden"); });
      siteMenu.querySelectorAll(".submenu-toggle").forEach(b => { if (b !== btn) b.setAttribute("aria-expanded","false"); });

      // Toggle submenu hiện tại
      panel.classList.toggle("hidden", !isHidden ? true : false);
      btn.setAttribute("aria-expanded", isHidden ? "true" : "false");
    });
  });

  // Link con → điều hướng (KHÔNG chặn default nữa)
  siteMenu?.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", () => {
      closeMenu(); // đóng menu sau khi click
    });
  });

  // Click ngoài menu → đóng
  document.addEventListener("click", (e) => {
    if (!siteMenu.classList.contains("hidden") &&
        !siteMenu.contains(e.target) && !menuBtn.contains(e.target)) {
      closeMenu();
    }
  });
  backdrop?.addEventListener("click", closeMenu);

  // ESC → đóng
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeMenu(); });
});
