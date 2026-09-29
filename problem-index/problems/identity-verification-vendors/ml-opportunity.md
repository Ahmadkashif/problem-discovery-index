# Machine Learning Opportunities — Identity Verification Vendors

**Industry:** [[identity-verification-vendors|Identity Verification Vendors]]
**Derived from:** [[problems/identity-verification-vendors/high-impact|High Impact]], [[problems/identity-verification-vendors/low-impact-1|Low Impact 1]], [[problems/identity-verification-vendors/low-impact-2|Low Impact 2]], [[problems/identity-verification-vendors/worker-life-1|Worker Life 1]], [[problems/identity-verification-vendors/worker-life-2|Worker Life 2]]

---

## 1. False Reject Measurement by Audit Panel and Recovery Instrumentation
#causal-inference #confidence-intervals #hypothesis-testing #gradient-boosting #cnns #evaluation-metrics #compliance #feature-engineering

**Problem statement:** A person who fails verification abandons and disappears, producing no outcome data, so the industry's most consequential error rate is estimated rather than measured. The failures are not uniformly distributed — NIST has documented demographic differentials in face matching, documents and devices vary in how well they capture, and database resolution skews toward thick files and stable addresses — and those skews compound in the same direction through an orchestration flow.

**ML task:** Direct false reject rate estimation from a consented, demographically documented audit panel, combined with full instrumentation of recovery paths as a second estimator
**Input data:** A recruited panel of genuine identities with documented demographics, document types and device classes, run through the live system periodically; every automated failure followed by manual review or an alternative path that confirmed the person genuine; failure cause decomposition; capture conditions; per-step abandonment.
**Target:** False reject rate stratified by demographic group, document type, device class and capture condition, with the contribution of each pipeline stage separated.
**Evaluation metric:** The deliverable is an interval, not an accuracy number, and its credibility rests entirely on the panel's construction — a panel that under-represents the populations most likely to fail measures nothing useful. Report per-stage attribution, because a face matching differential and a database resolution differential require different remedies and are currently invisible inside a single pass rate.
**Scope:** Recovery-path instrumentation costs nothing and is available today: every applicant who fails automatically and is later confirmed genuine is a confirmed false reject, and reporting those stratified by document, device and capture condition is a query rather than a research programme. The audit panel is the clean measurement and is a panel study, not a research programme — affordable, repeatable, and the only unbiased evidence obtainable. Biometric privacy law, BIPA especially, constrains retention of the images that would support deeper error analysis, which is a real tension and argues for a bounded consented panel rather than pervasive collection. 2 ML engineers, 1 researcher and a panel budget, 6 months.
**Data availability:** Recovery-path data exists and is unexploited. Demographic attributes do not exist in production data and should not be collected there; the consented panel is the appropriate vehicle.

---

## 2. Document Layout Generalisation and Revision Detection
#cnns #object-detection #semantic-segmentation #transfer-learning #bert #evaluation-metrics #feature-engineering #data-integration

**Problem statement:** Thousands of document types across hundreds of jurisdictions, each with layouts, security features and revision histories, are supported by a hand-maintained template library. Rare documents and older revisions fall to generic fallback logic, and a redesigned document silently starts failing until someone notices.

**ML task:** Layout-agnostic field extraction and security feature localisation generalising across unseen document types, with statistical detection of document revisions from production telemetry
**Input data:** Document images across all supported types with annotations; machine-readable zone and barcode contents as self-supervision; published document specifications; per-type failure rates and score distributions over time; capture device and condition metadata; genuine and known-fraudulent samples.
**Target:** Extracted fields and located security features on documents the system has not been trained on, and an alert when a document type's behaviour shifts.
**Evaluation metric:** Field accuracy on held-out document types never seen in training is the metric that matters, since performance on well-covered common documents is already adequate and is not where users fail. Report accuracy stratified by capture condition and device class rather than as a single number, because a headline figure averages over a device distribution that differs sharply between customer populations and hides exactly the failure being investigated.
**Scope:** Revision detection is nearly free and immediately valuable: a document type whose failure rate jumps has probably been redesigned, and that is visible in the vendor's own telemetry weeks before anyone reports it. Layout generalisation matters most precisely where templates fail — rare types, old revisions, small jurisdictions — which is where the people most harmed by coverage gaps carry their documents. Structured synthesis from published specifications is a legitimate way to bootstrap types whose genuine samples cannot lawfully be collected. 3 ML engineers, 7 months.
**Data availability:** Large annotated corpora exist inside vendors, heavily skewed toward common documents. Retention limits under biometric privacy law constrain what can be kept and for how long.

