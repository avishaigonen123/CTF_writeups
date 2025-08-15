document.addEventListener("DOMContentLoaded", () => {
  const counter = document.querySelector(".circle-counter");
  const countEl = counter.querySelector(".count");
  const progressEl = counter.querySelector(".progress");
  const total = parseInt(counter.dataset.count, 10);

  const circumference = 2 * Math.PI * 70;
  progressEl.style.strokeDasharray = circumference;

  let start = null;
  const duration = 1500; // animation time in ms

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3); // smooth finish
  }

  function animate(timestamp) {
    if (!start) start = timestamp;
    const elapsed = timestamp - start;
    let progress = Math.min(elapsed / duration, 1);

    // Apply easing for a smoother look
    progress = easeOutCubic(progress);

    // Calculate the value once, use for both text and circle
    const currentValue = Math.round(progress * total);
    countEl.textContent = currentValue;

    // Percentage of completion (relative to total)
    const percent = currentValue / total;
    const offset = circumference - percent * circumference;
    progressEl.style.strokeDashoffset = offset;

    if (progress < 1) {
      requestAnimationFrame(animate);
    } else {
      countEl.textContent = total;
      progressEl.style.strokeDashoffset = 0; // fully complete
    }
  }

  requestAnimationFrame(animate);
});
