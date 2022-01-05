const links = document.querySelectorAll('a[href^="#"]');

function handleScroll(e) {
  e.preventDefault();
  const id = this.getAttribute("href");
  console.log(id);
  const target = document.querySelector(id);

  distanceTop = target.getBoundingClientRect().top;

  window.scrollBy({ top: distanceTop, left: 0, behavior: "smooth" });
}

links.forEach((link) => (link.onclick = handleScroll));
