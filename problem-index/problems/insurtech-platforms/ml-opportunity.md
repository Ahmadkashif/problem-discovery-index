# Machine Learning Opportunities — Insurtech Platforms

**Industry:** [[insurtech-platforms|Insurtech Platforms]]
**Derived from:** [[problems/insurtech-platforms/high-impact|High Impact]], [[problems/insurtech-platforms/low-impact-1|Low Impact 1]], [[problems/insurtech-platforms/low-impact-2|Low Impact 2]], [[problems/insurtech-platforms/worker-life-1|Worker Life 1]], [[problems/insurtech-platforms/worker-life-2|Worker Life 2]]

---

## 1. Loss Run Parsing Across Carrier Formats
#large-language-models #bert #transformers #word-embeddings #transfer-learning #feature-engineering #evaluation-metrics

**Problem statement:** The loss run is the most determinative document in a commercial submission, arrives as a PDF in whichever format the expiring carrier uses, and there are hundreds of formats. It is keyed by hand, claim by claim, year by year, and an underwriting decision rests on the result.

**ML task:** Document layout analysis and structured extraction — claims with date of loss, description, cause, paid indemnity, paid expense, reserves and status, grouped by policy period and carrier
**Input data:** Loss run PDFs across carriers and formats, both native and scanned; the keyed values that assistants eventually entered, as labelled pairs; policy period metadata; carrier identity.
**Target:** The structured claim table as entered and verified.
**Evaluation metric:** Field-level exact match weighted by consequence — paid and reserved amounts and dates of loss carry far more weight than claim descriptions. Report the rate of silent errors separately from the rate of low-confidence flags, because a confidently wrong reserve figure changes an underwriting decision while a flagged uncertain one costs a glance.
**Scope:** Multi-carrier experience periods and mid-term carrier changes produce documents that must be reconciled rather than parsed independently, which is the part generic document AI handles worst. Reserve development across successive loss runs for the same account is a second-order extraction that is enormously valuable and never captured. 2-3 ML engineers plus an underwriting operations lead, 5-6 months.
**Data availability:** Very strong — every carrier and every agency holds years of loss runs paired with the values keyed from them. The labels are the keyed entries, which contain human transcription errors and therefore set a realistic ceiling that should be measured rather than assumed.

---

## 2. Submission Bind Probability and Appetite Triage
#gradient-boosting #logistic-regression #bert #feature-engineering #cross-validation #evaluation-metrics #confidence-intervals #revenue-impact

**Problem statement:** Carriers receive far more submissions than they can quote and decline most of them after the transcription work has already been done. Triage requires predicting whether a submission will be quoted and bound, and the carrier's real appetite is not what its appetite guide says — it is what its underwriters have actually written.

**ML task:** Sequential binary classification — quote or decline, then bind or lose — with calibrated probabilities used to rank the intake queue
**Input data:** Extracted submission attributes (class code, geography, size, coverage requested, limits, loss history summary); broker identity and their historical hit ratio with this carrier; the carrier's own history of quoted, declined and bound submissions with outcomes; incumbent carrier and expiring premium where disclosed; submission timing relative to effective date.
**Target:** Quote issued, and separately bound, with the recorded decline reason where present.
**Evaluation metric:** Ranking quality on the intake queue — what fraction of eventual binds appear in the top decile — rather than raw classification accuracy. Calibration matters because the score drives a resource allocation decision. Monitor deliberately for the failure mode where the model learns to reproduce historical underwriting patterns that ought to be examined rather than automated.
**Scope:** The fairness dimension needs explicit attention rather than a footnote. A model trained on historical underwriting decisions inherits whatever was in them, and in insurance the regulatory scrutiny of proxy discrimination is real and increasing. The defensible design triages workload rather than making or recommending the underwriting decision itself, and that distinction should be architectural rather than a policy statement. 2-3 ML engineers plus underwriting and compliance, 5-6 months.
**Data availability:** Complete inside the carrier's core system and rarely assembled as a dataset — submissions, declines, quotes, binds and subsequent losses live in different subsystems. Decline reasons come from a short code list that rarely captures the real reason, which limits diagnosis.

---

## 3. Filed Rate Manual Extraction and Configuration Verification
#large-language-models #bert #transformers #word-embeddings #monte-carlo-methods #evaluation-metrics #compliance

**Problem statement:** A filed rate must be translated into rating engine configuration by hand, fifty times with state variations, and configuration errors produce premiums that do not match the filed rate — a regulatory exposure typically discovered in a market conduct examination years later.

**ML task:** Table and algorithm extraction from filed rate manuals, plus automated differential testing between the extracted algorithm and the deployed configuration
**Input data:** Filed rate manuals and rule pages with factor tables, territory definitions, classification rules and rating algorithms; existing rating engine configurations; historical rated policies with their premium components; state-specific filing requirements and objections.
**Target:** A structured rating algorithm and factor set; and for verification, agreement between the configuration's computed premium and the filed algorithm's across generated scenarios.
**Evaluation metric:** For extraction, exact match on factor tables (high baseline, structurally clean) reported separately from algorithm structure accuracy (the hard part, where errors concentrate). For verification, the divergence rate across a scenario space sampled to cover parameter interactions, not just marginals — errors hide in interactions.
**Scope:** The verification half is more valuable than the extraction half and can be built first using only the manual as a reference implementation. Monte Carlo scenario generation across the rating parameter space is the mechanism, and coverage of interaction terms is what distinguishes it from the spot checks carriers currently do. 2 ML engineers plus an actuarial analyst, 5 months.
**Data availability:** Filed manuals are public through SERFF and internally held. Rating configurations are proprietary and structured. Historical rated policies provide a large natural test set that no carrier currently uses for systematic verification.

---

## 4. Certificate Requirement Extraction and Policy Verification
#large-language-models #bert #transformers #word-embeddings #evaluation-metrics #transfer-learning #compliance

**Problem statement:** Certificates are issued at enormous volume, generate no revenue, and carry professional liability when they represent coverage the policy does not provide. Verification requires comparing requested wording against the policy's endorsement schedule and is universally manual, so it is skipped under volume.

**ML task:** Requirement extraction from contracts, emails and portal specifications, plus semantic comparison against policy endorsement schedules
**Input data:** Contract insurance requirement clauses, certificate request emails and portal specifications; policy declarations and endorsement schedules; historical certificates issued with the underlying policies; endorsement form numbers and their standard wordings.
**Target:** A structured requirement set (limits, additional insured status, waiver of subrogation, primary and non-contributory, notice provisions); and a verified determination of whether the policy supports each element.
**Evaluation metric:** Recall on requirements is critical — a missed requirement produces a certificate that fails the holder's review and returns as rework — while precision on the verification determination is what protects against the liability. Report the two separately, and treat a false "policy supports this" as the severe error class.
**Scope:** Endorsement form numbers make verification far more tractable than it first appears, since standard forms have known effects; manuscript endorsements are the residual and should always route to a human. The renewal cascade — reissuing every certificate when the underlying policy renews — needs no models and removes a seasonal labour spike. 2 ML engineers plus a commercial lines expert, 4-5 months.
**Data availability:** Agencies hold certificates, policies and endorsement schedules together, which is an unusually complete corpus. Contract requirement language often never reaches the agency at all, arriving as a paraphrase from the client, which is a workflow gap rather than a data one.
