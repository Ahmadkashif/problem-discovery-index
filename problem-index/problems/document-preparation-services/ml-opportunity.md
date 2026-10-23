# Machine Learning Opportunities — Document Preparation Services

**Industry:** [[document-preparation-services|Document Preparation Services]]
**Derived from:** [[problems/document-preparation-services/high-impact|High Impact]], [[problems/document-preparation-services/low-impact-1|Low Impact 1]], [[problems/document-preparation-services/low-impact-2|Low Impact 2]], [[problems/document-preparation-services/worker-life-1|Worker Life 1]], [[problems/document-preparation-services/worker-life-2|Worker Life 2]]

---

## 1. Learning the Editor's Corrections: Dictator Profiles and Plausibility Catches
#tacit-knowledge-ml #transformers #seq2seq #large-language-models #evaluation-metrics #feature-engineering #worker-facing #compliance

**Problem statement:** Experienced healthcare documentation editors correct speech-recognition drafts using knowledge of each dictator's habits and of what is clinically plausible, a judgement they cannot specify and that leaves when they do. The ML problem is to learn that judgement from the logged diffs between machine drafts and edited finals, separate dictator-specific and plausibility corrections from routine recogniser fixes, and surface them to the next editor on the account.

**ML task:** Edit-reason classification over aligned draft–final token spans (recogniser error, dictator habit, clinical-plausibility catch, template rule), plus a per-dictator sequence-to-sequence post-editor that proposes corrections, and a span-level risk score for "this passage is where this dictator's drafts usually need a clinical catch"
**Input data:** Back-end speech-recognition drafts, edited finals and audio timestamps across many thousands of reports per account; dictator, specialty, report type and template metadata; QA audit records with AHDI severity categories; physician sign-off edits where captured; a small set of reason labels gathered by one-keystroke confirmation inside the editor.
**Target:** Reason class per edited span; the corrected text; a calibrated probability that an unedited span contains a critical error.
**Evaluation metric:** Recall on critical-error spans in held-out QA-audited reports is the binding metric. A missed laterality, negation or dose error fails the report under AHDI's scoring and can harm a patient, while a false flag costs the editor two seconds of listening. Report precision at the recall operating point, edited lines per hour before and after, and agreement of reason labels with a second editor, using the editors' own re-test agreement as the ceiling.
**Scope:** The data collection challenge is that the diff records what changed but not why, and not the edits deliberately left unmade. Reasons must be captured from the expert at the moment of editing with near-zero effort, and inferred elsewhere from patterns such as repeat corrections per dictator. The labelling challenge is that QA auditors disagree on severity and editors disagree with themselves under quota pressure, so a sample needs double annotation to measure reliability, and genuinely ambiguous audio has no ground truth beyond the physician's signature. The deployment challenge is that help must be faster than the editor's ear at several hundred lines an hour, and must stay inside each health system's business-associate agreement. Per-account models avoid the cross-client permission problem but learn more slowly. 2 ML engineers, a clinical linguist and 2–3 veteran editors as annotators, 6–9 months with one vendor; dictator-habit pre-correction pays off first, plausibility flags later.
**Data availability:** Documentation vendors and back-end recognition platforms hold years of draft–final pairs per account. They are PHI under business-associate agreements, so training typically has to stay within each customer's contract unless the agreement allows de-identified model improvement. Reason labels do not exist anywhere and must be built.

---

## 2. Predicting Edit Effort Before the File Is Taken
#gradient-boosting #feature-engineering #evaluation-metrics #cross-validation #automation #worker-facing #revenue-impact

**Problem statement:** Platforms price and pay human transcription per audio minute regardless of difficulty, so hard files go unclaimed and customers can't tell which files need a human. Predict, from the audio and the machine draft alone, how many human editing minutes each audio minute will take and how much the human pass will change the text.

**ML task:** Regression of editor minutes per audio minute and of post-edit word error rate against the machine draft, at file and segment level, with prediction intervals for pricing
**Input data:** Audio features (signal-to-noise, overlap ratio, speaker count from diarisation, speaking rate, accent and channel indicators); ASR token confidences and n-best disagreement; domain vocabulary density; customer style requirements (verbatim, timestamps); historical editor time logs and the final human transcript for each completed file.
**Target:** Editor minutes per audio minute; word error rate of the machine draft against the human final; probability that the human pass changes meaning-bearing words.
**Evaluation metric:** Mean absolute error on editor minutes, and interval coverage, since pricing needs a reliable upper bound more than a sharp point estimate. Under-predicting hard files is the costly error: it reproduces today's unclaimed queue. Also track the business outcome: time-to-claim for top-decile difficulty files and customer opt-down rates for files predicted to need no human.
**Scope:** Gradient-boosted trees on engineered features are the right first model and are explainable to workers who will see the posted rate. 1 data scientist and 1 engineer, 3–4 months on a platform's historical logs. The harder work is policy: what a worker is paid when the prediction is wrong, and how a customer is told a file doesn't need a human.
**Data availability:** Platforms hold editor time logs and draft–final pairs for millions of files. Rev's terms permit training its recognition models on self-serve customer content (enterprise customers can opt out), and other platforms' contracts vary.

