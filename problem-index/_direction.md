# Direction — Insight-Layer Discovery (Pass 2)

Single source of truth for this workstream. A fresh session should be able to read only this file and continue correctly.

**To launch a run:** tell a fresh agent `Read _run.md and execute it.` — `_run.md` is the standing operating order and takes its scope from the CURSOR below.

---

## CURSOR

**Status:** complete
**Batch size:** 5 industries
**Scope:** 118 industries

| | |
|---|---|
| **Completed** | 118 of 118 — `accounting-firms-smb` (15), `acupuncture-practices` (13), `alterations-tailoring` (13), `auto-body-shops` (13), `auto-dealers-independent` (13), `auto-repair-shops` (13), `behavioral-health-clinics` (13), `catering-companies` (13), `charter-bus-operators` (13), `childcare-centers` (13), `chiropractic-practices` (13), `cleaning-companies` (13), `cloud-infrastructure-consultants` (13), `coffee-shops-independent` (13), `cold-chain-logistics` (13), `collections-agencies` (13), `commercial-real-estate` (13), `compliance-consulting` (13), `contract-manufacturing` (13), `corporate-training` (13), `credit-unions` (13), `crop-farming` (13), `customs-brokers` (13), `cybersecurity-mssp` (13), `data-analytics-consultants` (13), `dental-practices` (13), `ecommerce-sellers` (13), `electrical-contractors` (13), `electronics-contract-mfg` (13), `energy-auditors` (13), `engineering-consultants` (13), `environmental-consultants` (13), `estate-planning` (13), `event-planning` (13), `faith-organizations` (13), `fleet-managers` (13), `food-distributors` (13), `food-manufacturing` (13), `food-trucks` (13), `freight-brokerage` (13), `funeral-homes` (13), `general-contractors` (13), `grant-writers` (13), `greenhouse-horticulture` (13), `gyms-independent` (13), `hair-salons-independent` (13), `hoa-management` (13), `home-health-agencies` (13), `home-inspection` (13), `hotels-boutique` (13), `hr-consultants` (13), `hvac-contractors` (13), `immigration-law` (13), `independent-insurance-agents` (13), `independent-publishers` (13), `independent-restaurants` (13), `independent-retailers` (13), `insurance-restoration` (13), `insurance-tpa` (13), `it-managed-services` (13), `it-staffing-firms` (13), `k12-private-schools` (13), `land-surveyors` (13), `landscaping` (13), `language-schools` (13), `last-mile-delivery` (13), `livestock-operations` (13), `marketing-agencies-smb` (13), `med-spas` (13), `medical-billing` (13), `medical-device-mfg` (13), `medical-supply-retail` (13), `metal-fabrication` (13), `mortgage-brokers` (13), `moving-companies` (13), `municipal-services` (13), `news-media-local` (13), `non-emergency-medical-transport` (13), `nonprofits-social-services` (13), `oil-gas-field-services` (13), `owner-operator-trucking` (13), `painting-contractors` (13), `personal-injury-law` (13), `personal-trainers` (13), `pest-control` (13), `pet-services` (13), `pharmacy-independents` (13), `physical-therapy` (13), `plumbing-contractors` (13), `podcasting-networks` (13), `printing-shops` (13), `property-management` (13), `public-adjusters` (13), `public-defenders` (13), `real-estate-appraisers` (13), `restaurant-suppliers` (13), `roofing-contractors` (13), `rv-dealerships` (13), `security-guard-firms` (13), `short-term-rentals` (13), `small-law-firms` (13), `software-dev-agencies` (13), `solar-installers` (13), `specialty-food-retail` (13), `staffing-agencies` (14), `tattoo-studios` (12), `tax-prep-firms` (13), `towing-companies` (12), `trade-associations` (13), `tutoring-centers` (12), `urgent-care` (13), `utility-contractors` (13), `veterinary-practices` (12), `video-production-smb` (12), `vocational-schools` (12), `warehouse-3pl` (13), `wealth-management-rias` (13), `youth-sports-orgs` (12) |
| **Current batch (24)** | warehouse-3pl ✅ · wealth-management-rias ✅ · youth-sports-orgs ✅ |
| **Next batch (25)** | — |
| **Order** | Alphabetical by `ls industries/`, so position is always recoverable |
| **Index entries so far** | See `_scorecard-index.md` |

**To resume:** read this file → read `_scorecard-index.md` → run the verification block at the bottom → continue at the next uncompleted industry in the current batch.

---

## 1. What we are selling

An engine that manages a business's internal data, research, and insights process. Already built and deployed for other verticals. We are scouting the next vertical to sell into.

**These prior deployments carry zero scoring weight.** They are references for credibility, not a pattern to match. The engine is domain-agnostic; treating prior verticals as an adjacency signal produces overfitted results. Do not reintroduce adjacency as a criterion.

