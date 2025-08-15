// document.addEventListener("DOMContentLoaded", () => {
//   const counter = document.querySelector(".circle-counter");
//   const countEl = counter.querySelector(".count");
//   const progressEl = counter.querySelector(".progress");
//   const total = parseInt(counter.dataset.count, 10);

//   const circumference = 2 * Math.PI * 70;
//   progressEl.style.strokeDasharray = circumference;

//   let start = null;
//   const duration = 1500; // animation time in ms

//   function easeOutCubic(t) {
//     return 1 - Math.pow(1 - t, 3); // smooth finish
//   }

//   function animate(timestamp) {
//     if (!start) start = timestamp;
//     const elapsed = timestamp - start;
//     let progress = Math.min(elapsed / duration, 1);

//     // Apply easing for a smoother look
//     progress = easeOutCubic(progress);

//     // Calculate the value once, use for both text and circle
//     const currentValue = Math.round(progress * total);
//     countEl.textContent = currentValue;

//     // Percentage of completion (relative to total)
//     const percent = currentValue / total;
//     const offset = circumference - percent * circumference;
//     progressEl.style.strokeDashoffset = offset;

//     if (progress < 1) {
//       requestAnimationFrame(animate);
//     } else {
//       countEl.textContent = total;
//       progressEl.style.strokeDashoffset = 0; // fully complete
//     }
//   }

//   requestAnimationFrame(animate);
// });


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
