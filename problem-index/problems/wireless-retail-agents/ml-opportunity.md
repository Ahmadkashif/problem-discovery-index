# Machine Learning Opportunities — Wireless Retail Agents

**Industry:** [[wireless-retail-agents|Wireless Retail Agents]]
**Derived from:** [[problems/wireless-retail-agents/high-impact|High Impact]], [[problems/wireless-retail-agents/low-impact-1|Low Impact 1]], [[problems/wireless-retail-agents/low-impact-2|Low Impact 2]], [[problems/wireless-retail-agents/worker-life-1|Worker Life 1]], [[problems/wireless-retail-agents/worker-life-2|Worker Life 2]]

---

## 1. Learning the Manager's Read of a Deal That Won't Stick
#tacit-knowledge-ml #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact #worker-facing

**Problem statement:** Veteran store and district managers sense, at the counter, which activations will cancel, go unpaid, never recharge or prove fraudulent before the carrier's chargeback window closes. They can't write the rule down, and new reps don't have it. The ML problem is to learn that read from the dealer's own activation history, the managers' recorded confidence calls and the chargeback outcomes that arrive months later, and to return it at the counter as an action on the deal.

**ML task:** Competing-risks time-to-event modelling (time to chargeback by cause: early cancellation or port-out, non-pay, fraud, never-recharged, feature removal) plus a calibrated probability that the line's commission survives the window, with a per-deal explanation
**Input data:** POS activation records (deal type, line count, device models and financing, plan, promotion, port-in source and tenure, trade-in model against account model, payment method, time of day, rep and store, rep tenure); the dealer's carrier commission and chargeback statements joined by line number, IMEI or order number; managers' and reps' quick confidence calls with reason chips captured during the flow; store-level history of fraud cases and inventory transfers.
**Target:** Time to chargeback and its cause, censored at the end of the window; the manager's confidence call as a secondary target for agreement measurement.
**Evaluation metric:** Time-dependent concordance and calibration of the survival probability at the window end, measured out of time on later months, because comp plans and promotions drift. For fraud, recall at a fixed step-up rate (e.g., the top 3% of deals sent for extra ID checks): a missed fraud ring costs devices and commission, while a needless step-up costs two minutes and some goodwill. Report model-to-manager agreement against the managers' own test-retest agreement as the ceiling, and audit every output for disparate impact across neighbourhoods and proxies for protected characteristics.
**Scope:** The data-collection challenge comes first: the expert's read has to be captured in the activation flow in under three seconds, or reps skip it, and declined deals must be logged too, or the model only ever learns from deals somebody believed in. The labelling challenge is that carrier reason codes are coarse and differ by carrier and month, a day-170 cancellation after a house move is not a fraud, and managers disagree with themselves after a recent loss, so a sample of deals needs repeated blind annotation to estimate agreement. The deployment challenge is that the flag must appear before the phone leaves the store, faster than the manager can walk over, and must recommend an action on the deal (step-up ID, fewer financed devices, a different promotion), never a refusal of service, since credit decisions belong to the carrier. 2 ML engineers, 1 data engineer for the statement join and an operations lead at one chain of 200+ stores, 6–9 months; value appears first as a district-level chargeback dashboard before any counter flag is trusted.
**Data availability:** Large chains hold years of POS history and carrier statements, but the join between them is usually done only for money and must be rebuilt. Customer-level data is the carrier's CPNI under the dealer agreement, so the model should run inside the dealer's systems on deal features, with carrier consent for any customer-level use. Manager annotations don't exist and must be collected prospectively.

---

## 2. Carrier Statement Parsing and Line Matching
#large-language-models #transformers #random-forests #feature-engineering #evaluation-metrics #data-integration #automation

**Problem statement:** Extract every line from carrier, master-agent and brand commission statements, whether CSV, portal export or PDF, into one schema, then match each to the POS transaction that earned it, even when identifiers changed through an exchange, port or SIM swap.

