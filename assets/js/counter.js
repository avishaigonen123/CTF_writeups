document.addEventListener("DOMContentLoaded", () => {
  const counter = document.querySelector(".circle-counter");
  const countEl = counter.querySelector(".count");
  const progressEl = counter.querySelector(".progress");
  const total = parseInt(counter.dataset.count, 10);

  // Define what 100% means for your circle — e.g., max number possible
  const maxValue = total; // or replace with a fixed number if you have one
  const circumference = 2 * Math.PI * 70;
  progressEl.style.strokeDasharray = circumference;

  let start = null;
  const duration = 1500; // ms

  function animate(timestamp) {
    if (!start) start = timestamp;
    const elapsed = timestamp - start;
    const progress = Math.min(elapsed / duration, 1);

    // Counter animation
    const currentValue = Math.floor(progress * total);
    countEl.textContent = currentValue;

    // Circle animation — relative to maxValue
    const percentOfMax = currentValue / maxValue;
    const offset = circumference - percentOfMax * circumference;
    progressEl.style.strokeDashoffset = offset;

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      countEl.textContent = total;
      progressEl.style.strokeDashoffset = circumference - (total / maxValue) * circumference;
    }
  }

  requestAnimationFrame(animate);
});
