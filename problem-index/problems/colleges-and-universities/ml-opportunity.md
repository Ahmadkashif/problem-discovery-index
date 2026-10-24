# Machine Learning Opportunities — Colleges & Universities

**Industry:** [[colleges-and-universities|Colleges & Universities]]
**Derived from:** [[problems/colleges-and-universities/high-impact|High Impact]], [[problems/colleges-and-universities/low-impact-1|Low Impact 1]], [[problems/colleges-and-universities/low-impact-2|Low Impact 2]], [[problems/colleges-and-universities/worker-life-1|Worker Life 1]], [[problems/colleges-and-universities/worker-life-2|Worker Life 2]]

---

## 1. Learning the Aid Director's Read of Price Sensitivity
#tacit-knowledge-ml #causal-inference #gradient-boosting #large-language-models #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced financial aid directors read an admitted student's file, appeal letter and competitor offer and "know" whether more grant aid will change the enrollment decision. The judgement is formed over thousands of cases, is never recorded, and drives most of a private college's discount. The ML problem is to estimate, per admitted student, how much each additional institutional grant dollar changes the probability of deposit, fall enrollment and second-year retention, and to show the director the past cases that justify the estimate.

**ML task:** Heterogeneous treatment-effect (uplift) estimation of institutional grant on enrollment and retention, plus language-model extraction of appeal triggers (competitor offer amount, income change, special circumstance) from appeal letters and call notes
**Input data:** Five or more years of admit records with academic rating, need, residency, visit and engagement history; leveraging-grid cell and the original and final award; appeal texts and competitor award letters; deposit, melt, enrollment, retention and graduation outcomes; policy changes in the grid from year to year.
**Target:** Expected change in enrollment probability per $1,000 of additional grant, with an interval; a structured appeal record; and the director's own prior estimate where the ledger captures it.
**Evaluation metric:** Out-of-year uplift calibration measured with Qini or AUUC on a held-out admission cycle, never random splits, because yield behaviour shifts every year. The money metric is simulated net tuition revenue at fixed class size against the existing grid. Asymmetric costs: overestimating uplift wastes aid, but underestimating it loses students the college needed, and a lost student costs four years of net tuition.
**Scope:** The data collection challenge comes first: the director's read must be captured while appeals are decided in April, so the system must draft a one-click record of the decision, the reason and the director's probability estimate from the letter and the call. History holds only before-and-after award amounts. The labelling challenge is that enrollment is a confounded label: grids assign more aid to some students by rule. Identification has to lean on grid thresholds (regression-discontinuity style comparisons), policy changes between years and the director's discretionary variation, with intra-rater consistency measured on repeated anonymised cases. The deployment challenge is speed: the estimate and the five nearest past cases must appear in the aid system during the appeal call, faster than the director's recall. 1 ML engineer, 1 data scientist with causal-inference experience and an aid office partner, 6–9 months; the first deliverable is the ledger and nearest-case retrieval, the uplift model second.
**Data availability:** Each institution holds its own admit, aid and outcome records and may use them freely for its own purposes. Cross-campus training data sits with enrolment consultancies. Enrolled students' retention and graduation outcomes are FERPA records whose reuse is limited to the disclosing institution's purposes (34 CFR 99.33(a)(2)); applicant and admit records of people who never enrolled rest on contract terms that are not public. A multi-campus model therefore needs checked contract rights or de-identification. A public-data MVP can use College Scorecard and IPEDS net price by income band to build the grid-level demo, with synthetic admit files for the appeal workflow.

---

## 2. Stop-Out Risk Ranked to Advisor Capacity
#survival-analysis #gradient-boosting #logistic-regression #evaluation-metrics #feature-engineering #worker-facing

**Problem statement:** Rank each advisor's students by the hazard of not re-enrolling next term, explain each ranking in terms the advisor can act on, and cap the weekly list at what one advisor can work.

**ML task:** Discrete-time survival model of term-to-term stop-out with gradient-boosted hazard estimates and per-student feature attributions
**Input data:** SIS enrollment and registration history, holds and their type, financial aid status including satisfactory academic progress and unmet need, LMS login and submission activity by week, early-alert flags and faculty comments, advising notes, grades at midterm, housing and meal plan status.
**Target:** Hazard of not enrolling at the next term's census date; time to stop-out; reason codes drawn from the top contributing features.
**Evaluation metric:** Precision at advisor capacity (of the top 30 students on each list, how many would have stopped out) and calibration by term, evaluated on a later term than training. A missed student who stops out costs years of tuition and a degree; an unnecessary call costs fifteen minutes. Report subgroup calibration, because a model that systematically under-ranks first-generation or transfer students repeats the inequity it should fix.
**Scope:** Most institutions already have the data in their SIS and LMS; the work is joining weekly LMS activity to term outcomes and building the explanation layer. Commercial risk scores exist (EAB, Civitas, Stellic) but rank all students rather than an advisor's workable list and rarely say why. 1 data scientist and 1 engineer, 4 months for one institution.
**Data availability:** Held by each institution, usable internally under FERPA. Vendors may hold multi-campus data only under the school-official exception, which limits reuse. For an MVP, IPEDS retention and graduation rates by institution give the benchmark and synthetic student-term records stand in for real ones.

