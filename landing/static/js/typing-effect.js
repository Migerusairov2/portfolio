const texts = ["what’s next.", "great ideas.", "digital futures.", "your vision."];
let index = 0;
let charIndex = 0;
let isDeleting = false;
const typingSpeed = 100;
const deletingSpeed = 50;
const delayBetween = 1500;
const el = document.getElementById("typing");

function typeEffect() {
  const current = texts[index];

  if (!isDeleting) {
    el.textContent = current.substring(0, charIndex++);
    if (charIndex > current.length) {
      setTimeout(() => isDeleting = true, delayBetween);
    }
  } else {
    el.textContent = current.substring(0, charIndex--);
    if (charIndex < 0) {
      isDeleting = false;
      index = (index + 1) % texts.length;
    }
  }

  setTimeout(typeEffect, isDeleting ? deletingSpeed : typingSpeed);
}

typeEffect();