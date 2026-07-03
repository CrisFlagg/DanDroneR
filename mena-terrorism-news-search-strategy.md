# MENA Terrorism & Militant Activity — News Search Strategy

**Purpose:** Find news articles about terrorist and militant activity in Northern Africa and the Middle East within a defined date window.

**Default country scope:**

| Northern Africa | Middle East |
|-----------------|-------------|
| Algeria | Bahrain |
| Egypt | Iran |
| Libya | Iraq |
| Morocco | Israel |
| Sudan | Jordan |
| Tunisia | Kuwait |
| | Lebanon |
| | Oman |
| | Palestine |
| | Qatar |
| | Saudi Arabia |
| | Syria |
| | Turkey |
| | United Arab Emirates |
| | Yemen |

---

## Search run log

Track each execution here. When you ask to **“freshen up my search”**, the agent reads this section, extends the date window from `last_event_date_covered` (or `search_run_completed`) through today, reruns the query phases, and appends a new row.

### Current parameters (active run)

| Field | Value |
|-------|-------|
| **Search run ID** | `run-2026-07-03-002` (latest) |
| **Search run completed (UTC)** | `2026-07-03T23:45:00Z` |
| **Event date window start** | `2026-06-01` |
| **Event date window end** | `2026-07-03` |
| **Definition mode** | `broad` (terrorism + militia + foiled plots + crisis editorials) |
| **Countries** | All 21 (see scope table above) |
| **Result artifact** | [`mena-terrorism-militant-news-june-july-2026.md`](mena-terrorism-militant-news-june-july-2026.md) |
| **Strategy doc version** | `1.1` |

### Run history

| Run ID | Completed (UTC) | Event window | Mode | Notes |
|--------|-----------------|--------------|------|-------|
| `run-2026-07-03-001` | 2026-07-03 | 2026-06-01 → 2026-07-03 | broad | Initial full search; strategy doc created; missed Al Jazeera El-Obeid editorial (gap queries added in §5) |
| `run-2026-07-03-002` | 2026-07-03 | 2026-06-01 → 2026-07-03 | broad | Gap-fill rerun (Pass B/C + §5 gap queries); 12 new rows + 2 citation merges in article index v1.1 |

### Hot spots to prioritize on freshen

Locations that produced multiple hits in the last run — run **drill-down passes** (§3) on these first:

- **Sudan** — El-Obeid (RSF drones, siege, UN/Amnesty warnings)
- **Syria** — Damascus (cafe bombing, checkpoint attack)
- **Iran / Gulf** — Strait of Hormuz, Kuwait, Bahrain, Jordan (IRGC strikes)
- **Lebanon / Israel** — Hezbollah rocket fire
- **Iraq** — militia drones from Iraqi territory
- **Libya** — militia mobilization, migrant crackdown violence
- **Morocco** — ISIS foiled plots, Polisario operations
- **Turkey** — Ankara counterterror raids, PKK de-escalation
- **Yemen / Saudi Arabia** — Houthi threats and engagements

---

## How to freshen the search (rerun for subsequent days)

Use this when you want new articles for days **after** the last run.

### What to say

Any of these prompts work:

- *“Freshen up my search”*
- *“Rerun the MENA terrorism search for new days since the last run”*
- *“Update the search through [DATE] using mena-terrorism-news-search-strategy.md”*

Optional modifiers:

- *“…narrow definition only”* → strict mode (§2)
- *“…Sudan and Syria only”* → limit country scope
- *“…include gap queries from §5”* → always run Pass B and Pass C

### What the agent should do

1. **Read this document** — especially *Search run log* and *Hot spots*.
2. **Compute the new window:**
   - `new_start` = day after `Event date window end` from the latest run  
     - Example: last end `2026-07-03` → `new_start` = `2026-07-04`
   - `new_end` = today (UTC) unless you specify a date
