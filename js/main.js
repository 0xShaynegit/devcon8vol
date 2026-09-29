const root = document.documentElement;
const header = document.querySelector(".site-header");
const nav = document.getElementById("nav");
const btn = document.querySelector(".menu-btn");
const icon = btn.querySelector("path");
const BARS = "M4 7h16M4 12h16M4 17h16";
const CROSS = "M6 6l12 12M18 6L6 18";

const onScroll = () => header.classList.toggle("is-scrolled", window.scrollY > 40);
onScroll();
window.addEventListener("scroll", onScroll, { passive: true });

const setOpen = (open) => {
  nav.classList.toggle("is-open", open);
  root.classList.toggle("menu-open", open);
  btn.setAttribute("aria-expanded", String(open));
  btn.setAttribute("aria-label", open ? "Close menu" : "Menu");
  icon.setAttribute("d", open ? CROSS : BARS);
};

btn.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
document.addEventListener("click", (e) => {
  if (nav.classList.contains("is-open") && !e.target.closest(".site-header")) setOpen(false);
});
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); btn.focus(); }
});
window.matchMedia("(min-width: 981px)").addEventListener("change", (e) => { if (e.matches) setOpen(false); });
