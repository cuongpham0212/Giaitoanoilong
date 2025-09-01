document.addEventListener("DOMContentLoaded", function () {
  const menuBtn = document.getElementById("menu-btn");
  const menu = document.getElementById("menu");

  // Toggle menu mobile
  menuBtn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
  });

  // Dropdown cho mobile
  const dropdownParents = menu.querySelectorAll(".group");
  dropdownParents.forEach(parent => {
    parent.addEventListener("click", (e) => {
      if (window.innerWidth < 1024) {
        e.preventDefault();
        const dropdown = parent.querySelector("div");
        if (dropdown) dropdown.classList.toggle("hidden");
      }
    });
  });
});