3. **Rerun all three passes** (§3) with dates substituted in every query:
   - Replace month literals (`June 2026`, `July 2026`) with the month(s) covering `new_start`–`new_end`
   - Add `after:[new_start]` to outlet-scoped queries where supported
4. **Run gap queries** (§5) for any hot spot active in the prior run.
5. **Drill down** on any location with ≥2 new hits.
6. **Merge results:**
   - Keep all rows from prior runs whose **event date** ≤ last window end
   - Append only **new** incidents (dedupe by event + location + date)
7. **Update this document:**
   - Add a row to *Run history*
   - Update *Current parameters* (`Search run completed`, `Event date window end`, new `Search run ID`)
8. **Deliver:** delta table (new articles only) plus optional updated full merged list

### Date substitution template

When freshening, rewrite query date tokens:

| Token in doc | Replace with |
|--------------|--------------|
| `[WINDOW_START]` | `new_start` (ISO date) |
| `[WINDOW_END]` | `new_end` (ISO date) |
| `[MONTH_A]` | month name of `new_start` + year |
| `[MONTH_B]` | month name of `new_end` if different from `MONTH_A` |
| `June 2026` / `July 2026` in §4 | current freshen months |

Example freshen query (if run on 2026-07-10):

```
terrorist attack Middle East North Africa July 2026 news
Sudan El Obeid drone strike July 2026 RSF
site:aljazeera.com/editorial Sudan July 2026
after:2026-07-04 Syria attack
```

### Freshen checklist

- [ ] Read latest row in *Run history*
- [ ] Set `new_start` / `new_end`
- [ ] Run Phase 1–8 queries (§4) with updated dates
- [ ] Run gap queries (§5)
- [ ] Drill down hot spots (§3)
- [ ] Dedupe against prior results
- [ ] Update *Search run log*
- [ ] Report delta + updated window to user

---

## 1. What we are looking for

### Primary targets (high confidence)

Articles that report **violent events** or **credible threats of violence** involving:

- **Designated or widely labeled terrorist groups** (e.g., ISIS/ISIL, Al-Qaeda affiliates, Hamas, Hezbollah, PKK, Houthis when described as militants/terrorists)
- **Jihadist or Islamist militant cells** (attacks, foiled plots, arrests of plotters, suicide bombings)
- **Insurgent/separatist armed operations** with civilian or infrastructure harm (e.g., Polisario operations, RSF drone campaigns against cities)
- **Cross-border militant strikes** (drone/missile/rocket attacks from non-state or state-proxy actors)
- **Militia violence** with terror-like tactics (sieges, indiscriminate shelling, attacks on schools/hospitals/aid convoys)

### Secondary targets (broader definition — include with label)

- **Foiled or planned attacks** (arrests, explosives manufacturing, “lone wolf” plots)
- **Counterterrorism operations with casualties** (army raids, shootouts with militants)
- **Major crisis reporting** when it documents ongoing militant violence patterns (editorials, explainers, UN/NGO warnings tied to specific attacks or siege conditions)
- **State military strikes** when they are part of an active conflict and target militant infrastructure or are reported alongside militant retaliation (e.g., IRGC strikes, Hezbollah rocket fire)

### Preferred source types

| Tier | Source type | Examples |
|------|-------------|----------|
| 1 | Major wire and international news | AP, Reuters, BBC, Al Jazeera, France 24, PBS |
| 2 | UN and multilateral bodies | UN News, OCHA, UN Security Council statements |
| 3 | Regional outlets and specialist monitors | ACLED, Long War Journal, Amnesty, HRW, MEMRI, Roya News |
| 4 | Government/official statements | Army communiqués, interior ministry reports (note bias) |

### Required metadata per result

For each included article, capture:

- **Date of event** (not just publication date)
- **Country / location**
- **Actor(s)** (perpetrator and target)
- **Incident type** (attack, plot foiled, siege, counterterror op, editorial/analysis)
- **Casualties / damage** (if reported)
- **URL and publication date**

---

