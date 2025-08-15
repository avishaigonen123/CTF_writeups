document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".circle-counter");

  counters.forEach(counter => {
    const countEl = counter.querySelector(".count");
    const progressEl = counter.querySelector(".progress");

    // Dynamically fetch the real count here (replace with actual backend fetch)
    const target = parseInt(counter.getAttribute("data-count")) || 0;

    let current = 0;
    const duration = 1500; 
    const frameRate = 60;
    const totalFrames = Math.round((duration / 1000) * frameRate);
    let frame = 0;

    const radius = progressEl.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    const animate = () => {
      frame++;
      const progress = frame / totalFrames;
      const eased = easeOutCubic(progress);

      current = Math.round(target * eased);
      countEl.textContent = current;

      const offset = circumference * (1 - eased);
      progressEl.style.strokeDashoffset = offset;

      if (frame < totalFrames) {
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
