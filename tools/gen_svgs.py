"""Generate the SVG visuals for the guardiano3/.github org profile README."""
import os
import sys
import textwrap

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace"
NAVY, BG, BLUE, CYAN, GREEN = "#0b1e33", "#060d16", "#1e88e5", "#22d3ee", "#34d97a"
TEXT, MUTED, LINE = "#f3f7fb", "#90a4bb", "#1c3653"
AMBER, ORANGE, RED = "#fbbf24", "#fb923c", "#f43f5e"


def card_defs(w, h, uid):
    return f"""
  <defs>
    <linearGradient id="bg{uid}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#081626"/><stop offset="1" stop-color="{NAVY}"/>
    </linearGradient>
    <linearGradient id="edge{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}" stop-opacity=".55"/>
      <stop offset=".5" stop-color="{CYAN}" stop-opacity=".25"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity=".55"/>
    </linearGradient>
    <linearGradient id="brand{uid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{BLUE}"/><stop offset=".55" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/>
    </linearGradient>
    <radialGradient id="glow{uid}" cx=".5" cy=".5" r=".5">
      <stop offset="0" stop-color="{CYAN}" stop-opacity=".9"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid{uid}" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#ffffff" stroke-opacity=".035"/>
    </pattern>
  </defs>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#bg{uid})"/>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="url(#grid{uid})"/>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="22" fill="none" stroke="url(#edge{uid})" stroke-width="1.5"/>"""


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{label}" font-family="{FONT}">\n<title>{label}</title>{body}\n</svg>\n')


def write(name, content):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(name, len(content.encode()), "bytes")


def eyebrow(x, y, text, uid):
    return (f'<circle cx="{x+4}" cy="{y-5}" r="4" fill="url(#brand{uid})"/>'
            f'<text x="{x+16}" y="{y}" fill="{MUTED}" font-size="13" font-weight="600" letter-spacing="2.5">{text}</text>')


# ---------------------------------------------------------------- icons
SHIELD = (f'<path d="M0 -16L13 -11V-1C13 8 7 13 0 16C-7 13 -13 8 -13 -1V-11Z" fill="none" stroke="{TEXT}" stroke-width="2.2" stroke-linejoin="round"/>'
          f'<path d="M-5 0l4 4l7 -8" fill="none" stroke="{GREEN}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')


# ---------------------------------------------------------------- feature cards
FEATURE_ICONS = {
    "bolt": f'<path d="M3 -15L-9 3h8l-3 13l13 -19h-8z" fill="none" stroke="{TEXT}" stroke-width="2.2" stroke-linejoin="round"/>',
    "layers": f'<path d="M0 -13l14 7l-14 7l-14 -7z" fill="none" stroke="{TEXT}" stroke-width="2.2" stroke-linejoin="round"/>'
              f'<path d="M-14 1l14 7l14 -7M-14 8l14 7l14 -7" fill="none" stroke="{CYAN}" stroke-width="2" stroke-linejoin="round"/>',
    "chat": f'<path d="M-14 -11h28v18h-15l-8 7v-7h-5z" fill="none" stroke="{TEXT}" stroke-width="2.2" stroke-linejoin="round"/>'
            f'<path d="M-8 -3h16M-8 2h10" stroke="{CYAN}" stroke-width="2" stroke-linecap="round"/>',
    "globe": f'<circle r="14" fill="none" stroke="{TEXT}" stroke-width="2.2"/>'
             f'<path d="M-14 0h28M0 -14c-7 8 -7 20 0 28M0 -14c7 8 7 20 0 28" fill="none" stroke="{CYAN}" stroke-width="1.8"/>',
    "code": f'<path d="M-7 -9l-9 9l9 9M7 -9l9 9l-9 9" fill="none" stroke="{TEXT}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M3 -13l-6 26" stroke="{CYAN}" stroke-width="2.2" stroke-linecap="round"/>',
    "hand": SHIELD,
}


def features():
    cards = [
        ("bolt", "Decisions while it matters",
         "A decision streams back for each chunk of audio, while the session is still live and before money moves."),
        ("chat", "Every score explained",
         "Each decision carries a 0–100 score, a risk level, the scam type and plain-language reasons your team can act on."),
        ("globe", "Built for scam pressure",
         "Impersonation, safe-account transfers, one-time-code requests and remote-access tricks: the scripts scammers really use."),
        ("layers", "Text and audio",
         "Score a message or transcript, analyse a recording, or stream a live session."),
        ("code", "API-first",
         "One versioned /v1 contract, API-key auth, a stable error envelope and a request ID on every response."),
        ("hand", "You own the action",
         "GuardianO3 never contacts your customer. Your systems decide: hold the transfer, warn, or escalate to a fraud team."),
    ]
    w, h, uid = 1200, 600, "f"
    cw, ch, gap, mx, my = 356, 236, 26, 40, 92
    b = [card_defs(w, h, uid)]
    b.append(eyebrow(40, 56, "WHY GUARDIANO3", uid))
    for i, (icon, title, body) in enumerate(cards):
        col, row = i % 3, i // 3
        x, y = mx + col * (cw + gap), my + row * (ch + gap)
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="18" fill="{BG}" fill-opacity=".6" stroke="{LINE}"/>')
        b.append(f'<rect x="{x}" y="{y}" width="{cw}" height="3" rx="1.5" fill="url(#brand{uid})" opacity=".85"/>')
        b.append(f'<circle cx="{x+46}" cy="{y+54}" r="26" fill="{NAVY}" stroke="url(#brand{uid})" stroke-width="1.6"/>')
        b.append(f'<g transform="translate({x+46} {y+54})">{FEATURE_ICONS[icon]}</g>')
        b.append(f'<text x="{x+24}" y="{y+116}" fill="{TEXT}" font-size="19" font-weight="700">{title}</text>')
        for k, ln in enumerate(textwrap.wrap(body, 42)):
            b.append(f'<text x="{x+24}" y="{y+146+k*22}" fill="{MUTED}" font-size="15">{ln}</text>')
    write("features.svg", svg(w, h, "\n".join(b), "Why GuardianO3: decisions while the session is live; "
          "every score explained; built for scam pressure; text and audio; API-first; you own the action"))


