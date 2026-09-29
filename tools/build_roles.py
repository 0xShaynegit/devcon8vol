"""Generate the six role pages from roles/registration.html so header, footer and layout never drift.
Run from the project root: python tools/build_roles.py
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
tpl = (ROOT / "roles" / "registration.html").read_text(encoding="utf-8")

TBC = '<span class="tbc">Mumbai TBC</span>'

ORDER = [
    ("registration", "Registration"),
    ("general-floor", "General Floor"),
    ("swag-station", "Swag Station"),
    ("stage-and-speaker", "Stage and Speaker"),
    ("devcomms", "DevComms"),
    ("info-desk", "Info Desk"),
    ("meeting-rooms", "Meeting Rooms"),
]


def tbc_section(items):
    lis = "\n".join(f"          <li>{i}</li>" for i in items)
    return ("tbc", "Still to confirm", f"""
        <p>Nothing here is guessed. These items stay marked until the Devcon team confirms them.</p>
        <ul>
{lis}
        </ul>""")


PAGES = {}

# ---------------------------------------------------------------- General Floor
PAGES["general-floor"] = dict(
    pos="18% 62%",
    lede="A mix of activities and a great shift for meeting attendees. You watch the doors, guide the crowd and keep the venue friendly and sponsor neutral.",
    desc="Volunteer guide for the General Floor at Devcon 8 in Mumbai: activities, where volunteers are posted, and the rules to enforce.",
    sections=[
        ("basics", "Your job", f"""
        <p>Check in and out with the Volunteer Attendance Lead at the Volunteer Room. Then stay in your general floor area for the whole shift. You can rotate between General Floor posts, or stay on one if you prefer.</p>
        <h3>Main activities</h3>
        <ul>
          <li>Help attendees with directions and finding rooms. Maps are displayed around the venue.</li>
          <li>As talks let out and queues form, keep people moving so no area congests. Point them to elevators and escalators.</li>
          <li>Answer general Devcon questions. Study the schedule.</li>
          <li>Make sure everyone wears a Devcon wristband, and speak to anyone who does not.</li>
          <li>Watch for unapproved vendors, giveaways and solicitation, and for suspicious behaviour. Escalate straight away.</li>
        </ul>
        <div class="callout">
          <strong>Check wristbands</strong>
          <p>Every post on the floor checks wristbands. If you see anyone without one, ask them why.</p>
        </div>"""),
        ("zones", "Where volunteers are posted", f"""
        <p>This is how the Devcon 7 floor was staffed in Bangkok. The Mumbai venue has a different layout, so treat it as a model for how posts are split, not as a plan. {TBC}</p>
        <div class="tbl-wrap"><table class="tbl">
          <caption>Devcon 7 posts, for reference</caption>
          <thead><tr><th>Zone</th><th>Volunteers</th><th>What they do</th></tr></thead>
          <tbody>
            <tr><td>Exits</td><td class="num">6</td><td>Two at each of three exits. Check wristbands.</td></tr>
            <tr><td>Registration area</td><td class="num">3</td><td>Send unregistered attendees to the desks and guide people coming from talks to the right doors.</td></tr>
            <tr><td>Hacker Space and Decompression Zone</td><td class="num">6</td><td>Two outside each checkpoint and one inside each room. Check wristbands and keep the rooms tidy.</td></tr>
            <tr><td>Central area (music stage and playground)</td><td class="num">3</td><td>One at the music stage, one at the playground, one between. Check wristbands and keep it tidy.</td></tr>
            <tr><td>Community hubs and impact booths</td><td class="num">3</td><td>Help the hub and booth organisers and answer their questions.</td></tr>
            <tr><td>Food stations</td><td class="num">8</td><td>Split across two stations. Spread the crowd evenly and answer questions about dietary options.</td></tr>
            <tr><td>Speaker space</td><td class="num">2</td><td>Only speakers and EF staff allowed in. Keep it tidy and help lost speakers find their rooms.</td></tr>
            <tr><td>Each of the two upper floors</td><td class="num">4</td><td>One at the co-work area and three on the walkways. Check wristbands and keep it tidy.</td></tr>
          </tbody>
        </table></div>
        <p>How to spot who belongs in the speaker space: speakers wear a speaker tag, and EF staff have "EF" noted under their pass QR code. {TBC}</p>"""),
        ("rules", "Important notes", f"""
        <ul>
          <li>Stay in constant contact with the stage volunteers so that lost speakers are spotted and sent the right way at once.</li>
          <li>Nobody sets up booths or promotional banners in the venue. The event is meant to stay sponsor neutral.</li>
          <li>If anyone hands out swag of any kind, such as t-shirts, stickers or pins, flag it immediately. Only pre-approved teams may distribute swag, under the <a href="https://devcon.org/en/code-of-conduct/" rel="noopener">code of conduct</a>.</li>
          <li>If the main stage is full for the opening or closing ceremony, send people to the stages where it is streamed.</li>
          <li>Check for wristbands. Always.</li>
        </ul>"""),
        tbc_section([
            "The Mumbai floor plan and exact post locations.",
            "How many volunteers each post needs.",
            "Food stations and dietary options on offer.",
            "How speakers and EF staff are identified.",
            "Whether the public may enter for toilets at any level, and what pass they would carry.",
        ]),
    ],
)

# ---------------------------------------------------------------- Swag Station
PAGES["swag-station"] = dict(
    pos="82% 62%",
    lede="Everyone loves swag, so your job is making sure everyone gets a piece of it. Scan, check, hand over, smile.",
    desc="Volunteer guide for the Swag Station at Devcon 8 in Mumbai: how to scan claims, the size guide and common questions.",
    sections=[
        ("basics", "The basics", f"""
        <p>Swag Station and General Floor are separate shifts. To keep your shift varied, your volunteer lead can swap you onto General Floor or send you to help your neighbours at the Info Desk. Check in and out with the Volunteer Attendance Lead at the Volunteer Room.</p>
        <h3>The Devcon 7 swag, for reference</h3>
        <div class="tbl-wrap"><table class="tbl">
          <caption>Bangkok items. The Mumbai list has not been announced. Mumbai TBC</caption>
          <thead><tr><th>Item</th><th>Cost</th><th>Sizes</th></tr></thead>
          <tbody>
            <tr><td>Ethereum Lantern</td><td>Free</td><td>One size</td></tr>
            <tr><td>Deva Herbal Inhaler</td><td>Free</td><td>One size</td></tr>
            <tr><td>Ethereum Pajama Pants</td><td>Free</td><td>Medium, XL, 2XL</td></tr>
            <tr><td>T-shirt, "Permissionless Innovation Reunion Tour"</td><td>Paid</td><td>S to XXL</td></tr>
            <tr><td>Rain coat, "Make Ethereum Cypherpunk"</td><td>Paid</td><td>S to XXL</td></tr>
          </tbody>
        </table></div>"""),
        ("scanning", "Scanning a claim", f"""
        <p>Devcon 7 used the Zupass app to track claims. {TBC}</p>
        <ol class="steps">
          <li><b>Ask them to open their pass</b><span>They bring up the Zupass screen for their swag, not their ticket.</span></li>
          <li><b>Read the result</b><span>A valid result means a first-time claim, so go and get their item.</span></li>
          <li><b>Already claimed?</b><span>The screen says so. Politely explain the item has been collected.</span></li>
          <li><b>"Invalid Ticket"</b><span>They are showing their ticket instead of their swag. Ask them to switch screens.</span></li>
        </ol>"""),
        ("sizes", "Size guide", f"""
        <p>Devcon 7 rules. Check the Mumbai boxes and labels before you rely on these. {TBC}</p>
        <ul>
          <li>Pajama pants: Small or Medium orders come from the Medium box, Large or XL from the XL box, XXL from the 2XL box.</li>
          <li>T-shirts and rain coats: sizes Small to XXL, each matching the size ordered.</li>
        </ul>"""),
        ("questions", "Questions you will get", f"""
        <div class="qa">
          <details><summary>"Can I change my t-shirt or hoodie size?"</summary><div class="ans"><p>Suggest they come back on the last day and check for unclaimed extras.</p></div></details>
          <details><summary>"I regret not ordering swag. Can I still order?"</summary><div class="ans"><p>Send them back into their order through the confirmation link to see whether any items are still available.</p></div></details>
        </div>"""),
        tbc_section([
            "The Mumbai swag items, prices and sizes.",
            "The claim app and how attendees find their swag pass.",
            "Where the Swag Station sits and how it connects to Registration.",
            "Which email holds the confirmation link attendees need.",
        ]),
    ],
)

# ---------------------------------------------------------------- Stage and Speaker
PAGES["stage-and-speaker"] = dict(
    pos="50% 40%",
    lede="Rooms, speakers and timing. You keep each session running on time and every speaker on the right stage.",
    desc="Volunteer guide for Stage and Speaker volunteers at Devcon 8 in Mumbai: room duties, presentation timings, and finding lost speakers.",
    sections=[
        ("basics", "The basics", f"""
        <p>There are many talks across the event, in rooms of two kinds. Stages are designed to feel immersive and different from one another, so they are easier to find, and each has a stage, a lectern and screens. Classrooms have a lectern, tables, chairs and whiteboards. Speakers who need extra resources, such as printed paper, must secure them beforehand, because Devcon 7 had no printers at the venue. Check in and out with the Volunteer Attendance Lead at the Volunteer Room.</p>
        <h3>The Devcon 7 rooms, for reference</h3>
        <div class="tbl-wrap"><table class="tbl">
          <caption>Bangkok layout: 6 talk rooms, 5 workshop rooms, 1 lightning room. Mumbai TBC</caption>
          <thead><tr><th>Room</th><th>Format</th><th>Capacity</th></tr></thead>
          <tbody>
            <tr><td>Main Stage</td><td>Theatre</td><td class="num">900</td></tr>
            <tr><td>Stages 1 to 6</td><td>Theatre</td><td class="num">300 to 450</td></tr>
            <tr><td>Classrooms A and B</td><td>Classroom</td><td class="num">172</td></tr>
            <tr><td>Classrooms C and D</td><td>Round tables</td><td class="num">150</td></tr>
            <tr><td>Classroom E</td><td>Large classroom</td><td class="num">150</td></tr>
            <tr><td>Breakouts 1 to 3</td><td>Mixed</td><td class="num">100 to 300</td></tr>
          </tbody>
        </table></div>"""),
        ("timings", "Presentation timings", f"""
        <p>Every session type has a fixed slot. You give time warnings and cut a speaker off if needed. Devcon 7 timings, for reference. {TBC}</p>
        <div class="tbl-wrap"><table class="tbl">
          <thead><tr><th>Session</th><th>Speaking time</th><th>Q&amp;A</th></tr></thead>
          <tbody>
            <tr><td>Lightning talk</td><td class="num">5 min</td><td class="num">2 min</td></tr>
            <tr><td>Talk</td><td class="num">10 min</td><td class="num">5 min</td></tr>
            <tr><td>Talk</td><td class="num">20 min</td><td class="num">5 min</td></tr>
            <tr><td>Panel</td><td class="num">45 min</td><td class="num">10 min</td></tr>
            <tr><td>Workshop (1h30)</td><td class="num">80 min</td><td>None</td></tr>
            <tr><td>Workshop (2h)</td><td class="num">110 min</td><td>None</td></tr>
            <tr><td>Workshop (3h)</td><td class="num">170 min</td><td>None</td></tr>
          </tbody>
        </table></div>
        <p>Speakers get a wireless microphone and a clicker for slides, and are asked to stay inside the lit speaking area so they are captured on camera for the livestream. Put them in touch with the Stage Manager before they go on.</p>"""),
        ("duties", "Your duties in the room", f"""
        <p>Volunteers in each room split into two kinds of work. The number of volunteers per room type in Devcon 7 was: Main Stage 5, talk rooms 3, lightning room 3, workshop rooms 2. {TBC}</p>
        <h3>Crowd duty</h3>
        <ul>
          <li>Tell attendees when a room is at full capacity.</li>
          <li>Tell attendees when a talk starts and stops.</li>
          <li>Keep the entrance clear.</li>
          <li>Fill seats from the front as people arrive.</li>
          <li>Keep the room quiet during the talk.</li>
        </ul>
        <h3>Speaker duty</h3>
        <ul>
          <li>Help the stage manager and the speakers set up.</li>
          <li>Watch the schedule so talks stay on time. Give warnings and cut speakers off if needed.</li>
          <li>Pass the microphone around when Q&amp;A begins.</li>
          <li>Find lost speakers. Each room's volunteers join a Telegram group with the room's stage manager, the stage and speaker management lead and the volunteer coordinator. When a speaker goes missing, that group coordinates getting them on stage in time.</li>
        </ul>"""),
        ("devices", "Translation devices", f"""
        <p>On the Main Stage, one volunteer manages loans of translation devices. Devcon 7 had devices for Malay, Thai, Vietnamese and Mandarin. {TBC}</p>
        <ol class="steps">
          <li><b>Handing out</b><span>Staff give the attendee a paper wristband and the device, and note the device number. You record the attendee's name and ticket number.</span></li>
          <li><b>Taking back</b><span>Staff cut the wristband. You mark the device as returned in the tracking sheet.</span></li>
        </ol>"""),
        tbc_section([
            "The Mumbai room list, capacities and themes.",
            "Session types and timings for Devcon 8.",
            "Volunteers per room.",
            "Languages offered on translation devices.",
            "The tracking sheet for device loans.",
        ]),
    ],
)

# ---------------------------------------------------------------- DevComms
PAGES["devcomms"] = dict(
    pos="30% 70%",
    lede="Shoot, write and share. You grow Devcon's presence on social channels and keep the press room in order.",
    desc="Volunteer guide for DevComms at Devcon 8 in Mumbai: talk highlights, attendee interviews and the press room.",
    sections=[
        ("basics", "The basics", f"""
        <p>DevComms volunteers shoot content, write content and increase Devcon's presence on social platforms such as X, Farcaster and Telegram. A group of volunteers also helps run the press room at the venue. Check in and out with the Volunteer Attendance Lead at the Volunteer Room.</p>
        <div class="callout">
          <strong>Bring your laptop</strong>
          <p>Volunteers on talk highlights need one to take notes as the talks happen.</p>
        </div>
        <p>The official accounts are on <a href="https://x.com/efdevcon" rel="noopener">X</a>, <a href="https://warpcast.com/devcon" rel="noopener">Farcaster</a> and <a href="https://www.instagram.com/efdevcon" rel="noopener">Instagram</a>.</p>"""),
        ("highlights", "Talk highlights", f"""
        <p>Two volunteers stay at the main stage at all times.</p>
        <ul>
          <li>Capture key quotes and highlights from the talks for the final recap post.</li>
          <li>Join the volunteer Telegram group and answer attendee questions. Use the <a href="info-desk.html">Info Desk guide</a> FAQ for help. {TBC}</li>
        </ul>"""),
        ("interviews", "Attendee interviews", f"""
        <p>Two volunteers move around the venue and talk to attendees about their Devcon experience.</p>
        <ul>
          <li>Always respect the privacy of attendees and of the spaces around them.</li>
          <li>Coordinate with your lead to organise what you collect. It goes to the videographer for final edits and publication.</li>
          <li>Join the volunteer Telegram group and answer attendee questions. {TBC}</li>
        </ul>"""),
        ("press", "The press room", f"""
        <p>Two volunteers stay at the press room at all times.</p>
        <ul>
          <li>Check everyone in by confirming they have a valid booking before they use the space.</li>
          <li>If someone with a booking finds the room occupied, verify the bookings and politely ask only those with a reservation to stay.</li>
          <li>Confirm everyone in the space wears a wristband, and that the room is free of swag or marketing material from any project.</li>
          <li>Help anyone who asks for help making a booking.</li>
        </ul>
        <p>Media and press enquiries go through the official form on <a href="https://devcon.org/en/" rel="noopener">devcon.org</a>.</p>"""),
        tbc_section([
            "The volunteer Telegram group and who moderates it.",
            "Where the press room is and how bookings work.",
            "Who the videographer and DevComms lead are.",
            "How many volunteers each of the three teams gets.",
        ]),
    ],
)

# ---------------------------------------------------------------- Info Desk
PAGES["info-desk"] = dict(
    pos="70% 70%",
    lede="The front line for every question. Expect anything, and be as helpful and friendly as you can.",
    desc="Volunteer guide for the Info Desk at Devcon 8 in Mumbai: the questions to expect, where to find answers, and device loans.",
    sections=[
        ("basics", "The basics", f"""
        <p>Info Desk volunteers are the front line of attendee questions. There will be approved vendors and booths for people to visit, and many questions about all of it. Check in and out with the Volunteer Attendance Lead at the Volunteer Room.</p>
        <p>If someone asks a question that is not covered here, find the answer, then tell your lead so it gets added. That way the next volunteer is ready.</p>
        <div class="callout">
          <strong>DevAI is your best friend</strong>
          <p>At Devcon 7, volunteers logged into <a href="https://app.devcon.org/" rel="noopener" style="color:var(--leaf)">app.devcon.org</a> and asked DevAI whenever they were unsure. {TBC}</p>
        </div>"""),
        ("questions", "Questions you should be ready for", f"""
        <p>These are the topics that came up most at Devcon 7. Answers change from year to year, so check the linked official pages first.</p>
        <div class="qa">
          <details><summary>General</summary><div class="ans">
            <ul>
              <li>Are there meeting rooms to book, and what are discussion corners? See the <a href="meeting-rooms.html">Meeting Rooms guide</a>.</li>
              <li>Are other events planned? See the side events list on the <a href="../index.html#resources">Resources</a> section.</li>
              <li>How can I contribute or sponsor? See the <a href="https://devcon.org/en/supporters/" rel="noopener">Supporters programme</a>.</li>
              <li>How do I get a press pass? Media and press enquiries go through the official form on <a href="https://devcon.org/en/" rel="noopener">devcon.org</a>.</li>
              <li>Where can I see talks from past Devcons? The <a href="https://archive.devcon.org/" rel="noopener">Devcon Archive</a>.</li>
              <li>Which language are talks in? Is there Wi-Fi? Where is the map? {TBC}</li>
              <li>The opening ceremony is on and the main stage is full. Where do I go? Send them to the stages where it is streamed.</li>
            </ul>
          </div></details>
          <details><summary>Tickets</summary><div class="ans">
            <ul>
              <li>Are tickets sold out, and can I still attend?</li>
              <li>Can I pay with ETH or DAI?</li>
              <li>Are there discounted tickets, and what are the refund and transfer rules?</li>
              <li>Are there day passes or on-site sales?</li>
            </ul>
            <p>Point everyone to the official <a href="https://devcon.org/en/tickets/faq/" rel="noopener">ticket FAQ</a>, which is always current.</p>
          </div></details>
          <details><summary>Getting around Mumbai</summary><div class="ans">
            <ul>
              <li>How do I get from the airport to the venue?</li>
              <li>Where is Devcon taking place, and is Mumbai safe?</li>
              <li>What is the weather like, do locals speak English, what is the food like, and is the tap water safe?</li>
              <li>How do I tip?</li>
            </ul>
            <p>The <a href="https://devcon.org/en/travel-guide/" rel="noopener">official travel guide</a> covers most of these, and the <a href="../index.html#travel">travel section</a> has the short version.</p>
          </div></details>
          <details><summary>Community</summary><div class="ans">
            <ul>
              <li>Where can I meet the Ethereum community in India? Start with the Community Hubs and the <a href="https://forum.devcon.org/" rel="noopener">Devcon Forum</a>.</li>
            </ul>
          </div></details>
        </div>"""),
        ("devices", "Headset loans", f"""
        <p>At Devcon 7, the Info-hub volunteers on each level managed borrowing of headsets for the Community Hubs on that level. {TBC}</p>
        <ol class="steps">
          <li><b>Handing out</b><span>Staff give the attendee a paper wristband and the device, and note the device number. You record the attendee's name and ticket number.</span></li>
          <li><b>Taking back</b><span>Staff cut the wristband. You mark the device as returned in the tracking sheet.</span></li>
        </ol>"""),
        ("hunt", "Treasure hunt", f"""
        <p>Devcon 7 ran a treasure hunt with volunteers playing NPCs. Whether Devcon 8 has one, and what the instructions are, has not been shared. {TBC}</p>"""),
        tbc_section([
            "The Info Desk and Info-hub locations.",
            "Whether the Devcon app and DevAI are available.",
            "Wi-Fi details and the language of talks.",
            "The device loan tracking sheet.",
            "Treasure hunt instructions, if there is one.",
        ]),
    ],
)

# ---------------------------------------------------------------- Meeting Rooms
PAGES["meeting-rooms"] = dict(
    pos="40% 62%",
    lede="Meeting rooms and discussion corners, booked ahead. You answer booking questions and manage access.",
    desc="Volunteer guide for Meeting Room volunteers at Devcon 8 in Mumbai: how bookings work and how to manage access.",
    sections=[
        ("basics", "The basics", f"""
        <p>Devcon 7 offered 11 meeting rooms and 4 discussion corners for attendees to book, plus 3 meeting rooms reserved for EF staff. {TBC} As a Meeting Room volunteer you are on the front line, answering booking questions and managing access. Check in and out with the Volunteer Attendance Lead at the Volunteer Room.</p>"""),
        ("rooms", "How meeting room bookings work", f"""
        <p>Devcon 7 used a booking page at reserve.devcon.org. {TBC}</p>
        <ol class="steps">
          <li><b>Read about the space</b><span>The booking page shows each space's capacity, layout and what comes with it. Read the rules of the space.</span></li>
          <li><b>Choose a room</b><span>In the meeting room section, select the room number to book.</span></li>
          <li><b>Pick a slot</b><span>A calendar booking system shows the free slots for the day.</span></li>
          <li><b>Show the invite</b><span>After submitting, the booker gets an email with a calendar invite. They show it to the volunteers at the meeting room desk and take the space.</span></li>
        </ol>"""),
        ("corners", "How discussion corners work", f"""
        <p>Discussion corners had a two-step process at Devcon 7. {TBC}</p>
        <ol class="steps">
          <li><b>Fill in the form</b><span>The booker submits a request form from the booking page.</span></li>
          <li><b>Lead reviews</b><span>The volunteer lead reviews the request. If approved, the booker receives an email with booking links.</span></li>
          <li><b>Book a slot</b><span>The email has a personal link for each colour-coded corner. The booker adds a 3 to 4 line description of the session and the organising entity.</span></li>
        </ol>
        <p>The link is for that booker only and must not be shared. They can make at most two consecutive bookings with it, and extra bookings are deleted from the calendar.</p>"""),
        ("duties", "Your responsibilities", f"""
        <ul>
          <li>Check everyone in by confirming they have a valid booking before they use the space.</li>
          <li>If someone with a booking finds the room occupied, verify the bookings and politely ask only those with a reservation to stay.</li>
          <li>Confirm everyone in the space wears a wristband, and that the room has no swag or marketing material from any project.</li>
          <li>Help anyone who asks for help making a booking.</li>
        </ul>"""),
        tbc_section([
            "The Devcon 8 booking site and how bookings are made.",
            "The number of meeting rooms and discussion corners, and any reserved for EF.",
            "Where the meeting room desk sits.",
            "Who reviews discussion corner requests.",
        ]),
    ],
)


def toc_html(sections):
    lis = "\n".join(f'        <li><a href="#{sid}">{title}</a></li>' for sid, title, _ in sections)
    return f"""<aside class="toc" aria-label="On this page">
      <h2>On this page</h2>
      <ol>
{lis}
      </ol>
    </aside>"""


def pager(slug):
    i = [s for s, _ in ORDER].index(slug)
    parts = []
    if i > 0:
        ps, pn = ORDER[i - 1]
        parts.append(f'<a class="pill ghost" href="{ps}.html">&larr; {pn}</a>')
    else:
        parts.append("<span></span>")
    parts.append('<a class="pill ghost" href="../index.html#roles">All roles</a>')
    if i < len(ORDER) - 1:
        ns, nn = ORDER[i + 1]
        parts.append(f'<a class="pill" href="{ns}.html">{nn} &rarr;</a>')
    else:
        parts.append("<span></span>")
    inner = "\n    ".join(parts)
    return f'<div class="wrap pager">\n    {inner}\n  </div>'


def build(slug, name, data, num):
    body = "\n\n".join(
        f'      <section id="{sid}">\n        <h2>{title}</h2>{html}\n      </section>'
        for sid, title, html in data["sections"]
    )
    main = f"""<main id="main">
  <section class="page-hero">
    <img class="page-hero-img" src="../images/volunteeringatdevcon8-devcon7-sea-volunteers-hero.webp" width="1280" height="852" alt="" style="--pos:{data['pos']}" fetchpriority="high">
    <div class="wrap">
      <p class="crumbs"><a href="../index.html">Home</a> / <a href="../index.html#roles">Roles</a> / {name}</p>
      <p class="eyebrow">Role {num:02d}</p>
      <h1>{name}</h1>
      <p class="lede">{data['lede']}</p>
    </div>
  </section>

  <div class="wrap doc">
    {toc_html(data['sections'])}

    <div class="prose">
{body}
    </div>
  </div>

  {pager(slug)}
</main>"""
    page = re.sub(r"<title>.*?</title>", f"<title>{name} Guide | Volunteering at Devcon 8</title>", tpl, flags=re.S)
    page = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{data["desc"]}">', page, flags=re.S)
    page = re.sub(r"<main id=\"main\">.*?</main>", lambda m: main, page, flags=re.S)
    return page


for idx, (slug, name) in enumerate(ORDER, start=1):
    if slug == "registration":
        continue
    out = ROOT / "roles" / f"{slug}.html"
    out.write_text(build(slug, name, PAGES[slug], idx), encoding="utf-8")
    print("wrote", out.name)

# patch the Registration pager (its content is hand-written, so only the pager changes)
reg = ROOT / "roles" / "registration.html"
txt = reg.read_text(encoding="utf-8")
new = pager("registration")
txt = re.sub(r'<div class="wrap pager">.*?</div>', lambda m: new, txt, count=1, flags=re.S)
reg.write_text(txt, encoding="utf-8")
print("patched registration pager")