## 2. What we are not looking for

### Exclude unless directly tied to a violent incident

- **General travel advisories** with no specific new attack (e.g., “Exercise Increased Caution” boilerplate)
- **Historical articles** outside the date window (verify event date, not just URL date)
- **Purely political or judicial news** with no violence (e.g., sentencing unrelated to ongoing militant activity — *exception:* terrorism-trial verdicts may be noted separately)
- **Routine military exercises** with no attack context (e.g., Egypt “Badr 2026” drills)
- **Economic, sports, or diplomatic news** unless an attack occurred at the venue or during the event
- **Social media posts** without corroboration by a news outlet (use only as leads)
- **Duplicate syndication** of the same AP/Reuters story (keep one canonical link)
- **Misdated aggregator pages** that republish old incidents with current timestamps

### Exclude by geography

- Countries **outside** the scope list (e.g., Niger, Mali — unless attack spills into a scoped border area and is relevant to Algeria/Morocco/Libya security)
- Attacks on **Western countries** by MENA-linked actors unless the attack occurred **inside** a scoped country

### Exclude by violence threshold (strict mode)

When the user asks for **terrorism only** (narrow definition), exclude:

- General civil-war battle reports with no civilian targeting
- Crime unrelated to militant/terror networks (e.g., lone mass shooter with psychiatric history and no group affiliation)
- Protest violence without militant organization involvement
- Migrant detention abuse (include only under **broad** definition / militia violence pass)

### Low-confidence items — flag, do not auto-include

- Wikipedia-only citations without primary news source
- Single-source unverified claims
- Propaganda releases with no independent corroboration

---

## 3. Search methodology

### Three-pass structure (recommended)

Run all three passes per country or hot spot. Merge and deduplicate by **event**, not headline.

#### Pass A — Incidents (attack-focused)

Goal: Find breaking news on specific attacks.

Query pattern:
```
[actor OR attack type] + [country/city] + [month year]
```

#### Pass B — Crisis & analysis (context-focused)

Goal: Find editorials, UN warnings, NGO investigations, “what we know” pieces.

Query pattern:
```
[location] + (massacre OR atrocities OR siege OR "crimes against humanity" OR "what do we know") + [month year]
```

#### Pass C — Outlet-scoped (coverage-focused)

Goal: Catch content search engines deprioritize (editorials, video, UN pages).

Query pattern:
```
site:aljazeera.com [location] [month year]
site:apnews.com [country] [militant actor]
site:news.un.org [location]
site:amnesty.org OR site:hrw.org [country]
```

### Follow-up drill-down rule

If any location appears in **≥2 results** (e.g., El-Obeid, Damascus, Strait of Hormuz), run:

```
site:aljazeera.com [location]
site:aljazeera.com/editorial [location]
[location] ACLED OR Amnesty OR "open-source investigation"
```

### Date filtering

- Always bound searches to the **active event window** in *Search run log* (`Event date window start` → `Event date window end`).
- On freshen runs, search only `new_start` → `new_end`; do not re-fetch already-cataloged events unless a major correction or new source appears.
- Include **both** the start month and end month of the active window in queries (editorials often lag events by 1–3 days).
- Prefer explicit windows: `[MONTH_A]`, `[MONTH_B]`, or `after:[WINDOW_START]` where supported.
- Verify **event date** in article body; reject if event precedes `new_start` or falls outside the requested window.

### Vocabulary clusters

Rotate synonyms across passes:

| Cluster | Terms |
|---------|-------|
| Attack | attack, bombing, strike, shooting, explosion, blast, raid |
| Actors | terrorist, militant, jihadist, militia, paramilitary, insurgent, IRGC, Hezbollah, Hamas, ISIS, PKK, Houthi, RSF, Polisario |
| Threat | plot, foiled, arrested, cell dismantled, lone wolf |
| Mass harm | massacre, atrocities, ethnic cleansing, crimes against humanity, siege, encirclement |
| Infrastructure | hospital, school, mosque, church, refinery, airport, aid convoy, power station |
| Institutional | UN warning, red alert, urgent debate, NGO appeal |

