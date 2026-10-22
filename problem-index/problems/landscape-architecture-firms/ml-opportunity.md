# Machine Learning Opportunities — Landscape Architecture Firms

**Industry:** [[landscape-architecture-firms|Landscape Architecture Firms]]
**Derived from:** [[problems/landscape-architecture-firms/high-impact|High Impact]], [[problems/landscape-architecture-firms/low-impact-1|Low Impact 1]], [[problems/landscape-architecture-firms/low-impact-2|Low Impact 2]], [[problems/landscape-architecture-firms/worker-life-1|Worker Life 1]], [[problems/landscape-architecture-firms/worker-life-2|Worker Life 2]]

---

## 1. Learning the Principal's Red Pen on Grading Plans
#tacit-knowledge-ml #cnns #semantic-segmentation #graph-neural-networks #evaluation-metrics #feature-engineering #compliance #worker-facing

**Problem statement:** Senior landscape architects review grading and drainage plans by eye and mark where water will pond, where accessible routes exceed slope limits, where beds sit above walks and where elevations fail to tie — a judgement they cannot fully specify. The ML problem is to learn where and why such a reviewer would place a redline on a proposed surface, and to rank deterministic slope and drainage findings the way that reviewer would.

**ML task:** Dense prediction (semantic segmentation) of review-flag locations on gridded surface rasters, multi-class classification of the flag type, plus node classification on a drainage graph of high points, low points, inlets, outlets and thresholds
**Input data:** Proposed and existing surface models exported from Civil 3D or Land F/X (TIN converted to 0.25–0.5 m elevation, slope, aspect and flow-accumulation rasters); building finished floor elevations and door locations; civil storm structures with rim and invert elevations; accessible route polylines; soil hydrologic group from the geotechnical report; historical PDF markups aligned to drawing coordinates; downstream RFIs, change orders, as-built survey points and punch-list items geolocated to the plan.
**Target:** Per-cell probability of a reviewer flag, with flag type (ponds at threshold, accessible route cross-slope or running slope, bed above walk, tie-in mismatch, outlet above inlet, flat swale in poorly draining soil); a ranked list of findings; and a secondary label of whether the location later produced an RFI, change order or punch-list item.
**Evaluation metric:** Recall of senior-reviewer flags at a fixed number of findings per sheet (for example the top 20), because a checker that buries the reviewer in hundreds of cells is abandoned; reported against the senior reviewer's own test-retest agreement on re-reviewed plans as the ceiling. Recall matters more than precision on accessibility and threshold drainage — a missed one becomes a claim — while precision governs adoption everywhere else. Downstream validation: share of later RFIs and change orders whose locations the model ranked highly.
**Scope:** The data collection challenge comes first: markups must be captured against geometry at the moment of review, which means a review layer inside Bluebeam or the CAD tool, plus retrospective alignment of a firm's archived marked-up PDFs to its CAD files — weeks of work per hundred projects. The labelling challenge is that reviewers disagree with themselves (stricter on public jobs, stricter after a claim) and outcomes are noisy (field regrading, survey error), so a sample of plans should be blind re-reviewed to measure intra-rater agreement, and downstream labels used to weight rather than replace markups. The deployment challenge is speed and vocabulary: findings must appear in seconds inside the drawing tool, phrased the way a principal would phrase them, or juniors will not open it. 2 ML engineers, 1 landscape architect with grading expertise, partnership with 3–5 firms, 9–12 months, with deterministic checks shipped first and the learned ranking layered on once a few thousand flags are captured.
**Data availability:** No public dataset exists. Firms hold surfaces and marked-up PDFs in project archives; RFIs and change orders sit in construction administration files; as-built surveys sit with surveyors and contractors. Pooling across firms is necessary for volume and must handle liability sensitivity.

---

## 2. Plant Survival by Species, Site and Specification
#survival-analysis #gradient-boosting #random-forests #feature-engineering #confidence-intervals #revenue-impact #data-integration

**Problem statement:** Landscape architects specify the same plant palettes project after project without knowing which species, sizes and conditions survive past the warranty. Estimate time-to-replacement for each specified plant given species, nursery size, planting date, exposure, soil, irrigation zone and maintenance regime.

