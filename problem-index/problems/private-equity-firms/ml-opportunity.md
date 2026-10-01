# Machine Learning Opportunities — Private Equity Firms

**Industry:** [[private-equity-firms|Private Equity Firms]]
**Derived from:** [[problems/private-equity-firms/high-impact|High Impact]], [[problems/private-equity-firms/low-impact-1|Low Impact 1]], [[problems/private-equity-firms/low-impact-2|Low Impact 2]], [[problems/private-equity-firms/worker-life-1|Worker Life 1]], [[problems/private-equity-firms/worker-life-2|Worker Life 2]]

---

## 1. Partner Screening Judgement Capture and Pass Grading
#tacit-knowledge-ml #large-language-models #gradient-boosting #survival-analysis #k-nearest-neighbors #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Senior partners decide which of several hundred inbound opportunities a year deserve work, from a first read of a teaser or CIM, using pattern recognition they cannot articulate. The firm records the decision as a dropdown and never compares it with what later happened to the companies it declined. The ML problem is twofold: reproduce the partner's screening call well enough to triage and explain new opportunities, and grade past passes against subsequently observed outcomes.

**ML task:** Binary classification (pursue vs pass) on first-read features plus LLM-derived document features; nearest-neighbour retrieval over prior opportunities; survival analysis of passed-company outcomes with right censoring
**Input data:** CRM opportunity records (source, banker, dates, deal team, stage reached, pass reason); structured facts extracted from CIMs and teasers at first read (revenue, EBITDA, growth, margin trajectory, customer concentration, end market, ownership, geography); the partner's free-text or voice-note reason; subsequent transaction, financing and distress events for the same company from PitchBook or Capital IQ via entity resolution.
**Target:** P(firm pursues past first screen); ranked similar prior opportunities with their decisions and outcomes; for passed companies, time-to-event for subsequent sale and, where disclosed, the realised multiple at that sale.
**Evaluation metric:** For screening reproduction, recall on the opportunities the firm actually pursued at a fixed review budget (the cost of a missed good deal far exceeds an extra hour of associate reading), plus agreement with partners measured against inter-partner agreement as the ceiling — a model that agrees with Partner A as often as Partner B does is at human level. For pass grading, report concordance and calibrated interval estimates by sector and deal source, never point estimates on small cells.
**Scope:** The data collection is the hard part and must come first. *Capturing the expert:* partners will not fill in forms, so reasons must be captured as a reply-to-email or a thirty-second voice note at the moment of decision, and structured facts must be extracted automatically from the document before it is deleted under NDA. *Labelling:* partners disagree with each other and with their past selves — expect moderate agreement, run a periodic blind re-screen of a small sample to measure it, and treat pass reasons as soft labels rather than ground truth; outcome labels for passes are delayed one to five years and censored, so survival methods are mandatory. *Deployment:* the output must arrive before the partner opens the CIM and read in under a minute — a one-paragraph view with the five nearest prior deals — or it will not be used. A firm with five or more years of CRM history can build a useful first version in 3–4 months with one ML engineer and one data engineer; grading passes credibly needs a decade of history or a consortium of firms.
**Data availability:** Every sponsor has the CRM history; most have incomplete reasons and have deleted the CIMs. Outcome data is purchasable from PitchBook or Capital IQ. The binding constraint is NDA retention: the firm's own notes and extracted facts are retainable, the seller's document often is not.

---

## 2. Data Room Financial Extraction and Cross-Document Reconciliation
#large-language-models #transformers #feature-engineering #evaluation-metrics #data-integration #automation #worker-facing

**Problem statement:** Historical financials and KPIs appear in the CIM, the management model, trial balances, the QoE report and monthly management accounts, each in a different layout and frequently disagreeing. Associates spread them by hand and reconcile them by eye.

