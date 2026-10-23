# Remaining Industry Implementation and Discovery Plan

**Status:** written 2026-10-22. Stage 0 complete 2026-10-22; batch loop running (see CURSOR).
**Input:** `_rest-of-the-industries.md`, the 714 NAICS 2022 industries the vault doesn't have yet.
**Output:** each of them, alone or merged with close siblings, built into the vault to the same standard as the Phase 4 industries (`hedge-funds` is the reference).
**Branch:** `phase4/capital-markets-research`. Never `main`.
**Standing run order:** this file. Launch a fresh agent in the vault root (`problem-index/`) with *"Read `_remaining-industry-implementation-and-discovery-plan.md` and execute it."* Nothing else needs pasting. The CURSOR at the bottom says where the run stands.
**Gates:** `python3 _state/rest/check_queue.py` (Stage 0) and `bash _state/rest/verify.sh <slug>` (every industry). Both are calibrated against the Phase 4 builds. There are no owner-approval gates except Stage E (§10), the only step that edits existing files.

---

## 1. What one finished industry looks like

Every new industry gets the full Phase 4 build, about 60–80 files and ~22,000 words:

| Layer | Files | What |
|---|---|---|
| Hub | `industries/<slug>.md` | Profile (with the NAICS codes it covers), Key Pain Themes, Current Tech Landscape, Problems, Analysis |
| Problems | `problems/<slug>/` × 7 | high-impact, low-impact-1/2, worker-life-1/2, ml-opportunity (tacit entry first), ai-agents-platforms |
| Niches (Pass 1) | `niches/<slug>/_overview.md` + 8 level-1 niches × 4 files | Two niches per axis (High Market Share, Low Digitized, Underserved Audience, Highly Automatable), each with profile, build, buy and fix, each carrying a `**Contested on:**` line |
| Contested sub-niches | usually 1–2 × 4 files | For any level-1 niche whose contested sentence can't be written as one sentence |
| Pass 2 pockets | ≥10, 1 or 4 files each | Insight-layer sweep: gate, rubric, and build/buy/fix only for qualifiers (≥50/60, no kill switch) |
| Lens scores | `lenses/_state/scores/<slug>.jsonl` | AI-proof, value clarity and digital nature for the industry and every niche directory |
| Source log | `_state/rest/sources/<slug>.md` | What was checked on the web, with URLs, and what was not |

**Scale.** After merging, expect roughly 300–400 new industries; Stage 0 fixes the number. At ~70 files each that is ~25,000 files, more than the whole vault today. Phase 4 built 7 industries with 7 parallel builders in about 5 hours, so plan on a batch of 10 taking 4–6 hours with review, and ~35 batches overall. That's many sessions. The cursor makes every one of them resumable.

## 2. Hard rules

1. **Additive only.** Never edit, move or delete a file that existed before this plan: the 257 industries, their problems and niches, `series/`, `history/`, `lineage/`, `origins/`, `_rest-of-the-industries.md`, every bookmark and shared index, and `lenses/_state/corrections.jsonl`. You may write only:
   - new `industries/<slug>.md`, `problems/<slug>/` and `niches/<slug>/` for slugs in the queue;
   - anything under `_state/rest/`;
   - this file's CURSOR and Findings log;
   - `_scorecard-index-rest.md`;
   - `lenses/_state/scores/<new-slug>.jsonl`;
   - the lens rankings that `lenses/_state/build.py` regenerates (`lenses/ai-proof.md`, `value-clarity.md`, `digital-nature.md`, `scores.csv`, `_state/stats.json`), only by running that script.
2. **Found a defect in an existing file?** Log it in the Findings log at the bottom and leave the file alone.
3. **Git.** Commit at the end of every batch, then `git push` straight away. Never push to `main`, and don't open a PR. Add the `Co-Authored-By:` trailer your harness specifies; the global `~/.claude/CLAUDE.md` requires one on every commit.
4. **Banned sources.** Never fetch or search inside LinkedIn, Crunchbase, ZoomInfo, PitchBook, Glassdoor, Apollo or RocketReach; the owner's IP gets blocked. If a search result points there, skip it.
5. **Facts.** Web-check the headline figures (§5.1). Anything not checked is written with `~` and "(estimate)". Never present a recalled number as a checked fact; this material feeds published content.
6. **Tags.** Use only tags in `_state/safe-tags.txt` (138). Don't audit against `metadata/tags.md`, which still lists deprecated tags. `profile.md` never carries a Tags line.
7. **Honest negatives.** A niche whose contested sentence is generic ("better UX", "lower price") has failed the filter: say so and decompose or drop it. A pocket with no 10-person insight function fails the gate. An industry where every pocket fails the gate is a valid result. Never inflate a score, widen the gate or invent a contested sentence to fill a slot.
8. **Parallel by slug only.** Builders write only their own slug's files, source log and scores file. Shared files (`_state/rest/queue.tsv`, this CURSOR, `_scorecard-index-rest.md`, the lens rankings) are written by the coordinating session alone.

## 3. Read first, in this order

1. This file, all of it.
2. `_phase2-plan.md` §2 (the contested filter) and §5 (per-industry method). Skip its batches and cursor.
3. `_direction.md` §1–§6: the Pass 2 gate, rubric, kill switches, seven value-chain positions and pocket format. Ignore its CURSOR and its §7 verification block, which belong to the original 118 and hard-code a path from another machine.
4. `lenses/_method.md`: the three lenses, factors and anchors.
5. The reference implementation, in full:
   - `industries/hedge-funds.md` and `problems/hedge-funds/*` (all 7 files);
   - `niches/hedge-funds/_overview.md`;
   - one level-1 niche: `niches/hedge-funds/research-compliance-mnpi/` (4 files);
   - one contested sub-niche: `niches/hedge-funds/covenant-and-document-monitoring/profile.md`;
   - one qualified pocket: `niches/asset-managers/esg-ratings-providers/` (4 files);
   - one gate failure: `niches/hedge-funds/short-activist-research/profile.md`.
