document.addEventListener("DOMContentLoaded", () => {
  const counter = document.getElementById("counter");
  if (!counter) return;

  const target = parseInt(counter.getAttribute("data-count"), 10);
  let current = 0;
  const duration = 2000; // total animation time in ms
  const frameRate = 60; // frames per second
  const totalFrames = Math.round((duration / 1000) * frameRate);
  let frame = 0;

  const animate = () => {
    frame++;
    const progress = frame / totalFrames;
    const eased = easeOutQuad(progress); // easing function
    current = Math.round(target * eased);

    // color from red → green as it counts up
    counter.style.color = `rgb(${255 - eased * 255}, ${eased * 255}, 0)`;
    counter.textContent = current;

    if (frame < totalFrames) {
      requestAnimationFrame(animate);
    } else {
      counter.textContent = target; // ensure it ends exactly on target
      counter.style.color = "#0f0"; // final color green
    }
  };

  requestAnimationFrame(animate);

  function easeOutQuad(t) {
    return t * (2 - t);
  }
});
