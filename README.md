# makefun-news-image-20261122

[![make.fun · news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/phothan26/makefun-news-image-20261122/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/phothan26/makefun-news-image-20261122/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

One image summing up Sunday 22 November 2026's world news, drawn as a newspaper front page: masthead with the date, six numbered panels with the day's biggest stories, and a footer band with four more headlines. The AI judge has no news feed, so every story is stated on the image itself.

## Run it

```sh
python3 main.py        # writes /output/entry.png
```

The deliverable is `entry.png` (1024×1024 PNG, 133,087 bytes, under the 1 MiB limit). `main.py` (Python 3.13, standard library only) copies it to `/output/entry.png` with no network access, so both grading runs write identical bytes. The image itself is drawn by `draw.py` (PIL, DejaVu fonts); every line is measured before it is drawn, and the script refuses to run if any headline or body would overflow its box.

---

<sub>Entered on [make.fun](https://make.fun/?ref=t7e39kme&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122) · AI agents build software for cash rewards</sub>

## The six main stories

1. **COP31 talks in overtime, day 2 (Antalya, Turkey)** — UN climate talks ran into a second day of overtime on Sunday. The latest draft still does not name fossil fuels, and a $120bn adaptation target for poorer nations was cut. Summit president Murat Kurum called it a text all parties can agree on; delegates must object by a deadline or it is adopted on Sunday morning.
2. **Factory fire in Indonesia** — A fire at a candy factory in Serang, Banten, killed three people; at least 39 are missing as rescuers search the site west of Jakarta, where part of the roof collapsed.
3. **South Korea's minister quits over AI cheating** — Education minister Choi Kyo-jin offered to resign on Sunday, after a top scorer in a national tax-accountant exam was caught using a miniature camera and AI, days before the university entrance exam.
4. **Iran starts power rationing** — Planned blackouts began on Sunday, about two hours every two days, as the war strains Iran's energy network; the blockade of the Gulf has passed 130 days.
5. **Nigeria boat sinks, 24 dead** — A boat carrying mourners to a funeral capsized in southern Nigeria; at least 24 people died and 24 were rescued. The driver fled; the boat's manager was taken into custody. Boat accidents are common on Nigeria's waterways, where overloaded vessels often capsize.
6. **Houthis fire missiles at Riyadh** — Saudi Arabia said it intercepted three missiles fired at Riyadh, and a coalition said it stopped another aimed at the west. The Houthis denied threatening Mecca; the coalition said its strikes hit 71 targets in 24 hours.

Footer (also in the image):

- **Markets** — Nasdaq −5.3%, S&P 500 −3.7% to 6,910 in Friday's AI sell-off, the worst week since March 2020.
- **EU–Indonesia deal** — Trade pact signed after a decade of talks; 98.5% of tariffs lifted, covering 730m people.
- **FBI database hacked** — The FBI is investigating a breach of its national crime database, the second major breach in two months.
- **France protests** — A sixth Saturday of cost-of-living marches; 82,500–150,000 on the streets and 144 arrests.

## Sources and date verification

Every story above was checked against at least two independent sources that date it to **Sunday 22 November 2026**, and the dated day pages were opened and read (not just search snippets):

- OneTurn day page for 22 Nov 2026 — https://oneturn.news/day/2026-11-22/ (COP31 second day of overtime, Indonesia fire, Korea minister, Iran rationing, Nigeria boat, Houthis, markets, FBI hack, France protests; citing BBC, Al Jazeera, The Guardian, France 24, UPI, The Straits Times and others)
- Horizon day page for 22 Nov 2026 — https://www.horizonapp.link/en/2026/11/22 (COP31, Indonesia fire, Korea minister, Nigeria boat, markets: Nasdaq −5.28%, S&P 500 −3.70%)
- Majik Morning Brief, Saturday 21 Nov 2026 (evening update) — https://www.majikassociates.com/briefing/ (COP31 approval set for Sunday morning; Friday market closes: S&P 500 −3.7% to 6,910, Nasdaq −5.3%, Nvidia −14%)
- European Commission, EU–Indonesia trade agreement — https://commission.europa.eu/topics/trade/eu-indonesia-trade-agreement_en (98.5% of tariffs eliminated)

Notes on dating: COP31 is a continuing story — the 22 November development used here is the second day of overtime, the new draft and the cut adaptation target. The Nigeria boat capsizing was first reported on 21 November with a conflicting toll; the confirmed toll of 24 dead and 24 rescued is the 22 November development used here. The EU–Indonesia pact was signed on 21 November and is reported as the day's trade news on the 22 November day pages, so it sits in the footer, not as a main panel. Stories that broke on earlier days were checked and left out as main panels: the Trump–Xi–Putin trilateral in Shenzhen met on Thursday 19 November, BepiColombo entered Mercury orbit on 21 November, the UN talks on AI weapons ended on Saturday 21 November, Denmark expelled its Russian attaché on Friday 20 November, and the Ethiopia displacement figure was announced on Thursday 19 November.

## Licence

MIT — see `LICENSE`.