---

## 3. Transfer Course Equivalency Matching
#transformers #word-embeddings #k-nearest-neighbors #large-language-models #evaluation-metrics #automation

**Problem statement:** Given a course on an incoming transcript (sending institution, course code, title, credits, and the catalogue description for the year taken), propose the receiving institution's equivalent course or elective category and the degree requirement it satisfies, with the precedent evaluations that support it.

**ML task:** Semantic retrieval and ranking of candidate equivalents over catalogue descriptions, followed by a classifier for direct-equivalent, departmental-elective or no-credit, conditioned on the receiving institution's historic decisions
**Input data:** The receiving institution's equivalency table (often tens of thousands of past decisions), catalogue descriptions and learning outcomes from sending institutions by catalogue year, transcripts (PDF or EDI), articulation agreements, faculty reviewer decisions and reasons.
**Target:** Ranked candidate equivalents with confidence; requirement applicability; route to faculty review when confidence is low.
**Evaluation metric:** Top-1 and top-3 agreement with faculty reviewer decisions on held-out transcripts, plus the share of courses auto-posted at a confidence threshold where agreement exceeds 98%. A false equivalency that lets a student skip a prerequisite is costlier than a referral to faculty, so precision at the auto-post threshold is the binding metric.
**Scope:** Equivalency tables give strong supervision for frequent sending institutions; the long tail of out-of-state and older catalogues is where description matching earns its keep. Transcript OCR and catalogue-year alignment are most of the engineering. 2 engineers, 4–5 months.
**Data availability:** Equivalency tables and catalogues are institutional and largely public (many tables are published for students); transcripts are FERPA records held by the receiving institution. GAO-17-574's estimate that transfer students lost 43% of their credits sets the stakes.

---

## 4. Award Notice Parsing and Policy-Change Impact
#large-language-models #bert #transformers #evaluation-metrics #compliance #data-integration

**Problem statement:** Parse every active federal notice of award into its operative terms, map each agency policy announcement to the clauses it changes, and list the affected awards with the costs at risk.

**ML task:** Clause segmentation and term extraction from award documents, plus classification linking policy notices to affected terms and awards
**Input data:** Notices of award and amendments, agency general terms and conditions, grants policy statements, negotiated F&A rate agreements, agency announcements and guide notices, award financial data from the ERP grants module.
**Target:** Structured award records (budget period, F&A base and rate, restrictions, prior approvals, special conditions); for each announcement, the affected awards with a cost-at-risk estimate and required actions.
**Evaluation metric:** Field-level extraction accuracy against post-award staff abstraction; recall of affected awards on past policy events (the 2025 NIH indirect-cost notice and termination waves are natural test sets). Missing an affected award is a compliance exposure; a false positive costs a reviewer a few minutes.
**Scope:** Agency documents are semi-structured and repetitive within an agency, so extraction reaches high accuracy quickly for NIH and NSF; DOD and foundation awards are the tail. 1 ML engineer and 1 research administration lead, 4 months.
**Data availability:** Award documents are held by the university; agency terms and notices are public, as are award listings in NIH RePORTER, NSF's award search and USAspending, which support a public-data prototype.

---

## 5. Institutional Financial Distress Early Warning
#survival-analysis #gradient-boosting #logistic-regression #time-series-forecasting #evaluation-metrics #data-integration #quick-win

**Problem statement:** Estimate each four-year institution's probability of closure, merger or severe financial distress over a three-year horizon from public data, and explain which trends drive it.

**ML task:** Survival modelling of time to closure or merger, with gradient-boosted classifiers for downgrade and deficit events and enrollment forecasts as inputs
**Input data:** IPEDS enrollment, admissions, finance, staffing and retention series; College Scorecard net price, debt and earnings; Department of Education financial responsibility composite scores; WICHE graduate projections by state; continuing disclosures and audited statements on EMMA for rated issuers; closure and merger lists from public trackers.
**Target:** Closure or merger within three years; probability of operating deficit; enrollment trajectory.
**Evaluation metric:** Time-dependent concordance and Brier score on institutions held out by year, with recall at a fixed alert rate. Closures are rare (about one public or nonprofit college a month in 2025–26 by public tracker counts, search summary), so precision is judged at the top of the list, not overall.
**Scope:** The quickest credible MVP in this industry: every input is public, and the output is legible to boards, state agencies, lenders, rating analysts and vendors' sales teams. The hard part is the label: closures, mergers and acquisitions need careful dating and IPEDS reporting lags a year or more. 1 data scientist, 6–8 weeks to a working model.
**Data availability:** Fully public. IPEDS and College Scorecard files download freely; EMMA disclosures are free to read but need PDF extraction.
