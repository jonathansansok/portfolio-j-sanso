//aqui: Nav selected function accesible y sin hardcodeos
function selected(link) {
  const options = document.querySelectorAll('#links a'); 
  options.forEach(a => a.classList.remove('selected')); 
  link.classList.add('selected'); 


  options.forEach(a => a.removeAttribute('aria-current'));
  link.setAttribute('aria-current', 'page');


  const nav = document.getElementById('nav');
  nav.classList.remove('responsive');
}

function responsiveMenu() {
  const nav = document.getElementById('nav');
  const btn = document.getElementById('nav-icon');
  const isOpen = nav.classList.toggle('responsive'); 
  if (btn) btn.setAttribute('aria-expanded', String(isOpen)); 
}