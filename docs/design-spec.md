# volunteeringatDevcon8: design spec (draft for approval)

Unofficial community resource for Devcon 8 (Mumbai) volunteers. Look-alike of the devcon.org structure, own artwork, dark green base. Not affiliated with Devcon or the Ethereum Foundation.

## Dials
- DESIGN_VARIANCE 5: offset hero, centred statement bands, asymmetric role cards
- MOTION_INTENSITY 5: load cascade, transform/opacity reveals, slow mandala rotation, marquee. No parallax library
- VISUAL_DENSITY 5: editorial, plenty of reference content per page
- BRAND_FIDELITY 2: new identity that borrows devcon.org's page anatomy, not its artwork, logo or purple

## Value structure (greyscale sketch)
Dark hero and header, bright leaf-green stat band, mid-dark body, one pale mint band for the FAQ, deepest green footer. Never more than two adjacent bands in the same tone.

## Palette (contrast computed with better-colors check_contrast.py)
| Token | Hex | Use |
|---|---|---|
| --forest-950 | #0B2A20 | page ground, header, footer |
| --forest-800 | #12382B | raised surface, cards |
| --forest-600 | #1B5A43 | borders, hover surface |
| --leaf | #B8F04C | primary CTA, stat band, links on dark |
| --marigold | #F4A62A | info strip under hero (Diwali / Mumbai nod), badges |
| --paper | #EEF5EE | light band (FAQ), ink on it is forest-950 |
| --ink | #EAF4EC | body text on dark (13.65:1 on ground) |
| --muted | #A9C4B4 | secondary text (8.23:1 on ground, 6.91:1 on surface) |

Marigold and leaf never carry text on paper (1.2 to 1.8:1). On paper, text is forest-950 only. Dark-mode is the default and only theme; light mode is a deliberate non-goal because the brief is dark green. Stated, not silent.

## Type (self-hosted woff2 from team/fonts/woff2)
- Display and body: Outfit variable (geometric, close to devcon.org's Poppins feel, and in the vault)
- Editorial accent for pull quotes and role numerals: Fraunces variable, italic, used sparingly
- Scale: h1 clamp(2.75rem, 7vw, 5.25rem) at 1.0 leading, -0.03em; body 1.0625rem at 1.6; ratio above 3.5x
- Devanagari for any Hindi greeting line: Noto Sans Devanagari, not in the vault, would need adding. Left out unless you want it.

## Page anatomy (mirrors devcon.org/en, own content)
1. Slim announce bar: "Unofficial volunteer resource. Not affiliated with Devcon or the Ethereum Foundation."
2. Sticky header that shrinks on scroll: wordmark, About, Roles, Shifts, Training, Travel, FAQ, filled leaf pill "Apply on devcon.org"
3. Hero, full-bleed, 80vh: dark green scene, large rotating line-art mandala disc behind a Mumbai skyline silhouette (own SVG, not their artwork), headline on the image, two CTAs
4. Marigold info strip: Venue Jio World Centre BKC, Dates 3 to 6 Nov 2026, Training 9, 16, 23 Oct
5. Trust bar: 4 days, 2 shifts, 7 roles, 3 training calls
6. Centred statement, then two-column "What volunteers do" with a stat band in leaf
7. Roles: seven cards, each links to its own page (Registration, General Floor, Swag, Stage and Speaker, DevComms, Info Desk, Meeting Room)
8. Shifts and training timeline
9. Travel teaser plus community resources (Nitasha's guides, side events sheet, Kaveh's Devcon 7 write-up, roadmap call recording)
10. Funding and stay ideas, with the non-affiliation disclaimer kept verbatim
11. Marquee of topics, pattern border band
12. FAQ on the paper band
13. Footer with official socials and legal links to devcon.org

## Rhythm breaks
Leaf stat band, marigold strip, paper FAQ band, marquee. Not alternating two tones.

## Imagery: open problem
The brief needs a person mid-action and real green. I have no volunteer photos and will not lift Devcon photography for an unaffiliated site. Hero ships with the SVG scene; every role page has a marked slot for a real volunteer photo you supply. The Jio World Centre site is used as reference for maps and floorplans only, and any map on the site is labelled "reference, awaiting official Devcon map".

## Motion
Load cascade on the hero (transform, opacity), slow mandala rotation, marquee, sticky header shrink, accordion. All gated by prefers-reduced-motion. Nothing hidden by default.

## Deliberate risk
A dark green Devcon is off-brand for the event itself. That is the point of the look-alike, and it is the thing most likely to be judged wrong at first render.

## Legal and links
Terms of service, privacy, code of conduct, attendee guidelines: always link to the live devcon.org URLs (terms-of-service, privacy-notice, code-of-conduct, Devcon8-Attendee-Guidelines-2026.pdf). No copies.
