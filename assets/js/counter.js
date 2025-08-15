document.addEventListener("DOMContentLoaded", () => {
  const counter = document.getElementById("counter");
  if (!counter) return;

  const target = parseInt(counter.getAttribute("data-count"), 10);
  let current = 0;
  const duration = 2000; // animation duration in ms
  const frameRate = 60; // FPS
  const totalFrames = Math.round((duration / 1000) * frameRate);
  let frame = 0;

  const animate = () => {
    frame++;
    const progress = frame / totalFrames;
    const eased = easeOutCubic(progress);
    current = Math.round(target * eased);

    counter.textContent = current;

    // smooth green fade from gray → green
    counter.style.color = `rgb(${50 - eased * 50}, ${180 + eased * 75}, ${50 - eased * 50})`;

    if (frame < totalFrames) {
      requestAnimationFrame(animate);
    } else {
      counter.textContent = target;
      counter.style.color = "#2ecc71"; // final green
    }
  };

  requestAnimationFrame(animate);

  // easing function for smoother animation
  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }
});