---

## 4. Search strings (query library)

**Last executed:** `run-2026-07-03-001` (2026-07-03 UTC) · Window: `2026-06-01` → `2026-07-03`

When freshening, keep query structure identical; substitute dates per *How to freshen the search*.

Below is the complete list of web search queries from the initial run. Queries are grouped by phase.

### Phase 1 — Initial broad search (narrow terrorism definition)

```
terrorist attack Middle East North Africa June 2026 news
terrorism Egypt Syria Iraq Yemen June July 2026
ISIS attack Africa Middle East 2026 June
terrorist attack Iraq Lebanon Sudan June 2026
Syria ISIS church bombing June 22 2026 Damascus
terror attack Egypt Libya Algeria Tunisia Morocco June July 2026
terror attack Israel Palestine Jordan June July 2026
```

### Phase 2 — Regional and actor-specific expansion

```
Houthi attack Saudi Arabia Yemen June July 2026
Sudan terrorist attack militia June 2026
Iraq militia drone attack Kuwait Saudi UAE June 2026
Hezbollah rocket attack Israel June 2026
Syria bombing attack June 2026 Damascus Homs
Egypt terrorist attack Sinai June July 2026
Iran terrorist attack IRGC strike June July 2026
Turkey PKK terrorist attack June July 2026
```

### Phase 3 — Incident verification and gap-filling

```
Houthi attack Saudi Arabia Yemen June July 2026
Sudan terrorist attack militia June 2026
Iraq militia drone attack Kuwait Saudi UAE June 2026
Hezbollah rocket attack Israel June 2026
Syria ISIS church bombing June 22 2026 Damascus
terror attack Egypt Libya Algeria Tunisia Morocco June July 2026
terror attack Israel Palestine Jordan June July 2026
Hamas attack Israel Gaza June 2026 rocket
Libya militia attack bombing June 2026
Jordan terrorist attack June July 2026
Iraq militia attack June 2026 Gulf drone
```

### Phase 4 — Shipping / Hormuz / Gulf escalation

```
Iraq drone attack Gulf June 2026 after June 1
Qatar Oman attack June July 2026 drone missile
Bahrain Kuwait IRGC drone missile attack June 28 2026
Iran attacks cargo ship off Oman June 2026
```

### Phase 5 — Sudan deep dive

```
Sudan El Obeid drone strike June 2026 RSF
```

### Phase 6 — Libya date verification

```
Libya UNSMIL rocket attack Tripoli June 2026 date
```

### Phase 7 — Broader definition (Algeria, Egypt, Morocco, Tunisia, Libya, Turkey)

```
Algeria attack violence bombing militia June July 2026
Egypt attack violence Sinai security incident June July 2026
Morocco attack violence militia bombing June July 2026
Tunisia attack violence militia bombing June July 2026
Libya militia attack violence bombing Tripoli June July 2026
Turkey attack violence PKK bombing June July 2026
```

### Phase 8 — Country-specific follow-ups

```
Algeria army kills terrorists militants June 2026
Egypt armed attack shooting violence June 2026
Libya armed clashes militia June 2026 Tripoli Zawiya
Turkey security operation clash killed June July 2026
Tunisia militant raid killed June July 2026 Kasserine
Libya violence shooting June 2026 Tajoura Tripoli
Morocco Polisario drone strike confirmation June 2026
Turkey PKK clash operation killed June 2026 northern Iraq
Libya migrant raid violence June 2026
Algeria Tebessa seven terrorists killed June 19 2026
```

---

## 5. Search strings to add (gaps identified after review)

These queries were **not** run initially but would have improved coverage — especially for editorials and crisis reporting (e.g., the missed Al Jazeera editorial on El-Obeid).

### Crisis / analysis pass (Sudan example)

