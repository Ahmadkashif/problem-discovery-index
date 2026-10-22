# Machine Learning Opportunities — Drafting Services

**Industry:** [[drafting-services|Drafting Services]]
**Derived from:** [[problems/drafting-services/high-impact|High Impact]], [[problems/drafting-services/low-impact-1|Low Impact 1]], [[problems/drafting-services/low-impact-2|Low Impact 2]], [[problems/drafting-services/worker-life-1|Worker Life 1]], [[problems/drafting-services/worker-life-2|Worker Life 2]]

---

## 1. Learning Where the Senior Checker Looks
#tacit-knowledge-ml #cnns #object-detection #graph-neural-networks #evaluation-metrics #transfer-learning #worker-facing #revenue-impact

**Problem statement:** A senior checker scans a shop drawing or drawing sheet and stops where an error is likely — a connection that will not fit up, an elevation that disagrees with another sheet, a bar that cannot be placed — from pattern recognition built over thousands of sheets. The ML problem is to learn that attention from the checker's own historical markups and from downstream outcomes, and rank the regions and model objects of a new sheet by the probability that they hold an error.

**ML task:** Region-level object detection on rendered sheets plus node-level binary classification on the model's object graph (members, connections, bars, spools), producing a calibrated error probability per region and object with an error-category label
**Input data:** Issued and checked sheet PDFs with checker markups exported from Bluebeam; Tekla, SDS2, Revit or rebar-software models with object attributes and connectivity; engineer-of-record review comments ("approved as noted", "revise and resubmit") with dates; fabricator shop queries, field-fix reports and back-charges where the bureau can obtain them; client and project metadata.
**Target:** For each region or object: whether the checker marked it, the markup category (fit-up, elevation or dimension conflict, design conflict, missing information, standard violation, question for engineer), and whether an error was later confirmed downstream.
**Evaluation metric:** Recall of downstream-confirmed errors within the top-k flagged regions per sheet, at a k small enough that review stays faster than the checker's own scan — a missed fit-up error costs a field fix and a back-charge; a false flag costs seconds. Report precision alongside, because a checker who sees mostly false flags stops reading them. Measure model agreement with held-out checker markups against the checker's own test-retest agreement on re-checked sheets as the ceiling.
**Scope:** The data collection challenge is the core of the project: the expert must be captured while performing the task, so the first deliverable is a markup capture layer that links every cloud to a model object and category at near-zero extra effort, and historical markups must be aligned to model objects after the fact through sheet-to-model view mapping. The labelling challenge is that checkers disagree with themselves under deadline and mix errors with preferences and questions; a sample of sheets must be re-checked blind to estimate intra-rater reliability, and the downstream outcome must be used as the stronger label where it exists. The deployment challenge is speed: flags must appear within the checker's normal review, in the tool they already use, faster than their own scan. 2 ML engineers and 1 detailing subject-matter lead with one or two partner bureaus or a fabricator with an in-house detailing department, 9–12 months; value appears first as retrieval ("the last five times this connection type was marked") before a ranking model is trusted.
**Data availability:** Checked PDFs and models sit in every bureau's archive but are rarely retained in versioned form. Downstream outcomes belong to fabricators and general contractors and must be obtained by partnership; a fabricator that runs its own detailing team holds both sides and is the natural first partner. Client NDAs constrain pooling across bureaus.

---

## 2. Drafting-Effort Estimation From Bid Drawings
#gradient-boosting #feature-engineering #loss-functions #cross-validation #object-detection #revenue-impact

**Problem statement:** Predict the drafting or detailing hours a job will take — and therefore the per-sheet, per-ton or hourly price — from the bid drawings and the client's history, before the bureau commits to a quote.

**ML task:** Quantile regression of total job hours (and hours per sheet type) from features extracted from the bid set and client history
**Input data:** Bid and design drawing PDFs; extracted counts of sheets by type, grid lines, members and connection types, unique versus typical details, skewed and sloped geometry, clouded or "by others" areas; tonnage where quoted; client identity and past revision behaviour; the bureau's past quotes, actual hours and revision rounds.
**Target:** Actual hours to first submittal and to final approval; number of revision rounds.
**Evaluation metric:** Pinball loss at the 50th and 80th percentiles, and the overrun rate (share of jobs whose actual hours exceed the quoted 80th-percentile estimate). Underestimation costs more than overestimation, because a lost bid costs margin on one job while an underpriced fixed-fee job costs the job's margin and the capacity it consumed.
**Scope:** Features come from document parsing and symbol detection on PDFs; the model itself is modest. The hard part is that a single bureau's history is a few hundred jobs, so the model needs strong priors from extracted drawing features and pooled data from several bureaus or one large offshore enterprise. 1 ML engineer and 1 data engineer, 4–5 months.
**Data availability:** Quotes and timesheets exist at every bureau, of uneven quality; bid sets are retained. Labels need cleaning — hours are often logged to the job, not the sheet.

