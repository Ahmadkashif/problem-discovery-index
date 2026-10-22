# Machine Learning Opportunities — Title & Settlement Offices

**Industry:** [[title-and-settlement-offices|Title & Settlement Offices]]
**Derived from:** [[problems/title-and-settlement-offices/high-impact|High Impact]], [[problems/title-and-settlement-offices/low-impact-1|Low Impact 1]], [[problems/title-and-settlement-offices/low-impact-2|Low Impact 2]], [[problems/title-and-settlement-offices/worker-life-1|Worker Life 1]], [[problems/title-and-settlement-offices/worker-life-2|Worker Life 2]]

---

## 1. Learning the Examiner's Disposition of Each Instrument
#tacit-knowledge-ml #transformers #large-language-models #gradient-boosting #graph-neural-networks #evaluation-metrics #worker-facing #compliance

**Problem statement:** A senior examiner reads each instrument in a search package and decides, largely by feel, whether it becomes a Schedule B-I requirement, a B-II exception, an insure-over request to the underwriter, or nothing. The ML problem is to learn those dispositions from the office's own history, predict them for a new search package, and flag the instruments where the model and the examiner's past behaviour disagree.

**ML task:** Instrument-level multi-class classification (requirement type, exception type, insure-over, no action) over a chain-of-title graph, plus a file-level calibrated probability that the file will be "difficult"
**Input data:** Search packages (deed, mortgage, assignment, release, judgment, lien, probate, plat and easement images with OCR text and index data); the party-instrument graph built from grantor-grantee links; the office's final commitments with requirement and exception text; underwriter insure-over approvals from email; county and underwriter identifiers.
**Target:** Disposition per instrument, aligned to the final commitment's B-I and B-II lines; file difficulty as later recorded (curative actions taken, hours, closing slipped).
**Evaluation metric:** Recall on instruments the senior examiner raised as requirements is the binding metric — a missed live lien or break in the chain becomes a claim, while a spurious flag costs a minute of examiner time. Report precision at the recall the office accepts, agreement with senior examiners against the senior examiners' own test-retest agreement on a re-examined sample as the ceiling, and time per clean file before and after.
**Scope:** Collection comes first and is the hardest part: commitments record the requirements that were raised but not the instruments that were read and deliberately ignored, so the examination screen must capture a one-click disposition and reason per instrument going forward, and history must be aligned instrument-to-requirement after the fact. Labelling is noisy because examiners disagree with each other and with themselves, especially at month-end, and local practice varies by county and underwriter, so the model must be trained per office or per county with a re-labelled agreement sample. Deployment has to be faster than the examiner: on a clean refinance chain the examiner takes minutes, so the model must pre-populate the commitment and highlight only the instruments it is unsure of. 2 ML engineers and a senior examiner as domain lead for 6–9 months for one multi-county agency, with value arriving first as retrieval ("the last 20 times we saw this pattern in this county, we did X").
**Data availability:** The search packages and commitments sit in the agency's production system and plant, typically for decades. The dispositions of ignored instruments and the reasons for raised ones do not exist and must be captured. Underwriters hold the claim outcomes; an agency alone sees very few claims.

---

## 2. Seller Impersonation Risk Scoring at Order Open
#gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Score every seller-side order, at the moment it is opened, for the probability that the seller is not the owner of record, so the office applies enhanced verification to the few that warrant it.

**ML task:** Binary classification with heavy class imbalance and calibrated probability
**Input data:** Property attributes (vacant land, free and clear, years held, absentee owner, tax mailing address history); transaction attributes (price against an automated valuation, cash buyer, days from listing to contract, remote signing requested, payout to a new account, seller contact channel); recorded-instrument features (prior signatures, notary history); outcomes from the office's and its underwriter's fraud incident records.
**Target:** Confirmed impersonation attempt (stopped or completed) versus legitimate sale.
**Evaluation metric:** Recall at a fixed review budget, because the office can only call so many owners of record a week; a missed impersonation becomes a claim, while a false alarm costs a phone call. Report the precision-recall curve and calibration by property type, since vacant land dominates the positives.
**Scope:** Positives are scarce per office, so the realistic build pools incidents across an underwriter's agents or a vendor's customers. Simple models — logistic regression and gradient boosting on 30–50 features — are adequate and explainable to an underwriter. 1 data scientist and 1 engineer, 3–4 months to a first version, contingent on pooled incident data.
**Data availability:** Property and transaction features are available from public records and the order itself. Labelled fraud incidents sit with underwriters, wire-verification vendors and ALTA's members, and are not shared systematically.

