document.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc-list");
  if (!tocList) return;
  
document.addEventListener("DOMContentLoaded", () => {
  const tocList = document.getElementById("toc-list");
  if (!tocList) return;

  const headers = document.querySelectorAll("h2, h3");

  headers.forEach(header => {
    if (!header.id) return;

    const li = document.createElement("li");
    li.classList.add(`toc-${header.tagName.toLowerCase()}`);

    const a = document.createElement("a");
    a.href = `#${header.id}`;
    a.textContent = header.textContent;

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
