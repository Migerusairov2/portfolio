const texts = [
  "what’s next",
  "great ideas",
  "digital futures",
  "your vision"
];

let index = 0;
const el = document.getElementById("fadeText");

function changeText() {
  el.style.animation = "none";   // reset animation
  void el.offsetWidth;           // trigger reflow
  el.style.animation = "fadeUp 0.6s ease";

  el.textContent = texts[index];
  index = (index + 1) % texts.length;
}

changeText();
setInterval(changeText, 2200);
