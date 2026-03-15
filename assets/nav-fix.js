document.addEventListener("DOMContentLoaded", () => {
    const openBtns = document.querySelectorAll(".wp-block-navigation__responsive-container-open");
    const closeBtns = document.querySelectorAll(".wp-block-navigation__responsive-container-close");
    const menus = document.querySelectorAll(".wp-block-navigation__responsive-container");

    openBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            menus.forEach(menu => {
                menu.classList.add("is-menu-open");
                menu.classList.add("has-modal-open");
                menu.style.display = "flex";
            });
            document.body.style.overflow = "hidden";
        });
    });

    closeBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            menus.forEach(menu => {
                menu.classList.remove("is-menu-open");
                menu.classList.remove("has-modal-open");
                menu.style.display = "none";
            });
            document.body.style.overflow = "";
        });
    });
});
