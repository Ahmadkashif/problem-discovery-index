# Machine Learning Opportunities — Property & Casualty Insurers

**Industry:** [[property-casualty-insurers|Property & Casualty Insurers]]
**Derived from:** [[problems/property-casualty-insurers/high-impact|High Impact]], [[problems/property-casualty-insurers/low-impact-1|Low Impact 1]], [[problems/property-casualty-insurers/low-impact-2|Low Impact 2]], [[problems/property-casualty-insurers/worker-life-1|Worker Life 1]], [[problems/property-casualty-insurers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Adjuster's Escalation Read
#tacit-knowledge-ml #transformers #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Experienced bodily injury adjusters can tell within days of first notice which liability claims will draw an attorney, build up treatment and end in a policy-limits demand, a judgement they cannot write down and that leaves when they retire. The ML problem is to learn that read from file text, early structured signals and senior adjusters' own annotations, and surface it to every adjuster before the letter of representation arrives.

**ML task:** Early-warning classification of attorney representation and limits-demand risk at day 3, 10 and 30, plus time-to-event modelling of escalation and a calibrated ultimate-severity range
**Input data:** First notice of loss text, adjuster file notes, recorded-statement transcripts, police reports, first medical bills and provider identities, venue and plaintiff-firm history, claimant contact patterns, prior claims for the same parties, and senior adjusters' structured reads captured during handling.
**Target:** Representation within 90 days; limits demand; suit; ultimate paid indemnity and expense at closure; agreement with senior adjusters' reads.
**Evaluation metric:** Recall of eventually escalating claims at a fixed review capacity (the top 5–10% of new claims an early-resolution unit can work, estimate), with Brier score and calibration of the representation probability measured strictly out of time. A missed escalation costs a severity jump; a false alarm costs a specialist's call. The read model is also scored against senior adjusters' test-retest agreement, which sets its ceiling.
**Scope:** The data collection challenge comes first. The expert's read has to be captured as the adjuster forms it, through a confirm-or-correct prompt drafted from the file in seconds, because historical reserves record a number, not the suspicion behind it. The labelling challenge is that outcomes arrive years later and are changed by the handling: a claim correctly flagged and settled early never shows its escalation, so labels need intervention-aware treatment, and repeated annotation of a sample is needed to measure how far adjusters disagree with themselves. The deployment challenge is speed: the score must arrive in the first days, inside the claims system, faster than the adjuster's own instinct and with reasons in claims vocabulary, or it will be ignored. 2 ML engineers, 1 claims data scientist and a senior claims lead, 9–12 months, delivering value first as retrieval of similar closed claims before any score drives triage.
**Data availability:** Carriers hold years of closed liability claims with notes and outcomes in their own systems. The decisive asset, adjusters' early reads in structured form, does not exist and must be built prospectively. Defence-counsel material after suit carries privilege and should be excluded from training.

---

## 2. Individual Claim Reserving From Case Facts to Ultimate
#survival-analysis #gradient-boosting #bayesian-inference #monte-carlo-methods #confidence-intervals #evaluation-metrics #revenue-impact

**Problem statement:** Aggregate triangle methods cannot see that a jump in incurred losses comes from a change in case-reserving practice rather than in losses. Estimate each open claim's ultimate cost from its own facts and history, and aggregate to reserve indications that the reserving actuary can compare with chain-ladder and Bornhuetter–Ferguson.

**ML task:** Claim-level ultimate severity and closure-time modelling (micro-level reserving) with simulation to an aggregate reserve distribution
**Input data:** Claim-level transaction histories (payments, reserve changes, reopenings), claim characteristics, adjuster and office identifiers, litigation status, and the case-reserve adequacy history of each office.
**Target:** Ultimate paid on each claim; time to closure; aggregate unpaid by line and accident year with a distribution.
**Evaluation metric:** Out-of-time error of aggregate unpaid indications against later actual development, compared with triangle methods on the same data; coverage of the stated reserve range. A reserve indication that is precise but biased low is the costly failure, so bias by accident year is reported first.
**Scope:** A reserving team's companion, not a replacement. The actuary still selects. 1 actuary-data scientist pair, 6 months to a first line of business, with commercial auto and other liability first because that is where development is adverse.
**Data availability:** Internal and complete at claim level at most carriers, though system migrations break histories. Ultimates for recent accident years are unknown, so validation must use older years.

---

## 3. Subrogation Opportunity Detection at First Notice
#bert #logistic-regression #feature-engineering #evaluation-metrics #automation #workflow-orchestration #revenue-impact

**Problem statement:** Classify every new property and auto claim for third-party recovery potential at first notice, from the loss description, police report and photos, and route it with the governing state's fault rules and deadlines attached.

**ML task:** Text classification of recovery potential and recovery type (third-party driver, product, contractor, landlord or tenant), plus a recovery-amount regression for prioritisation
**Input data:** FNOL narratives, adjuster notes, police reports, photos, policy and contract documents (waivers of subrogation), state fault and limitation rules, and historical recovery outcomes.
**Target:** Whether a recovery was later achieved or would have been on review, the recovery type, and the net recovered amount.
**Evaluation metric:** Recall on recoverable claims at a review budget, measured against a recovery vendor's later review of closed files, which is the best available record of what was missed; net recovered dollars per reviewed claim.
**Scope:** Labels are biased toward the recoveries adjusters already notice, so a sample of closed files needs independent review to label the misses. 1 ML engineer and 1 recovery specialist, 4 months.
**Data availability:** Internal claim files and recovery-unit records; contingency recovery vendors hold the best record of what carriers miss.

---

## 4. Time-Limited Demand Extraction From Correspondence
#large-language-models #transformers #seq2seq #evaluation-metrics #compliance #workflow-orchestration #worker-facing

**Problem statement:** Detect policy-limits and other time-limited settlement demands in incoming correspondence and extract the deadline, the conditions and the governing state's statutory requirements into a structured checklist on the claim.

**ML task:** Document classification plus structured extraction (deadline, amount, conditions, required release language, payment form) with state-rule lookup
**Input data:** Scanned and emailed letters from plaintiff firms, medical records packages, claim metadata, and state time-limited demand statutes.
**Target:** Demand yes/no; extracted fields with source spans; computed true response deadline.
**Evaluation metric:** Recall on time-limited demands must approach 100%, because a missed demand is a bad-faith exposure while a false positive costs a minute of reading. Field-level exact-match accuracy on deadlines and conditions, with every extraction linked to its source text.
**Scope:** Modest modelling, careful product: the model triages and drafts, and the adjuster confirms. 1 ML engineer, 1 claims-legal subject-matter lead, 3–4 months to a first line.
**Data availability:** Carriers hold years of correspondence in claim files; labels need a few thousand annotated letters (estimate), drawn first from known demand files.

---

## 5. Unfair-Discrimination Testing of Rating and Claims Models
#causal-inference #hypothesis-testing #bayesian-inference #logistic-regression #confidence-intervals #compliance

**Problem statement:** Test rating variables, external data and claims models for disproportionate effects on protected classes when insurers do not collect race or ethnicity, as regulators following the NAIC's 2023 AI model bulletin increasingly ask.

**ML task:** Protected-class inference with probabilistic proxies (surname-and-geography methods), disparity estimation with uncertainty, and attribution of disparity to individual rating variables
**Input data:** Policy and quote data with rating variables, external data scores, claims decisions, geocoded addresses and surnames, and census reference distributions.
**Target:** Estimated outcome rates by inferred class with confidence intervals; each variable's contribution to measured disparity.
**Evaluation metric:** Calibration of the proxy against a sample with self-reported data where available, and stability of disparity estimates across proxy methods. False reassurance is worse than a flagged variable that turns out benign, because the regulator will run its own test.
**Scope:** Statistically subtle and legally sensitive: results must be documented for a regulator and interpreted with counsel. 1 statistician and 1 pricing actuary, 4–6 months per rating plan.
**Data availability:** Internal rating data and public census tables; little ground truth on protected classes, which is the core methodological difficulty.