```
"el-Obeid" massacre fears "what do we know" July 2026
"el-Obeid" (siege OR atrocities OR "ethnic cleansing") June 2026
Sudan RSF school hospital drone June 2026
Amnesty RSF el-Fasher el-Obeid July 2026
```

### Outlet-scoped pass

```
site:aljazeera.com/editorial Sudan July 2026
site:aljazeera.com el-Obeid June 2026
site:aljazeera.com/news Sudan RSF drone
site:news.un.org El Obeid June 2026
site:apnews.com Sudan RSF drone
```

### Per-country template (copy and adapt)

```
site:aljazeera.com [COUNTRY] (attack OR militia OR militant OR terrorist) [MONTH_A]
site:aljazeera.com/editorial [COUNTRY] [MONTH_A]
[COUNTRY] (foiled plot OR arrested OR cell dismantled) [MONTH_A]
[ACTOR] [COUNTRY] (drone OR bombing OR rocket) [MONTH_A]
after:[WINDOW_START] [COUNTRY] (attack OR militant OR militia)
```

### Freshen-only quick queries (run every update)

Minimal set to run on each freshen if time-boxed:

```
terrorist attack Middle East North Africa [MONTH_A] [MONTH_B] news
militia attack violence [MONTH_A] after:[WINDOW_START]
site:aljazeera.com [MONTH_A] after:[WINDOW_START] (attack OR militia OR militant)
site:apnews.com Middle East [MONTH_A] after:[WINDOW_START]
site:news.un.org after:[WINDOW_START] (Sudan OR Syria OR Gaza OR Lebanon)
```

---

## 6. Inclusion decision flowchart

```
Article found
    │
    ├─ Event date within window? ──NO──> Exclude (note if historically relevant)
    │         │
    │        YES
    │         │
    ├─ Location in country scope? ──NO──> Exclude (or note cross-border relevance)
    │         │
    │        YES
    │         │
    ├─ Describes violence, threat, or militant actor? ──NO──> Exclude
    │         │
    │        YES
    │         │
    ├─ Primary news / UN / rights org source? ──NO──> Flag low confidence
    │         │
    │        YES
    │         │
    └─> Include → tag as: ATTACK | FOILED PLOT | MILITIA | COUNTER-TERROR | ANALYSIS/EDITORIAL
```

---

## 7. Known limitations of this strategy

1. **Web search bias:** Favors `/news/` over `/editorial/`, `/video/`, and `/features/`.
2. **English-only:** Arabic/French primary sources may be underrepresented.
3. **Paywalls:** Some outlets (Le Monde, etc.) return partial content.
4. **State media framing:** Official “terrorist neutralized” reports need corroboration.
5. **Duplicate events:** Same incident may appear across 10+ URLs — dedupe by event.
6. **Retroactive reporting:** H1 summaries (e.g., Algeria June 27 army report) cover events across months — extract only in-window incidents.

---

## 8. Example of a missed article and the fix

**Missed:** [Fears of new massacre in Sudan’s el-Obeid: What do we know?](https://www.aljazeera.com/editorial/2026/7/2/fears-of-new-massacre-in-sudans-el-obeid-what-do-we-know) (Al Jazeera editorial, July 2, 2026)

**Why missed:** Phase 1–5 queries targeted `attack`, `drone strike`, `terrorist` — not `massacre fears`, `what do we know`, or `site:aljazeera.com/editorial`.

**Fix:** Add Pass B (crisis/analysis) and Pass C (outlet-scoped) before finalizing results.

---

## 9. Output format for search results

When compiling findings, use a table per country:

| Date | Type | Incident summary | Actor | Source URL |
|------|------|------------------|-------|------------|

**Type codes:** `ATTACK` | `FOILED` | `MILITIA` | `COUNTER-TERROR` | `EDITORIAL` | `UN/NGO`

---

*Document version: 1.1 — Created July 3, 2026 · Search run log added July 3, 2026*