---

## 3. Markup Reading and Task Extraction
#transformers #large-language-models #object-detection #seq2seq #automation #workflow-orchestration #worker-facing

**Problem statement:** Turn a client's red-marked PDF set — handwritten or digital clouds, arrows, notes and references — into a structured task list linked to sheets and drawing elements, with implied changes on unmarked sheets proposed and ambiguous items flagged as questions.

**ML task:** Markup detection and segmentation, handwriting recognition, then sequence-to-sequence generation of structured change tasks with element linking and an ambiguity classifier
**Input data:** Marked-up PDF sets (scanned and Bluebeam), the clean underlying sheets, sheet indexes, prior markups and the tasks drafters actually performed in response, and the subsequent issued set.
**Target:** Per markup: transcription, the change requested, the sheet and element affected, other sheets implied, and a flag for whether a drafter could act without asking.
**Evaluation metric:** Task-level recall against the changes visible in the next issued set (a missed markup becomes a rejected deliverable), precision of element linking, and the share of ambiguity flags that the client's answer confirms as genuinely ambiguous. Time from receipt of markups to a checked task list.
**Scope:** Vision-language models now read handwriting and drawing context well enough to start; fine-tuning on markup-to-task pairs from a bureau's archive is the differentiator. The cross-sheet inference ("this change implies three others") is the hard tail. 2 engineers, 5–6 months.
**Data availability:** Every bureau holds years of incoming markups and the issued sets that answered them; pairing them is the labelling work and is largely automatable by diffing consecutive issues.

---

## 4. Design Revision Change Detection and Impact Mapping
#cnns #semantic-segmentation #graph-neural-networks #k-nearest-neighbors #data-integration #automation

**Problem statement:** Given two issues of a design set, find every change — clouded or not — and map each to the model objects, piece marks and shop drawings it affects.

**ML task:** Registered image differencing with learned change segmentation on sheet pairs, change classification (dimension, elevation, member size, opening, note), and graph matching from design-drawing elements to detailing-model objects
**Input data:** Successive design-set PDFs or models; revision narratives and clouds; the detailing model with object-to-sheet references; historical change logs and the edits detailers made in response.
**Target:** A list of changes with location, type and whether it was clouded; for each, the affected objects and sheets.
**Evaluation metric:** Recall of changes that required a detailing edit (a missed change becomes a mis-fabricated piece); share of unclouded changes found; precision high enough that detailers trust the list over manual overlay.
**Scope:** Pixel differencing is easy; the value is in suppressing noise (re-plotted text, shifted viewports) and in linking a two-dimensional change to three-dimensional objects. 2 engineers, 5 months for steel, longer per additional trade.
**Data availability:** Successive issues are in every bureau's project folders; detailers' responding edits are recoverable from model history where versioning is on.

---

## 5. Client Standard Inference and Conformance Checking
#random-forests #k-nearest-neighbors #word-embeddings #decision-trees #feature-engineering #quick-win #automation

**Problem statement:** Learn a client's CAD or BIM standard from a few of its sample drawings and check, or convert, each outgoing set against it.

**ML task:** Classification of drawing entities and styles into standard roles (layer purpose, text style, dimension style, title-block field), similarity matching of layer and family names across naming schemes, and anomaly scoring of non-conforming entities
**Input data:** Client sample sets in DWG, DXF or RVT; client standards manuals; the bureau's working templates; past rejections citing standards issues.
**Target:** A client standard profile; per outgoing drawing, a list of non-conforming entities with proposed fixes.
**Evaluation metric:** Precision and recall of non-conformance flags against client rejection comments; share of sets accepted without standards comments. Precision matters more than in most checking tasks, because a drafter given dozens of false flags per sheet will ignore all of them.
**Scope:** Largely classical machine learning on entity attributes plus name embeddings; the work is in parsing file formats and building profiles per client. 1–2 engineers, 3–4 months. A quick win for any bureau with many clients.
**Data availability:** Sample sets and rejection emails are held by every bureau; labels come from accepted versus rejected deliverables.