---

## 3. Personalised Verification Routing with Randomised Policy Comparison
#gradient-boosting #causal-inference #k-nearest-neighbors #confidence-intervals #hypothesis-testing #evaluation-metrics #workflow-orchestration #data-integration

**Problem statement:** Orchestration stacks several vendors behind static routing rules, every applicant walks the same decision tree, and each additional step loses genuine users disproportionately among people for whom that step is hardest. Vendor performance varies substantially by applicant segment and nobody measures it, despite orchestration layers holding exactly the data required.

**ML task:** Prediction of which verification path will succeed for a given applicant, plus randomised comparison of routing policies and per-segment vendor evaluation
**Input data:** Applicant signals available at the first step including device, geography, thin-file indicators and document availability; every path taken with per-step outcomes and abandonment; vendor sub-scores; confirmed fraud outcomes; manual review confirmations; randomised routing assignment arms.
**Target:** The path most likely to verify this applicant at acceptable fraud risk, and per-vendor accuracy by segment.
**Evaluation metric:** Genuine applicants verified per hundred started, not pass rate — pass rate improves when the hardest applicants abandon earlier, which is the opposite of the goal. Fraud rate is the paired guardrail. Policy comparison requires randomised assignment; comparing flow changes on aggregate pass rate conflates the policy with whoever happened to apply that month, which is how most such changes are currently judged.
**Scope:** Per-segment vendor measurement is the single most valuable analysis an orchestration platform could run and is essentially unexploited, even though the platform sends the same applicant population to different vendors with outcomes attached. Attributing abandonment to specific steps by population turns flow design from a cost-per-check exercise into a genuine-applicants-lost one. Randomised routing is straightforward for an orchestration layer to operate and almost nobody does it. 2 ML engineers, 5 months.
**Data availability:** Complete inside orchestration platforms. The vendors themselves hold only their own slice, which is why the orchestration layer is the right place for this work.

---

## 4. Review Assistance and Decision Explanation
#cnns #object-detection #large-language-models #k-nearest-neighbors #bert #evaluation-metrics #worker-facing #automation

**Problem statement:** Reviewers judge authenticity from glare-covered, folded, thermally faded photographs of documents they may never have seen, comparing faces across age and lighting in under a minute, with no feedback ever. Separately, solutions engineers reconstruct by hand why a specific real person was rejected, from sub-scores that were never designed to be explained.

**ML task:** Image enhancement and security feature localisation for review, similar-case retrieval across document types and failure patterns, and generation of decision explanations from the actual pipeline path
**Input data:** Document images and capture metadata; genuine specimen references per type and revision; automated check results with sub-scores and thresholds; historical review cases with decisions and any confirmed outcomes; escalation records and their resolutions; the decision path taken per applicant.
**Target:** An enhanced, annotated document view with findings; ranked similar prior cases; and a legible account of why a given applicant failed and what would have changed it.
**Evaluation metric:** For review assistance, reviewer accuracy on a held-out set with known ground truth, and time per case as a secondary measure — accuracy first, because this role currently has no calibration signal at all. For explanations, whether a solutions engineer accepts the generated account without rewriting it, and whether the applicant-facing guidance derived from it actually leads to a successful retry, which is the only outcome that matters to the person who failed.
**Scope:** Image enhancement — glare reduction, perspective correction, contrast normalisation, super-resolution — is mature technology that would materially change what a reviewer can see and is not routinely applied in review interfaces. Applicant-facing guidance at the moment of failure, specific to what actually failed, converts a large share of rejections into successful retakes and disproportionately helps people on older devices. Face match scores should be presented alongside human judgement with their documented limitations stated, since both fail and they do not fail in the same way. 2 ML engineers, 5 months.
**Data availability:** Review cases and escalations are retained. Ground truth is scarce, which makes the audit panel from the first opportunity the natural evaluation set for this one too.
