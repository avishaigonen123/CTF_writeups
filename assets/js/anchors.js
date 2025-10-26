// anchors.js
// Automatically adds "#" anchor links to all headings (h1–h6)

document.addEventListener("DOMContentLoaded", () => {
  const headings = document.querySelectorAll("h1, h2, h3, h4, h5, h6");

  headings.forEach(h => {
    // Generate ID if missing
    if (!h.id) {
      h.id = h.textContent
        .trim()
        .toLowerCase()
        .replace(/[^\w\s-]/g, '')  // remove punctuation
        .replace(/\s+/g, '-');     // spaces to hyphens
    }

    // Avoid duplicates
    if (h.querySelector(".anchor")) return;

    // Create anchor element
    const a = document.createElement("a");
    a.href = `#${h.id}`;
    a.className = "anchor";
    a.textContent = "#";
    h.prepend(a);
  });
});
