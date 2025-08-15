document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".circle-counter");

  counters.forEach(counter => {
    const countEl = counter.querySelector(".count");
    const progressEl = counter.querySelector(".progress");

    if (!countEl || !progressEl) return;

    const target = parseInt(counter.getAttribute("data-count")) || 0;
    let current = 0;

    const radius = parseFloat(progressEl.getAttribute("r")) || 90;
    const circumference = 2 * Math.PI * radius;

    // Apply correct dasharray and offset
    progressEl.style.strokeDasharray = circumference;
    progressEl.style.strokeDashoffset = circumference;

    const duration = 1500; // animation duration in ms
    const startTime = performance.now();

    const animate = (time) => {
      const elapsed = time - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = easeOutCubic(progress);

      current = Math.round(target * eased);
      countEl.textContent = current;

      const offset = circumference * (1 - eased);
      progressEl.style.strokeDashoffset = offset;

      if (progress < 1) {
        requestAnimationFrame(animate);
      } else {
        countEl.textContent = target;
        progressEl.style.strokeDashoffset = 0;
      }
    };

    requestAnimationFrame(animate);

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }
  });
});