**ML task:** Table detection and structured extraction from PDF and Excel; entity and line-item alignment across documents; discrepancy detection
**Input data:** Data room files (PDF financial statements, Excel management models, trial balances, QoE databooks), the firm's model template and line-item taxonomy, prior associates' spreads as supervision.
**Target:** A normalised line-item time series per source with page and cell provenance, and a list of material discrepancies between sources.
**Evaluation metric:** Field-level exact-match accuracy on key line items (revenue, gross profit, EBITDA, adjustments) at the confidence threshold used for auto-population; discrepancy detection recall, because a missed restatement is far costlier than a false alarm the associate dismisses in seconds.
**Scope:** Modern multimodal LLMs make extraction tractable; the work is the alignment layer and the firm-specific line-item taxonomy. 2 engineers, 3–4 months to a tool associates use on live deals.
**Data availability:** Good inside the firm during a live deal; historical spreads exist in old models and provide supervision. Data room contents are under NDA and must be processed within the deal's retention rules.

---

## 3. Portfolio KPI Definition Drift and Early-Warning Detection
#change-point-detection #time-series-forecasting #gradient-boosting #large-language-models #evaluation-metrics #data-integration

**Problem statement:** Portfolio company problems usually show in monthly numbers before they show at the board, but the numbers are mapped by hand and companies change their own definitions without saying so. The task is to detect both genuine deterioration and silent definitional change.

**ML task:** Change-point detection on monthly KPI series; forecasting against budget; classification of detected breaks as operational vs definitional
**Input data:** Monthly packages per portfolio company over the hold period, budgets and reforecasts, covenant compliance certificates, management commentary text, and the history of mapping adjustments.
**Target:** Flags of material breaks with a probability that the break is a definition change rather than performance; forecast of covenant headroom three to six months forward.
**Evaluation metric:** Lead time of flags ahead of the board or lender learning of the problem, at a false-alarm rate the operating partner tolerates (on the order of one per company per quarter). Covenant headroom forecast evaluated by interval coverage, not point error.
**Scope:** Small data per company (often 36–60 monthly observations) means pooling across the portfolio and across funds. 1 data scientist, 3 months for a first version on top of an existing monitoring platform.
**Data availability:** Fully owned by the sponsor via its reporting rights. Labels for "this was a definition change" exist only in finance staff emails and must be reconstructed.

---

## 4. Value Creation Initiative Attribution
#causal-inference #linear-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Every deal closes with a value creation plan — pricing, procurement, sales force expansion, add-ons — and EBITDA growth at exit is attributed to the plan in fundraising materials without any measurement of which initiative caused what.

**ML task:** Causal effect estimation on panel data (difference-in-differences, synthetic control across sites, product lines or portfolio companies)
**Input data:** Initiative logs with start dates and scope; site- or product-level monthly financials; add-on acquisition dates and contribution; market indices for the end markets.
**Target:** Estimated EBITDA impact per initiative type with confidence intervals; organic vs acquired vs multiple-driven value bridges.
**Evaluation metric:** Interval width and placebo-test pass rate; for the firm, whether initiative types ranked by measured effect differ from those ranked by partner belief.
**Scope:** Hard because initiatives overlap and treatment is rarely staggered cleanly; multi-site portfolio companies are the tractable starting point. 1 data scientist plus operating partner time, 4–6 months.
**Data availability:** Owned by the sponsor but initiative start dates and scopes are rarely recorded systematically — the first deliverable is a log.

---

## 5. Proprietary Sourcing — Founder-Owned Sale Readiness
#gradient-boosting #survival-analysis #graph-neural-networks #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Sponsors pay premiums in banker-run auctions and prize "proprietary" deals, which in practice means reaching a founder-owned company before a banker is hired. Predicting which companies will transact in the next 12–24 months focuses scarce business development time.

**ML task:** Time-to-event prediction of a company's sale process starting; relationship-graph features for warm-introduction paths
**Input data:** Private company data (Grata, SourceScrub, PitchBook) — headcount trajectories, web and hiring signals, founder age and tenure, ownership history; CRM touchpoints and email metadata; advisor-hire and banker engagement signals; the firm's relationship graph.
**Target:** Hazard of a sale process within 12/24 months; best introduction path.
**Evaluation metric:** Precision at the top of the ranked list among companies the business development team can realistically contact each quarter (top 200–500); time-dependent concordance.
**Scope:** Labels (company entered a sale process) are observable but noisy; commercial data vendors are already building versions of this. 1–2 engineers, 4 months; most value is in combining vendor signals with the firm's own CRM history, which no vendor has.
**Data availability:** Purchasable signals plus the firm's own CRM. Outcome labels from transaction databases with partial coverage of lower-middle-market deals.
