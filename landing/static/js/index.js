document.addEventListener("DOMContentLoaded", function () {
    const button = document.getElementById("scrollBtn");
    const target = document.getElementById("about");

    button.addEventListener("click", function () {
        target.scrollIntoView({
            behavior: "smooth"
        });
    });
});


let lastScroll = 0;
const header = document.querySelector('header');
const scrollBtn = document.getElementById('scrollBtn');

window.addEventListener('scroll', () => {
    const currentScroll = window.scrollY;

    // Header style
    if (currentScroll > 50) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }

    // Hide scroll button after scrolling
    if (currentScroll > 50) {
        scrollBtn.classList.add('hide');
    } else {
        scrollBtn.classList.remove('hide');
    }

    lastScroll = currentScroll;
});

