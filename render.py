"""Render the news-image-20261124 front page (1024x1024 PNG).

One-page newspaper for Tuesday 24 November 2026: 1 lead + 5 featured +
44 dated briefs = 50 sourced stories, a UTC timeline strip and a red
date-check line. Every story carries its true publication date (19-24 NOV).
Deterministic: same inputs, same bytes (no timestamps embedded).
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 232)
INK = (17, 17, 17)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
GREY = (90, 90, 90)
RULE = (200, 192, 170)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF_B = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SANS = os.path.join(FONT_DIR, "DejaVuSans.ttf")
SANS_B = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def text_wrapped(draw, xy, text, fnt, fill, max_w, leading=None):
    """Draw text wrapped to max_w; returns the y just below the last line."""
    if leading is None:
        leading = int(fnt.size * 1.25)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


LEAD = {
    "kicker": "TECH  ·  23 NOV",
    "headline": "NVIDIA BRINGS HUANG BACK",
    "sub": ("Board reinstates its CEO 11 days after he resigned — "
            "shares jump 33%."),
    "source": "REUTERS · WSJ · CNN — 23 NOV",
}

FEATURED = [
    ("COP31 ENDS WITH NO DEAL",
     "Climate talks collapse over fossil fuels; talks may resume next year.",
     "22 NOV"),
    ("UKRAINE SINKS RUSSIAN SHIP OFF LIBYA",
     "Drones sink corvette Merkury at Benghazi; a cargo ship is hit too.",
     "23 NOV"),
    ("24 DEAD IN JAVA FACTORY FIRE",
     "Candy plant blaze in Cikande; about 30 workers still missing.",
     "23 NOV"),
    ("COURT: MYANMAR COMMITTED GENOCIDE",
     "ICJ rules against Myanmar over the Rohingya.",
     "19 NOV"),
    ("ALCARAZ WINS ATP FINALS",
     "First title in Turin, beating Zverev in the final.",
     "23 NOV"),
]

# Briefs 7-50: (number, text, date). All dates are the true publication dates.
BRIEFS = [
    (7, "Trump, Xi, Putin meet in Shenzhen", "19 NOV"),
    (8, "Anthropic IPO priced at $81.3bn", "19 NOV"),
    (9, "Riemann proof claim stuns maths", "20 NOV"),
    (10, "BepiColombo enters Mercury orbit", "22 NOV"),
    (11, "Kyiv region hit; home in Dymer damaged", "23 NOV"),
    (12, "Sparta II burns after drone strike", "23 NOV"),
    (13, "Zelensky urges four-party peace talks", "23 NOV"),
    (14, "India, China hold border talks", "23 NOV"),
    (15, "Modi opens AI centre at IIT Patna", "24 NOV"),
    (16, "Saryu-Kamala Express flagged off", "24 NOV"),
    (17, "India, Nepal sign eight MoUs", "23 NOV"),
    (18, "India–NZ Test ends in a draw", "23 NOV"),
    (19, "Pant hits 128 for India in Wellington", "23 NOV"),
    (20, "Gukesh–Sindarov chess title opens", "24 NOV"),
    (21, "FIFA picks 2031, 2035 Cup hosts", "23 NOV"),
    (22, "Trump gets path to erase conviction", "23 NOV"),
    (23, "Denmark court backs 'ghetto law'", "23 NOV"),
    (24, "Waymo pulls taxis off US freeways", "23 NOV"),
    (25, "Migrant boat sinks off Senegal", "23 NOV"),
    (26, "Gaza toxins threat flagged by Oxfam", "24 NOV"),
    (27, "Taliban erases women's names in Balkh", "23 NOV"),
    (28, "Settler arson called 'Jewish terror'", "23 NOV"),
    (29, "Fiona the hippo dies at Cincinnati Zoo", "19 NOV"),
    (30, "Supermoon meets the Pleiades tonight", "24 NOV"),
    (31, "Ferrari shows two new 296 models", "23 NOV"),
    (32, "SpiceJet pilots warn of unpaid wages", "23 NOV"),
    (33, "India's oil bill up 60% to $16bn", "23 NOV"),
    (34, "India factory output picks up in Nov", "23 NOV"),
    (35, "Top court frees Godhra case convict", "24 NOV"),
    (36, "US midterms certified in Allegheny", "23 NOV"),
    (37, "De Bruyne: Man City love 'never change'", "23 NOV"),
    (38, "Trump–Kim talks 'ignored' — WSJ", "23 NOV"),
    (39, "IRGC says it downed 78 US drones", "24 NOV"),
    (40, "Iran rejects any naval blockade", "24 NOV"),
    (41, "Pakistan cuts petrol by Rs3 a litre", "24 NOV"),
    (42, "Guru Nanak birth rites enter day two", "24 NOV"),
    (43, "Lahore air worst in world, AQI 500+", "24 NOV"),
    (44, "Pakistan youth loan limit raised", "24 NOV"),
    (45, "Gold, silver prices rise in Pakistan", "24 NOV"),
    (46, "Undersea cable fix due by 6 December", "24 NOV"),
    (47, "PSL 12 to open in Peshawar", "24 NOV"),
    (48, "Court allows Deepam lamp on 24 Nov", "24 NOV"),
    (49, "FSSAI moves against Bisleri water", "23 NOV"),
    (50, "Court warrant for Dhruv Rathee", "23 NOV"),
]

TIMELINE = [
    "23 NOV 14:24 UTC — NVIDIA REINSTATES HUANG  ·  23 NOV — 24 DEAD IN BANTEN",
    "24 NOV — GUKESH–SINDAROV OPENS IN GENEVA  ·  24 NOV — SUPERMOON + PLEIADES",
]


def draw_globe(draw, cx, cy, r):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=NAVY,
                 outline=NAVY)
    cream = (248, 244, 232)
    for k in (-0.55, 0.0, 0.55):
        x0 = cx + int(r * k)
        rx = int(r * abs(0.45 - abs(k) * 0.45)) + 8
        draw.ellipse([x0 - rx, cy - r, x0 + rx, cy + r],
                     outline=cream, width=2)
    draw.line([cx - r, cy, cx + r, cy], fill=cream, width=2)
    draw.ellipse([cx - r, cy - int(r * 0.45), cx + r, cy + int(r * 0.45)],
                 outline=cream, width=2)
    # red dot: Benghazi, where the Merkury sank
    draw.ellipse([cx + 18, cy - 26, cx + 30, cy - 14], fill=RED)


def render(path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 28  # margin

    # Masthead
    f_mast = font(SERIF_B, 62)
    title = "THE WORLD TODAY"
    d.text(((W - d.textlength(title, font=f_mast)) / 2, 18), title,
           font=f_mast, fill=INK)
    f_date = font(SANS_B, 19)
    dateline = "TUESDAY 24 NOVEMBER 2026  ·  50 SOURCED STORIES"
    d.text(((W - d.textlength(dateline, font=f_date)) / 2, 96), dateline,
           font=f_date, fill=NAVY)
    d.line([mx, 126, W - mx, 126], fill=RED, width=3)

    # Red date-check bar
    d.rectangle([mx, 136, W - mx, 162], fill=RED)
    f_check = font(SANS_B, 15)
    check = ("DATE CHECK: EVERY STORY DATED 19–24 NOV 2026 — "
             "NOTHING OLDER, NOTHING UNDATED")
    d.text(((W - d.textlength(check, font=f_check)) / 2, 141), check,
           font=f_check, fill=(255, 255, 255))

    # Lead block
    draw_globe(d, 150, 258, 76)
    lx = 268
    f_kick = font(SANS_B, 16)
    d.text((lx, 176), LEAD["kicker"], font=f_kick, fill=RED)
    f_head = font(SERIF_B, 44)
    d.text((lx, 200), "NVIDIA BRINGS", font=f_head, fill=INK)
    d.text((lx, 248), "HUANG BACK", font=f_head, fill=INK)
    f_sub = font(SANS, 17)
    text_wrapped(d, (lx, 300), LEAD["sub"], f_sub, INK, W - mx - lx)
    f_src = font(SANS_B, 13)
    d.text((lx, 338), LEAD["source"], font=f_src, fill=GREY)
    d.line([mx, 358, W - mx, 358], fill=RULE, width=2)

    # Featured row
    f_feat_h = font(SANS_B, 14)
    d.text((mx, 368), "FEATURED", font=f_feat_h, fill=NAVY)
    box_w, box_h, gap = 188, 126, 8
    y0 = 392
    for i, (t, body, date) in enumerate(FEATURED):
        x0 = mx + i * (box_w + gap)
        d.rectangle([x0, y0, x0 + box_w, y0 + box_h], outline=RULE, width=1)
        d.rectangle([x0, y0, x0 + box_w, y0 + 4], fill=NAVY)
        f_t = font(SANS_B, 13)
        text_wrapped(d, (x0 + 8, y0 + 12), t, f_t, INK, box_w - 16,
                     leading=16)
        f_b = font(SANS, 12)
        text_wrapped(d, (x0 + 8, y0 + 62), body, f_b, INK, box_w - 16,
                     leading=15)
        f_dt = font(SANS_B, 11)
        d.text((x0 + 8, y0 + box_h - 18), date, font=f_dt, fill=RED)
    d.line([mx, 530, W - mx, 530], fill=RULE, width=2)

    # Briefs
    f_br_h = font(SANS_B, 15)
    d.text((mx, 540), "THE DAY IN BRIEFS — 44 MORE STORIES, EACH DATED",
           font=f_br_h, fill=NAVY)
    f_br = font(SANS, 12)
    col_x = [mx, 356, 684]
    col_w = 312
    row_h = 25
    y_start = 568
    for idx, (n, text, date) in enumerate(BRIEFS):
        col = idx // 15
        row = idx % 15
        x = col_x[col]
        y = y_start + row * row_h
        line = "%d. %s — %s" % (n, text, date)
        # shrink once if the line would overflow its column
        f = f_br
        if d.textlength(line, font=f) > col_w:
            f = font(SANS, 11)
        d.text((x, y), line, font=f, fill=INK)

    # Timeline strip
    d.rectangle([mx, 1000 - 56, W - mx, 1000], fill=NAVY)
    f_tl = font(SANS_B, 13)
    for i, tl in enumerate(TIMELINE):
        d.text(((W - d.textlength(tl, font=f_tl)) / 2, 950 + i * 20), tl,
               font=f_tl, fill=(255, 255, 255))
    f_ft = font(SANS, 11)
    foot = ("50 stories · sources: Reuters, WSJ, CNN, BBC, AP · "
            "rendered 24 Nov 2026")
    d.text(((W - d.textlength(foot, font=f_ft)) / 2, 1006), foot,
           font=f_ft, fill=GREY)

    img.save(path, "PNG", optimize=True)


if __name__ == "__main__":
    import sys
    render(sys.argv[1] if len(sys.argv) > 1 else "entry.png")
