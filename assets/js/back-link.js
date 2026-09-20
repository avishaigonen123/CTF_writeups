// Points the "back" link at the parent folder of the current page.
//
// Guarded on DOMContentLoaded: this file previously ran immediately and relied
// on the #back-link div happening to be parsed first. That only worked because
// the include emitted the div and the script together. Now that the markup and
// the script are loaded from different places, the guard is required.
document.addEventListener("DOMContentLoaded", function () {
  var link = document.getElementById("back-link");
  if (!link) return;

  // Go one folder up from the current URL.
  var parts = window.location.pathname.split("/").filter(Boolean);

  // Remove the last part (current page or last folder).
  parts.pop();

  // If we're already at the root level, make sure the parent is '/'.
  var parent = parts.length > 0 ? "/" + parts.join("/") + "/" : "/";

  link.href = parent;
});