---

## 3. Severity-Weighted Accuracy Scoring of Every Transcript
#bert #transformers #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #automation

**Problem statement:** Transcript quality is scored by a second person on a small random sample, by hand, against a severity scheme (AHDI's critical and noncritical categories in medicine, client style rules elsewhere), and two auditors often disagree. Classify every edit, and every residual difference between a transcript and an audited version, into severity categories automatically, so every document carries a score and auditors only review disagreements.

**ML task:** Multi-class classification of aligned difference spans into severity categories (critical, noncritical, minor or style, no error), with document-level score aggregation under the client's scoring method and statistical comparison against human auditors
**Input data:** Historical QA audit sheets with marked errors and categories; the transcript before and after audit; report type and template; the client's style guide and the AHDI category definitions; double-audited samples for reliability.
**Target:** Severity label per span; document score under the chosen method (error value from 100, or errors per lines reviewed); flag for auditor review where model and rubric are uncertain.
**Evaluation metric:** Cohen's kappa against expert auditors, reported beside the auditors' own kappa with each other, which is the realistic ceiling. Recall on critical-category spans, because a missed critical error is the one that fails a report and matters clinically. Confidence intervals on per-editor monthly scores, which matter because those scores set pay and service credits.
**Scope:** A fine-tuned BERT-class encoder on span pairs with document context does most of the work. The hard part is agreeing the rubric across clients and keeping the model's scores explainable when an editor disputes one. 1 ML engineer and a QA lead, 4 months to a pilot alongside human auditors.
**Data availability:** Vendors' QA departments keep audit sheets, often in spreadsheets with the error text pasted in, so alignment to source spans needs reconstruction. Double-audited samples must usually be created for the reliability study.

---

## 4. Thesis Format Conformance from the Rendered Page
#cnns #object-detection #feature-engineering #evaluation-metrics #automation #quick-win

**Problem statement:** Graduate school format reviewers reject dissertation deposits for page-level faults — margins, page-number position and numerals, caption placement, front-matter order, landscape pages — that a template can't prevent and a language tool can't see. Detect those faults on the rendered PDF and predict which corrections this school's reviewer will return.

**ML task:** Page-layout object detection (page number, header, caption, figure, table, heading, body block) on rendered page images, combined with rule checks compiled from each school's thesis manual, plus a classifier trained on past reviewer correction lists to rank likely rejection reasons
**Input data:** Rendered page images and PDF structure of deposited theses; the institution's manual turned into measurable rules; reviewers' historical correction lists linked to the drafts they were written about.
**Target:** Bounding boxes and classes for layout elements; rule violations with page references; a ranked list of predicted reviewer corrections.
**Evaluation metric:** Recall on violations a human reviewer would return, measured against held-out reviewed deposits; a missed fault costs a rejection round near the deadline, while a false flag costs a student a minute. First-pass acceptance rate before and after deployment is the outcome metric.
**Scope:** Document layout detectors pretrained on public page-layout datasets transfer well to theses. Encoding each manual is the recurring cost and suits a rules editor that a graduate school's own reviewer can maintain. 1 engineer and 1 ML engineer, 3 months for a pilot school; each additional school takes weeks.
**Data availability:** Deposited theses are public in repositories and ProQuest, but rejected drafts and correction lists sit in graduate-school email and review systems and need a partner institution.

---

## 5. Which Resume Version Wins Interviews
#survival-analysis #logistic-regression #causal-inference #feature-engineering #revenue-impact #worker-facing

**Problem statement:** Resume writers sell documents meant to win interviews and almost never learn whether they did. Estimate, from client-reported application outcomes, how resume features (length, quantified accomplishments, keyword coverage of the target posting, format, seniority framing) relate to time-to-first-interview, separating document effects from the client's market.

**ML task:** Time-to-event modelling of first interview and offer by resume version, with propensity adjustment for client seniority, field, location and application volume
**Input data:** Resume versions with extracted features; target postings; client application logs (applications sent, dates, callbacks, interviews) collected through a tracker the writer gives the client; client profile and labour-market tightness for the target occupation.
**Target:** Hazard of first interview per application; interviews per 100 applications by version.
**Evaluation metric:** Concordance index on held-out clients, with confidence intervals wide enough to be honest at the sample sizes a writing business can collect. The headline is effect sizes with intervals, not a leaderboard, because the decision is which practices to keep.
**Scope:** Statistically modest; the difficulty is collecting outcomes from clients who disappear once hired. A volume platform with thousands of orders a month could reach usable samples in a year, while a solo writer never will alone, which argues for a shared tracker across writers. 1 data scientist, 3 months after a year of outcome collection.
**Data availability:** No one collects this today. Platforms hold the documents and could prompt clients for outcomes; applicant tracking systems hold the real callback data but belong to employers.
