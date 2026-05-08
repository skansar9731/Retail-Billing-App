const sidebar = document.getElementById("sidebar");

const menuButton = document.getElementById("menuButton");

const overlay = document.getElementById("sidebarOverlay");


// Open Sidebar

menuButton.addEventListener("click", () => {

    sidebar.classList.remove("max-lg:-translate-x-full");

    overlay.classList.remove("hidden");

});


// Close Sidebar

overlay.addEventListener("click", () => {

    sidebar.classList.add("max-lg:-translate-x-full");

    overlay.classList.add("hidden");

});


// Auto Close Sidebar On Mobile Nav Click

const navLinks = document.querySelectorAll("aside nav a");

navLinks.forEach((link) => {

    link.addEventListener("click", () => {

        if (window.innerWidth < 1024) {

            sidebar.classList.add("max-lg:-translate-x-full");

            overlay.classList.add("hidden");

        }

    });

});