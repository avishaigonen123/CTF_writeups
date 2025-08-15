document.addEventListener("DOMContentLoaded", () => {
  const counters = document.querySelectorAll(".circle-counter");

  counters.forEach(counter => {
    const countEl = counter.querySelector(".count");
    const progressEl = counter.querySelector(".progress");

    const target = parseInt(counter.getAttribute("data-count")) || 0;
    let current = 0;

    const radius = progressEl.r.baseVal.value;
    const circumference = 2 * Math.PI * radius;

    progressEl.style.strokeDasharray = circumference;
    progressEl.style.strokeDashoffset = circumference;

    const duration = 1500;
    const frameRate = 60;
    const totalFrames = Math.round((duration / 1000) * frameRate);
    let frame = 0;

    const animate = () => {
      frame++;
      const progress = frame / totalFrames;

      // springy easing
      const eased = easeOutElastic(progress);

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

    // springy easing function
    function easeOutElastic(t) {
      const c4 = (2 * Math.PI) / 3;
      return t === 0
        ? 0
        : t === 1
        ? 1
        : Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * c4) + 1;
    }
  });
});