## 2. What we are looking for

An organization where:
> a dedicated research/insight function of **10+ people** produces an analytical artifact that is **the billable deliverable**, built on a **proprietary corpus the firm owns**, delivered against a **deadline set by a third party**, with a **named buyer** who owns the budget.

Ticket size is not a filter. Do not screen on ACV.

## 3. The gate (apply FIRST, before scoring)

**Does this pocket plausibly contain a dedicated research/insight function of 10+ people?**

If no, the pocket is still written into the vault with a plain profile and a `Verdict: Logged — fails gate`, but it is **not** scored and **not** entered in the index. This gate is what keeps the work honest — it eliminates most of the operator layer, and that is the correct result, not a problem to engineer around.

## 4. The rubric (survivors only)

| # | Question | Weight |
|---|---|---|
| Q1 | **Is the insight the invoice?** Does the buyer's own client pay for, or decide to hire them because of, the research output itself? | ×3 |
| Q2 | **Does output scale only by adding people — doing repeatable-shaped work?** Revenue-linear labor, same-shaped deliverable at volume, not bespoke one-offs. | ×2 |
| Q3 | **Do they own data nobody else has, and under-use it?** A proprietary corpus that lets them produce what a competitor structurally cannot. | ×3 |
| Q4 | **Does a clock set by someone else govern the work?** Filing, permit, audit, court, pitch, or regulatory deadlines where late costs money. | ×2 |
| Q5 | **One accountable buyer, and many more behind them?** Named exec with budget, plus a fragmented market so one reference unlocks the next. | ×2 |

Score each 0–5. **Max 60.**

Q1 outranks Q2 deliberately. A big team alone is a cost-savings sale, capped in price and killed in procurement. Insight-as-revenue is what makes it premium-priced.

### Kill switches — binary, scored separately, never averaged in

- **Compliance gates severe enough to stall procurement** — MNPI, attorney–client privilege, HIPAA, ITAR, FDA computer-system validation.
- **Data isn't theirs to use** — research performed on client-owned data with reuse restrictions.
- **Entrenched incumbent owns the workflow** and the data sits locked in their schema.

A pocket with a live kill switch is written into the vault and flagged, but does not enter the index regardless of score.

### Index threshold

Enter in `_scorecard-index.md` only if **score ≥ 50/60 AND no live kill switch**. Everything else lives in the vault only. The index is for findings worth sharing.

## 5. The discovery method — seven-position value-chain sweep

Pass 1 swept *across* the operator layer of each industry and found firms of 1–15 people. Research functions do not exist at that altitude. Pass 2 sweeps the positions **above and beside** the operators. For each industry, ask what sits at each position:

1. **Aggregator / rollup platforms** — PE platforms, MSOs, franchisors, buying groups. Corp dev and integration analytics teams.
2. **Payer & intermediary layer** — insurers, TPAs, lenders, underwriters who must research the industry to price risk.
3. **Data & benchmark vendors** — firms whose product *is* data about this industry.
4. **Association research arms** — benchmark and standards production.
5. **Specialist advisory & valuation firms** — consultancies, study firms, expert witnesses, valuation shops serving the industry.
6. **Regulatory & enforcement bodies** — where applicable.
7. **Suppliers selling into the industry** — vendors running market research, competitive intelligence, and technical content operations.

Target **at least 10 pockets per industry.** Go granular — small, specific sub-pockets are wanted. Log every pocket found, including ones that fail the gate; the negative results are part of the map.

---

## 6. How to write

### Vault safety — non-negotiable

- **Additive only.** Never edit, move, or delete any Pass 1 niche, any file under `problems/`, or any `industries/*.md`. Pass 1's 944 niches are untouchable.
- **Never rewrite the Pass 1 half of an `_overview.md`.** Append a `## Pass 2 — Insight-Layer Discovery` section below a `---` rule.
- **Tags: canonical registry only** (`metadata/tags.md`). If a concept isn't listed, it gets no tag. Never reintroduce a deprecated tag.
- Run the verification block after every industry.

### File layout

```
niches/<industry>/<pocket-slug>/profile.md      ← ALWAYS
niches/<industry>/<pocket-slug>/build.md        ← only if score >= 50
niches/<industry>/<pocket-slug>/buy.md          ← only if score >= 50
niches/<industry>/<pocket-slug>/fix.md          ← only if score >= 50
```

**Documented invariant change:** Pass 1 niches always have exactly 4 files. Pass 2 niches have **1 file (profile only) or 4 files**. This is intentional — writing three speculative opportunity notes for a pocket scoring 22/60 is waste. Verification must allow 1-or-4 for `Insight Layer` niches. Do not "fix" this.

### profile.md — write plainly