**ML task:** Document layout extraction into a canonical schema, followed by probabilistic record linkage with a learned match scorer
**Input data:** Twelve-plus months of statements per carrier and brand; POS transactions with line numbers, IMEIs, SIMs, order numbers, rep IDs and dates; device exchange and return logs; historical manual matches made by reconciliation staff.
**Target:** Structured statement lines (identifier, transaction type, amount, period, reason code); match or no-match per candidate pair, with confidence.
**Evaluation metric:** Field-level extraction accuracy on held-out statements from a format the model has not seen; precision and recall of auto-matches at the threshold where they post without review. False matches are worse than misses, because they hide a short payment, so precision at auto-post must be at or above 99%.
**Scope:** The extraction is commodity LLM work once a few examples per layout exist; the value is in surviving format changes without a developer. Matching is a classic linkage problem with good labels from past manual work. 1 ML engineer and 1 data engineer, 4 months for three carriers.
**Data availability:** Dealers hold all their statements and POS data. Historical manual matches exist in spreadsheets and need cleaning to become labels.

---

## 3. Comp Plan and Spiff Bulletin to Expected-Commission Rules
#large-language-models #seq2seq #decision-trees #evaluation-metrics #workflow-orchestration #automation

**Problem statement:** Turn each month's carrier compensation plan, spiff bulletins and promotion notices into executable rules that compute what every activation should have paid, so reconciliation can tell a correct payment from a short one and reps can see their expected commission at the time of sale.

**ML task:** Structured information extraction into a rule schema (eligibility conditions, SKUs, effective dates, amounts, tiers, chargeback conditions), with consistency checking against observed payments
**Input data:** Comp-plan PDFs and bulletins over several years; the rule tables back-office staff built by hand from them; statements showing what was actually paid.
**Target:** A versioned rule set per plan period; for each activation, expected commission and the rule that produced it.
**Evaluation metric:** Share of statement lines whose actual payment equals the rule-computed expected payment, on months held out from training. Unexplained differences are routed to review and, if they are real short payments, recovered. Rule-extraction errors that create false disputes cost credibility with the carrier, so precision on "short-paid" calls matters more than coverage.
**Scope:** Plans are long, change monthly and use carrier-specific jargon. Hand-built rule tables from past months provide supervision, and observed payments give a free check. 1 ML engineer plus a commission analyst, 4–5 months.
**Data availability:** Dealers receive the plans; past rule tables exist where a chain has a reconciliation team. Plans are confidential to the dealer–carrier relationship, so the system must run inside each dealer's environment.

---

## 4. Store Traffic, Visit Intent and Staffing Forecast
#time-series-forecasting #exponential-smoothing #temporal-fusion-transformers #gradient-boosting #evaluation-metrics #worker-facing

**Problem statement:** Forecast hourly store traffic split by intent (sales, service, bill pay) so stores are staffed for the selling hours and conversion is measured on buyers rather than everyone who walks in.

**ML task:** Hierarchical multi-horizon forecasting of store-hour traffic by visit type, with intent inferred from door counts, transaction logs and a short visit-reason intake
**Input data:** Door-counter data, POS transactions and service logs by hour; device launch dates and carrier promotion calendars; bill-due cycles; tax-refund season (a prepaid peak); outage reports; local events and weather.
**Target:** Visitors per store-hour by intent, with prediction intervals.
**Evaluation metric:** Weighted absolute percentage error at store-hour level, and interval coverage for the peak hours that drive staffing. Under-forecasting peaks costs sales and survey scores, so evaluate quantile loss at the upper quantiles.
**Scope:** Standard retail forecasting with an unusual intent label. The visit-reason intake supplies labels within weeks. 1 data scientist, 3 months.
**Data availability:** Chains hold counters and POS data. Intent labels are new and must be collected with the intake.

---

## 5. Trade-In Condition Grading at the Counter
#cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #automation

**Problem statement:** Grade a traded-in phone at the counter from photos the way the carrier's processing centre will grade it weeks later, so the credit promised to the customer matches the credit paid and the dealer avoids disputes and reversals.

**ML task:** Defect detection and segmentation (screen cracks, housing damage, burn-in, missing parts) and multi-class condition grading against the trade-in programme's grade definitions
**Input data:** Standardised photos captured at intake; device diagnostics output; the processing centre's final grade and any credit adjustment for each device.
**Target:** Programme grade per device and probability that the final grade will fall below the promised grade.
**Evaluation metric:** Agreement with the processing centre's grade, weighted by the credit difference, and recall on devices that will be downgraded, because a missed downgrade becomes a customer dispute weeks later.
**Scope:** The computer-vision task is mature, but the labels come from the trade-in administrator, so a pilot needs its cooperation. 1 CV engineer, 4 months on one chain's intake volume.
**Data availability:** Photos are not captured systematically today. Final grades exist at the trade-in administrator and reach the dealer only as credit adjustments.
