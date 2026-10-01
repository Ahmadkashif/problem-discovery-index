# Content Topics — Workflow Automation for Finance Research Teams

**For:** a personal-brand content strategy commercially aligned with a company selling workflow automation to research teams in finance.
**Audience:** people on finance research teams (buy-side analysts, sell-side associates, PE and IB deal teams, data and research ops, research compliance) who want to automate their own research workflows.
**Built from:** the Phase 4 vault layer (7 new industries, 503 files, branch `phase4/capital-markets-research`) plus the existing 250-industry vault, which supplies the cross-industry angles.
**Date:** 2026-10-02

---

## Is the gap closed?

Yes, for this purpose. Coverage of core finance research terms before and after Phase 4:

| Term | Before | After |
|---|---|---|
| FactSet | 0 | 39 files |
| Expert network(s) | 0 | 72 |
| Earnings call | 0 | 10 |
| PitchBook / Capital IQ | 2 / 2 | 28 / 29 |
| MNPI | — | 41 |
| Research-team pockets (Insight Layer) in finance's core | 0 | 107 |

What is still thin: earnings-call *mechanics* (10 files) and channel checks (4). Neither blocks a topic.

## The positioning line

> **Finance research teams make thousands of dated, checkable judgements a year — and almost none of them are ever graded, kept, or reused.**

Every Phase 4 industry produced the same finding independently, so the line comes from the evidence rather than being imposed on it (`problem-index/_scorecard-index-phase4.md` § The pattern). It is also the commercial bridge: automating the **capture** of research work is what makes the research **reusable**, and that applies to any research team, not just a hedge fund.

---

## Pillar 1 — The judgement that walks out the door

*Tacit knowledge in finance research: what experienced analysts know, why it's never recorded, and what a lightweight capture workflow looks like.*

| # | Topic / hook | The workflow | Vault source | Cross-industry angle |
|---|---|---|---|---|
| 1.1 | **"Your fund marks every position daily. It has never marked a single thesis."** | Drafting a three-field thesis (view, catalyst, falsifier) from the analyst's own notes, confirmed in under a minute | `problems/hedge-funds/high-impact.md` | Neobanks freeze accounts by model and never grade the decision: `problems/neobanks/high-impact.md` |
| 1.2 | **"The coverage franchise lives in one analyst's head"** | Handover packs built from a departing analyst's notes, models and call history | `problems/sell-side-equity-research/high-impact.md` | `problems/asset-managers/high-impact.md` (same pattern, buy side) |
| 1.3 | **"The pass decision nobody grades"** | Logging *why* a deal was declined as a voice note or email reply, then checking it against what happened to the company | `problems/private-equity-firms/high-impact.md` | `niches/data-marketplace-brokers/the-sourcing-analyst/fix.md`: rejected vendors get re-evaluated 18 months later |
| 1.4 | **"The buyer list built from memory"** | Ten years of NDA → IOI → LOI trackers dying in per-deal Excel files | `problems/investment-banking-boutiques/high-impact.md` | — |
| 1.5 | **"Every number in your terminal hides a judgement call"** | Collection analysts' mapping decisions kept as numbers, not decisions | `problems/financial-data-vendors/high-impact.md` | Collision estimating data and vehicle valuation guides (top of `_scorecard-index.md`) |

## Pillar 2 — The answer key arrives for free

*Research outputs that later get graded in public, and the teams that never check. This is the most original pillar: no one else can make this argument across seven sub-industries.*

| # | Topic / hook | Vault source |
|---|---|---|
| 2.1 | **"Alt-data vendors are graded every earnings day — and don't keep score"** | `niches/hedge-funds/alt-data-kpi-research-providers/` (56/60) |
| 2.2 | **"Thousands of covenant calls, zero track record"** | `niches/hedge-funds/credit-intelligence-services/`, `niches/investment-banking-boutiques/distressed-credit-intelligence/` |
| 2.3 | **"Every quarter's valuation mark has an exam it never sits"** (marks vs exit prices) | `niches/private-equity-firms/portfolio-valuation-advisory/` (55/60) |
| 2.4 | **"Expert calls are full of predictions. Nobody checks them."** | `niches/expert-networks/transcript-library-platforms/build.md` |
| 2.5 | **"Consensus is an average of people with very different track records"** | `niches/sell-side-equity-research/estimates-consensus-data/` |
| 2.6 | **"Which QoE adjustments survive diligence? Nobody has counted."** | `niches/investment-banking-boutiques/quality-of-earnings-providers/` |

**Cross-industry post:** "The same blind spot in fund ratings, ESG scores and credit models": `niches/wealth-management-rias/investment-research-fund-data/`, `niches/asset-managers/esg-ratings-providers/`, `niches/credit-unions/model-validation-firms/`.

## Pillar 3 — Earnings night and other deadlines you don't set

*Mechanical, clock-bound research work. These are the most immediately relatable posts and the easiest wins to automate.*

