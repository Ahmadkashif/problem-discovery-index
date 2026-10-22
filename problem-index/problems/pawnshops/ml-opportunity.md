# Machine Learning Opportunities — Pawnshops

**Industry:** [[pawnshops|Pawnshops]]
**Derived from:** [[problems/pawnshops/high-impact|High Impact]], [[problems/pawnshops/low-impact-1|Low Impact 1]], [[problems/pawnshops/low-impact-2|Low Impact 2]], [[problems/pawnshops/worker-life-1|Worker Life 1]], [[problems/pawnshops/worker-life-2|Worker Life 2]]

---

## 1. Learning the Counter Appraisal
#tacit-knowledge-ml #cnns #transfer-learning #gradient-boosting #survival-analysis #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Experienced pawnbrokers look at an item for seconds and "know" what it will resell for in their store and how far to lend against it — a judgement built over thousands of tickets that they cannot specify and that new clerks lack. The ML problem is to learn that valuation from the store's own graded history and give the next clerk a calibrated range at the counter.

**ML task:** Multimodal regression of realised resale value with prediction intervals (image embedding from a pretrained vision backbone, fine-tuned, joined to tabular item, store and market features in a gradient-boosted model), plus a calibrated probability that the ticket is redeemed or renewed rather than forfeited
**Input data:** Intake photographs where captured; the structured fields every police form already requires (category, brand, model, serial, metal, karat, weight, stones); the clerk's loan or purchase amount and, once captured, the clerk's own resale estimate; pseudonymised customer ticket history; store, date and day of week; spot gold and silver on the day; outcomes from the POS — redeemed, renewed, forfeited, sale price and days to sale, scrapped at melt, police seizure.
**Target:** Net realised value for forfeited and purchased items (sale price, or melt value for scrapped metal); redemption within maturity plus grace; derived loss given forfeit (loan plus accrued fees minus realised value).
**Evaluation metric:** Pinball loss and empirical coverage of the 10th–90th percentile interval on realised value, measured strictly out of time and by store; for lending, expected loss per dollar lent at the recommended amount against the clerk's actual amount. Over-valuation on an item that forfeits costs money directly; under-valuation loses a customer the data never sees, so walk-aways must be logged to measure that side. Model–clerk agreement is reported against each clerk's own test–retest agreement on re-photographed items as the ceiling.
**Scope:** The data collection challenge comes first: the appraiser's estimate must be captured at the counter by the person doing it, so the system needs a near-zero-effort surface — a photograph and one number — that a clerk will use with a queue at the door, and historic tickets must be reconstructed from loan amounts, which blend value with negotiation and the read on the customer. The labelling challenge is selection and drift: realised prices exist only for the forfeited third, which is not a random third, gold-backed values move with spot, and the same clerk lends differently on a busy Friday than a slow Tuesday, so labels need repeated appraisals of the same items to estimate intra-rater reliability and selection correction using redeemed items' attributes. The deployment challenge is speed: an answer in seconds on a phone, faster than the clerk's own recall, framed so the customer is not handed the number. 2 ML engineers, 1 data engineer and 1 product lead embedded with a district of 20–50 stores, 6–9 months, with value appearing first as retrieval ("the last eleven of this model sold here for $180–240") before any price model is trusted.
**Data availability:** Chains hold millions of tickets with outcomes in their POS; photographs are captured only where a jurisdiction or chain policy demands them, so image coverage must be built prospectively. Independents' data sits in per-store vendor databases they own, too thin to train on alone.

---

## 2. Redemption, Renewal and Forfeit Timing
#survival-analysis #gradient-boosting #causal-inference #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** A pawn store's income is fees on tickets that renew or redeem; a forfeit converts that fee stream into inventory of uncertain value. Predict, per ticket, when it will redeem, renew or forfeit, and estimate which servicing actions change the outcome.

**ML task:** Competing-risks survival modelling (redeem, renew, forfeit) at ticket level, plus uplift estimation of reminder and payment-option interventions
**Input data:** Ticket history per customer (amount, collateral category, count of prior redemptions and forfeits, renewal pattern), loan-to-estimated-value ratio, day-of-month and payday proxies, store, season, reminder and payment events, randomised or staggered outreach logs.
**Target:** Time to each terminal event; incremental probability of redemption or renewal caused by an outreach.
**Evaluation metric:** Time-dependent concordance and integrated Brier score for the survival model, out of time; for uplift, Qini coefficient on held-out randomised outreach. A false "will redeem" on a ticket that forfeits costs nothing extra; a missed at-risk ticket loses a fee stream and a customer, so recall on at-risk tickets is the operating constraint.
**Scope:** Labels are clean and plentiful — every ticket ends in one of three recorded outcomes within months. The hard part is causal: chains already send reminders, so measuring their effect needs a period of randomised timing. 1 data scientist and 1 engineer, 4 months to a model; uplift results after one or two quarters of experiments.
**Data availability:** Fully held in the POS. Outreach and payment logs may sit in a separate messaging or payments tool and need joining.