# ---------------------------------------------------------------- buttons, divider, footer
def button(name, label, icon, primary):
    w, h = 210, 48
    fill = 'fill="url(#g)"' if primary else f'fill="{NAVY}"'
    stroke = "" if primary else f' stroke="{BLUE}" stroke-opacity=".7" stroke-width="1.5"'
    color = BG if primary else TEXT
    icons = {
        "globe": f'<circle r="8" fill="none" stroke="{color}" stroke-width="1.8"/><path d="M-8 0h16M0 -8c-4 5 -4 11 0 16M0 -8c4 5 4 11 0 16" fill="none" stroke="{color}" stroke-width="1.5"/>',
        "key": f'<circle cx="-4" cy="0" r="5" fill="none" stroke="{color}" stroke-width="1.8"/><path d="M1 0h9M6 0v4M9 0v3" stroke="{color}" stroke-width="1.8" stroke-linecap="round"/>',
        "mail": f'<rect x="-9" y="-6" width="18" height="12" rx="2" fill="none" stroke="{color}" stroke-width="1.8"/><path d="M-9 -5l9 6l9 -6" fill="none" stroke="{color}" stroke-width="1.6"/>',
    }
    body = f"""
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{BLUE}"/><stop offset=".55" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/>
  </linearGradient></defs>
  <rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{(h-2)/2}" {fill}{stroke}/>
  <g transform="translate(42 24)">{icons[icon]}</g>
  <text x="62" y="30" fill="{color}" font-size="16" font-weight="700">{label}</text>"""
    write(name, svg(w, h, body, label))


def divider():
    w, h = 1200, 28
    body = f"""
  <defs><linearGradient id="d" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{BLUE}" stop-opacity="0"/><stop offset=".25" stop-color="{BLUE}"/>
    <stop offset=".5" stop-color="{CYAN}"/><stop offset=".75" stop-color="{GREEN}"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
  </linearGradient>
  <radialGradient id="dg"><stop offset="0" stop-color="#ffffff"/><stop offset=".35" stop-color="{CYAN}" stop-opacity=".8"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient></defs>
  <rect x="0" y="13" width="{w}" height="2" fill="url(#d)" opacity=".7"/>
  <ellipse rx="60" ry="9" cy="14" fill="url(#dg)"><animate attributeName="cx" values="200;1000;200" dur="7s" repeatCount="indefinite"/></ellipse>"""
    write("divider.svg", svg(w, h, body, "divider"))


def footer():
    w, h = 1200, 170
    body = f"""
  <defs><linearGradient id="fw" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="{BLUE}"/><stop offset=".55" stop-color="{CYAN}"/><stop offset="1" stop-color="{GREEN}"/>
  </linearGradient></defs>
  <path d="M0 70 C 200 30, 400 110, 600 70 S 1000 30, 1200 70 V170 H0Z" fill="url(#fw)" opacity=".18">
    <animate attributeName="d" dur="9s" repeatCount="indefinite" values="
      M0 70 C 200 30, 400 110, 600 70 S 1000 30, 1200 70 V170 H0Z;
      M0 80 C 200 110, 400 40, 600 80 S 1000 110, 1200 60 V170 H0Z;
      M0 70 C 200 30, 400 110, 600 70 S 1000 30, 1200 70 V170 H0Z"/></path>
  <path d="M0 95 C 250 60, 450 130, 700 95 S 1050 60, 1200 95 V170 H0Z" fill="url(#fw)" opacity=".28"/>
  <path d="M0 120 C 300 95, 500 150, 800 120 S 1100 100, 1200 118 V170 H0Z" fill="{NAVY}"/>
  <text x="600" y="152" text-anchor="middle" fill="{TEXT}" font-size="15" font-weight="700" letter-spacing="5">OBSERVE · ORIENT · OVERRIDE</text>"""
    write("footer.svg", svg(w, h, body, "Observe, Orient, Override"))


features()
button("btn-website.svg", "Website", "globe", True)
button("btn-console.svg", "Get an API key", "key", False)
button("btn-contact.svg", "Contact us", "mail", False)
divider()
footer()
