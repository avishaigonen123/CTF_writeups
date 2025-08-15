  // Go one folder up from current URL
  const parts = window.location.pathname.split('/').filter(Boolean);
  
  // Remove the last part (current page or last folder)
  parts.pop(); 
  
  // If we're already at the root level, make sure the parent is '/'
  const parent = parts.length > 0 ? '/' + parts.join('/') + '/' : '/';
  
  // Update the back-link href attribute
  document.getElementById('back-link').href = parent;