---

## 3. Stolen-Property Risk at Intake
#autoencoders #graph-theory #logistic-regression #feature-engineering #evaluation-metrics #compliance

**Problem statement:** A small fraction of transactions involve stolen goods, and a seized item takes the loan money with it and exposes the clerk. Using the operator's own transaction history, score each pawn or purchase for the patterns that preceded police holds and seizures.

**ML task:** Rare-event classification combining an autoencoder reconstruction score on transaction features with seller–item–store graph features and a calibrated logistic model
**Input data:** The operator's own tickets across its stores: seller frequency and velocity, new-in-box items, multiple units of one model, item categories with high theft rates, store-hopping by one seller across the chain's locations, serial-number reuse, time of day; police hold and seizure records as labels; local do-not-buy lists where supplied by police.
**Target:** Probability that a transaction later draws a police hold or seizure.
**Evaluation metric:** Precision in the top-k flagged transactions per store per week, where k is what a manager can review, and recall on later-seized items. Base rates are tiny — Oregon reports a police pickup rate of 0.094% — so area under the precision–recall curve, not accuracy, is the honest summary.
**Scope:** The model must stay within the operator's own data: cross-industry reporting databases such as LeadsOnline are for law enforcement only, and Florida makes records delivered to police usable only for official law enforcement purposes. Labels are few and noisy (a hold is not proof of theft). Fair-treatment review is needed so the score does not proxy for neighbourhood or ethnicity. 1 data scientist with a loss-prevention lead, 4–5 months.
**Data availability:** Chains hold the transactions and their own hold and seizure logs; independents lack the volume. Police may share do-not-buy lists but not their investigative data.

---

## 4. Intake Description Extraction for Reporting Forms
#large-language-models #transformers #cnns #object-detection #automation #compliance #worker-facing

**Problem statement:** Every ticket must carry a complete description — brand, model, serial number, metal and karat, stones, firearm specifications — in the form each jurisdiction requires. Extract these from photographs of the item, its label plate and its hallmark, and pre-fill the form for the clerk to confirm.

**ML task:** Object detection of label plates, serial plates and hallmarks; text recognition and vision-language extraction into a jurisdiction-specific schema; category classification
**Input data:** Intake photographs; existing ticket descriptions as weak labels; manufacturer model and serial formats; jurisdiction field rules.
**Target:** Structured fields with confidence; flags for missing or invalid required fields.
**Evaluation metric:** Field-level exact-match accuracy, with serial numbers held to zero silent error — a wrong serial with high confidence is worse than a blank that forces the clerk to type it, because it breaks police matching. Secondary: time per ticket and the share of records an agency rejects or queries.
**Scope:** Serial and model plates are a tractable reading problem; hallmarks on worn jewellery and engraved firearm markings are the hard tail. 2 engineers, 4–5 months for the main categories (electronics, tools, firearms), with jewellery hallmarks later.
**Data availability:** Photographs must be captured; descriptions typed historically give weak supervision. Field rules come from ordinances and statutes.

---

## 5. Forfeit Pricing and the Scrap-or-Retail Decision
#time-series-forecasting #gradient-boosting #bayesian-inference #markov-decision-processes #evaluation-metrics #revenue-impact

**Problem statement:** Each forfeited item must be priced and routed — store floor, online, wholesale, or for precious metal, the refiner at melt. Predict sale probability over time at candidate prices, and choose markdowns and channel to maximise net value, timing scrap against the spot price.

**ML task:** Hierarchical demand modelling by model, category and store (Bayesian shrinkage for thin categories), sale-hazard estimation at price levels, and a sequential pricing policy over markdown steps; for gold pieces, a retail-versus-melt decision under a spot-price forecast distribution
**Input data:** Sales history with listed price, markdowns, channel and days on shelf; item attributes and condition grade; store traffic proxies; spot gold and silver history; refiner settlement terms; seasonality (tax-refund season, holidays).
**Target:** Sale probability by day and price; net realised value by channel.
**Evaluation metric:** Realised margin and days-on-shelf against the current rule on a held-out set of stores, with aged-inventory share as a guardrail; for scrap timing, regret against a hindsight-optimal sale date, reported honestly because spot is close to unforecastable at short horizons.
**Scope:** Single-unit items make demand estimation thin, so pooling across similar models and stores matters more than model choice. The gold decision is mostly a rule (retail premium over melt above a threshold, else scrap) with a forecast on top. 2 data scientists, 4–6 months.
**Data availability:** Held in the POS and e-commerce systems; condition grades must be captured at intake to be useful.
