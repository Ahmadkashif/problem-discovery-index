# Machine Learning Opportunities — Payroll Platforms

**Industry:** [[payroll-platforms|Payroll Platforms]]
**Derived from:** [[problems/payroll-platforms/high-impact|High Impact]], [[problems/payroll-platforms/low-impact-1|Low Impact 1]], [[problems/payroll-platforms/low-impact-2|Low Impact 2]], [[problems/payroll-platforms/worker-life-1|Worker Life 1]], [[problems/payroll-platforms/worker-life-2|Worker Life 2]]

---

## 1. Tax Rate Change Detection and Pre-Disbursement Anomaly Verification
#change-point-detection #large-language-models #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #compliance #revenue-impact

**Problem statement:** More than eleven thousand US taxing jurisdictions publish rate and rule changes as PDFs, web updates and mailed notices, and payroll providers maintain them by staffing research teams to read. Calculations are checked against the provider's own rate tables, so a wrong table produces confidently wrong withholding across every affected employee until an agency notice arrives months later.

**ML task:** Change detection over crawled agency publications with structured rate extraction, plus population-level anomaly detection on computed withholding before funding
**Input data:** Agency bulletins, municipal code, rate schedules and filing instructions, crawled and versioned; current rate tables; computed withholding per employee per period across the provider's base, with jurisdiction, wage band and employer attributes.
**Target:** A detected rate or rule change with effective date and structured values; and separately, a withholding computation that diverges from the expected distribution for comparable employees in the same jurisdiction.
**Evaluation metric:** For detection, recall against known changes with lead time before the effective date — a change caught after it takes effect has already produced errors. For anomaly verification, precision at a very high threshold, since a false alarm halting a payroll run is itself a serious failure, balanced against recall on injected synthetic rate errors, which is the honest way to measure a detector for events that are rare and catastrophic.
**Scope:** The anomaly check is the more important half and is architecturally simple: a rate table error shows up as a population-wide shift in seconds, and nothing looks. Employer-specific inputs — unemployment rate notices and deposit schedules that arrive by mail — need document capture rather than crawling, and are where a large share of errors originate. 3 ML engineers plus tax research analysts, 6 months.
**Data availability:** Agency publication is public and wildly heterogeneous, with some local jurisdictions effectively unpublished. Internal withholding computations across tens of millions of employees are complete and are the strongest asset here.

---

## 2. Wage and Hour Configuration Verification
#hypothesis-testing #monte-carlo-methods #descriptive-statistics #confidence-intervals #large-language-models #evaluation-metrics #compliance

**Problem statement:** Regular rate of pay, overtime thresholds, break premiums and differential inclusion are configured by an employer's administrator from a settings page. Errors — most commonly excluding a non-discretionary bonus from the regular rate — underpay overtime invisibly for years and surface in litigation.

**ML task:** Differential testing between configured pay rules and the statutory calculation across generated scenarios, plus cross-employer anomaly detection on realised pay patterns
**Input data:** Configured earnings and overtime rules per employer; statutory rules by jurisdiction in structured form; historical timesheets and pay results; cross-employer distributions of overtime share, break premium rate and differential usage by industry and state.
**Target:** Divergence between configured and statutory outcomes on a generated scenario; and outlier employers on realised pay ratios.
**Evaluation metric:** Scenario coverage across rule interactions rather than marginals, since errors hide in combinations — a bonus in a week with a missed break and a shift differential is where the calculation actually breaks. For anomaly detection, precision on flagged employers as judged by a wage and hour specialist review.
**Scope:** Encoding the statutory calculation per jurisdiction is the substantial work and is a legal-engineering task rather than a modelling one. Monte Carlo scenario generation over schedule and earnings patterns is the mechanism. The output goes to the employer as a compliance finding, which requires care in framing since it is effectively telling a customer they may have been underpaying staff. 2 ML engineers plus employment counsel, 5-6 months.
**Data availability:** Complete internally. Cross-employer comparison is the provider's unique asset and is unused for this purpose.

---

## 3. Garnishment Order Extraction and Withholding Verification
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance

**Problem statement:** Garnishment orders other than standardised child support forms arrive as free-form court documents and are read by human processors. Priority sequencing across multiple concurrent orders, disposable earnings definitions and state exemption limits are where errors concentrate, and an over-withholding error takes money from an employee already in financial difficulty.

**ML task:** Document extraction of order type, amount, payee, effective date, duration and issuing authority, followed by rule-based priority and exemption computation with verification
**Input data:** Garnishment orders across types, courts and states; historical processor-entered order records as labels; federal CCPA limits and state exemption tables; employee earnings and existing order stack; remittance records.
**Target:** Structured order fields as confirmed by a processor, and the correct withholding amount under the applicable priority and exemption rules.
**Evaluation metric:** Field-level accuracy weighted toward amount, type and effective date. For the withholding computation, verification against an independently implemented rule engine, with over-withholding treated as the severe error class since the harm falls on the employee and is slow to unwind.
**Scope:** The extraction is a moderate document task; the priority and exemption logic is the part that is currently inconsistent across providers and is a rules problem requiring legal review per state. Employees with multiple concurrent orders are simultaneously the hardest case and the population most harmed by error, and should be the design centre rather than an edge case. 2 ML engineers plus a garnishment compliance specialist, 4-5 months.
**Data availability:** Providers hold large volumes of orders paired with processor-entered records. Orders contain sensitive personal information and require careful handling and access control in any training pipeline.

---

## 4. Pay Run Exception Detection Against Individual Baselines
#change-point-detection #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #automation #worker-facing

**Problem statement:** Payroll specialists hunt for exceptions on the afternoon of the funding deadline by scanning a preview register. Everything they find — implausible hours, missing tax setup, terminated employees with hours, rate changes without effective dates, unapproved timesheets — was detectable days earlier as the data arrived.

**ML task:** Per-employee anomaly detection against their own history, combined with completeness checks and approval-risk prediction
**Input data:** Timesheet entries as they arrive; employee pay history and hour patterns; employment status and effective-dated changes; tax setup completeness; manager approval history and latency; bank account validation status; employer funding balance history.
**Target:** Exceptions that a specialist ultimately acted on, derived from corrections made between preview and final register.
**Evaluation metric:** Detection lead time in days before the funding deadline, and precision per exception type — a specialist chasing a false flag loses the time the system was supposed to save. Baseline against the specialist's own catch rate at preview, which is the fair comparison.
**Scope:** Individual baselining is what makes this work; a fixed hour threshold flags every part-time employee and misses the salaried one whose hours doubled. Approval-risk prediction — which managers will be late, based on their own history — allows escalation to start before the manager is late rather than after. Population-level pre-funding verification is a separate and higher-stakes check that belongs in the same pipeline. 2 ML engineers, 4 months.
**Data availability:** Complete and high frequency. Corrections between preview and final are the natural label and are recorded in audit logs that are rarely mined.
