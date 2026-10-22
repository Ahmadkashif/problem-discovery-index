# Machine Learning Opportunities — Notary & Signing Services

**Industry:** [[notary-signing-services|Notary & Signing Services]]
**Derived from:** [[problems/notary-signing-services/high-impact|High Impact]], [[problems/notary-signing-services/low-impact-1|Low Impact 1]], [[problems/notary-signing-services/low-impact-2|Low Impact 2]], [[problems/notary-signing-services/worker-life-1|Worker Life 1]], [[problems/notary-signing-services/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Experienced Notary's Read of the Wrong Signer
#tacit-knowledge-ml #cnns #gradient-boosting #object-detection #evaluation-metrics #confidence-intervals #compliance #worker-facing

**Problem statement:** Signing agents with thousands of signings behind them sense an impostor or a coerced signer before they can say why — an ID that feels wrong, a signer who does not know the property, a companion who answers for them — and refuse a handful of signings a year on that read. The ML problem is to learn that judgement from structured captures of the credential, the signer and the agent's own prompted observations, combined with transaction context, and to deliver it to new agents as a calibrated flag before the signer signs.

**ML task:** Two stages. (a) Image classification and region detection on credential photos (front, back, barcode, portrait, security features) to score authenticity and portrait-to-live-face match; (b) a calibrated binary classifier for transaction-level impostor or undue-influence risk, combining the image score, the agent's structured answers and title-file context.
**Input data:** Phone images of the credential front and back; a live face capture; the decoded barcode and machine-readable zone; the signer's signature image; four or five prompted agent answers (did the signer know the property, who else was present, did anyone answer for them, did they read before signing); title-file context held by the ordering title company (vacant land, absentee or deceased owner of record, seller-arranged notary, cash buyer, recent ID issue date, mismatch between ID address and owner's mailing address).
**Target:** For (a), genuine versus altered or counterfeit credential and match versus non-match; for (b), whether the transaction was later confirmed fraudulent (title claim, quiet-title suit, police report, owner dispute) within 24 months, plus the expert's refuse/proceed decision as an auxiliary label.
**Evaluation metric:** Recall at a fixed review budget on confirmed impostor transactions is primary: a missed impostor costs a six-figure claim, while a false flag costs a phone call to the owner of record. Report precision at that operating point, expected calibration error, and false-flag rates broken out by age band, ID-issuing state and language of the signer — a model that flags elderly or immigrant signers disproportionately would deny legal acts and is a failure regardless of recall. Expert agreement is reported against the experts' own test-retest agreement on re-shown cases as the ceiling.
**Scope:** The data-collection challenge dominates: the expert's judgement happens in a minute at a stranger's table, so capture has to be a ten-second phone flow the agent does anyway for the journal, rolled out first with title companies' approved-notary panels, who have the strongest incentive. The labelling challenge is that confirmed fraud is rare and delayed and lives in title claim files rather than in the notary's journal, so a label-linking agreement with at least one title underwriter or large agency is a precondition; experts also disagree with themselves, so a sample of captures should be re-reviewed blind by three senior agents to measure intra- and inter-rater reliability. The deployment challenge is speed and fairness: the flag must arrive on-device in seconds, offline, and the notary always keeps the decision. A team of 2 ML engineers, 1 mobile engineer and 1 notary-law lead, 9-12 months, with the credential-image stage useful within 4 months.
**Data availability:** Credential image datasets exist commercially through identity verification vendors; the transaction context sits with title companies; confirmed outcomes sit with title insurers. None of it is joined to the notary's act today. Expert annotations must be created from scratch, starting with a few hundred senior agents. The file-level seller-risk score that supplies the context features is the title office's own model, analysed under [[title-and-settlement-offices|Title & Settlement Offices]]; this entry adds the notary-side capture and the expert's read.

---

## 2. Signing Package Completeness Check From Phone Photos
#object-detection #cnns #transformers #evaluation-metrics #feature-engineering #automation #quick-win

**Problem statement:** Before leaving the table, detect every required signature, initial, date and notarial certificate field in a wet-ink loan package that is blank, misplaced or inconsistent, using the package's own requirements rather than generic form detection.

**ML task:** Page classification (which document and page this is) plus field-level object detection (signature, initial, date, notary seal, certificate venue and date) and a rule check of detected fields against the lender's and title company's requirement list.
**Input data:** Phone photos or scans of executed pages; the original unsigned package PDF (for page alignment and expected field locations); lender and title company package conventions; the notary's state certificate rules.
**Target:** Per-page list of required fields with status (present, blank, wrong signer, wrong date) and per-package pass/fail.
**Evaluation metric:** Recall on blank required fields, measured on a held-out set of packages that were later rejected or redrawn, because a missed blank causes a redraw and a funding delay; precision matters second, since each false alarm costs the agent a page flip at the table. Track the downstream redraw rate per hundred signings before and after deployment.
**Scope:** Detecting signature boxes is a solved problem; the work is aligning crumpled photographed pages to the original PDF and maintaining per-lender conventions. 2 engineers, 4-5 months to a pilot with one signing service. On-device inference is preferable because packages contain borrowers' financial data.
**Data availability:** Signing services and title companies hold years of returned packages and their redraw records; labelling blank fields is quick for non-experts once page templates are aligned.

---

## 3. Forged-Seal and Commission Verification on Recorded Instruments
#cnns #object-detection #graph-theory #k-nearest-neighbors #evaluation-metrics #compliance #data-integration

**Problem statement:** Many forged deeds carry a forged or stolen notary seal and signature. Given a recorded or submitted instrument, read the notarial certificate and seal, check the commission against state records, compare the seal impression and signature with that notary's known genuine acts, and flag networks of instruments that share a suspicious notary, signer or address.

**ML task:** Optical reading of seal text (name, commission number, expiry) and certificate fields; similarity search of seal and signature images against a notary's reference set; graph construction over notaries, signers, grantees, addresses and recording dates to surface clusters.
**Input data:** Recorded instrument images from county recorders or eRecording submissions; state commission lists (name, number, county, expiry); reference seal and signature images from verified acts; grantor-grantee indexes.
**Target:** Commission valid at the act date (yes/no); seal and signature consistency score; cluster-level suspicion score.
**Evaluation metric:** Precision at the top of the ranked list matters most, since every flag triggers a human review at a recorder or title company; report recall on known forged instruments from prosecuted cases as the secondary check. Graph clusters are evaluated by the share later confirmed in investigations.
**Scope:** Commission checks are deterministic once state lists are ingested; seal similarity needs a reference set per notary, which exists only where acts are already recorded. 2 ML engineers and a data engineer, 6 months for one state's recordings.
**Data availability:** Recorded instruments are public but fragmented by county; commission lists are public in most states with varying formats; confirmed forgery labels come from prosecutions and title claims.

---

## 4. Signing Order Assignment by Predicted Reliability and True Cost
#gradient-boosting #survival-analysis #linear-regression #time-series-forecasting #evaluation-metrics #workflow-orchestration #revenue-impact

**Problem statement:** For each incoming signing order, predict for every eligible agent the probability of on-time, error-free completion and the agent's true time cost, so the dispatcher assigns the most reliable agent at a fee the agent will accept, and agents see an honest effective hourly rate before accepting.

**ML task:** Binary classification of clean completion (no redraw, no late scanback, no no-show) per agent-order pair; regression of total agent time (drive, print, wait, sign, return); time-to-acceptance survival model for offers at different fees.
**Input data:** Order history (loan type, lender, page count, document arrival time, appointment time and location), agent history (completions, redraws, cancellations, response times), drive times at appointment hour, offer fees and acceptance times, payer days-to-pay.
**Target:** Clean completion flag; total agent minutes; time-to-fill at a given fee.
**Evaluation metric:** Redraw and no-show rate per hundred orders on the assigned agent versus current practice, in an A/B test; calibration of completion probabilities; mean absolute error on agent minutes. Fairness check: new agents must still receive enough orders to build history, so measure exploration share explicitly.
**Scope:** Standard tabular modelling with an operations-research assignment step. 1 data scientist and 1 engineer, 3-4 months on a signing service's history; harder for an individual agent, who would need pooled data.
**Data availability:** Signing services and marketplaces hold the order and outcome data; agents hold their own mileage and payment records.

---

## 5. State Notarial Rule Engine With Language-Model Certificate Review
#large-language-models #bert #decision-trees #evaluation-metrics #compliance #automation

**Problem statement:** Given the notary's commission state, the act type, the signer's location and the document's destination, determine the required journal fields, permissible identity evidence, thumbprint trigger, certificate wording and recording-retention rule, and review a drafted or completed certificate for defects.

**ML task:** A maintained rule base (decision logic per state and act) for deterministic requirements, plus language-model classification of certificate text against the applicable state form and extraction of statutory changes from new legislation and Secretary of State guidance into rule updates for human approval.
**Input data:** State notary statutes, administrative rules and handbooks; certificate forms; historical recorder rejections citing notarial defects; journal entries.
**Target:** Requirement set per act; certificate valid / defective with the defect named; proposed rule changes with citations.
**Evaluation metric:** Accuracy against a gold set of certificates reviewed by notary-law specialists, with recall on defective certificates prioritised because a defect surfaces at recording or in litigation; for rule extraction, the share of proposed updates accepted by the reviewer without edits.
**Scope:** The rule base is the asset and the cost: 50 states, several act types, frequent amendments. 1 engineer and 1 notary-law researcher, 4-6 months to cover the 15 highest-volume states, then continuous maintenance.
**Data availability:** Statutes and handbooks are public; recorder rejection reasons are held by eRecording vendors and title companies and are rarely structured.
