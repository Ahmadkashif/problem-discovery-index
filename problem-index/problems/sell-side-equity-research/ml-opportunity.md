# Machine Learning Opportunities — Sell-Side Equity Research

**Industry:** [[sell-side-equity-research|Sell-Side Equity Research]]
**Derived from:** [[problems/sell-side-equity-research/high-impact|High Impact]], [[problems/sell-side-equity-research/low-impact-1|Low Impact 1]], [[problems/sell-side-equity-research/low-impact-2|Low Impact 2]], [[problems/sell-side-equity-research/worker-life-1|Worker Life 1]], [[problems/sell-side-equity-research/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Analyst's Revision Judgment
#tacit-knowledge-ml #gradient-boosting #feature-engineering #evaluation-metrics #confidence-intervals #causal-inference #worker-facing

**Problem statement:** A senior analyst adjusts management guidance and consensus into their own estimates using a learned sense of each management team's guiding behaviour and of which line items matter. Predict, per company and line item, the direction and size of the analyst's adjustment from guidance, and separately whether that adjustment historically improved accuracy — so the pattern can be transferred to associates and successors and its value measured.

**ML task:** Regression of analyst estimate minus guidance midpoint, plus a calibrated classifier for whether the adjustment beat the unadjusted guide; per-company guidance-bias estimation as a hierarchical feature
**Input data:** The department's published estimate history by line item and date (from its own archive or its I/B/E/S and Visible Alpha submissions); company guidance history extracted from press releases and transcripts; realised reported values; consensus at each date; model file versions where retained; the analyst's note text accompanying each revision; stock price reaction on report days.
**Target:** The analyst's adjustment to guidance (signed, % of guide), and a binary "adjustment improved absolute forecast error" label per revision.
**Evaluation metric:** Mean absolute error of predicted adjustment against the analyst's actual adjustment on held-out quarters, but the decisive metric is whether model-suggested adjustments reduce forecast error versus guidance alone for analysts other than the one it learned from — evaluated by company and by quarter, with intervals, because per-company histories are short (40–60 quarters at best) and a pattern fitted on twelve quarters is a story, not a finding.
**Scope:** Data collection is the hard part. Model files are personal, inconsistently versioned and laid out differently by every analyst; the reliable spine is the published estimate history, which every department holds. Labelling must use the contemporaneous record, since analysts rationalise old revisions when asked. Deployment must sit inside the model and preview template and be faster than the analyst's own read on earnings morning, or it will be ignored; and analysts may resist a tool that makes them replaceable, so the first deliverable should be a private calibration report to the analyst. 1 ML engineer, 1 data engineer and a senior analyst sponsor, 6 months for a first sector.
**Data availability:** Published estimates, guidance and realised values are complete and owned or licensed by the department. Model versions and the reasons for revisions are the gap and must be captured going forward.

---

## 2. Filing-to-Model Line-Item Mapping
#transformers #large-language-models #feature-engineering #evaluation-metrics #data-integration #automation

**Problem statement:** Map each value in a newly released press release, supplementary sheet or 10-Q into the correct row of a specific analyst's idiosyncratic model, applying that analyst's historical adjustments, and flag presentation changes.

**ML task:** Table extraction plus learned schema matching between source line items and model rows, conditioned on prior quarters' fills of the same model
**Input data:** Prior quarters' source documents and the corresponding filled model cells (the historical fill is the training signal); current release; vendor-standardised data from Daloopa or Canalyst where licensed.
**Target:** Proposed value and source reference for each model input cell, with a confidence and a "presentation changed" flag.
**Evaluation metric:** Cell-level exact accuracy at the confidence threshold where a cell is auto-filled; precision on auto-filled cells matters more than coverage, because a silently wrong segment number propagates into published estimates. Recall on presentation-change flags measured against restatements and re-segmentations.
**Scope:** Extraction from releases is largely solved; the value is in the per-model mapping, which is learnable from three or four prior quarters of fills. 2 engineers, 4 months to cover a department's models.
**Data availability:** Every department has years of filled models and the matching source documents; the join between them is implicit in cell values and must be reconstructed.

---

## 3. Rule 2241 Pre-Review of Draft Reports
#large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration #quick-win

**Problem statement:** Before supervisory analyst review, flag specific Rule 2241, Reg AC and house-policy failures in a draft research report: missing price-target basis or risks, companies mentioned without disclosures, rating changes without required language, promotional tone, and conflicts with the live restricted and quiet-period lists.

**ML task:** Multi-label classification of report passages against a checklist, plus entity extraction of every issuer mentioned, reconciled against the disclosure database and control-room lists
**Input data:** Historical draft and final reports with supervisory analyst edits and comments; the firm's written supervisory procedures; disclosure database; restricted and watch list history.
**Target:** Passage-level flags with the rule or procedure cited.
**Evaluation metric:** Recall on the failure classes supervisory analysts actually corrected historically (missing a disclosure is the costly error), with precision tracked so the flag rate does not train reviewers to ignore it.
**Scope:** Drafts-versus-finals give a labelled corpus of corrections for free. 1–2 engineers and a compliance sponsor, 3–4 months. Must run inside the information barrier; it reads pre-publication research.
**Data availability:** Good and internal; retention rules mean edit history exists for years.

---

## 4. Interaction-to-Vote Attribution
#causal-inference #gradient-boosting #linear-regression #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Estimate which research interactions (notes read, models downloaded, calls, meetings, events, bespoke work) are associated with changes in a client's broker vote for an analyst or sector team, controlling for client size and prior relationship.

**ML task:** Panel regression and gradient-boosted models of vote share change on interaction features, with causal adjustment for selection (analysts call the clients who already like them)
**Input data:** CRM interaction logs; platform readership data; corporate access records; vote results per client per period; commission or RPA payments.
**Target:** Change in vote points or payment per client-analyst pair per period.
**Evaluation metric:** Out-of-period predictive accuracy of vote change, with intervals; and stability of the attributed effects across periods, since a driver that flips sign each period is noise.
**Scope:** Small number of periods per client (two votes a year) and inconsistent CRM logging limit precision; honest output is directional guidance by interaction type. 1 data scientist, 3 months, plus a CRM hygiene effort.
**Data availability:** Votes and readership exist; interaction logging quality is the binding constraint.

---

## 5. Grounded First-Take Note Drafting
#large-language-models #transformers #k-nearest-neighbors #evaluation-metrics #worker-facing #automation

**Problem statement:** Draft a first-take earnings note in the house template and the analyst's voice, with every figure traced to a model cell or source line, retrieving the analyst's prior notes on the company for framing.

**ML task:** Retrieval-augmented text generation with numeric grounding and verification
**Input data:** The filled model and variance table; the release; the analyst's prior notes on the company; house style guide.
**Target:** A draft note with figure-level citations.
**Evaluation metric:** Numeric fidelity (zero tolerance — every figure must match its cited source), analyst edit distance, and time to publication.
**Scope:** Depends on opportunity 2 for clean numbers. 1–2 engineers, 3 months. Drafts must be reviewed; the analyst signs a Reg AC certification for the content.
**Data availability:** Years of published notes per analyst; excellent.
