# The Academy of Magic & Marvels

A five-day Grade 5 Python apprenticeship from the **Beyond Vibe Coding** curriculum: students leave able to *read, trace, and reason about* code — not just run it. Your computer is your wand, VS Code is your workshop, and Python is the language it obeys. Exactly, and only exactly.

## → Enter the Academy

**[Open the hub — marvels_academy_hub.html](marvels_academy_hub.html)**

This repo has no `index.html` by design: this README is the site root, and the hub is the front door. Every lesson page is fully self-contained (all CSS/JS inline) and links back through the hub.

## The week

| Day | Hall | New magic | Artifact |
|---|---|---|---|
| 1 | [Wand Registration](day1_wand_registration.html) | `print`, misfires & tracebacks, variables, `input`, `int()`, f-strings | The Registration Scroll |
| 2 | [Runeweaving](day2_runeweaving.html) | `for` / `range`, string repetition, two corresponding patterns, rich ink | The Grand Tapestry |
| 3 | [Potions & the Restricted Shelf](day3_potions_restricted_shelf.html) | `if` / `elif` / `else`, lists & indexing, `len`, `random.choice`, `in` | The Stockroom Gatekeeper |
| 4 | [The Spellbook & the Commission](day4_spellbook_commission.html) | `def` + parameters — then the capstone | Your Marvel: a customized [Wandlight](wandlight_pygame.py) |
| 5 | [The Counter-Curse Clinic](day5_countercurse_clinic.html) | zero new syntax — the five-step protocol & the VS Code debugger | The Counter-Curse Log + Grand Demonstration |

The Commission is **due by the end of Day 4**. Day 5 lifts curses; it does not start castings.

## Files

Flat repo, no build step. Ship everything together — the hub must always be re-uploaded alongside any new or changed page.

```
README.md                            ← you are here (site root)
marvels_academy_hub.html             ← the front door
day1_wand_registration.html
day2_runeweaving.html
day3_potions_restricted_shelf.html
day4_spellbook_commission.html
day5_countercurse_clinic.html
wandlight_pygame.py                  ← the Day 4 engine, byte-identical to the in-page listing
```

## Student setup

- VS Code with the Python extension, Python 3.10+ (traceback "Did you mean" hints assume 3.10+).
- Installs happen the day they're needed, in the VS Code terminal:
  - Day 2: `pip install rich`
  - Day 4: `pip install pygame`
  - Day 1 stretch only: `pip install pyfiglet`
- Pages are self-paced with predict-before-reveal answers built in, so the teacher is never the bottleneck.

## House laws

- **One change per run.**
- **Read it, trace it, then run it.**
- Every loop is countable: game and animation loops are `for frame in range(N)` — never `while`.
- Excluded from the whole apprenticeship by design: `while`, `return` values, dictionaries, classes, sprites/image files, file I/O, `try`/`except`, nested `if` gates.

## Standards

Each page carries a collapsed teacher panel with verbatim standards, the teaching chunks, and the evidence collected. Verified claims: CCSS-M **5.OA.B.3** (Day 2), **5.G.A.2** (Day 4), CSTA **E5-ALG-PS-01** (Day 4). Four grade-5 CSTA PRO-progression codes remain marked `??` / *Needs verification* pending confirmation at the source viewer — they are placeholders, not claims.

Mapped to: Computer Science Teachers Association. (2026). *2026 CSTA PK–12 computer science standards.* https://csteachers.org/pk12standards/ · CC BY-NC-SA 4.0. Mathematics standards © 2010 NGA Center for Best Practices & CCSSO. "Mapped to" is this project's claim; it is not a CSTA- or CCSS-reviewed designation.

---

*The Academy of Magic & Marvels · Apprentice Cohort · keep your grimoire close*
