const sidebar = document.getElementById("sidebar");

const menuButton = document.getElementById("menuButton");

const overlay = document.getElementById("sidebarOverlay");


// Open Sidebar

if (menuButton) {

    menuButton.addEventListener("click", () => {

        sidebar.classList.remove("max-lg:-translate-x-full");

        overlay.classList.remove("hidden");

    });

}


// Close Sidebar

if (overlay) {

    overlay.addEventListener("click", () => {

        sidebar.classList.add("max-lg:-translate-x-full");

        overlay.classList.add("hidden");

    });

}


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


const transactionToggle = document.getElementById(
    "transactionToggle"
);

const transactionMenu = document.getElementById(
    "transactionMenu"
);

const transactionArrow = document.getElementById(
    "transactionArrow"
);


if (
    transactionToggle &&
    transactionMenu &&
    transactionArrow
) {

    transactionToggle.addEventListener("click", () => {

        // Toggle Menu

        if (
            transactionMenu.style.display === "block"
        ) {

            transactionMenu.style.display = "none";

            transactionArrow.style.transform =
                "rotate(0deg)";

        }

        else {

            transactionMenu.style.display = "block";

            transactionArrow.style.transform =
                "rotate(180deg)";

        }

    });
const invoiceToggle =
    document.getElementById(
        "invoiceToggle"
    );

const invoiceMenu =
    document.getElementById(
        "invoiceMenu"
    );

const invoiceArrow =
    document.getElementById(
        "invoiceArrow"
    );


if (

    invoiceToggle &&

    invoiceMenu &&

    invoiceArrow

) {

    invoiceToggle.addEventListener(
        "click",
        () => {

            if (

                invoiceMenu.style.display
                === "block"

            ) {

                invoiceMenu.style.display =
                    "none";

                invoiceArrow.style.transform =
                    "rotate(0deg)";

            }

            else {

                invoiceMenu.style.display =
                    "block";

                invoiceArrow.style.transform =
                    "rotate(180deg)";

            }

        }
    );

}
}