---

## 3. Curative and Release Cycle-Time Modelling
#survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** For each open requirement or post-closing item — a payoff letter, a lien release, a probate filing, a corrective deed — predict how long it will take to clear and which items are genuinely late, so escrow officers set realistic closing dates and post-closers chase the right items.

**ML task:** Time-to-event regression with censoring, by item type and counterparty
**Input data:** Requirement and open-item histories from the production system with open and close dates; counterparty identity (servicer, lienholder, court, HOA); county recording lags from e-recording confirmations; state release-statute deadlines; closing dates and slips.
**Target:** Days to clearance; probability of clearance before the scheduled closing date or the statutory deadline.
**Evaluation metric:** Concordance index and calibration of the probability of clearing before the date that matters, measured out of time. Under-predicting duration is the costly error, because it produces a confident closing date that slips.
**Scope:** The data exists in every production system but is messy: items are closed late in bulk, and servicers change names through acquisitions, so counterparty resolution is half the work. 1 data scientist, 3 months for one large agency; most of the value comes from servicer-level baselines.
**Data availability:** Held by each agency in its production system; more valuable pooled across agencies by a software vendor, which raises the client-data question discussed in the Pass 2 layer.

---

## 4. Closing Disclosure and Settlement Statement Reconciliation
#large-language-models #transformers #seq2seq #evaluation-metrics #compliance #automation

**Problem statement:** Extract every fee, credit, proration and payoff from the lender's Closing Disclosure and the agent's settlement statement, map both to a common schema, and report only the differences that matter under TRID, with the governing figure for each.

**ML task:** Document extraction into a structured schema, line matching, and rule-based classification of each difference by TRID consequence
**Input data:** CD PDFs from many lenders' systems, ALTA settlement statements, fee sheets, payoff letters, title premium calculations and the rate manual, state transfer-tax tables.
**Target:** Matched line pairs with amounts; a list of differences labelled immaterial, needs correction, tolerance issue, or redisclosure trigger.
**Evaluation metric:** Line-level extraction accuracy and pair-matching F1, with zero tolerance for silent misses on redisclosure triggers. Track email rounds per file and files whose closing slipped on redisclosure.
**Scope:** The CD is a standard form, so extraction is tractable; the hard part is mapping agent line items to CD sections and encoding the title premium disclosure rule and state-specific charges. 2 engineers and an escrow lead, 4 months.
**Data availability:** Both documents pass through the agent's production system on every financed file; lenders' CD formats vary but follow the regulatory model form.

---

## 5. Deed-Book Transcription and Legal Description Parsing
#cnns #transformers #seq2seq #evaluation-metrics #data-integration #automation

**Problem statement:** In counties without a title plant or a usable online index, abstractors search handwritten and typed deed books and grantor-grantee indexes by hand. Transcribe the images, extract parties, dates, instrument types and legal descriptions, and check that metes-and-bounds descriptions close and match adjoining parcels.

**ML task:** Handwritten and typed text recognition, named-field extraction, and parsing of metes-and-bounds calls into geometry with closure checks
**Input data:** Scanned deed books, index books and plats from county recorders, often 19th- and early-20th-century handwriting; existing plant records as labelled pairs where a plant exists.
**Target:** Structured instrument records (grantor, grantee, date, book and page, instrument type, legal description) and a polygon per description with closure error.
**Evaluation metric:** Character and field error rate on held-out books from unseen counties, and recall on instruments affecting the searched parcel — an unindexed instrument the search misses is the failure that matters.
**Scope:** Handwriting recognition on historical records is mature in genealogy; the title-specific work is field extraction and legal description parsing. 2 ML engineers, 6 months for a county-agnostic model, plus per-county fine-tuning.
**Data availability:** Many counties have scanned their books but not indexed them; access and licensing vary county by county. Title plant owners hold the labelled pairs.