6. For operator-tier industries (most of what's left: farms, factories, wholesalers, trades), the Pass 2 half of `niches/metal-fabrication/_overview.md` shows what an honest sweep of a physical industry looks like.
7. The content checks in `../_context/features/problem-identification/evals.md` and `../_context/features/niche-discovery/evals.md`.

**Known traps.** These contradictions are documented; don't copy the wrong version:

- **Agents note fields.** `problem-index/CLAUDE.md` gives the wrong fields for `ai-agents-platforms.md`. Use **Concept / Inputs / Outputs / Actions / Why now / Market**, as every Phase 2 and Phase 4 file does.
- **Tags and queue.** The repo-root `CLAUDE.md` lists deprecated tags (`#cnn`, `#llm`, `#nlp`) and an old processing queue. Ignore both.
- **Note length.** The repo-root `CLAUDE.md` says problem notes are 2–3 sentences per section. The current bar is the reference length (§9.1).
- **Old hubs.** Phase 1 hubs such as `metal-fabrication.md` use an older heading set. Copy structure from `hedge-funds` only.
- **Hard-coded scripts.** `_state/verify.sh` and `_state/verify-stageb.sh` hard-code `/Users/mac/...`. Don't run them.

## 4. Stage 0: discovery, from 714 codes to a locked queue

Run once, by the coordinator, single-threaded. It decides what gets built, so do it carefully.

### 0.1 Seed the triage sheet

```bash
python3 - <<'PY'
import re
t = open("_rest-of-the-industries.md").read().split("## Already covered")[0]
rows = re.findall(r"^\| (\d{6}) \| (.*?) \| `([^`]*)` \|", t, re.M)
with open("_state/rest/naics-triage.tsv", "w") as f:
    f.write("naics\ttitle\tsector\tdecision\tslug\treason\n")
    for c, title, slug in rows:
        f.write(f"{c}\t{title}\t{c[:2]}\t\t{slug}\t\n")
print(len(rows), "rows")   # expect 714
PY
```

### 0.2 Triage every row

Set `decision` to one of four values:

| Decision | Meaning | `slug` | `reason` |
|---|---|---|---|
| `new` | Becomes a vault industry. Exactly one `new` row per slug | the new slug | optional |
| `merge` | Folded into another row's industry | that row's slug | required: why the work is the same |
| `covered` | On closer reading, an existing vault industry's typical firm sits under this code | the existing slug | required |
| `skip` | No operator population of its own (e.g. legal shells), so nothing to build | empty | required |

**Merge test.** Merge two codes only when all four hold: same kind of firm, same workers, same buyer and same core workflow, so they would share most of their problems. A different regulator, licence or tacit skill keeps them apart. NAICS splits by product and the vault splits by work. For example, a dozen machinery-building codes may be one or two industries, but a sawmill and a cabinet shop are not. Manufacturing (272 codes) and Wholesale (59) need the most merging. Expect roughly one industry per two or three codes there, and close to one per code in services.

**Boundary test.** For every `new` slug, find the 2–3 closest existing industries:

```bash
grep -il '<keyword>' industries/*.md
```

Read their Profiles, then write one boundary sentence in the queue's `boundary` column, Phase 4 style: *"Not `food-manufacturing`: covers dairy processors only, whose milk-pricing and pasteurisation compliance differ."* If the honest answer is "this is the same industry", change the decision to `covered`.

**Slugs.** Kebab-case, a plural firm-type noun (`logging-companies`, `title-and-settlement-offices`), at most 40 characters, and no collision with `_state/rest/baseline-industries.txt` (the 257 slugs at plan start). The suggested slugs in `_rest-of-the-industries.md` are a starting point; many long ones need shortening.

### 0.3 Write the queue

`_state/rest/queue.tsv` has one row per industry to build. It has exactly these tab-separated columns, which the verifier reads by position:

```
order	batch	slug	name	category	naics	status	boundary
1	1	architecture-firms	Architecture Firms	Professional Services	541310	todo	Not `engineering-consultants`: ...
```

- `naics` is a comma-separated list of every code triaged `new` or `merge` to that slug.
- `status` is one of `todo`, `building`, `done` or `blocked`.
- `category` comes from the table below.
- **Batches.** About 10 industries each, drawn from one sector so an interrupted run leaves a coherent block.

**Sector order.** The owner sells remotely, and the three-lens study (`lenses/`) found the service sectors are where remote buyers are. So services go first. Manufacturing goes late because it needs the most merging, and earlier batches will have settled the method. The owner may reorder rows before a batch starts; never reorder rows already `building` or `done`.

| Order | NAICS sector | Codes left | `category` value |
|---|---|---|---|
| 1 | 54 Professional, Scientific & Technical Services | 23 | Professional Services |
| 2 | 51 Information | 19 | Media, Telecom & Information |
| 3 | 52 Finance & Insurance | 20 | Financial Services (carriers and agencies: Insurance) |
| 4 | 56 Administrative, Support & Waste Services | 29 | Business Support & Waste Services |
| 5 | 61 Educational Services | 10 | Education |
| 6 | 62 Health Care & Social Assistance | 21 | Healthcare & Clinical (624xxx: Social Assistance) |
| 7 | 53 Real Estate, Rental & Leasing | 16 | Real Estate, Rental & Leasing |
| 8 | 71 Arts, Entertainment & Recreation | 22 | Arts, Entertainment & Recreation |
| 9 | 81 Other Services | 33 | Specialty Services |
| 10 | 72 Accommodation & Food Services | 8 | Hospitality & Food Service |
| 11 | 42 Wholesale Trade | 59 | Wholesale & Distribution |
| 12 | 44-45 Retail Trade | 44 | Retail & E-Commerce |
| 13 | 48-49 Transportation & Warehousing | 40 | Transportation & Logistics |
| 14 | 23 Construction | 18 | Construction & Trades |
| 15 | 22 Utilities | 12 | Utilities & Energy |
| 16 | 21 Mining, Quarrying, Oil & Gas | 19 | Mining & Extraction |
| 17 | 11 Agriculture, Forestry, Fishing & Hunting | 22 | Agriculture & Food |
| 18 | 31-33 Manufacturing | 272 | Manufacturing & Industrial |
| 19 | 55 Management of Companies | 3 | Holding & Management Companies (likely mostly `skip`) |
| 20 | 92 Public Administration | 24 | Nonprofit & Government (merge by function; check `municipal-services` and `public-defenders`) |

### 0.4 Check and commit

```bash
python3 _state/rest/check_queue.py      # must print QUEUE-CLEAN
```

It checks four things:

- every one of the 714 codes is triaged exactly once;
- every `new` or `merge` slug is queued once with matching codes;
- `covered` slugs exist;
- new slugs don't collide with existing ones, and categories and statuses are valid.

Then fill in the CURSOR's Stage 0 lines and the batch table, commit (`rest: stage 0, triage 714 NAICS codes into N industries`) and push.

## 5. The loop: one batch at a time

The **coordinator** (the session that read this file) runs every batch the same way:

1. **Start the batch.** Read the CURSOR and pick the first batch with `todo` rows. Set those rows to `building` in `queue.tsv`.
2. **Launch builders.** Start one builder subagent per industry, in the background, up to 10 at once. Paste the §7 brief into each, with its row filled in. If no subagent tool is available, run the same brief yourself, one industry at a time.
3. **Verify each industry as its builder reports.** Run `bash _state/rest/verify.sh <slug>`. On failure, send the exact failure lines back to that builder to fix. After two failed rounds on the same issue, fix it yourself, or set the row to `blocked` with a Findings-log note and carry on.
4. **Review.** Run one reviewer subagent for every 5 industries, with the §8 brief. Reviewers are read-only and return findings with file and fix. Get every finding fixed (by the builder, or by you) and re-run the verifier on the touched slugs.
5. **Close the batch.** Only the coordinator does these steps, in order:
   1. Append the batch's qualifiers to `_scorecard-index-rest.md`, creating it from the header of `_scorecard-index-phase4.md` if needed: a ranked table row plus a 1–3 sentence case each. Re-rank the whole table.
   2. Set rows to `done`.
   3. Rebuild the lens rankings:

      ```bash
      D=$(mktemp -d)
      python3 lenses/_state/digest.py "$D"
      python3 lenses/_state/verify.py "$D" lenses/_state/scores   # must print VERIFY-CLEAN
      python3 lenses/_state/build.py "$D" lenses/_state/scores
      ```

   4. Run the full checks: `bash _state/rest/verify.sh` (all `done` rows) and `python3 _state/rest/check_queue.py`.
   5. Update the CURSOR: batch row, totals, qualifiers, and one or two sentences on the batch's pattern, as `_phase2-plan.md` does.
   6. Commit (`rest: batch N, <sector> (<k> industries, <files> files)`) and push.
6. **Next batch.** Go straight on. Don't stop between batches to ask.

**Stop early only if** a verifier fails twice on something you can't fix inside new files, or context is running low. Either way, finish closing the current batch first (step 5), so the cursor is never stale.

**To resume** after an interruption:

1. Read the CURSOR.
2. Run `check_queue.py`.
3. For each `building` row, run `verify.sh <slug>`:
   - if it's clean and reviewed, close it;
   - otherwise, relaunch its builder with "complete the existing files; don't duplicate".

## 6. Per-industry method (what a builder does)

### 6.1 Discover before writing

Research the industry, then write. Answer these questions. The sources listed are examples that work; any public, non-banned source is fine.

| Question | Where to look |
|---|---|
| How many firms, how big, how much revenue? | US Census Economic Census, Statistics of US Businesses and County Business Patterns tables by NAICS code (data.census.gov; the API needs a key, so use the published tables or search results); USDA Census of Agriculture for sector 11; BLS QCEW |
| Who works there and what do they do all day? | BLS OEWS industry staffing patterns, O*NET task lists, apprenticeship and trade-school curricula, public job ads |
| Who pays, for what, on what contract and margin? | 10-K filings of public players (SEC EDGAR full-text search), trade association benchmark summaries, trade press |
| What rules and clocks govern the work? | The regulators (OSHA, EPA, FDA, USDA, DOT/FMCSA, state licensing boards), standards bodies, inspection and permit cycles |
| What tools are in use, and where do they fall short? | Vendor sites and pricing pages, G2 and Capterra category pages, trade press reviews |
| What hurts, in workers' own words? | Trade forums, subreddits for the trade, trade-press interviews |
| What do experienced people "just know"? | Trade press, apprenticeship material, forums ("you develop a feel for...") |

Budget about 8–15 searches per industry. Web-check at least three headline figures (market size, firm count, and one named tool, regulation or player) and write everything else as an estimate. Record the work in `_state/rest/sources/<slug>.md`:

```markdown
# Sources — <Industry Name>

## Checked
- <claim as written in the vault> — <URL> (accessed YYYY-MM-DD)

## Estimates (not checked)
- <claim> — <basis: recalled, derived from X, analogy to Y>

## Searches that found nothing
- <query> — <what was missing>
```

Read the closest existing hubs named in the queue's `boundary` column. Where a new note touches their territory, link to them (`[[data-marketplace-brokers|Data Marketplace Brokers]]`) instead of duplicating them.

### 6.2 Stage A: hub and problems

1. **Hub.** Write `industries/<slug>.md` (§9.2).
2. **Five problem notes, all distinct.** They cover five different workflows. The two low-impacts are different customisation gaps, and the two worker-lifes are different personal pains.
   - **High impact.** For craft, physical, clinical or judgement-heavy work, the high-impact problem **is** the tacit-knowledge problem. Its "Why It's Unsolved" covers the data-collection challenge (capturing the expert doing the task), the labelling challenge (experts disagree with themselves) and the deployment challenge (it must be faster than the expert).
3. **ML opportunities.** `ml-opportunity.md` has 4–5 entries, with a `#tacit-knowledge-ml` entry **first**. Each is specific enough for an engineer to scope in a meeting. The entries span at least three different techniques.
4. **Agents and platforms.** `ai-agents-platforms.md` has 3–4 distinct product concepts, not rephrasings of each other.

### 6.3 Stage B: niche layer

1. **Pick eight level-1 niches, two per axis:**
   - 🔵 High Market Share: where the money is;
   - 🟠 Low Digitized: where paper, phone and memory still run the work;
   - 🟣 Underserved Audience: a person or segment the tools ignore;
   - ⚡ Highly Automatable: the most mechanical, repeatable work.
2. **Write the contested sentence for each:** *"Every serious competitor in this niche is fighting to X, and whoever does X best takes the account."*
3. **Decompose where the sentence won't come.** A niche whose sentence produces two contests with different winners is not terminal. It still gets its own 4 files, with a `**Contested on:**` line that says so honestly. It is then decomposed into 🎯 contested sub-niches: sibling directories, `**Category:** Contested Sub-Niche`, 4 files each, linked indented under the parent. Phase 2 and Phase 4 found about one non-terminal niche per industry. That is an observation, not a quota.
4. **Write `## Filter Notes`.** Cover:
   - which niches are terminal;
   - why the decomposed one wasn't;
   - the close calls;
   - 2–3 candidates considered and rejected, with the reason.

### 6.4 Stage C: Pass 2 insight layer

1. **Sweep.** Cover the seven value-chain positions of `_direction.md` §5 (aggregators and rollups, payers and intermediaries, data and benchmark vendors, association research arms, specialist advisory and valuation, regulators, suppliers selling in) and log **at least 10 pockets**.
2. **Gate first:** is there plausibly a dedicated research or insight function of 10+ people?
3. **Score the survivors** on Q1–Q5 (max 60), and judge the kill switches separately, as yes or no.
4. **Write the files.** Every pocket gets a plain `profile.md`. Qualifiers (≥50/60 and no live kill switch) also get build, buy and fix, plus a `**Contested on:**` line in all four files.
5. **Append** the Pass 2 half to the industry's own `_overview.md`, below a `---`.

Most operator-tier industries yield few or no qualifiers. That is the expected, correct result, and the empty positions are part of the map.

### 6.5 Stage D: lens scores

Write `lenses/_state/scores/<slug>.jsonl`, one JSON line per item: the industry, plus every directory under `niches/<slug>/` (level-1 niches, sub-niches and pockets).

```json
{"id":"<slug>/<dir>","ai_proof":[phys,liab,trust,judg,dur],"clarity":[what,how,rep,fb],"digital":[input,prod,deliv,buy],"why_ai":"<one sentence>","why_clarity":"<one sentence>","why_digital":"<one sentence>"}
```

- **Factors** are integers from 1 to 5, scored against the anchors in `lenses/_method.md`.
- **What to score.** Score an industry as its typical operator's core work, and a function niche as that function. Score an insight pocket as that organisation's own work, not the frontline work of the parent industry.
- **Calibration.** Compare against the 2–3 most similar rows in `lenses/scores.csv`.

### 6.6 Self-check

Run `bash _state/rest/verify.sh <slug>` until it prints `REST-VERIFY-CLEAN`, then report (§7).

## 7. Builder brief (paste one per industry, fill the angle brackets)

```text
You are building one new industry into the Obsidian vault at <absolute path to problem-index/>.
Industry: <name>   slug: <slug>   category: <category>   NAICS 2022: <codes>
Boundary: <boundary sentence from queue.tsv>

1. Read _remaining-industry-implementation-and-discovery-plan.md §2, §3, §6 and §9, then the reference
   files listed in §3 item 5. Follow them exactly. Do not redesign the method.
2. Research first (§6.1). Write _state/rest/sources/<slug>.md as you go.
3. Build Stage A, B, C and D for this slug only (§6.2–6.5). Write ONLY these paths:
   industries/<slug>.md, problems/<slug>/, niches/<slug>/, lenses/_state/scores/<slug>.jsonl,
   _state/rest/sources/<slug>.md. Never edit any other file, and never touch queue.tsv, the CURSOR or any index.
4. Never fetch LinkedIn, Crunchbase, ZoomInfo, PitchBook, Glassdoor, Apollo or RocketReach.
5. If some files already exist for this slug, read them and complete the set; don't duplicate.
6. Run `bash _state/rest/verify.sh <slug>` and fix until it prints REST-VERIFY-CLEAN.
7. Reply with: file count; the 8 niches and any sub-niches; Pass 2 pocket count split into
   qualified / below threshold / kill switch / fails gate; each qualifier's name, score and a 1-3 sentence
   case; the three headline figures you web-checked; anything you suspect is wrong in an existing vault
   file (don't fix it); and the verifier's last line.
```

## 8. Reviewer brief (one per 5 industries)

```text
Review these new vault industries, read-only: <slugs>. Vault root: <absolute path>.
Read §2, §6 and §9 of _remaining-industry-implementation-and-discovery-plan.md and the hedge-funds reference first.
The structural verifier already passed; check what it cannot:
- Boundary: does any new industry duplicate an existing one, and do the merged NAICS codes really share the work?
- Specificity: named workflows, tools, regulations and numbers. Flag every "improves efficiency"-style sentence.
- Tacit: is the first ml-opportunity entry a real expert judgement, with the collection, labelling and deployment
  challenges explained? For craft, physical or clinical work, is the high-impact note the tacit problem?
- Distinctness: five problem notes on five workflows; ml entries spanning at least three techniques.
- Filter: is every contested sentence specific? Do the Filter Notes justify the decomposition and the rejections?
- Pass 2: are gate verdicts honest (no inflated headcounts), scores consistent with similar pockets in
  _scorecard-index.md and _scorecard-index-phase4.md, and kill switches judged separately?
- Facts: spot-check two figures per industry against its source log. Any number with neither a source nor
  "~"/"estimate" is a finding.
- Lenses: are the scores consistent with lenses/_method.md anchors and similar rows in lenses/scores.csv?
Return a list: file, problem, suggested fix. Say "no findings" for a clean industry. Don't edit anything.
```

## 9. Formats

### 9.1 Conventions

- **Wikilinks depend on the source directory.**
  - From `industries/`, use vault-root paths: `[[problems/<slug>/high-impact|🔴 High Impact: <Title>]]`.
  - From `problems/`, use the bare industry slug: `[[<slug>|<Name>]]`.
  - From `niches/`, use prefixed paths: `[[industries/<slug>|<Name>]]` and `[[niches/<slug>/<dir>/profile|🔍 <Name>]]`.
  - Every link must resolve.
- **Emoji:**
  - problem lists: 🔴 High Impact · 🟡 Low Impact · 🟢 Worker Life · 🧠 ML Opportunities · 🤖 AI Agents & Platforms;
  - niche axes: 🔵 High Market Share · 🟠 Low Digitized · 🟣 Underserved Audience · ⚡ Highly Automatable;
  - other niche types: 🎯 Contested Sub-Niche · 🔍 Pass 2 pocket;
  - opportunity notes: 🔨 Build · 🛒 Buy · 🔧 Fix.
- **Type strings, exactly:**
  - `High Impact`
  - `Low Impact (Customisation Opportunity)`
  - `Worker Life Changing`
  - `Build (Greenfield Opportunity)`
  - `Buy & Customize (Vertical Adaptation)`
  - `Fix (Pain Point)`
- **Spelling split.** `low-impact` uses "Customi**s**ation Gap" and `buy.md` uses "Customi**z**ation Gap".
- **Tag counts:**
  - problem notes: 6–8;
  - build, buy and fix: 5–10;
  - ml and agent entries: a tag line under each `## N.` heading.
  - Mix technique tags with context tags (`#tacit-knowledge-ml #quick-win #automation #data-integration #workflow-orchestration #compliance #worker-facing #revenue-impact #ai-agent #ai-platform`).
- **Lengths.** These are the Phase 4 medians, in words. Aim near them; don't pad.

  | Note | Words |
  |---|---|
  | hub | ~770 |
  | high-impact | ~840 |
  | low-impact | ~450 each |
  | worker-life | ~450 each |
  | ml-opportunity | ~1,380 |
  | ai-agents-platforms | ~750 |
  | `_overview.md`, both halves | ~1,600 |
  | niche profile | ~270 |
  | build | ~270 |
  | buy | ~230 |
  | fix | ~230 |
  | qualified pocket profile | ~340 |
  | gate-failure pocket profile | ~150 |

### 9.2 Hub — `industries/<slug>.md`

```markdown
# <Industry Name>

## Profile
**Category:** <category from queue.tsv>
**NAICS 2022:** <code>, <code> — <short titles>
**Market Size:** ~<figure> (<source or "estimate">)
**Tech Maturity:** <Low | Medium | High> — <one sentence on why>
**Workforce:** <who does the work day to day>

## Key Pain Themes
<2–3 paragraphs: specific workflows, the people in them, the consequence, and the external clocks.>

## Current Tech Landscape
<1 paragraph: named tools and vendors, what each does well, and the record that no tool owns.>

## Problems
- [[problems/<slug>/high-impact|🔴 High Impact: <Title>]]
- [[problems/<slug>/low-impact-1|🟡 Low Impact: <Title>]]
- [[problems/<slug>/low-impact-2|🟡 Low Impact: <Title>]]
- [[problems/<slug>/worker-life-1|🟢 Worker Life: <Title>]]
- [[problems/<slug>/worker-life-2|🟢 Worker Life: <Title>]]
- [[problems/<slug>/ml-opportunity|🧠 ML Opportunities]]
- [[problems/<slug>/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
<1 paragraph: the industry's central unmeasured judgement, what blocks fixing it (organisational, legal or
structural), and where the strongest commercial opening sits, including saying so if the operators themselves
are poor buyers.>
```

### 9.3 Problem notes — `problems/<slug>/`

The metadata block is the same for all five notes:

```markdown
# <Problem Title>

**Industry:** [[<slug>|<Industry Name>]]
**Type:** <High Impact | Low Impact (Customisation Opportunity) | Worker Life Changing>
**One-liner:** <one sentence>
**Tags:** <6–8 tags>
```

Headings per note:

| Note | `##` headings, in order |
|---|---|
| high-impact | The Problem · Why It's Unsolved · What a Solution Looks Like · Impact If Solved |
| low-impact-1, low-impact-2 | The Problem · What Already Exists · The Customisation Gap · Impact If Solved |
| worker-life-1, worker-life-2 | The Problem · Why It Matters to the Worker · What a Solution Looks Like · Impact If Solved |

`ml-opportunity.md`:

```markdown
# Machine Learning Opportunities — <Industry Name>

**Industry:** [[<slug>|<Industry Name>]]
**Derived from:** [[problems/<slug>/high-impact|High Impact]], [[problems/<slug>/low-impact-1|Low Impact 1]], [[problems/<slug>/low-impact-2|Low Impact 2]], [[problems/<slug>/worker-life-1|Worker Life 1]], [[problems/<slug>/worker-life-2|Worker Life 2]]

---

## 1. <Tacit-knowledge opportunity title>
#tacit-knowledge-ml <technique tags> <context tags>

**Problem statement:** <1–2 sentences>

**ML task:** <e.g. multi-label classification + calibrated probability>
**Input data:** <modality, format, sources>
**Target:** <labels or outputs>
**Evaluation metric:** <primary metric, why, and asymmetric costs>
**Scope:** <team, timeline, honest difficulty; for the tacit entry, the collection, labelling and deployment challenges>
**Data availability:** <who holds it, what labelling it needs>

---

## 2. <Next> … (4–5 entries in total, separated by ---)
```

`ai-agents-platforms.md`:

```markdown
# AI Agents & Platform Opportunities — <Industry Name>

**Industry:** [[<slug>|<Industry Name>]]

---

## 1. <Agent or Platform Name>
<#ai-agent or #ai-platform plus technique and context tags>

**Concept:** <2–3 sentences on what it does autonomously>
**Inputs:** <data, triggers, user commands>
**Outputs / Actions:** <what it produces or does>
**Why now:** <the recent capability that makes it buildable>
**Market:** <who pays, rough size, existing buyer category or not>

---

## 2. … (3–4 entries in total)
```

### 9.4 Niche overview — `niches/<slug>/_overview.md`

```markdown
# Niche Analysis — <Industry Name>

**Parent Industry:** [[industries/<slug>|<Industry Name>]]

## Niche Selection

<1 paragraph framing. Say what the market sizes measure (e.g. tooling and services spend), not industry revenue.>

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | <Name> | 🔵 High Market Share | ~$<n> | <Low/Medium/High> | <role> |
| … 8 rows, two per axis, in axis order 🔵 🔵 🟠 🟠 🟣 🟣 ⚡ ⚡ |

## Why These Niches

<1 paragraph: why each pair earned its axis.>

## Niches

- [[niches/<slug>/<niche>/profile|🔵 <Name>]]
  - [[niches/<slug>/<sub-niche>/profile|🎯 <Name>]]   ← indented two spaces, under its non-terminal parent
- … all 8

## Filter Notes

<Terminal or not, per niche; why the decomposed one wasn't; close calls; rejected candidates.>

---

## Pass 2 — Insight-Layer Discovery

<1 paragraph method statement, as in the reference.>

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | <Name> | <Data vendor / Specialist advisory / …> | <headcount range> | **<n>** | ✅ Indexed |
| … numbering continues from 9; sort qualifiers first, then by score; Verdict ∈ ✅ Indexed · Below threshold · ⚠️ Kill switch · Fails gate (score "—") |

## Why These Pockets

<2–3 paragraphs: the central finding (including "the operators themselves fail the gate"), the shape the
qualifiers share, and the strongest near-miss.>

## Niches — Pass 2
- [[niches/<slug>/<pocket>/profile|🔍 <Name>]]
- … every pocket
```

### 9.5 Level-1 niche and contested sub-niche — `niches/<slug>/<niche>/`

**`profile.md`.** It carries no Tags line. For a sub-niche, `**Category:**` is `Contested Sub-Niche`.

```markdown
# <Niche Name>

**Parent Industry:** [[industries/<slug>|<Industry Name>]]
**Category:** <High Market Share | Low Digitized | Underserved Audience | Highly Automatable | Contested Sub-Niche>
**Contested on:** Every serious competitor in this niche is fighting to <X>, and whoever <does X best> takes the account.

## Profile
**Market Size:** ~$<n> <what is counted> (estimate)
**Share of Parent Industry:** ~<n>% (estimate)
**Digital Adoption:** <level> — <why>
**Target Buyer:** <role>
**Automation Potential:** <level and qualifier>

## What Makes This a Distinct Niche
## Current Tools & Gaps
## Problems
- [[niches/<slug>/<niche>/build|🔨 Build: <Title>]]
- [[niches/<slug>/<niche>/buy|🛒 Buy: <Title>]]
- [[niches/<slug>/<niche>/fix|🔧 Fix: <Title>]]
```

A non-terminal level-1 niche's line reads like this: `**Contested on:** *Not terminal as stated.* The honest partial sentence is … Decomposed into contested sub-niches below.`

**`build.md`, `buy.md`, `fix.md`.** These share one metadata block:

```markdown
# <Opportunity Title>

**Niche:** [[niches/<slug>/<niche>/profile|<Niche Name>]]
**Industry:** [[industries/<slug>|<Industry Name>]]
**Type:** <Build (Greenfield Opportunity) | Buy & Customize (Vertical Adaptation) | Fix (Pain Point)>
**One-liner:** <one sentence>
**Tags:** <5–10 tags>
**Contested on:** <the same sentence as the profile>
```

Headings per note:

| Note | `##` headings, in order |
|---|---|
| build | The Problem · Why Nobody Has Built This · What to Build · Target Customer · Impact If Built |
| buy | The Problem · What Already Exists · The Customization Gap · Target Customer · Impact If Solved |
| fix | The Problem · Why It's Still Broken · What a Fix Looks Like · Who Feels the Pain · Impact If Fixed |

### 9.6 Pass 2 pocket — `niches/<slug>/<pocket>/profile.md`

```markdown
# <Pocket Name>

**Parent Industry:** [[industries/<slug>|<Industry Name>]]
**Category:** Insight Layer
**Value-Chain Position:** <one of the seven positions>
**Contested on:** <qualifiers only>

## What They Do
<2–4 plain sentences: who they are, what they produce, who pays.>

## Insight Function
**Size:** <headcount range>
**Output:** <the billable artifact>
**Proprietary data:** <the corpus they own>
**Clock:** <the third-party deadline>
**Buyer:** <named role>

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | n |
| Q2 Labor mass + repeatable | ×2 | n |
| Q3 Proprietary data moat | ×3 | n |
| Q4 External clock | ×2 | n |
| Q5 Buyer + market | ×2 | n |
| **Weighted total** | | **n/60** |

**Kill switches:** <none, or name it and say why>
**Verdict:** <Qualified — indexed | Logged — below threshold | Logged — kill switch | Logged — fails gate (<reason>)>

## Problems
<qualifiers only: the 🔨 / 🛒 / 🔧 links; omit the section otherwise>
```

Gate failures show `—` for every score and `**—/60**`. Qualifiers add build, buy and fix in the §9.5 format, with `**Niche:**` pointing at the pocket profile.

## 10. Stage E: merge into the shared registers (held for the owner)

Stage E is the only step that edits existing files. It runs only on the owner's explicit yes, as its own commit. Prepare the diff list when the queue is done, or sooner if the owner asks:

- `_bookmark.md`: a section listing the new industries by batch;
- `niches/_bookmark.md`: the Pass 1 and Pass 2 logs;
- `_scorecard-index.md`: fold in `_scorecard-index-rest.md` (and the pending Phase 4 index), re-ranked, after reconciling pockets scored twice under two industries;
- `problem-index/CLAUDE.md` counts, and its wrong `ai-agents-platforms` field list;
- `../industries.ts`, if the owner wants the reference list kept in step.

## 11. Out of scope

- `history/`, `lineage/`, `origins/`, `series/`, the book and content work.
- The company census.
- Fixing anything in existing files (log it instead).
- Industries outside NAICS 2022. Propose those in the Findings log; don't build them.

---

## CURSOR

**Stage:** batch loop. Batches 1–5 closed 2026-10-22, batches 6–9 closed 2026-10-23 (batch 9 early, with 2 of its 8 industries); placement-priority batches next.
**Triage:** 714 of 714 codes (new 421 · merge 265 · covered 17 · skip 11)
**Queue:** 421 industries in 49 batches
**Done:** 68 industries · 4,475 files (4,339 vault + 136 state) · 4 qualifiers
**Last verifier run:** `verify.sh` (all done rows) → REST-VERIFY-CLEAN; `check_queue.py` → QUEUE-CLEAN; lenses rebuilt via `_state/rest/lens_rebuild.sh` (2026-10-23, batch 9 close)
**Next action:** (paused) batch 9 closed early on 2026-10-23 with contract-packagers and auctioneers; its six waste industries moved to batch 9b. The owner asked for a short-term placement filter, so the next batches are the placement-priority ones being set up the same evening.
**Paused (owner, 2026-10-23):** the owner paused the run after the in-flight auctioneers build, at 67% of the weekly quota, to keep quota for higher-impact daytime work. From now on the run happens at night only, when the owner restarts it; there is no auto-resume heartbeat. On restart: finish batch 9 (waste-haulers onward). Scheduled by the owner (session-only crons): resume Sat 2026-10-24 00:03 PKT with **3 parallel agents** until the weekly quota reset at 15:00 PKT (no new builders after 14:30); at 14:52 the cap returns to 1 and the run pauses again.
**Run constraint (owner, 2026-10-22):** at most **1 subagent at a time** from batch 5's remaining builds onward (it was 3 until then), builders, reviewers and fix rounds combined; the live cap is in `_state/rest/agent-cap.txt`. §5 step 2's "up to 10 at once" is overridden. The owner set it to 1 to keep quota for other work: the first 37 industries used about 36 points of a 47%-used weekly quota, roughly 1% of a week per industry. Builders must not spawn forks or subagents (the brief says so).
**Coordinator tooling (2026-10-22):** `_state/rest/brief.py <slug>` prints the §7 brief with built siblings and review lessons; `set_status.py`; `resort_p2.py <slug>` re-sorts a Pass 2 table after a fix; `lens_rebuild.sh` runs §5.3 while later batches are mid-build (it leaves non-`done` slugs out); `build_scorecard.py` writes `_scorecard-index-rest.md` from `qualifiers.jsonl` and checks each profile still says Qualified at the same total. Builder reports, review checklists and pending findings live in `_state/rest/reports/`.

**Stage 0 notes.** Every decision and boundary sentence lives in `_state/rest/stage0_triage.py`, which writes both TSVs; don't re-run it once any row is past `todo`, because it resets statuses. The count (421) sits above the plan's 300–400 guess because services stayed close to one industry per code, as §0.2 expects; manufacturing came to 272 + 5 cross-sector codes in 119 industries (~2.3 per industry) and wholesale to 59 codes in 31. Covered: 17 codes folded into existing hubs (e.g. 541214 → `payroll-platforms`, 813920 → `trade-associations`). Skipped: 11 single-operator or shell codes (Federal Reserve, USPS, NASA, DoD, State, holding companies, household employers, video rental). Category: 8132–8139 nonprofits (foundations, advocacy, civic clubs, unions, political) use `Nonprofit & Government` instead of the table's `Specialty Services`, and the 52xxx insurance carriers and benefit pools use `Insurance`. Residual "all other" codes were built around their largest firm type; the `reason` column says which (e.g. 238990 → asphalt paving; fence and pool builders also sit there).

| Batch | Sector | Industries | Done | Files | Qualifiers | Pattern |
|---|---|---|---|---|---|---|
| 1 | 54 Professional Services | 10 | 10 | 667 | 1 | Design and technical services. Every operator fails the gate: they sell design or production, not research. Builders put four pockets beside the operators at 51–52, and review cut three: a client's permit schedule isn't a third-party clock, five-firm markets earn Q5 2–3, and licensing an owned library doesn't grow with headcount. One survived: product-regulation intelligence (51), harmonised with the indexed regulatory-content pockets. |
| 2 | 54 Professional Services | 10 | 10 | 659 | 1 | Media, marketing services and legal-adjacent work. Four first-pass qualifiers became one: pipeline intelligence and PR measurement fell to 49 on Q5 (three- to four-vendor markets), and invalidity search houses took the work-product kill switch, the vault's majority rule for litigation support. The survivor is IND regulatory strategy (50), at the threshold. Sibling duplicates (CertifID, imaging research, ELN) were collapsed into one profile each. |
| 3 | 51 Information | 7 | 7 | 464 | 2 | Film, music and media production. Builders scored no qualifiers; reviewers found two missed ones by holding siblings to the same rubric. Collecting societies (51) were rescored against the indexed permissions agencies, and the sound-recording societies (51) against them, both on the global society field (45 and 40 on US-only scoring). Most other pockets failed the gate once headcount was counted per firm rather than summed. |
| 4 | 51 Information | 7 | 7 | 459 | 0 | Telecom, broadcast, satellite and libraries. No qualifiers: the operators analyse their own networks and invoice nothing, and most nearby data sits under CPNI, issuer or member-data kill switches or in one- or two-vendor markets. Parallel builds caused cross-sibling duplicates (robocall engines, Kagan, merger economists, credit ratings), so each was collapsed to one profile. The SIM-swap rule status was standardised in one sourced sentence. Direct-to-home pay TV, public-school libraries and IoT resale are logged as unanalysed. |
| 5 | 52 Finance & Insurance | 8 | 8 | 522 | 0 | Banks, card issuers, finance companies, mortgage lenders, pawnshops, money transmitters, commodity brokers and trust companies. No qualifiers: the operators' decision histories are borrower or beneficiary data, and the pockets around them work on client loan-level or holdings data under service agreements (a live kill switch unless checked terms permit aggregate use) or sell to a handful of firms. Review cut the one first-pass qualifier (pipeline hedge advisors, 49 with a kill switch), re-gated enforcement units as production, and collapsed cross-sibling duplicates (fair lending, structured-finance analytics, ABS ratings, consent-order remediation) to one profile each. Third-party loan servicing, commercial and multifamily mortgage banking, and commodity dealing are logged as uncovered. |
| 6 | 52 Finance & Insurance | 7 | 7 | 471 | 0 | Pension funds, benefit pools and the five insurance carrier types. No qualifiers: risk-bearers price insight into premium (Q1 2–3), the actuaries, repricers and auditors who invoice work on plan- or carrier-owned data (PHI under BAAs, client claim files), and the clean data pockets are one- to three-firm markets. Review aligned every signed actuarial opinion on a statutory date at ~48 with a kill switch, re-gated per-report and examination staff as production (zoning reports, plan audits, regulators), and treated state insurance departments and cat-model companies as single organisation families. Commercial/multifamily mortgage banking stays uncovered, and life/A&H reinsurance has only two Pass 2 pockets. |
| 7 | 56 Admin, Support & Waste | 9 | 9 | 582 | 0 | Facilities management, executive search, PEOs, document preparation, answering services, mail centers, credit bureaus, repossession and court reporting. No qualifiers: the operators sell labour, and the analytics around them sit on client- or member-furnished data (PHI, FCRA furnishing, client call and claim files) or in one- to three-firm markets. The one first-pass qualifier, building-performance-standard compliance consultancies, fell from 51 to 46 on review: NYC's audit and benchmarking records are public (Q3 3) and the LL97 filing can be extended (Q4 4). Review also re-gated per-report and examiner staff and per-organisation headcounts, and set a contributed-data kill-switch rule (FCRA furnishing or member trust = live) for Stage E to apply to tenant screening and identity graphs. |
| 8 | 56 Admin, Support & Waste | 8 | 8 | 521 | 0 | Travel agencies, tour operators, visitors bureaus, ticketing, investigation and screening, armored car, alarm integrators and locksmiths. No qualifiers: the operators sell labour or inventory risk, the platforms around them are one- to three-firm markets with self-set clocks, and most insight teams turned out to be production staff once counted per firm (investigators, desk analysts, implementation staff). Review dropped three kill switches where checked terms gave vendors product rights (Alarm.com, SmartRent and Schlage, ticket-fraud signals) and re-gated summed or production headcounts. The guard licensing boards were found to be one organisation family licensing PIs, alarm firms, locksmiths and repossessors, and the guards' alarm-monitoring pocket is misfiled now that central stations have their own industry (both logged for Stage E). |
| 9 | 56 Admin, Support & Waste | 2 | 2 | 130 | 0 | Contract packagers and auctioneers, closed early on 2026-10-23 so the placement-priority batches could run next. No qualifiers: the packagers' EPR compliance pocket fell to 41 under a kill switch, the ABL collateral-appraisal pocket stays at 50 under a live kill switch with ~10–25 central analysts, and auction-house pockets cap Q3 at 3 because hammer prices are public. The six waste industries moved to batch 9b. |
| 10 | 61 Education | 9 | 0 | — | — | — |
| 11 | 62 Health Care | 9 | 0 | — | — | — |
| 12 | 62 Health Care | 9 | 0 | — | — | — |
| 13 | 53 Real Estate & Rental | 9 | 0 | — | — | — |
| 14 | 71 Arts & Recreation | 8 | 0 | — | — | — |
| 15 | 71 Arts & Recreation | 8 | 0 | — | — | — |
| 16 | 81 Other Services | 8 | 0 | — | — | — |
| 17 | 81 Other Services | 7 | 0 | — | — | — |
| 18 | 81 Other Services | 7 | 0 | — | — | — |
| 19 | 72 Accommodation & Food | 6 | 0 | — | — | — |
| 20 | 42 Wholesale | 8 | 0 | — | — | — |
| 21 | 42 Wholesale | 8 | 0 | — | — | — |
| 22 | 42 Wholesale | 8 | 0 | — | — | — |
| 23 | 42 Wholesale | 7 | 0 | — | — | — |
| 24 | 44-45 Retail | 10 | 0 | — | — | — |
| 25 | 44-45 Retail | 10 | 0 | — | — | — |
| 26 | 44-45 Retail | 10 | 0 | — | — | — |
| 27 | 48-49 Transportation | 8 | 0 | — | — | — |
| 28 | 48-49 Transportation | 7 | 0 | — | — | — |
| 29 | 48-49 Transportation | 7 | 0 | — | — | — |
| 30 | 23 Construction | 8 | 0 | — | — | — |
| 31 | 23 Construction | 8 | 0 | — | — | — |
| 32 | 22 Utilities | 8 | 0 | — | — | — |
| 33 | 21 Mining | 8 | 0 | — | — | — |
| 34 | 11 Agriculture | 8 | 0 | — | — | — |
| 35 | 11 Agriculture | 8 | 0 | — | — | — |
| 36 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 37 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 38 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 39 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 40 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 41 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 42 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 43 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 44 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 45 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 46 | 31-33 Manufacturing | 10 | 0 | — | — | — |
| 47 | 31-33 Manufacturing | 9 | 0 | — | — | — |
| 48 | 92 Public Administration | 9 | 0 | — | — | — |
| 49 | 92 Public Administration | 8 | 0 | — | — | — |

---

## Findings log

*Append-only. Defects or contradictions found in existing files go here, not into those files.*

- 2026-10-22 (plan author): Phase 4 qualifiers carry `**Contested on:**` inconsistently. The three `hedge-funds` qualifier profiles lack it, though their build/buy/fix files have it; `asset-managers` has it everywhere. `_phase2-plan.md` §2 says the filter applies to pockets, so this plan requires the line on all four files of every qualifier, and `_state/rest/verify.sh` enforces it. That is why §3 points to an `asset-managers` pocket as the qualifier reference.
- 2026-10-22 (batch 1, landscape-architecture-firms builder): `niches/landscaping/landscape-architecture-firms/profile.md` scores design firms as a 46/60 insight pocket with Q1 = 5, but design (not research) is their invoice and they have no 10-person insight function; under `_direction.md` they should fail the gate.
- 2026-10-22 (batch 1, same): `niches/landscaping/landscape-design-install/profile.md` calls Land F/X a "$3,000+/year" CAD tool; it is an AutoCAD add-on (Planting F/X ~$695/yr plus the AutoCAD licence).
- 2026-10-22 (batch 1, same): `niches/engineering-consultants/design-liability-insurers/profile.md` names a live kill switch (claim files under privilege) but its verdict reads "Logged — below threshold", while the overview marks it ⚠️ Kill switch.
- 2026-10-22 (batch 1, architecture-firms builder): kill-switch verdict mismatches — `niches/engineering-consultants/engineering-firm-aec-practices/profile.md` and `niches/electrical-contractors/electrical-inspection-agencies/profile.md` each name a live kill switch but read "Logged — below threshold" while their overviews mark ⚠️ Kill switch (same pattern as `design-liability-insurers`).
- 2026-10-22 (batch 1, same): `engineering-consultants` has both a Pass 1 niche `forensic-engineering` and a Pass 2 pocket `forensic-engineering-firms` (indexed at 51) covering the same organisations — a double count to reconcile at Stage E.
- 2026-10-22 (batch 1, graphic-design-studios builder): `niches/food-manufacturing/food-regulatory-affairs-consultancies/profile.md` (and that industry's overview row) labels Registrar Corp and EAS Consulting as "Regulatory & enforcement bodies"; they are private consultancies ("Specialist advisory & valuation").
- 2026-10-22 (batch 1, same): `niches/metal-fabrication/_overview.md` uses a "↔ Cross-referenced" verdict, outside the four verdicts the plan allows (✅ Indexed · Below threshold · ⚠️ Kill switch · Fails gate).
- 2026-10-22 (batch 1, specialty-design-studios builder): `niches/alterations-tailoring/technical-design-spec-houses/profile.md` and `niches/metal-fabrication/osha-metalworking-enforcement/profile.md` name live kill switches but read "Logged — below threshold"; their overviews mark ⚠️ Kill switch.
- 2026-10-22 (batch 1, same): `_rest-of-the-industries.md` maps 541420 Industrial Design Services to `product-design-studios`, but that hub covers digital product and UX design (Figma, conversion). Industrial design of physical products has no home in the vault; a candidate for a later addition. (The Stage 0 queue repeated the mistake in three boundary sentences; corrected in `queue.tsv` and `stage0_triage.py` on 2026-10-22.)
- 2026-10-22 (batch 1, drafting-services builder; not web-checked): `niches/metal-fabrication/structural-steel-fabricators/fix.md` and its profile name FabSuite and FabTrol as current products; FabSuite has been sold as Tekla PowerFab since Trimble's acquisition.
- 2026-10-22 (batch 1 review): the operators-fail-the-gate verdict in `niches/landscape-architecture-firms/_overview.md` contradicts the existing `niches/landscaping/landscape-architecture-firms/profile.md`, which passes the same firms at 20–150 people and scores them 46/60. Reconcile at Stage E.
- 2026-10-22 (batch 1 review): Pantone-type colour organisations are now scored in three places — `niches/printing-shops/colour-standard-licensing` (standards and colour science, 43) and the forecasting slice in `niches/graphic-design-studios/colour-standards-forecasting` and `niches/specialty-design-studios/colour-systems-forecast-publishers` (both 40). Cross-linked; treat as one organisation family at Stage E.
- 2026-10-22 (batch 1, testing-laboratories builder): the kill-switch verdict mismatch is systemic. Profiles that name a live kill switch but read "Logged — below threshold" while their overview row says ⚠️ Kill switch include `environmental-consultants/environmental-analytical-laboratories`, `engineering-consultants/materials-testing-labs`, `medical-device-mfg/testing-certification-laboratories`, `electrical-contractors/electrical-product-certification`, `ecommerce-sellers/consumer-product-compliance-testing`, `metal-fabrication/nondestructive-testing-services` and `metal-fabrication/materials-testing-failure-analysis` (possibly `cleaning-companies/disinfectant-efficacy-testing-labs`). A vault-wide sweep at Stage E would settle it.
- 2026-10-22 (batch 1, same): private labs and certifiers filed under "Regulatory & enforcement bodies": `electrical-contractors/electrical-product-certification`, `ecommerce-sellers/consumer-product-compliance-testing`, `cannabis-compliance-testing-labs`, `cleaning-companies/disinfectant-efficacy-testing-labs`.
- 2026-10-22 (batch 1, same): `niches/alterations-tailoring/softlines-testing-labs/profile.md` says "Kill switches: none" but its verdict text says client confidentiality blocks the analysis.
- 2026-10-22 (batch 1, geophysical-survey-firms builder): `industries/land-surveyors.md` says "roughly 50,000 licensed firms" and a "$7 billion" market; Census SUSB 2022 for 541370 shows 6,927 firms, 54,801 employees and $8.88B receipts, so the firm count looks like employees or licensees. The hub also carries deprecated tags (#cnn, #llm, #nlp).
- 2026-10-22 (batch 1, logistics-consultants builder): `niches/freight-brokerage/freight-procurement-consultancies/profile.md` (indexed at 51) scores Q4 = 5 on shipper bid calendars, which are the client's own schedule; at Q4 = 4 it would be 49 and leave the index. Reconcile at Stage E.
- 2026-10-22 (batch 1, same): cross-reference scorecards whose rows don't sum to the stated total — `last-mile-delivery/freight-procurement-crossref` (49 vs 51), `warehouse-3pl/freight-rate-benchmark-crossref` (52 vs 54), `warehouse-3pl/parcel-audit-crossref` (52 vs 54), `warehouse-3pl/supply-chain-risk-crossref` (47 vs 54), `warehouse-3pl/industrial-property-data-crossref` (53 vs 54).
- 2026-10-22 (batch 1, same): freight audit & payment is scored 46 with a kill switch under `warehouse-3pl` and 40 without one under `cold-chain-logistics`; and client confidentiality is a kill switch for logistics network consulting but not for freight procurement consultancies, though the same firms (e.g. Chainalytics) do both.
- 2026-10-22 (batch 1, contract-research-labs builder): forensic engineering is scored twice — `niches/engineering-consultants/forensic-engineering-firms` (51, indexed) and the new `niches/testing-laboratories/forensic-engineering-failure-analysis` (46, kill switch for work-product privilege). Reconcile at Stage E; the privilege kill switch argues against the indexed 51.
- 2026-10-22 (batch 1, same): `niches/pest-control/glp-efficacy-toxicology-cros/profile.md` names a live kill switch but reads "Logged — below threshold". `niches/grant-writers/sbir-sttr/profile.md` gives $980M and 9% without estimate markers and lacks a Contested on line.
- 2026-10-22 (batch 2, biotech-research-firms builder): `niches/cleaning-companies/disinfectant-efficacy-testing-labs/profile.md` and `niches/veterinary-practices/animal-health-clinical-development/profile.md` name live kill switches but read "Logged — below threshold" (add to the vault-wide sweep).
- 2026-10-22 (batch 2, public-relations-agencies builder): `niches/marketing-agencies-smb/agency-ma-brokerage/profile.md` has numeric Q1–Q5 scores but a `—/60` total and a fails-gate verdict (gate failures should show "—" in every row). `niches/contract-manufacturing/supply-chain-risk-intelligence/profile.md` files Resilinc, Everstream, Interos and Exiger under "Payer & intermediary layer"; they are data and benchmark vendors.
- 2026-10-22 (batch 2, media-rep-firms builder): `niches/news-media-local/media-brokerage-valuation/profile.md` says fails gate but its scorecard rows carry numbers; `niches/news-media-local/broadcast-regulatory-filings/profile.md` reads "below threshold" while its overview row says ⚠️ Kill switch, and its kill switch ("federal procurement") is not one of the defined kill switches.
- 2026-10-22 (batch 2, same): `local-audience-measurement` (49, Q3 = 4) and `audio-audience-measurement` (52, Q3 = 5) score the same kind of currency panel differently, so one is indexed and the other is not.
- 2026-10-22 (batch 2, same; not checked): `niches/news-media-local/local-tv-stations/profile.md` names "Jeebly" as a station CMS, which looks invented; `niches/podcasting-networks/podcast-ad-sales-houses/profile.md` lists Midroll/Stitcher as a current sales house, which looks dated.
- 2026-10-22 (batch 2, direct-mail-agencies builder): `niches/printing-shops/direct-mail-data-postal-optimization/profile.md` and `niches/last-mile-delivery/postal-regulatory-analysis/profile.md` name live kill switches but read "below threshold" (add to the vault-wide sweep).
- 2026-10-22 (batch 2, same): Q5 drift in indexed pockets — `marketing-agencies-smb/search-competitive-intelligence-data` (51) and `collections-agencies/identity-skip-trace-data-providers` (54) score Q5 = 4 for markets of a few large firms; at 2–3 the first would leave the index. Reconcile at Stage E.
- 2026-10-22 (batch 2, portrait-photography-studios builder; not checked): `niches/video-production-smb/wedding-videography-studios/profile.md` gives "$3B" and "22%" without estimate markers, high next to The Knot's ~$2,300 average videographer spend. `niches/video-production-smb/_overview.md` uses "↔ Cross-referenced", and it and `niches/event-planning/_overview.md` write "✗ Fails gate" (outside the allowed verdicts).
- 2026-10-22 (batch 2, commercial-photographers builder): `niches/independent-publishers/copyright-office-registration/profile.md` names a kill switch but reads "below threshold", and scores the US Copyright Office 42 while the new `niches/graphic-design-studios/trademark-copyright-offices/profile.md` scores it 33 with a kill switch. `niches/ecommerce-sellers/brand-protection-enforcement/profile.md` files private vendors (Red Points, Corsearch, MarkMonitor) under "Regulatory & enforcement bodies". `niches/video-production-smb/real-estate-media-producers/profile.md` and `drone-aerial-production/profile.md` give unmarked market sizes and lack Contested on lines.
- 2026-10-22 (batch 2 review): `niches/medical-device-mfg/device-regulatory-affairs-consulting/profile.md` (53) rests Q3 = 4 on precedent mined from FDA's public record plus client correspondence the firm can't reuse; its biotech twin `niches/biotech-research-firms/ind-regulatory-strategy-consultancies` was rescored to Q3 = 3 (50) for that reason. Reconcile at Stage E.
- 2026-10-22 (batch 2, notary-signing-services builder): `niches/small-law-firms/real-estate-closing-attorneys/fix.md` cites IC3 "$400M+" annual real estate wire fraud losses as the largest BEC category; IC3's real estate category was $173M (2024) and $275M (2025). `niches/esignature-document-workflow/notarization-and-witnessing/profile.md` and its overview give unmarked market sizes ($620M, 9%).
- 2026-10-22 (Stage 0 note): Census classifies notary public services under 541199, not 541120; the queue built them as `notary-signing-services` (541120) by firm type, and `legal-support-services` (541199) leaves them out.
- 2026-10-22 (batch 2, title-and-settlement-offices builder): `niches/land-surveyors/title-plant-search-operations/profile.md` (55, indexed) and its copy `niches/small-law-firms/title-plant-search-crossref/profile.md` count 500–3,000 searchers and examiners (production headcount) as the insight function, give Q4 = 5/4 on closing dates, and score Q1 4–5 for work priced into the premium; rescored under this plan's rules it would likely fall below threshold. `niches/land-surveyors/title-underwriting-claims-research/profile.md` treats "the analysis prices an insurance product" as a kill switch (it is a Q1 point) with a non-standard verdict. `niches/hoa-management/resale-certificate-document-services/profile.md` gives Q4 = 5 on closing dates. `niches/small-law-firms/real-estate-closing-attorneys/profile.md` has an unsourced "$5–7B" market and Category "Underserved" instead of "Underserved Audience".
- 2026-10-22 (batch 2, legal-support-services builder): attorney work product is treated inconsistently as a kill switch — live in `personal-injury-law/medical-record-review-chronology`, not in `accounting-firms-smb/forensic-litigation-support` (53) or `personal-injury-law/trial-consulting-jury-research`. `niches/small-law-firms/_overview.md` marks E-Discovery (44) and ALSP (40) ⚠️ Kill switch while their profiles read "Logged — below threshold and fenced" (non-standard).
- 2026-10-22 (batch 2 review): `niches/accounting-firms-smb/forensic-litigation-support/profile.md` (indexed at 53) scores litigation work commissioned through counsel with no kill switch, against the vault majority (about 11 pockets) that treats it as a live "data isn't theirs" kill switch. Reconcile at Stage E with the forensic-engineering overlap.
- 2026-10-22 (batch 3, film-distributors builder): 132 existing overviews have no Pass 2 section (e.g. `streaming-video-platforms`, `stock-media-marketplaces`), so pockets profiled under new industries (streaming demand and title valuation here) may be duplicated if those industries get a Pass 2 run later.
- 2026-10-22 (batch 3, postproduction-studios builder): `niches/video-production-smb/_overview.md` marks Production Incentive & Tax Credit Advisory ⚠️ Kill switch while its profile reads "below threshold" with a non-defined kill switch; the same overview uses "↔ Cross-referenced" and "✗ Fails gate". `industries/video-production-smb.md` has no NAICS line and an unsourced "~$20B, ~25,000 companies". `niches/streaming-video-platforms/*/profile.md` put an emoji inside the Category line, which breaks exact-match category checks.
- 2026-10-22 (batch 3, music-publishers builder): `niches/music-distribution-platforms/_overview.md` says production music and sync licensing are covered by Stock Media Marketplaces, whose hub and niches cover images and video only. `niches/podcasting-networks/podcast-rights-licensing-crossref` and `niches/video-production-smb/rights-licensing-crossref` are second profiles at 53 that treat music sync clearance as the same pocket as the text-permissions agency under independent-publishers. `music-distribution-platforms` profiles carry emoji in Category lines and its hub gives an unmarked market size.
- 2026-10-22 (batch 3, recording-studios builder): production music has no home — `niches/stock-media-marketplaces/_overview.md` (~l.41) rejects it to music-distribution-platforms, whose overview (~l.41) rejects it to stock media; it is now logged as a pocket under `recording-studios` (512290 names stock music libraries). `_rest-of-the-industries.md` still maps 512290 to `audio-production-services` (merged into recording-studios by Stage 0).
- 2026-10-22 (batch 3, directory-and-list-publishers builder): indexed `niches/independent-retailers/commercial-credit-bureaus/profile.md` (56) scores Q5 = 4 for ~four bureaus and Q4 = 4 on a "point of application" clock, and lacks Contested on lines; `niches/pharmacy-independents/drug-compendia-pricing-publishers/profile.md` (56) scores Q5 = 4 for a handful of compendia and lacks Contested on lines. Both likely stay ≥50 but are inflated. Kill switches named with "below threshold" verdicts in `marketing-agencies-smb/local-listings-reputation-data`, `data-analytics-consultants/data-marketplaces-brokers` and `real-estate-appraisers/mls-public-records-aggregators`.
- 2026-10-22 (batch 3, greeting-card-publishers builder): `niches/independent-retailers/wholesale-trade-show-operators/profile.md` merges physical trade-show operators and online wholesale marketplaces (Faire) into one pocket. The vault's only CPSC pocket, `niches/specialty-design-studios/apparel-product-safety-regulators/profile.md`, is scoped to apparel and children's products though CPSC and Reese's Law cover all consumer products.
- 2026-10-22 (batch 4, broadcast-stations builder): `niches/news-media-local/local-tv-stations/profile.md` says "roughly 1,750 commercial stations" (FCC: 1,390 commercial full-power; ~1,777 is all full-power incl. educational) and gives unsourced "$22B" and "55%". `industries/news-media-local.md` lists "Jeeves/TownNews" as a CMS; TownNews' platform is BLOX.
- 2026-10-22 (batch 4, wired-broadband-providers builder): rating agencies scored two ways — `municipal-services/municipal-credit-rating-analysis` (56, no kill switch, Q5 4) vs `financial-data-vendors/credit-rating-agency-analytics` (47, kill switch for confidential issuer data, "three firms"). `utility-contractors/telecom-fiber/profile.md` claims make-ready "takes 3-18 months per pole" (FCC's 75-day clock; new rules May 2026) and frames BEAD as a $42.5B fibre driver (NTIA's 2025 restructuring; ~22% of locations to satellite). `grant-writers/rural-tribal/buy.md` gives an unsourced "20-30% of rural communities lack broadband".
- 2026-10-22 (batch 4, telecom-resellers builder): `niches/independent-restaurants/transaction-tax-content-automation/profile.md` (55) scores Q5 = 4 for Avalara, Vertex and a few peers (2–3 under this plan's rule; still qualifies at 51–53). Carrier-derived phone-number data is a kill switch in `directory-and-list-publishers/phone-number-intelligence` (32) but only lowers Q3 in `collections-agencies/phone-number-reputation-consent-data` (46).
- 2026-10-22 (batch 4, wireless-retail-agents builder): retailer-held data is judged both ways — a live kill switch in `greeting-card-publishers/publisher-category-insight-teams` (32) but none in `greenhouse-horticulture/live-goods-category-management` (43). FCC SIM-swap rules still have no published compliance date (pending OMB); notes calling them "in effect" would be wrong.
- 2026-10-22 (batch 4, satellite-operators builder): `niches/crop-farming/satellite-crop-analytics/profile.md` names a live kill switch but reads "below threshold". `niches/land-surveyors/aerial-lidar-data-providers/profile.md` (49) counts photogrammetrists and processing engineers (production) as the insight function. Direct-to-home satellite TV (DIRECTV, DISH) sits in 517111 but no industry covers it (wired-broadband-providers never mentions it).
- 2026-10-22 (batch 4, libraries-and-archives builder): `niches/independent-publishers/library-supply-circulation-data/profile.md` reads "below threshold" with a live kill switch (patron privacy) while its overview says ⚠️ Kill switch; `niches/independent-publishers/_overview.md` uses "↔ Cross-referenced" and "✗ Fails gate".
- 2026-10-22 (batch 4 review): public-school libraries (an estimated majority of ALA's ~120,000 libraries) sit in no built or queued industry (`libraries-and-archives` excludes them; only `k12-private-schools` exists). The 517810 satellite tracking/telemetry slice is assigned to `telecom-resellers` by Stage 0 but analysed only in prose under `satellite-operators`' ground-station work.
- 2026-10-22 (batch 4, telecom-resellers): IoT/M2M connectivity resale (device certification and network sunsets across hosts) is left unanalysed as a known gap.
- 2026-10-22 (batch 4, wired-broadband-providers): direct-to-home satellite pay TV (DIRECTV, DISH; NAICS 517111 by exception) is named as unanalysed in the wired hub's Filter Notes.
- 2026-10-22 (batch 5, community-banks builder): `industries/credit-unions.md` carries a hub Tags line with deprecated or unsafe tags (#llm, #nlp, #tabular-ml…). `niches/commercial-real-estate/cre-securities-research-firms/profile.md` reads "below threshold" while its overview says ⚠️ Kill switch. `niches/embedded-finance-platforms/*/profile.md` put emoji in Category lines. NAICS 522180 also covers credit unions; community-banks claims only its thrift half (reconcile if credit-unions gets a NAICS line).
- 2026-10-22 (batch 5, credit-card-issuers builder): kill switches named with "below threshold" verdicts in `collections-agencies/cfpb-consumer-research`, `collections-agencies/creditor-recovery-analytics`, `auto-dealers-independent/subprime-auto-credit-research` and `credit-unions/model-validation-firms`. Q5 = 4 for two-to-few-firm markets in indexed `credit-unions/deposit-loan-pricing-data` (54) and `collections-agencies/credit-scoring-model-developers` (54). Model-risk supervision is a kill switch in the credit-scoring pocket but not in `credit-unions/financial-crime-consortium-analytics`. payment-processors, payment-fraud-vendors, bnpl-providers, neobanks, identity-verification-vendors and lending-marketplaces have no Pass 2 sections.
- 2026-10-22 (batch 5, sales-finance-companies builder): indexed `collections-agencies/identity-skip-trace-data-providers` (54) scores Q4 = 3 though its Clock says no third-party deadline (→52) and treats FCRA permissible purpose as no kill switch; indexed `credit-unions/financial-crime-consortium-analytics` (51) gives Q5 = 4 for three vendors (→49 at Q5 3). `auto-dealers-independent/subprime-auto-credit-research` and `dms-vendor-data-teams` name kill switches but read "below threshold". Unchecked: credit-unions files still say "CU Direct" (renamed Origence in 2019).
- 2026-10-22 (batch 5, mortgage-lenders builder): scorecards whose rows don't sum to the stated total — `mortgage-brokers/mortgage-qc-compliance-audit` (51 vs 52), `mortgage-brokers/gse-selling-guide-content` (46 vs 47), `real-estate-appraisers/appraisal-management-review-crossref` (47 vs 50), `real-estate-appraisers/appraisal-standards-qualification-bodies` (37 vs 39), `real-estate-appraisers/appraiser-licensing-boards` (27 vs 31), `real-estate-appraisers/property-condition-risk-data-crossref` (52 vs 54), `credit-unions/corporate-cu-investment-research` (37 vs 40). `mortgage-brokers/servicing-analytics-organizations` and `gse-selling-guide-content` name kill switches but read "below threshold"; the QC audit pocket passes the gate on review underwriters (production).
- 2026-10-22 (batch 5, money-service-businesses builder): indexed `customs-brokers/sanctions-screening-data-providers` (55) gives Q5 = 4 to a three-firm market (→51–53, still qualifies); `credit-unions/financial-crime-consortium-analytics` takes its clock from SAR deadlines that bind members, not the vendor. NAICS 522390 also covers loan servicing, which no queue row claims; crypto kiosks (FinCEN MSBs) are left to `crypto-exchanges`, whose hub doesn't mention them.
- 2026-10-22 (batch 5, pawnshops builder): `niches/independent-retailers/retail-crime-intelligence/profile.md` names a kill switch but reads "below threshold".
- 2026-10-22 (batch 5, mortgage-lenders): NAICS 522292 commercial and multifamily mortgage bankers (agency multifamily, CMBS conduits) are out of scope and covered by no industry.
- 2026-10-22 (batch 5, commodity-brokers builder): indexed `crop-farming/ag-market-intelligence-providers` (54) gives Q5 = 4 to a handful of providers (→50–52). Kill switches named with "below threshold" verdicts in `livestock-operations/cattle-risk-protection-underwriting`, `crop-farming/crop-insurance-actuarial-research`, `crop-farming/usda-agricultural-statistics`, `livestock-operations/usda-livestock-market-news`. Non-standard verdicts in `oil-gas-field-services/energy-price-reporting-crossref` and `livestock-operations/livestock-market-reporting-crossref`.
- 2026-10-22 (batch 5, trust-companies builder): kill switches named with "below threshold" verdicts in `estate-planning/corporate-trustee-fiduciary-teams` and `wealth-management-rias/custodian-platform-analytics` (overview tables say ⚠️ Kill switch). Indexed `accounting-firms-smb/business-valuation-practices` (54) says "Kill switches: none" though ESOP, estate and litigation valuations run on client financials, often through counsel (lesson k), and `estate-planning/fiduciary-litigation-support` carries that kill switch. `crypto-exchanges/custody-and-key-operations` puts an emoji in its Category line.
- 2026-10-22 (batch 5 review B): NAICS 523160 merges commodity dealing (old 523130: prop trading firms, energy trading desks, swap dealers) with brokerage; no queue row claims the dealing half. `oil-gas-field-services/midstream-flow-data-providers` (49) gives Q2 = 4 where lesson (i) suggests 3 (AIS commodity-flow sibling scores 3).
- 2026-10-22 (batch 6, pension-funds builder): kill switches named with "below threshold" verdicts in `municipal-services/public-pension-actuarial` (overview says ⚠️ Kill switch) and `private-equity-firms/lp-private-markets-consultants` (its overview row uses the non-standard verdict "Below threshold (confidentiality constraint)"). Boundary to check when built: public retirement systems report under public-administration codes, so the queued `benefits-administration-agencies` row (923130, 923140) may brush against public pension administration.
- 2026-10-22 (batch 6, self-insured-benefit-pools builder): kill switches named with "below threshold" verdicts (overview says ⚠️) in `insurance-tpa/self-insured-actuarial-consulting`, `insurance-tpa/claims-audit-firms`, `insurance-tpa/claims-platform-vendor-data`, `hr-consultants/benefits-brokerage-analytics`, `behavioral-health-clinics/parity-compliance-analysis`, `pharmacy-independents/pharmacy-benefit-consulting-audit`. `urgent-care/price-transparency-data-vendors` uses "regulatory dependency", not one of `_direction.md`'s three kill-switch types. Indexed `insurance-tpa/tpa-claims-analytics-organizations` (55) runs on client claim data under service agreements, a live kill switch under lessons (k)/(l). `insurance-tpa/municipal-benefits` and `self-insured-employers` give unmarked market sizes; insurance-tpa, municipal-services, hr-consultants and independent-insurance-agents Pass 2 tables use the non-standard verdict "✗ Fails gate". Labor unions (NAICS 813930) are named in prose only, pending their build.
- 2026-10-23 (batch 6, life-insurance-carriers builder): `independent-insurance-agents/insurance-regulatory-data-organization` names a kill switch ("regulator governance and procurement"; procurement isn't one) but reads "below threshold" while its overview says ⚠️. Indexed `funeral-homes/death-verification-data-providers` (54) says access to the "national death index" was narrowed (it was SSA's Death Master File; the NCHS NDI was always research-only), and its Q4 4 rests on "every day undetected", not a third-party deadline (lesson a). `financial-data-vendors/credit-rating-agency-analytics` says "the market is three firms", leaving out AM Best and KBRA. `pension-funds/prt-insurer-pricing-teams` names Life Insurance Carriers in prose only (wikilink at Stage E).
- 2026-10-23 (batch 6, health-insurance-carriers builder): `insurance-tpa/claims-fraud-analytics-vendors` reads "below threshold" while its overview says ⚠️, and its kill switch (unfair claims practice regulation) isn't one of `_direction.md`'s three types. Price transparency is profiled twice with conflicting verdicts: `medical-billing/price-transparency-data-vendors` (49, no kill switch) and `urgent-care/price-transparency-data-vendors` (49, ⚠️ "regulatory dependency"). Indexed `acupuncture-practices/conservative-care-guideline-publishers` (54, no kill switch) counts Carelon and EviCore policy units and claims authorization and appeal outcomes as its data (PHI), conflicting with `physical-therapy/pt-utilization-management-networks` (51, HIPAA kill switch). Non-standard kill-switch reasons beside HIPAA: `medical-billing/cms-program-integrity` ("federal procurement"), `medical-billing/payer-claims-adjudication` ("serves an insurance function"), `pharmacy-independents/pharmacy-quality-measurement` ("federal programme dependency").
- 2026-10-23 (batch 6, property-casualty-insurers builder): weather verification is profiled twice with different scores and no cross-link (`public-adjusters/weather-verification-data` 45, `insurance-restoration/weather-verification-data` 49). Kill switches named with "below threshold" verdicts (overview ⚠️) in `independent-insurance-agents/reinsurance-broking-analytics`, `premium-audit-services`, `surplus-lines-stamping-offices` ("government-adjacent procurement", lesson n) and `home-inspection/insurance-property-inspection-networks`. Kill switches outside the three types: `public-adjusters/state-insurance-regulators` ("government procurement"), `chiropractic-practices/insurance-fraud-investigation-bureaus` ("law enforcement sensitivity"), `mortgage-brokers/mortgage-insurance-underwriting` ("fair lending scrutiny"). `independent-insurance-agents/advisory-loss-cost-forms-bureaus` says "the licensed statistical agent" (singular), omitting AAIS and others.
- 2026-10-23 (batch 6 review A): indexed `public-adjusters/catastrophe-modelling-firms` (56) scores Q2 5 and Q5 4 for a 3–4-vendor model-licensing market; under lessons (h)/(i) it would be ~50 (still qualifies). State insurance departments are now profiled three ways (`public-adjusters/state-insurance-regulators` plus life and health slices); treat as one organisation family at Stage E. Price transparency's two existing copies are linked inconsistently by siblings; batch 6 links the medical-billing copy.
- 2026-10-23 (batch 6, title-insurance-carriers builder): `land-surveyors/title-underwriting-claims-research` names a kill switch ("prices an insurance product") outside `_direction.md`'s three types with a non-standard verdict; under batch 6 rules (risk-bearer Q1 2, Q5 2–3 for four families plus regionals, per-firm headcount) it would be ~43–45, no kill switch. `land-surveyors/title-plant-search-operations` and `small-law-firms/title-plant-search-crossref` profile one pocket with different positions and Q1/Q4/Q5 splits (both 55); the land-surveyors copy gives Q4 5 for contractual closing dates. `commercial-real-estate/property-condition-assessment-firms` gives Q4 5 for loan closing dates (~43 under lesson a). `title-and-settlement-offices` hub, overview and `underwriter-agency-audit-teams` still say title-insurance-carriers is "in the build queue" (wikilink at Stage E).
- 2026-10-23 (batch 6, reinsurers builder): `satellite-operators/space-insurance-underwriting`, `catastrophe-imagery-analytics` and `_overview.md` still call Reinsurers queued (wikilink at Stage E); `catastrophe-imagery-analytics` links Catastrophe Modelling Firms without the 🔍 emoji. Kill-switch rule for reinsurers on cedent data, to confirm at Stage E: pricing own risk from submissions = no kill switch (`self-insured-benefit-pools/public-entity-excess-underwriters`, carrier pricing units); productising cross-cedent data = kill switch (`life-insurance-carriers/life-reinsurer-underwriting-research`).
- 2026-10-23 (batch 6 review B): NAICS 524130 includes life and A&H reinsurers (RGA, the US life arms of Munich Re and SCOR); `reinsurers` covers P&C only, and life reinsurance has only two Pass 2 pockets under `life-insurance-carriers` (no Pass 1 coverage of YRT treaty pricing, facultative life or longevity reinsurance). `reinsurers/cat-bond-modelling-calculation-agents` (43) are the capital-markets teams of the firms in indexed `public-adjusters/catastrophe-modelling-firms` (56): one organisation family at Stage E. The state-insurance-regulators family now also includes `reinsurers/reinsurance-supervisors` (NAIC slice beside the BMA).
- 2026-10-23 (batch 7, facilities-management-firms builder): indexed `home-inspection/commercial-property-condition-assessment` (51) qualifies only on Q4 5 for loan closing dates (the client's deal schedule, lesson a); the same firms score 45 at `commercial-real-estate/property-condition-assessment-firms`. Procurement named as a kill switch (lesson n) in `municipal-services/infrastructure-asset-management-consulting` (verdict "below threshold"), `it-staffing-firms/dol-classification-enforcement` and `hvac-contractors/refrigerant-transition-compliance` (verdict below threshold, overview ⚠️). `hvac-contractors/field-service-platform-data-teams` names a kill switch but reads "below threshold" (overview ⚠️). NAICS 561210 also covers contract operation of jails and prisons (correctional officers are the code's second-largest occupation, 14,170): see the queued `correctional-facilities` row.
- 2026-10-23 (batch 7, executive-search-firms builder): `hr-consultants/executive-compensation-consultants` names a kill switch ("independence rules", not one of the three types) but reads "below threshold" (overview ⚠️). `staffing-agencies/_overview.md` uses the verdict "↔ Cross-referenced", and it and `hr-consultants/_overview.md` use "✗ Fails gate". `recruiting-tech-vendors` and `talent-assessment-platforms` have no Pass 2 sections. `corporate-training/talent-assessment-publishers/profile.md` lacks a blank line before `## Problems` (cosmetic).
- 2026-10-23 (batch 7, professional-employer-organizations builder): `insurance-tpa/state-workers-comp-boards` names "government procurement" as a kill switch (lesson n) and reads "below threshold" (overview ⚠️). Kill switches named with "below threshold" verdicts (overview ⚠️) in `staffing-agencies/worker-classification-advisory` and `hr-consultants/payroll-platform-research-institutes`. `hr-consultants/peo-compliance-research` (49) profiles the PEOs themselves, now this industry's operators (reconcile at Stage E), and scores Q4 5 partly on "payroll cycles", the firm's own schedule (47 at Q4 4). `hr-consultants/peo-alternative-consultants` build/fix notes carry unsourced figures ("20-30% more labor-intensive", "$5,000-20,000 per client").
- 2026-10-23 (batch 7, document-preparation-services builder): labour-market data vendors (Lightcast in both) are indexed at 54 in `corporate-training/labor-market-skills-data` but scored 49 in `it-staffing-firms/labor-market-analytics-providers`. Indexed `cloud-infrastructure-consultants/it-research-advisory-firms` (54) gives Q4 3 on self-set calendars (lesson a) and Q5 4 for ~four large firms (lesson h): ~50 or lower. Emoji in Category lines and unmarked sizes in `localization-services/post-editing-economics` and `digital-accessibility-firms/document-and-media-accessibility`.
- 2026-10-23 (batch 7, answering-services builder): field-service data pockets disagree on the kill switch: `hvac-contractors/field-service-platform-data-teams` names one but reads "below threshold", while `plumbing-contractors/field-service-software-analytics` says "Kill switches: none". `urgent-care/urgent-care-malpractice-underwriting` says "Kill switches: none listed, though claim files carry protected health information" (ambiguous; binary rule suggests live). `problems/funeral-homes/worker-life-2.md` states "40-50% of deaths occur between 6 PM and 6 AM" with no source.
- 2026-10-23 (batch 7, private-mail-centers builder): `last-mile-delivery/postal-regulatory-analysis` names kill switches ("federal procurement; sealed cost data") but reads "below threshold" (overview ⚠️); `direct-mail-agencies/usps-mail-acceptance-and-pricing` uses "federal procurement and regulator status" (lesson n). Pre-ruling scores: `last-mile-delivery/carrier-network-corporate-analytics` Q4 5 on peak season (lesson a) and Q5 3 for a handful of carriers (lesson h); `last-mile-delivery/address-verification-geocoding` Q2 4 and Q4 3 on real-time validation. Gate-failure profiles showing numeric scores beside "—/60": `pest-control/pest-franchise-system-analytics`, `last-mile-delivery/courier-business-brokerage`. last-mile and metal-fabrication overviews use legacy verdicts "↔ Cross-referenced" and "✗ Fails gate".
- 2026-10-23 (batch 7, credit-bureaus builder): `mortgage-brokers/_overview.md` row 17 says ⚠️ Kill switch but `mortgage-credit-reporting` reads "below threshold", and its switch ("consumer credit reporting regulation") isn't one of the three types. `collections-agencies/credit-scoring-model-developers` bases its kill switch on "model risk governance and fair lending supervision" (consistent basis: furnished data isn't theirs). Indexed `property-management/tenant-screening-data` (54, no kill switch) treats manager-contributed rental payment histories as proprietary, against the contributed-FCRA-data ruling (reconcile at Stage E). Background-screening "crossref" second profiles in staffing-agencies, it-staffing-firms, security-guard-firms, tutoring-centers and youth-sports-orgs conflict with the single-profile rule. Queue overlap: credit-bureaus' boundary includes employment-screening bureaus while investigation-and-screening-firms claims FCRA background screening (credit-bureaus left criminal background screening to it).
- 2026-10-23 (batch 7, repossession-services builder): `sales-finance-companies/repossession-and-remarketing` lists "Clearplan for assignment management" (RDN handles assignment; Clearplan is the agents' field app), and the sales-finance Pass 2 prose says LPR networks are "left to the queued Repossession Agencies industry" (now `repossession-services/lpr-location-data-networks`, 41; cross-link at Stage E). `collections-agencies/skip-tracing-operations` double-counts vendors ("LexisNexis, TLO, Accurint, TransUnion TLOxp": TLO = TLOxp, Accurint = LexisNexis). Vault notes quoting "~1.73M repossessions" (Cox) cite one of two widely different estimates (RDN-derived counts run ~2x higher).
- 2026-10-23 (batch 7, court-reporting-firms builder): `video-production-smb/legal-video-specialists` gives unmarked figures ($500M market, 4% share, 500–1,000 operators, $500–$2,000 per deposition). `industries/legal-support-services.md` (Analysis), `legal-support-services/legal-support-rollups` and `legal-support-services/_overview.md` still call Court Reporting Firms queued (wikilink at Stage E).
- 2026-10-23 (batch 7 review B): contributed-data kill-switch rule to settle at Stage E: live when data is furnished under FCRA furnishing or membership terms or held in trust for members (bureau prescreen, credit-scoring-model-developers, SBFE); not live when supplied on terms giving the vendor product rights. Indexed `property-management/tenant-screening-data` (54, manager-contributed payment histories) and `collections-agencies/identity-skip-trace-data-providers` (54, credit header under supply agreements) should be ruled on together under it.
- 2026-10-23 (batch 8, travel-agencies builder): `event-planning/corporate-meetings-agency-analytics` and `event-planning/smm-consultancies` name client-data kill switches but read "below threshold" (overview ⚠️). `event-planning/destination-marketing-research` uses "public procurement" as its kill switch (lesson n); `short-term-rentals/destination-tourism-research` uses "funding is largely public or lodging-tax derived" (not a valid type) and reads "below threshold" (overview ⚠️). `charter-bus-operators/multi-day-tour-operators` has unmarked figures ($1.2-1.8B, ~15-20%) and may mislabel Tourwriter and Rezdy as travel-agency platforms (unchecked). `hotels-boutique/hotel-performance-benchmarking` and `event-planning/meetings-intelligence-data` lack a blank line before `## Problems` (cosmetic).
- 2026-10-23 (batch 8, tour-operators builder): `hotels-boutique/pms-channel-manager-data-teams` names a kill switch but reads "below threshold" (overview ⚠️). `hotels-boutique/ota-partner-analytics` (47) scores Q4 5 on daily pricing (not a third-party deadline) and Q5 4 for a handful of OTAs (~37–41 under current lessons). `charter-bus-operators/group-travel-demand-research` (37) is sized at 5–20 people with a gate-failure-style verdict reason. `charter-bus-operators/motorcoach-association-research` shows numeric rows with "—/60"; the charter-bus overview uses "✗ Fails gate". Confirmed: `charter-bus-operators/multi-day-tour-operators` mislabels Rezdy (tour/activity booking, merged with Checkfront 2023) and Tourwriter (tour operators/DMCs) as travel-agency platforms.
- 2026-10-23 (batch 8, visitors-bureaus builder): `event-planning/destination-marketing-research` uses the position "Regulatory & enforcement bodies" (wrong for bureaus), and overlaps `short-term-rentals/destination-tourism-research` (both 34, blended population). `hotels-boutique/lodging-tax-authorities` lists "government procurement" beside taxpayer confidentiality and reads "below threshold" (overview ⚠️). `hotels-boutique/short-term-rental-market-data` uses "platform dependency" (not a valid type) with mismatched verdicts.
- 2026-10-23 (batch 8, ticketing-agencies builder): `investment-banking-boutiques/antitrust-economic-consulting` and `commodity-brokers/futures-manipulation-litigation-economists` profile the same firms (Compass Lexecon, Cornerstone, Analysis Group) as two pockets (both 46 KS; check for a double entry at Stage E). `payment-fraud-vendors`, `edge-cdn-providers` and `web-data-extraction-firms` overviews have no Pass 2 sections. Coverage gap closed here: Ticketmaster, Live Nation, StubHub and SeatGeek appeared nowhere in the vault before this build.
- 2026-10-23 (batch 8 review A): `short-term-rentals/destination-tourism-research` also sums headcount across organisations (beside its invalid public-funding kill switch). `hotels-boutique/ota-partner-analytics` (47) is the generous outlier against the marketplace data pockets scored 37–39 here.
- 2026-10-23 (batch 8, tour-operators fix round): `charter-bus-operators/motorcoach-insurance-underwriting` (34) may sum underwriters across firms (the per-firm rule failed the matching adventure-liability pocket).
- 2026-10-23 (batch 8, investigation-and-screening-firms builder): indexed `hr-consultants/background-screening-providers` (55) profiles this industry's own operators; its 300–2,000 headcount counts researchers and verifiers (production, lesson j), Q4 5 rests on clients' hiring turnaround (lesson a) and Q5 4 is high for a First Advantage–HireRight–Checkr market (~47–50 rescored); it still names Sterling as independent and lacks a blank line before `## Problems`. The five background-screening crossref copies disagree on position (it-staffing-firms "Suppliers", others "Data & benchmark vendors"). `childcare-centers/childcare-background-check-vendors` files private vendors under "Regulatory & enforcement bodies".
- 2026-10-23 (batch 8, armored-car-services builder): `community-banks/banking-agency-community-bank-research` counts "federal procurement" in its kill switch (lesson n; confidential supervisory information alone may carry it). `security-guard-firms/_overview.md` uses legacy verdicts "✗ Fails gate" and "↔ Cross-referenced".
- 2026-10-23 (batch 8, security-alarm-integrators builder): procurement kill switches (lesson n) in `security-guard-firms/state-security-licensing-boards` and `electrical-contractors/electrical-inspection-agencies` (verdict "below threshold", overview ⚠️). `security-guard-firms/video-analytics-vendors` names a kill switch but reads "below threshold" (overview ⚠️). `security-guard-firms/alarm-monitoring-analytics` sums headcount across central stations (lesson b), takes Q4 from seconds-level response (lesson a) and is positioned "Suppliers" though central stations are now this industry's operators. `security-guard-firms/security-rollup-corporate-analytics` (41) and `electrical-contractors/electrical-distributor-analytics` (43) look high under lessons (a), (b), (h). `electrical-contractors/_overview.md` uses "✗ Fails gate"; `electrical-contractors/code-standards-development-bodies` lacks a blank line before `## Problems`. `answering-services/_overview.md` (batch 7, committed) names this industry in prose (wikilink at Stage E).
- 2026-10-23 (batch 8, locksmiths builder): indexed `towing-companies/roadside-assistance-network-analytics` (50) sums headcount across networks (lesson b), takes Q4 4 from client SLA minutes (lesson a) and Q5 4 for a handful of networks (lesson h); likely below 50 rescored. `towing-companies/_overview.md` uses legacy verdicts. `pest-control/pest-lead-generation-marketplaces` (38) sums headcount across platforms; `moving-companies/moving-lead-generation-platforms` (43) takes Q4 4 from customers' move dates. `marketing-agencies-smb/local-listings-reputation-data` uses "publisher API dependency" (not a valid type) with a "below threshold" verdict. `security-guard-firms/state-security-licensing-boards` omits locksmith licensing (CA BSIS, Texas DPS).
- 2026-10-23 (batch 8 review B): `security-guard-firms/alarm-monitoring-analytics` (41) is misfiled (central stations belong in 561621, now `security-alarm-integrators`) and passes the gate only by counting 200–1,000 operations and quality staff (production). `security-guard-firms/state-security-licensing-boards` passes the gate only by counting licensing staff; BSIS and Texas PSP also license PIs, alarm firms, locksmiths and repossessors (one organisation family across five industries). `expert-networks/commercial-due-diligence-advisors` (50 KS) scores Q4 5 on bid dates, a client clock (~46 under lesson a).
- 2026-10-23 (batch 9, contract-packagers builder): kill switches named with "below threshold" verdicts (overview ⚠️) in `printing-shops/packaging-testing-labs`, `food-manufacturing/packaging-testing-migration-labs` and `cold-chain-logistics/thermal-packaging-qualification-labs`; the same testing-lab family is profiled three times with different positions (reconcile at Stage E). `independent-retailers/weights-measures-consumer-protection` uses "government procurement" as its kill switch (lesson n), reads "below threshold" (overview ⚠️), and its overview title differs from the profile's. `contract-manufacturing/cm-quoting-cost-engineering` scores Q4 4 on clients' RFQ deadlines (lesson a). printing-shops and food-manufacturing overviews use legacy verdicts.
- 2026-10-23 (batch 9, auctioneers builder): the Copart/IAA salvage duopoly is scored 17 points apart: `towing-companies/salvage-auction-data` 47 (Q1 4, Q5 3) vs `property-casualty-insurers/salvage-auction-platforms` 30 (Q1 2, Q5 1). `real-estate-appraisers/appraiser-licensing-boards` (31) lists "government procurement" as a live kill switch (lesson n).
- 2026-10-23 (batch 9 review A part 1): older appraisal-shaped pockets scored under looser rules: indexed `private-equity-firms/portfolio-valuation-advisory` (55, no kill switch on Lincoln's published index) and indexed `commercial-real-estate/commercial-appraisal-firms` (53; passes the gate on per-job appraisers and takes Q4 5 on loan closings) would likely be re-gated or rescored under the batch 6–9 rules.
