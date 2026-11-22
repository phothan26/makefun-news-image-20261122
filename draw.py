"""Draw the front page for Sunday 22 November 2026 with PIL.

Pure vector drawing + DejaVu text, deterministic: same bytes every run.
Every line is measured before it is drawn; the script raises if any text
would overflow its box, so a truncated headline can never slip through.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (25, 25, 25)
MUTED = (90, 84, 72)
RED = (163, 22, 33)
NAVY = (31, 42, 68)
RULE = (180, 172, 155)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, s, f, max_w):
    """Greedy word wrap; raises if a single word is too wide."""
    words = s.split(" ")
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, f) <= max_w:
            cur = trial
        else:
            if not cur:
                raise ValueError(f"word too wide: {w!r}")
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, lines, f, x, y, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=f, fill=fill)
        y += leading
    return y


def panel(draw, box, num, kicker, headline, body, accent, pic, head_size=27):
    x0, y0, x1, y1 = box
    draw.rectangle(box, outline=RULE, width=2)
    draw.rectangle([x0, y0, x1, y0 + 30], fill=accent)
    draw.text((x0 + 10, y0 + 5), f"{num}", font=font(SANS_B, 17), fill=(255, 255, 255))
    draw.text((x0 + 34, y0 + 7), kicker, font=font(SANS_B, 13), fill=(255, 255, 255))
    # pictogram top-right of the header bar
    pic(draw, x1 - 44, y0 - 2)
    hx, hy = x0 + 12, y0 + 40
    hw = (x1 - x0) - 24
    hf = font(SERIF, head_size)
    hl = wrap(draw, headline, hf, hw)
    if len(hl) > 2:
        raise ValueError(f"headline needs {len(hl)} lines: {headline!r}")
    hy = draw_wrapped(draw, hl, hf, hx, hy, INK, head_size + 6)
    bf = font(SANS, 15)
    bl = wrap(draw, body, bf, hw)
    if hy + len(bl) * 20 > y1 - 8:
        raise ValueError(f"body overflows panel {num}: {len(bl)} lines")
    draw_wrapped(draw, bl, bf, hx, hy + 6, (50, 48, 44), 20)


# --- pictograms (small, drawn in the header bar, white on accent) ---
def pic_globe(d, x, y):
    d.ellipse([x + 6, y + 4, x + 30, y + 28], outline=(255, 255, 255), width=2)
    d.ellipse([x + 14, y + 4, x + 22, y + 28], outline=(255, 255, 255), width=1)
    d.line([x + 6, y + 16, x + 30, y + 16], fill=(255, 255, 255), width=1)


def pic_flame(d, x, y):
    d.polygon([(x + 18, y + 4), (x + 26, y + 16), (x + 30, y + 24),
               (x + 22, y + 30), (x + 12, y + 30), (x + 8, y + 22),
               (x + 12, y + 14)], fill=(255, 255, 255))


def pic_paper(d, x, y):
    d.rectangle([x + 9, y + 5, x + 27, y + 29], outline=(255, 255, 255), width=2)
    for i, yy in enumerate((11, 17, 23)):
        d.line([x + 13, y + yy, x + 23, y + yy], fill=(255, 255, 255), width=2)


def pic_bolt(d, x, y):
    d.polygon([(x + 20, y + 4), (x + 10, y + 18), (x + 17, y + 18),
               (x + 14, y + 30), (x + 26, y + 15), (x + 19, y + 15)],
              fill=(255, 255, 255))


def pic_boat(d, x, y):
    d.polygon([(x + 6, y + 20), (x + 30, y + 20), (x + 26, y + 28),
               (x + 10, y + 28)], fill=(255, 255, 255))
    d.line([x + 18, y + 6, x + 18, y + 20], fill=(255, 255, 255), width=2)
    d.polygon([(x + 18, y + 6), (x + 28, y + 17), (x + 18, y + 17)],
              fill=(255, 255, 255))


def pic_shield(d, x, y):
    d.polygon([(x + 18, y + 4), (x + 29, y + 9), (x + 29, y + 19),
               (x + 18, y + 30), (x + 7, y + 19), (x + 7, y + 9)],
              outline=(255, 255, 255), width=2)
    d.line([x + 12, y + 16, x + 16, y + 21], fill=(255, 255, 255), width=2)
    d.line([x + 16, y + 21, x + 25, y + 11], fill=(255, 255, 255), width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin
    # masthead
    title = "THE WORLD TODAY"
    tf = font(SERIF, 58)
    tw = text_w(d, title, tf)
    d.text(((W - tw) / 2, 16), title, font=tf, fill=INK)
    df = font(SANS_B, 21)
    date = "SUNDAY 22 NOVEMBER 2026"
    dw = text_w(d, date, df)
    d.text(((W - dw) / 2, 88), date, font=df, fill=RED)
    d.line([M, 122, W - M, 122], fill=INK, width=3)
    d.line([M, 127, W - M, 127], fill=INK, width=1)

    # lead panel: COP31
    panel(d, (M, 140, W - M, 362), 1, "CLIMATE  ·  ANTALYA, TURKEY",
          "COP31 TALKS IN OVERTIME FOR A SECOND DAY",
          "UN climate talks ran into a second day of overtime on Sunday. The latest "
          "draft still does not name fossil fuels, and a $120bn adaptation target for "
          "poorer nations was cut. Delegates must object by a deadline or the text is "
          "adopted on Sunday morning. Summit president Murat Kurum called it a text "
          "all parties can agree on; developing nations were angered by the cut.",
          (18, 90, 80), pic_globe, head_size=33)

    # row of three
    y2, y3 = 376, 600
    w3 = (W - 2 * M - 2 * 14) // 3
    panel(d, (M, y2, M + w3, y3), 2, "DISASTER  ·  SERANG, BANTEN",
          "3 DEAD, 39 MISSING IN FACTORY FIRE",
          "A fire at a candy factory killed three people. At least 39 are missing as "
          "rescuers search the site west of Jakarta; part of the roof collapsed.",
          (163, 60, 32), pic_flame, head_size=24)
    panel(d, (M + w3 + 14, y2, M + 2 * w3 + 14, y3), 3, "SOUTH KOREA  ·  SEOUL",
          "MINISTER QUITS IN AI CHEAT SCANDAL",
          "Education minister Choi Kyo-jin offered to resign on Sunday, after a top "
          "exam scorer was caught using a miniature camera and AI.",
          (31, 42, 68), pic_paper, head_size=24)
    panel(d, (M + 2 * w3 + 28, y2, W - M, y3), 4, "ENERGY  ·  TEHRAN",
          "IRAN STARTS POWER RATIONING",
          "Planned blackouts began on Sunday, about two hours every two days, as the "
          "war strains Iran's energy network. The blockade of the Gulf has passed 130 days.",
          (120, 84, 20), pic_bolt, head_size=24)

    # row of two
    y4, y5 = 614, 838
    w2 = (W - 2 * M - 14) // 2
    panel(d, (M, y4, M + w2, y5), 5, "DISASTER  ·  SOUTHERN NIGERIA",
          "NIGERIA BOAT SINKS, 24 DEAD",
          "A boat carrying mourners to a funeral capsized in southern Nigeria. At least "
          "24 people died and 24 were rescued. The driver fled; the boat's manager was "
          "taken into custody. Boat accidents are common on Nigeria's waterways, where "
          "overloaded vessels often capsize.",
          (90, 60, 110), pic_boat)
    panel(d, (M + w2 + 14, y4, W - M, y5), 6, "CONFLICT  ·  SAUDI ARABIA",
          "HOUTHIS FIRE MISSILES AT RIYADH",
          "Saudi Arabia said it intercepted three missiles fired at Riyadh, and a "
          "coalition said it stopped another aimed at the west. The Houthis denied "
          "threatening Mecca. The coalition said its strikes hit 71 targets in 24 hours.",
          (140, 40, 40), pic_shield)

    # footer band
    fx0, fy0, fx1, fy1 = M, 852, W - M, 996
    d.rectangle([fx0, fy0, fx1, fy1], fill=NAVY)
    d.text((fx0 + 14, fy0 + 8), "ALSO TODAY", font=font(SANS_B, 14),
           fill=(255, 210, 90))
    items = [
        ("MARKETS", "Nasdaq \u22125.3%, S&P 500 \u22123.7% to 6,910 in Friday's AI "
                    "sell-off, the worst week since March 2020."),
        ("EU\u2013INDONESIA DEAL", "Trade pact signed after a decade of talks; 98.5% "
                    "of tariffs lifted, covering 730m people."),
        ("FBI DATABASE HACKED", "The FBI is investigating a breach of its national "
                    "crime database, the second major breach in two months."),
        ("FRANCE PROTESTS", "A sixth Saturday of cost-of-living marches; 82,500\u2013"
                    "150,000 on the streets and 144 arrests."),
    ]
    ff = font(SANS, 13)
    fb = font(SANS_B, 13)
    col_w = (fx1 - fx0 - 28 - 14) // 2
    for i, (kick, txt) in enumerate(items):
        cx = fx0 + 14 + (i % 2) * (col_w + 14)
        cy = fy0 + 34 + (i // 2) * 56
        # wrap with a narrower first line (the kicker sits on it), full width after
        kw = text_w(d, kick + " \u2014 ", fb)
        words, lines, cur, first = txt.split(" "), [], "", True
        for w in words:
            lim = col_w - kw if first else col_w
            trial = (cur + " " + w).strip()
            if text_w(d, trial, ff) <= lim:
                cur = trial
            else:
                if not cur:
                    raise ValueError(f"footer word too wide: {w!r}")
                lines.append(cur)
                cur, first = w, False
        if cur:
            lines.append(cur)
        if len(lines) > 3:
            raise ValueError(f"footer item overflows: {kick}")
        d.text((cx, cy), kick + " \u2014 ", font=fb, fill=(255, 210, 90))
        for j, ln in enumerate(lines):
            lx = cx + kw if j == 0 else cx
            d.text((lx, cy + 1 + j * 16), ln, font=ff, fill=(235, 235, 235))
    img.save(OUT, optimize=True)
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
