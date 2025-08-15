  const parts = window.location.pathname.split('/').filter(Boolean);
  
  // Remove the last part (current page or last folder)
  parts.pop(); 
  
  // If we're already at the root level, make sure the parent is '/'
  const parent = parts.length > 0 ? '/' + parts.join('/') + '/' : '/';
  
  // Update the back-link href attribute
  let a= document.getElementById('back-link');
  console.log(a)
  alert(a)
  a.href = parent;