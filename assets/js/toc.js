document.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc-list");
  if (!tocList) return; // 🚨 critical

  const headers = Array.from(
    document.querySelectorAll(".page-main h2, .page-main h3")
  );

  if (headers.length === 0) {
    document.getElementById("toc").style.display = "none";
    return;
  }

  headers.forEach(header => {
    if (!header.id) return;

    const cleanText = Array.from(header.childNodes)
      .filter(n => n.nodeType === Node.TEXT_NODE)
      .map(n => n.textContent)
      .join("")
      .trim();

    if (!cleanText) return;

    const li = document.createElement("li");
    li.className = `toc-${header.tagName.toLowerCase()}`;

    const a = document.createElement("a");
    a.href = `#${header.id}`;
    a.textContent = cleanText;

    a.addEventListener("click", e => {
      e.preventDefault();
      document.getElementById(header.id)
        .scrollIntoView({ behavior: "smooth", block: "start" });
      history.pushState(null, "", `#${header.id}`);
    });

    li.appendChild(a);
    tocList.appendChild(li);
  });
});
