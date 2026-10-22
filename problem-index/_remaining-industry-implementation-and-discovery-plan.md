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

**Stage:** batch loop. Batches 1–3 closed 2026-10-22; batch 4 building.
**Triage:** 714 of 714 codes (new 421 · merge 265 · covered 17 · skip 11)
**Queue:** 421 industries in 49 batches
**Done:** 27 industries · 1,790 files (1,736 vault + 54 state) · 4 qualifiers
**Last verifier run:** `verify.sh` (all done rows) → REST-VERIFY-CLEAN; `check_queue.py` → QUEUE-CLEAN; lenses rebuilt via `_state/rest/lens_rebuild.sh` (2026-10-22)
**Next action:** finish batch 4 (Information: broadcast, wired, wireless, resellers, retail agents, satellite, libraries), review, close; then batch 5 (Finance)
**Run constraint (owner, 2026-10-22):** at most **3 subagents in parallel**, builders and reviewers combined. §5 step 2's "up to 10 at once" is overridden. Builders must not spawn forks or subagents (the brief says so).
**Coordinator tooling (2026-10-22):** `_state/rest/brief.py <slug>` prints the §7 brief with built siblings and review lessons; `set_status.py`; `resort_p2.py <slug>` re-sorts a Pass 2 table after a fix; `lens_rebuild.sh` runs §5.3 while later batches are mid-build (it leaves non-`done` slugs out); `build_scorecard.py` writes `_scorecard-index-rest.md` from `qualifiers.jsonl` and checks each profile still says Qualified at the same total. Builder reports, review checklists and pending findings live in `_state/rest/reports/`.

**Stage 0 notes.** Every decision and boundary sentence lives in `_state/rest/stage0_triage.py`, which writes both TSVs; don't re-run it once any row is past `todo`, because it resets statuses. The count (421) sits above the plan's 300–400 guess because services stayed close to one industry per code, as §0.2 expects; manufacturing came to 272 + 5 cross-sector codes in 119 industries (~2.3 per industry) and wholesale to 59 codes in 31. Covered: 17 codes folded into existing hubs (e.g. 541214 → `payroll-platforms`, 813920 → `trade-associations`). Skipped: 11 single-operator or shell codes (Federal Reserve, USPS, NASA, DoD, State, holding companies, household employers, video rental). Category: 8132–8139 nonprofits (foundations, advocacy, civic clubs, unions, political) use `Nonprofit & Government` instead of the table's `Specialty Services`, and the 52xxx insurance carriers and benefit pools use `Insurance`. Residual "all other" codes were built around their largest firm type; the `reason` column says which (e.g. 238990 → asphalt paving; fence and pool builders also sit there).

| Batch | Sector | Industries | Done | Files | Qualifiers | Pattern |
|---|---|---|---|---|---|---|
| 1 | 54 Professional Services | 10 | 10 | 667 | 1 | Design and technical services. Every operator fails the gate: they sell design or production, not research. Builders put four pockets beside the operators at 51–52, and review cut three: a client's permit schedule isn't a third-party clock, five-firm markets earn Q5 2–3, and licensing an owned library doesn't grow with headcount. One survived: product-regulation intelligence (51), harmonised with the indexed regulatory-content pockets. |
| 2 | 54 Professional Services | 10 | 10 | 659 | 1 | Media, marketing services and legal-adjacent work. Four first-pass qualifiers became one: pipeline intelligence and PR measurement fell to 49 on Q5 (three- to four-vendor markets), and invalidity search houses took the work-product kill switch, the vault's majority rule for litigation support. The survivor is IND regulatory strategy (50), at the threshold. Sibling duplicates (CertifID, imaging research, ELN) were collapsed into one profile each. |
| 3 | 51 Information | 7 | 7 | 464 | 2 | Film, music and media production. Builders scored no qualifiers; reviewers found two missed ones by holding siblings to the same rubric. Collecting societies (51) were rescored against the indexed permissions agencies, and the sound-recording societies (51) against them, both on the global society field (45 and 40 on US-only scoring). Most other pockets failed the gate once headcount was counted per firm rather than summed. |
| 4 | 51 Information | 7 | 0 | — | — | — |
| 5 | 52 Finance & Insurance | 8 | 0 | — | — | — |
| 6 | 52 Finance & Insurance | 7 | 0 | — | — | — |
| 7 | 56 Admin, Support & Waste | 9 | 0 | — | — | — |
| 8 | 56 Admin, Support & Waste | 8 | 0 | — | — | — |
| 9 | 56 Admin, Support & Waste | 8 | 0 | — | — | — |
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
