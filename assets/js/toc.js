document.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc-list");
  if (!tocList) return;

  const headers = Array.from(document.querySelectorAll("h2, h3"))
  .filter(h => !h.closest("#toc"));
  headers.forEach(header => {
    if (!header.id) return;

    const li = document.createElement("li");
    li.classList.add(`toc-${header.tagName.toLowerCase()}`);

    const a = document.createElement("a");
    a.href = `#${header.id}`;
    a.textContent = header.childNodes[0].textContent.trim();

    a.addEventListener("click", e => {
      e.preventDefault();
      document.querySelector(a.getAttribute("href"))
        .scrollIntoView({ behavior: "smooth", block: "start" });
      history.pushState(null, "", a.getAttribute("href"));
    });

    li.appendChild(a);
    tocList.appendChild(li);
  });
});
