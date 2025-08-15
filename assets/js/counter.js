// counter.js
document.addEventListener("DOMContentLoaded", () => {
  const counter = document.getElementById("counter");
  const target = +counter.getAttribute("data-count"); // Get the value from data-count
  let current = 0;

  const increment = Math.ceil(target / 100); // speed of increment
  const interval = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(interval);
    }
    counter.textContent = current;
  }, 20); // adjust speed (ms) here
});
