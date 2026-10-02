const card = document.createElement("div");
card.className = "place-card";
card.id = "place-card";
card.setAttribute("role", "tooltip");
card.hidden = true;
document.body.appendChild(card);

let current = null;
let pinned = false;

const el = (tag, cls, text) => {
  const node = document.createElement(tag);
  if (cls) node.className = cls;
  if (text) node.textContent = text;
  return node;
};

const fill = (place) => {
  const d = place.dataset;
  card.textContent = "";
  card.appendChild(el("p", "pc-title", d.title));
  if (d.area) card.appendChild(el("p", "pc-area", d.area));
  const list = el("dl", "pc-list");
  [["Rating", d.rating], ["Hours", d.hours], ["Price", d.price]].forEach(([k, v]) => {
    if (!v) return;
    list.appendChild(el("dt", "", k));
    list.appendChild(el("dd", "", v));
  });
  card.appendChild(list);
  if (d.about) card.appendChild(el("p", "pc-about", d.about));
  card.appendChild(el("p", "pc-note", "Approximate. Check Google Maps for current hours and prices."));
};

const position = (place) => {
  const r = place.getBoundingClientRect();
  const cw = card.offsetWidth;
  const ch = card.offsetHeight;
  const left = Math.min(Math.max(12, r.left), window.innerWidth - cw - 12);
  let top = r.bottom + 8;
  if (top + ch > window.innerHeight - 12) top = Math.max(12, r.top - ch - 8);
  card.style.left = left + "px";
  card.style.top = top + "px";
};

const hide = () => {
  if (!current) return;
  current.querySelector("a").removeAttribute("aria-describedby");
  current.querySelector(".place-i").setAttribute("aria-expanded", "false");
  card.hidden = true;
  current = null;
  pinned = false;
};

const show = (place) => {
  if (current === place) return;
  hide();
  current = place;
  fill(place);
  card.hidden = false;
  position(place);
  place.querySelector("a").setAttribute("aria-describedby", "place-card");
};

document.addEventListener("pointerover", (e) => {
  if (e.pointerType !== "mouse" || pinned) return;
  const place = e.target.closest(".place");
  if (place) show(place);
});

document.addEventListener("pointerout", (e) => {
  if (e.pointerType !== "mouse" || pinned) return;
  const place = e.target.closest(".place");
  if (place && !place.contains(e.relatedTarget)) hide();
});

document.addEventListener("focusin", (e) => {
  if (pinned) return;
  const place = e.target.closest(".place");
  if (place) show(place);
  else hide();
});

document.addEventListener("focusout", (e) => {
  if (pinned) return;
  const place = e.target.closest(".place");
  if (place && !place.contains(e.relatedTarget)) hide();
});

document.addEventListener("click", (e) => {
  const button = e.target.closest(".place-i");
  if (button) {
    const place = button.closest(".place");
    if (pinned && current === place) { hide(); return; }
    show(place);
    pinned = true;
    button.setAttribute("aria-expanded", "true");
    return;
  }
  if (pinned && !e.target.closest(".place-card")) hide();
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && current) {
    const button = current.querySelector(".place-i");
    hide();
    if (document.activeElement === button) button.blur();
  }
});

window.addEventListener("scroll", () => {
  if (!current) return;
  if (pinned) position(current);
  else hide();
}, { passive: true, capture: true });

window.addEventListener("resize", () => { if (current) position(current); });
