// ===== NAV =====
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

// ===== MODAL =====
const modal = document.getElementById('projModal');
const modalImg = document.getElementById('projModalImg');
const modalTitle = document.getElementById('projModalTitle');
const modalDesc = document.getElementById('projModalDesc');
const modalLinksWrap = document.getElementById('projModalLinks');

let lastFocus = null;

function openProjectModal({ imgSrc, imgAlt, title, descHTML, links }) {
  if (!modal) return;
  modalImg.src = imgSrc || '';
  modalImg.alt = imgAlt || 'Project preview';
  modalTitle.textContent = title || '';
  modalDesc.innerHTML = descHTML || '';
  modalLinksWrap.innerHTML = '';
  (links || []).forEach(({ href, label }) => {
    if (!href) return;
    const a = document.createElement('a');
    a.href = href;
    a.target = '_blank';
    a.rel = 'noopener noreferrer';
    a.className = 'link-pill';
    a.textContent = label;
    modalLinksWrap.appendChild(a);
  });
  lastFocus = document.activeElement;
  document.body.classList.add('modal-open');
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  modal.querySelector('.proj-modal__dialog').focus();
}

function closeProjectModal() {
  if (!modal) return;
  modal.classList.remove('open');
  document.body.classList.remove('modal-open');
  modal.setAttribute('aria-hidden', 'true');
  if (lastFocus && typeof lastFocus.focus === 'function') lastFocus.focus();
}

// Abrir modal desde imagen
document.addEventListener('click', (e) => {
  const imgEl = e.target.closest('.project img');
  if (!imgEl) return;
  const card = imgEl.closest('.project');
  const info = card?.querySelector('.info');
  const title = info?.querySelector('h4')?.textContent?.trim() || '';
  const descHTML = info?.querySelector('p')?.innerHTML || '';
  const links = Array.from(info?.querySelectorAll('.links a') || []).map(a => ({
    href: a.getAttribute('href'),
    label: a.textContent.trim()
  }));
  openProjectModal({
    imgSrc: imgEl.getAttribute('src') || '',
    imgAlt: imgEl.getAttribute('alt') || '',
    title,
    descHTML,
    links
  });
});

// “More”: abre modal en desktop, clampa en mobile
document.addEventListener('click', (e) => {
  const moreBtn = e.target.closest('.toggle-more');
  if (!moreBtn) return;
  const isDesktop = window.matchMedia('(min-width: 801px)').matches;
  const card = moreBtn.closest('.project');
  const info = card?.querySelector('.info');

  if (isDesktop) {
    const imgEl = card.querySelector('img');
    const title = info?.querySelector('h4')?.textContent?.trim() || '';
    const descHTML = info?.querySelector('p')?.innerHTML || '';
    const links = Array.from(info?.querySelectorAll('.links a') || []).map(a => ({
      href: a.getAttribute('href'),
      label: a.textContent.trim()
    }));
    openProjectModal({
      imgSrc: imgEl?.getAttribute('src') || '',
      imgAlt: imgEl?.getAttribute('alt') || '',
      title,
      descHTML,
      links
    });
  } else {
    const expanded = info.classList.toggle('expanded');
    moreBtn.setAttribute('aria-expanded', expanded ? 'true' : 'false');
    moreBtn.textContent = expanded ? 'Less' : 'More';
  }
});

// Accesibilidad del botón con teclado
document.addEventListener('keydown', (e) => {
  if ((e.key === 'Enter' || e.key === ' ') && e.target.classList?.contains('toggle-more')) {
    e.preventDefault();
    e.target.click();
  }
});

// Cerrar modal (backdrop o botón con data-close)
document.addEventListener('click', (e) => {
  if (!modal || !modal.classList.contains('open')) return;
  if (e.target.matches('[data-close]')) closeProjectModal();
});

// Escape + focus trap
document.addEventListener('keydown', (e) => {
  if (!modal || !modal.classList.contains('open')) return;
  if (e.key === 'Escape') closeProjectModal();
  if (e.key === 'Tab') {
    const dialog = modal.querySelector('.proj-modal__dialog');
    const focusables = dialog.querySelectorAll('a,button,input,textarea,select,[tabindex]:not([tabindex="-1"])');
    const list = Array.from(focusables).filter(el => !el.hasAttribute('disabled') && el.offsetParent !== null);
    if (!list.length) return;
    const first = list[0], last = list[list.length - 1];
    if (e.shiftKey && document.activeElement === first) { last.focus(); e.preventDefault(); }
    else if (!e.shiftKey && document.activeElement === last) { first.focus(); e.preventDefault(); }
  }
});

document.querySelectorAll("#projects .project").forEach((card) => {
  let t = null;

  const show = () => {
    card.classList.add("show-hint");
    clearTimeout(t);
    t = setTimeout(() => card.classList.remove("show-hint"), 900);
  };

  card.addEventListener("touchstart", show, { passive: true });
});