Plain and compact. State what the pocket does and who pays for it. No essays; the analytical payload is the scorecard.

```markdown
# <Pocket Name>

**Parent Industry:** [[industries/<slug>|<Industry Name>]]
**Category:** Insight Layer
**Value-Chain Position:** <one of the seven>

## What They Do
<2-4 plain sentences. Who they are, what they produce, who pays for it.>

## Insight Function
**Size:** <headcount range of the research/insight function>
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

**Kill switches:** <none — or name it>
**Verdict:** <Qualified — indexed | Logged — below threshold | Logged — fails gate | Logged — kill switch>

## Problems
<only if 4-file: the three links. Otherwise omit this section.>
```

### build.md / buy.md / fix.md — only for qualifiers

Match Pass 1 exactly. Required headings, in order:

- **build.md** — `Type: Build (Greenfield Opportunity)` — The Problem · Why Nobody Has Built This · What to Build · Target Customer · Impact If Built
- **buy.md** — `Type: Buy & Customize (Vertical Adaptation)` — The Problem · What Already Exists · The Customization Gap · Target Customer · Impact If Solved
- **fix.md** — `Type: Fix (Pain Point)` — The Problem · Why It's Still Broken · What a Fix Looks Like · Who Feels the Pain · Impact If Fixed

Each carries `**Niche:**`, `**Industry:**`, `**Type:**`, `**One-liner:**`, `**Tags:**` under the H1. `profile.md` carries **no** Tags line.

### Wikilink conventions (match the source directory)

- From `niches/**` → `[[industries/<slug>|Name]]` and `[[niches/<industry>/<pocket>/profile|🔍 Name]]`
- Pass 2 emoji is **🔍** (joins 🔵 High Market Share · 🟠 Low Digitized · 🟣 Underserved · ⚡ Highly Automatable)

### Per-industry checklist

1. Sweep all seven positions; find ≥10 pockets.
2. Write a plain `profile.md` for every pocket, gate-first then scored.
3. Write `build/buy/fix` only for pockets scoring ≥50 with no kill switch.
4. Append the `## Pass 2` section to that industry's `_overview.md` — table of all pockets, a Why These Pockets paragraph, and the 🔍 niche list.
5. Add qualifying pockets to `_scorecard-index.md`.
6. Update this file's CURSOR block.
7. Run verification.

---

## 7. Verification block — run after every industry

```bash
cd /Users/mac/Desktop/code/personal/problem-index

# Pass 1 niches must still have exactly 4 files (must print nothing)
find niches -mindepth 2 -maxdepth 2 -type d | while read d; do
  grep -q '^\*\*Category:\*\* Insight Layer' "$d/profile.md" 2>/dev/null && continue
  echo "$(ls $d | wc -l) $d"
done | grep -v '^ *4 '

# Pass 2 niches must have 1 or 4 files (must print nothing)
grep -rl '^\*\*Category:\*\* Insight Layer' niches --include='profile.md' | xargs -n1 dirname | while read d; do
  n=$(ls $d | wc -l); [ "$n" -eq 1 ] || [ "$n" -eq 4 ] || echo "BAD($n) $d"
done

# No non-canonical tags (must print nothing but the known false positive)
grep -rhoE '(^|\s)#[a-z][a-z0-9-]{2,}' niches problems --include='*.md' | tr -d ' ' | sort -u > /tmp/used.txt
grep -o '^#[a-z0-9-]\+' metadata/tags.md | sort -u > /tmp/canon.txt
comm -23 /tmp/used.txt /tmp/canon.txt | grep -v foodtruckfriday

# Pass 1 integrity — 118 industries, 944 Pass 1 niches, parity intact
echo "industries: $(ls industries/*.md | wc -l) (expect 118)"
echo "pass1 niches: $(grep -rL '^\*\*Category:\*\* Insight Layer' niches --include='profile.md' | wc -l) (expect 944)"
comm -3 <(ls industries | sed 's/\.md$//' | sort) <(ls problems | sort)

# All wikilinks in Pass 2 overview sections resolve
grep -rho '\[\[niches/[^|\]*' niches/*/_overview.md _scorecard-index.md 2>/dev/null \
  | sed 's/\[\[//; s/\\$//' | sort -u | while read -r l; do
  [ -f "$l.md" ] || echo "BROKEN: $l"
done
```

## 8. Files this workstream owns

| File | Purpose |
|---|---|
| `_direction.md` | this file — direction + cursor |
| `_scorecard-index.md` | qualifying findings only (≥50, no kill switch) |
| `niches/_bookmark.md` → Pass 2 section | per-industry completion log |
| `niches/<industry>/<pocket>/` | the pockets themselves |
| `niches/<industry>/_overview.md` → Pass 2 section | per-industry pocket table |
