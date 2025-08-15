document.addEventListener("DOMContentLoaded", () => {
  const counter = document.querySelector(".circle-counter");
  const countEl = counter.querySelector(".count");
  const progressEl = counter.querySelector(".progress");
  const total = parseInt(counter.dataset.count, 10);

  const circumference = 2 * Math.PI * 70;
  progressEl.style.strokeDasharray = circumference;

  let start = null;
  const duration = 1500; // animation length in ms

  function animate(timestamp) {
    if (!start) start = timestamp;
    const elapsed = timestamp - start;

    const progress = Math.min(elapsed / duration, 1); // clamp to [0,1]

    // Number update
    countEl.textContent = Math.floor(progress * total);

    // Circle update
    const offset = circumference - progress * circumference;
    progressEl.style.strokeDashoffset = offset;

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      countEl.textContent = total; // ensure final value
    }
  }

  requestAnimationFrame(animate);
});