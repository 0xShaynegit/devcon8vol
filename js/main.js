const header = document.querySelector(".site-header");
const nav = document.getElementById("nav");
const btn = document.querySelector(".menu-btn");

const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 40);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

btn.addEventListener("click", () => {
  const open = nav.classList.toggle("is-open");
  btn.setAttribute("aria-expanded", String(open));
});
nav.addEventListener("click", (e) => {
  if (e.target.closest("a")) {
    nav.classList.remove("is-open");
    btn.setAttribute("aria-expanded", "false");
  }
});
