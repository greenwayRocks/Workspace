function initMap() {
  const loc = { lat: 27.613883, lng: 84.01738 };

  const map = new google.maps.Map(document.querySelector(".map"), {
    zoom: 14,
    center: loc,
  });

  const marker = new google.maps.Marker({ position: loc, map: map });
}

window.addEventListener("scroll", () => {
  if (window.scrollY > 150) {
    document.querySelector("#navbar").style.opacity = 0.9;
  } else {
    document.querySelector("#navbar").style.opacity = 1;
  }
});

function smoothScroll(e) {
  e.preventDefault();
  const el = this.getAttribute("href");
  const target = document.querySelector(el);

  const targetPosition = target.getBoundingClientRect().top - 100;
  window.scrollBy({ top: targetPosition, left: 0, behavior: "smooth" });

  // Check
}

const myLinks = document.querySelectorAll("a[href^='#']");

myLinks.forEach((link) => {
  console.log(link);
  link.onclick = smoothScroll;
});
