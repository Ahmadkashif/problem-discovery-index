# Machine Learning Opportunities — Money Service Businesses

**Industry:** [[money-service-businesses|Money Service Businesses]]
**Derived from:** [[problems/money-service-businesses/high-impact|High Impact]], [[problems/money-service-businesses/low-impact-1|Low Impact 1]], [[problems/money-service-businesses/low-impact-2|Low Impact 2]], [[problems/money-service-businesses/worker-life-1|Worker Life 1]], [[problems/money-service-businesses/worker-life-2|Worker Life 2]]

---

## 1. Learning the Investigator's Read of an Agent Location
#tacit-knowledge-ml #gradient-boosting #survival-analysis #graph-neural-networks #feature-engineering #evaluation-metrics #compliance

**Problem statement:** Senior agent-oversight investigators look at an agent's transaction pattern, field-visit notes and complaint history and "know" that a store is captured by a fraud ring, structuring for a crew, or merely busy — a judgement built over hundreds of cases that is not in the written procedure. The ML problem is to learn that read from the investigators' historical escalations and conclusions, joined to the late outcomes, and rank the whole agent network by time-to-adverse-outcome with reasons an investigator recognises.

**ML task:** Time-to-event (survival) modelling of agent adverse outcomes, with investigator escalation as an auxiliary early label; graph features over shared senders, receivers, phones and devices across locations; per-flag explanation by feature attribution and nearest past cases
**Input data:** Agent-month transaction aggregates (volume, ticket distribution, corridor mix versus the neighbourhood's customer base, threshold-adjacent amounts, refund and cancellation rates, consumer-fraud reports per thousand transfers); sender and receiver overlap between agents; field-visit forms and free-text notes; complaints and law-enforcement requests; ACH sweep returns; ownership and clerk changes; training completion; every investigator action and closing memo.
**Target:** Time to termination for cause, law-enforcement action or confirmed fraud concentration (late, clean label); investigator escalation and disposition (early, noisy label); agreement between model flag and senior-investigator review.
**Evaluation metric:** Concordance and time-dependent recall at a fixed review budget (the share of later-confirmed bad agents ranked in the top few percent, 6–12 months before the outcome), measured strictly out of time. Recall matters more than precision: a missed complicit agent is an enforcement and victim-loss event, a false flag costs a field visit. Report agreement with senior investigators against their own test-retest agreement on re-reviewed cases as the ceiling.
**Scope:** The data collection challenge is the hard part: the investigator's reasoning has to be captured as they close each case, so the build starts with a structured closing step that drafts the reason from the case record for one-click confirmation, and with historical memos aligned to agent histories after the fact. The labelling challenge is that confirmed complicity is rare and arrives years late, terminations mix misconduct with commercial disputes, and investigators rate the same pattern differently after a recent enforcement action — so a sample of cases must be re-reviewed blind to estimate intra-rater reliability. The deployment challenge is speed and credibility: the flag must reach the investigator before next week's transfers, with the two or three features and comparable cases that drove it, or it will be overruled by sales pressure. 2 ML engineers, 1 data engineer and a senior investigator embedded half-time, 9–12 months, with value arriving first as a consolidated agent file and retrieval of comparable past cases.
**Data availability:** Large transmitters hold years of agent histories and case records; the outcome labels are confidential under the BSA and cannot be pooled across firms. Small MSBs with a few hundred agents lack enough confirmed outcomes to train on and would rely on transfer from a larger model or on rules.

---

## 2. Scam-Induced Transfer Interdiction at the Point of Send
#gradient-boosting #transformers #logistic-regression #evaluation-metrics #worker-facing #compliance

**Problem statement:** Predict, before the transfer is paid, whether a sender is a fraud victim (romance, grandparent, impersonation, online purchase scams) and give the clerk or the app specific questions to ask, so the transfer can be paused without insulting genuine senders.

**ML task:** Binary classification with calibrated probability per send, plus typology classification to select the intervention script
**Input data:** Sender history (first-time sender, change in corridor, change in amount, frequency acceleration); receiver history across the network (number of distinct senders, prior fraud reports, payout location); stated relationship and purpose; channel and agent; time and session features in app; consumer fraud reports and refund claims as outcomes.
**Target:** Transfer later reported or confirmed as consumer fraud within 90 days; typology label.
**Evaluation metric:** Recall of reported-fraud dollars at a fixed intervention rate (for example 1% of sends), with precision reported per typology; measure the conversion loss on paused genuine transfers. Victim losses are not reversible once paid out, so recall dominates, but a pause rate above a few percent drives genuine senders to competitors.
**Scope:** Labels under-count fraud because many victims never report; positive-unlabelled methods and receiver-side network signals help. The model must run in under a second at the terminal. 2 data scientists and 1 engineer, 5–6 months, with counter-script design done with agent trainers.
**Data availability:** Transmitters hold send and refund data and consumer complaints; FTC and law-enforcement data on scam typologies is public at aggregate level. Clerk interventions and their outcomes are not recorded today and need capture.

---

## 3. Sender and Receiver Resolution Across Agents and Scripts
#k-nearest-neighbors #word-embeddings #graph-neural-networks #dbscan #evaluation-metrics #data-integration #compliance

**Problem statement:** Group transfers into resolved persons across agent locations, name spellings and transliterations, mistyped ID numbers and changing phones, so structuring and network monitoring work on people rather than on keystrokes.

**ML task:** Probabilistic entity resolution (pairwise matching with learned similarity on transliterated names, IDs, phones, addresses and behaviour) followed by graph clustering
**Input data:** Sender and receiver fields from every transfer; ID images where captured; device and phone data from app channels; analyst merge and split decisions as supervision.
**Target:** Same-person links and resolved clusters.
**Evaluation metric:** Pairwise precision and recall on analyst-adjudicated pairs, with cluster-level purity; error costs are asymmetric in both directions — a missed merge hides structuring, a false merge creates a false SAR — so report both at the operating threshold and track the downstream effect on alert volume and SAR conversion.
**Scope:** Multilingual name matching is the crux and needs script-aware embeddings and phonetic features. 2 engineers, 4–6 months to a first graph; continuous after.
**Data availability:** Entirely internal and abundant; supervision comes from analysts' historical manual linking and a labelled sample.

---

## 4. Corridor-Day Price Elasticity and FX Margin Setting
#bayesian-inference #causal-inference #gradient-boosting #hypothesis-testing #revenue-impact #automation

**Problem statement:** Estimate how send volume in each corridor responds to the fee and the FX spread a transmitter shows against competitors' landed amounts that day, and set prices that hold volume while keeping margin.

**ML task:** Hierarchical Bayesian demand model of volume on own and competitor landed amount, with causal identification from pricing experiments and exogenous FX moves
**Input data:** Own transfers by corridor, channel, amount band and day; fees and FX rates shown; competitor landed amounts from pricing intelligence feeds; promotions; payday and holiday calendars in sending and receiving countries.
**Target:** Volume and new-sender conversion by corridor-day as a function of price.
**Evaluation metric:** Out-of-time accuracy of predicted volume response to price changes, and realised margin per transfer against a pricing-team baseline in randomised tests. Overstating elasticity gives away margin; understating it cedes corridors, so evaluate both directions.
**Scope:** Prices are endogenous to competitor moves, so the first months are spent designing small randomised price tests. 2 data scientists, 6 months.
**Data availability:** Own data is complete; competitor pricing comes from vendors such as FXC Intelligence or in-house scraping.

---

## 5. Payout-Partner Prefunding Forecasts
#time-series-forecasting #temporal-fusion-transformers #exponential-smoothing #evaluation-metrics #revenue-impact #automation

**Problem statement:** Forecast next-day and next-week payout demand by partner and currency so treasury prefunds each payout partner just enough, without failed payouts or idle cash trapped abroad.

**ML task:** Multi-series probabilistic forecasting with calendar and event covariates
**Input data:** Daily payout volume by partner and currency; send pipeline; paydays and holidays in sending and receiving countries; FX moves; partner settlement cut-offs; past shortfalls.
**Target:** Quantiles of payout demand per partner-currency-day.
**Evaluation metric:** Pinball loss at the quantiles treasury funds to, plus realised shortfall days and average idle prefunded balance against the current method. A shortfall stops payouts and costs customers; idle balance costs working capital, so both are reported.
**Scope:** A well-trodden forecasting problem with messy event effects (holidays, remittance tax changes, devaluations). 1 data scientist and 1 treasury analyst, 3–4 months.
**Data availability:** Fully internal; quality depends on clean settlement records.
