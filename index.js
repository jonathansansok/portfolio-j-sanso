//aqui: Nav selected function accesible y sin hardcodeos
function selected(link) {
  const options = document.querySelectorAll('#links a'); //aqui: toma todos los <a>
  options.forEach(a => a.classList.remove('selected')); //aqui: limpia la clase activa
  link.classList.add('selected'); //aqui: marca el link activo

  //aqui: actualiza aria-current para lectores de pantalla
  options.forEach(a => a.removeAttribute('aria-current'));
  link.setAttribute('aria-current', 'page');

  //aqui: cierra el menú responsive al elegir una opción
  const nav = document.getElementById('nav');
  nav.classList.remove('responsive');
}

//aqui: menú responsive con control ARIA
function responsiveMenu() {
  const nav = document.getElementById('nav');
  const btn = document.getElementById('nav-icon');
  const isOpen = nav.classList.toggle('responsive'); //aqui: alterna la clase
  if (btn) btn.setAttribute('aria-expanded', String(isOpen)); //aqui: sincroniza ARIA
}