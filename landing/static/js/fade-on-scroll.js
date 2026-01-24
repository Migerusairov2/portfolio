const targets = document.querySelectorAll('.title h2');

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('show');
            observer.unobserve(entry.target); // animate once
        }
    });
}, {
    threshold: 0.2
});

targets.forEach(el => observer.observe(el));
