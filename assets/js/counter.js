document.addEventListener("DOMContentLoaded", () => {
  const counter = document.querySelector(".circle-counter");
  const countEl = counter.querySelector(".count");
  const progressEl = counter.querySelector(".progress");
  const total = parseInt(counter.dataset.count, 10);
  
  let current = 0;
  const circumference = 2 * Math.PI * 70;
  progressEl.style.strokeDasharray = circumference;

  const animate = () => {
    if (current <= total) {
      countEl.textContent = current;
      const offset = circumference - (current / total) * circumference;
      progressEl.style.strokeDashoffset = offset;
      current++;
      requestAnimationFrame(animate);
    }
  };
  
  animate();
});