| # | Topic / hook | Vault source |
|---|---|---|
| 3.1 | **"The associate on earnings night"**: spreading the print into *your* model, not the vendor's template | `problems/sell-side-equity-research/worker-life-1.md`, `low-impact-2.md` |
| 3.2 | **"The pod analyst through earnings season"** | `problems/hedge-funds/worker-life-1.md`, `niches/hedge-funds/earnings-model-maintenance/build.md` |
| 3.3 | **"The collection analyst at 2 a.m."**: the human behind the number on your terminal | `problems/financial-data-vendors/worker-life-1.md` |
| 3.4 | **"Ticking and tying at midnight"**: checking every number in a deck by hand as a risk-control problem, not an hours problem | `problems/investment-banking-boutiques/worker-life-2.md` |
| 3.5 | **"Rebuilding the model at midnight"** | `problems/private-equity-firms/worker-life-1.md` |
| 3.6 | **"Writing for other people's deadlines"**: RFPs, due diligence questionnaires (DDQs), consultant databases and quarter-end commentary | `problems/asset-managers/low-impact-1.md`, `worker-life-1.md` |

**Cross-industry angle:** the vault's Pass 2 rubric scores every research team on its **external clock** (Q4). A post on *"automate first where the deadline isn't yours"* can use examples from R&D tax credit studies and tax research publishers (both 58/60 in `_scorecard-index.md`).

## Pillar 4 — Synthesis is the step nobody tools

| # | Topic / hook | Vault source |
|---|---|---|
| 4.1 | **"Thirty expert calls and no synthesis"**: the memo loses the count, the source mix and the dissent | `problems/expert-networks/worker-life-2.md`, `niches/expert-networks/cross-call-synthesis/fix.md` |
| 4.2 | **"Six diligence reports and no shared record of findings"** | `niches/private-equity-firms/transaction-diligence/build.md` |
| 4.3 | **"IC memo assembly from the data room"** | `problems/private-equity-firms/low-impact-1.md` |
| 4.4 | **"AI summaries speed up consensus"**: everyone gets the same transcript summary at the same minute, and the edge comes from comparing it with *your own* prior expectations | `niches/asset-managers/fundamental-equity-research/fix.md` |
| 4.5 | **"Why per-call AI summaries invent numbers"** | `niches/expert-networks/cross-call-synthesis/fix.md` |

## Pillar 5 — Compliance as a research bottleneck

| # | Topic / hook | Vault source |
|---|---|---|
| 5.1 | **"MNPI clearance is the real speed limit on research"** | `problems/hedge-funds/low-impact-2.md`, `niches/hedge-funds/research-compliance-mnpi/build.md` |
| 5.2 | **"Pre-publication review is a bounded reading task, and you already have the training data"** (drafts vs finals) | `problems/sell-side-equity-research/low-impact-1.md` |
| 5.3 | **"Screening expert calls by attestation and sample"** | `problems/expert-networks/low-impact-1.md` |

## Pillar 6 — Your research inputs are wrong in ways you can't see

*Data quality told as a research-workflow story. This is the cross-industry pillar with the most reach outside finance.*

| # | Topic / hook | Vault source |
|---|---|---|
| 6.1 | **"Why your number differs from Capital IQ's"** | `problems/financial-data-vendors/worker-life-2.md` |
| 6.2 | **"Alt-data trials are a race against the trial clock"** | `problems/hedge-funds/low-impact-1.md`, `niches/hedge-funds/alt-data-evaluation/build.md` |
| 6.3 | **"Right shape, wrong value"**: scrapers that keep working after they break | `niches/web-data-extraction-firms/extraction-correctness/` |
| 6.4 | **"Accuracy measured by the team being measured"** | `niches/financial-data-vendors/content-operations-research/fix.md` |
| 6.5 | **"Your research system is a spreadsheet, and that's not stupid"** | `series/eras/wave-03-pc-spreadsheet.md`, `series/failures/reinhart-rogoff.md`, `jpmorgan-london-whale.md` |

---

## Suggested sequencing

1. **Open with Pillar 2** (the answer key arrives for free). It is the most distinctive argument and sets up everything else.
2. **Alternate Pillar 1 and Pillar 3.** Pillar 1 is the big idea and Pillar 3 is the relatable daily pain, so they keep both strategists and practitioners engaged.
3. **Use Pillars 4–6 to show breadth**, including the cross-industry posts that open doors to research teams outside finance.

Each pillar can carry a recurring format, e.g. a weekly *"Nobody grades this"* post (Pillar 2) and a monthly *"The 2 a.m. job"* worker profile (Pillar 3).

## Before publishing — must-check list

- **Market sizes, niche shares and headcounts in the vault are estimates.** Don't quote them as facts.
- **Unverified claims the builders flagged.** Check these before quoting:
  - deal dates: AlphaSense/Tegus, S&P/Visible Alpha, BlackRock/Preqin, MSCI/Burgiss
  - the FCA August 2024 research-payment rule
  - EU ESG Ratings Regulation dates
  - FINRA 5150 and the M&A broker exemption
  - Hindenburg's wind-down
  - the App Annie SEC action
  - the 2010–13 expert-network prosecutions
  - the Capvision raid
- **Figures that were web-checked**, still worth citing to the original source:
  - Lincoln's 7,000+ quarterly marks
  - HFR ~$5.15T industry capital (end-2025)
  - Neudata ~$2.8B alt-data spend (2025)
  - Burton-Taylor ~$44.3B market-data spend (2024)
  - Dealogic ~$6.0B independent-adviser fees (1H 2026)
- **The six scoring overlaps** in `_scorecard-index-phase4.md` don't affect topics, but don't cite a single score for those pockets.