**ML task:** Survival analysis (time-to-failure with right censoring) with tree-ensemble risk models for heterogeneous effects
**Input data:** As-built plant schedules and planting plans; warranty replacement logs from the one-year walk-through; maintenance contractors' replacement work orders; street-level and aerial imagery for later status; soil test reports; irrigation hydrozones; local climate records (heat days, freeze events, drought); nursery source and stock type.
**Target:** Time from planting to replacement or death, censored at the last observation; secondary label of cause where recorded (drought stress, poor drainage, vandalism, wrong exposure).
**Evaluation metric:** Concordance index and time-dependent calibration at 1, 3 and 5 years, reported per species group with confidence intervals because many species have few plantings. The asymmetric cost is a confident "survives" prediction on a species that fails at scale, so calibration in the low-survival tail matters more than overall concordance.
**Scope:** The model is simple; the dataset is the work. A useful version needs a few thousand tracked plantings across a climate region, which no single firm has. 1 data scientist, 1 data engineer and a horticulturist, 6 months for a regional pilot with a maintenance contractor and two design firms.
**Data availability:** Plant schedules are held by firms; replacement records by maintenance contractors and owners; imagery is purchasable. Joining them per plant is the hard, mostly manual step.

---

## 3. Plant Substitution Equivalence Ranking
#word-embeddings #k-nearest-neighbors #contrastive-learning #large-language-models #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** When a specified plant is unavailable at the required size, rank available substitutes by functional and visual equivalence for that specific location, and flag the downstream effect on quantities and cost.

**ML task:** Similarity learning over plant trait vectors and text descriptions, trained on historical approve/reject decisions, plus retrieval against current nursery availability
**Input data:** Plant trait data (mature height and spread, form, foliage, bloom, hardiness zone, sun, soil, water and salt tolerance); nursery availability lists parsed from PDFs and spreadsheets; the project's planting specification and schedule; historical substitution requests with the landscape architect's decision and comments.
**Target:** Ranked list of acceptable substitutes per request; predicted approve/reject for a proposed substitute with the governing reason.
**Evaluation metric:** Precision at 3 against the landscape architect's eventual choice, and agreement with approve/reject decisions on held-out projects. A wrong approval costs more than a wrong rejection, so the reject class needs high recall.
**Scope:** Trait data is partly public and partly in software plant databases; historical decisions sit in submittal logs. 1 ML engineer and 1 landscape architect, 4 months to a pilot inside a submittal workflow.
**Data availability:** Approve/reject decisions are recorded in submittal logs but rarely with structured reasons; capturing reasons going forward is part of the build.

---

## 4. Landscape Ordinance Extraction and Compliance Calculation
#large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation #quick-win

**Problem statement:** Convert each jurisdiction's landscape provisions — parking-lot trees and islands, buffer yards, street frontage, canopy and tree mitigation, water budgets — into structured, versioned rules, and compute compliance tables directly from the CAD model.

**ML task:** Information extraction from legal text into a rule schema (sequence-to-structure generation), followed by deterministic calculation
**Input data:** Municipal codes from code publishers and city sites, including amendments; examples of approved compliance tables from past permit sets; reviewer comment letters on rejected sets; CAD object quantities.
**Target:** Rule records (provision, applicability condition, ratio or quantity, credit rules, effective date) and computed compliance values with pass/fail per provision.
**Evaluation metric:** Field-level accuracy of extracted rules against a hand-built gold set for 50 jurisdictions, and agreement of computed tables with approved permit sets. Silent errors are the failure that matters — a wrong ratio presented confidently is worse than a provision marked for human review.
**Scope:** Extraction is tractable with current LLMs; coverage and maintenance are the real costs, because codes change. 2 engineers and 1 landscape architect, 4 months to cover the 100 most active jurisdictions in two states.
**Data availability:** Codes are public. Reviewer comment letters are held by firms and are the best source of what reviewers actually enforce.

---

## 5. Coding Public Engagement Comments for Park Plans
#bert #large-language-models #k-means-clustering #dbscan #evaluation-metrics #worker-facing #automation

**Problem statement:** Classify open-ended public comments from meetings, cards, surveys and map pins into designer-defined themes, cluster spatial comments by location, and surface where groups disagree.

**ML task:** Multi-label text classification with few-shot theme definitions, plus density-based spatial clustering of geolocated comments
**Input data:** Transcribed comment cards and dot-vote boards, survey open-ended responses, meeting notes, translated comments, map-pin comments with coordinates and demographic fields where collected.
**Target:** Theme labels per comment, sentiment toward each design option, spatial clusters with summary text.
**Evaluation metric:** Macro-F1 against a designer's hand-coded sample, with per-language breakdown to make sure minority-language comments are not miscoded; coverage of comments linked to at least one theme. Under-representing a group is the asymmetric failure.
**Scope:** Off-the-shelf models handle most of it; the product work is the review interface and traceability to source comments. 1 engineer, 3 months.
**Data availability:** Firms and cities hold past engagement material; many final reports are public records with appendices of raw comments.
