# Machine Learning Opportunities — Wholesale Auto Auctions

**Industry:** [[wholesale-auto-auctions|Wholesale Auto Auctions]]
**Derived from:** [[problems/wholesale-auto-auctions/high-impact|High Impact]], [[problems/wholesale-auto-auctions/low-impact-1|Low Impact 1]], [[problems/wholesale-auto-auctions/low-impact-2|Low Impact 2]], [[problems/wholesale-auto-auctions/worker-life-1|Worker Life 1]], [[problems/wholesale-auto-auctions/worker-life-2|Worker Life 2]]

---

## 1. Capturing the Inspector's Suspicion Before the Car Runs
#tacit-knowledge-ml #cnns #transfer-learning #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing

**Problem statement:** Experienced inspectors hear, feel and smell defects that never reach the condition report: a cold-start tick, a shift flare, a mildew note, a turned fender bolt. Learn that read from instrumented inspections and the outcomes the auction already holds, and predict before the car runs which arbitrable defects it is likely to carry.

**ML task:** Multi-label classification over NAAA Appendix I defect categories (engine, transmission, structural, flood, electrical, ADAS) with calibrated probabilities. Audio and motion are encoded by CNNs fine-tuned from pretrained audio and image models, then fused with tabular features in a gradient-boosted classifier.
**Input data:** Fifteen-second cold-start audio, as a log-mel spectrogram; the phone's accelerometer and audio trace on the lot drive; condition-report photographs; paint-meter readings; trouble codes read at inspection; the inspector's free-text or voice "suspicion" note; VIN decode (year, make, model, engine, transmission); inspector ID and tenure.
**Target:** Whether the car later drew a granted arbitration claim, a failed post-sale inspection or a guarantee return in each category, plus the inspector's own suspicion flag as a secondary target for agreement analysis.
**Evaluation metric:** Recall at a fixed flag rate per category, measured on a held-out period and held-out inspectors, alongside calibration (expected calibration error). A missed transmission or structural defect costs a claim worth thousands. A false flag costs the inspector a few seconds of extra recording, so recall is weighted over precision. Report model–inspector agreement against the inspectors' own test–retest agreement on blind re-inspections, which sets the ceiling.
**Scope:** The data collection challenge comes first. The inspector's evidence must be captured during the inspection without slowing work that is paid by the car, which means a recording step under 30 seconds built into the existing condition-report app. The labelling challenge is that arbitration under-reports defects and depends on the buyer as much as the car. Labels need buyer-propensity correction and a re-inspected sample, and the threshold changed on 1 June 2026 ($800, or 2% at $50,000 and up), so pre- and post-June claims are not comparable. The deployment challenge is that a prompt must appear before the inspector closes the report, and only when it adds something they did not already note. Team: 2 ML engineers, 1 audio/signal specialist and 1 product engineer embedded with an inspection operation, 9–12 months. Value shows first in two or three categories where audio carries signal: engine noise, transmission and flood.
**Data availability:** The national auctions hold millions of condition reports joined to arbitration outcomes. ACV's ML inspection team says it processes "hundreds of thousands of vehicle inspections annually". The audio and motion capture and the suspicion notes do not exist at most auctions and must be collected prospectively. Expect 6–9 months to gather enough labelled positives in each category.

---

## 2. Arbitration-Risk Scoring of a Condition Report
#large-language-models #gradient-boosting #logistic-regression #evaluation-metrics #compliance #quick-win

**Problem statement:** Before a car runs, read the seller announcement and condition report, compare them with the VIN's factory equipment and recall campaigns, and score the probability and expected cost of a granted arbitration under the 2026 guidelines, with the clause each risk breaks. This is the two-week MVP.

**ML task:** Rules plus a classifier. An LLM maps free-text announcements to Appendix I categories and flags generic wording the guidelines no longer honour. Deterministic rules apply the $800/2% thresholds and filing windows. A gradient-boosted classifier, with a logistic regression baseline, estimates P(granted claim) and expected adjustment.
**Input data:** Announcement text and sale light; condition-report fields and trouble codes; the NHTSA vPIC decode (trim, ADAS equipment, drivetrain); NHTSA recalls API campaigns for the year, make and model, including "park it" flags; expected price against MMR; seller type and history.
**Target:** Granted claim within the filing window (yes/no), the claim category, and the settled adjustment amount.
**Evaluation metric:** Precision of the top-k flags shown to the seller (a flag nobody acts on teaches users to ignore the tool), recall on claims in the categories the 2026 rules changed (generic announcements, warning lights, ADAS), and calibration of expected cost by price band.
**Scope:** The MVP is buildable in two weeks on public inputs alone. It needs vPIC decoding, the recalls API, an LLM prompt holding the guideline categories, and a rules table for thresholds and the generic-announcement ban. It produces a ranked list of risks with clauses. The learned layer needs a few months of an auction's claim history to replace the rules-only score. 1 engineer for the MVP; 1 ML engineer and 1 analyst for 3 months for the learned version.
**Data availability:** Public APIs are free and answered test calls on 2026-10-28. The recalls API gives campaigns by model, not VIN-level open status, which needs the manufacturer's lookup or a commercial feed. Claim history is held by each auction.

---

## 3. Title-Window Breach Forecasting
#survival-analysis #gradient-boosting #feature-engineering #workflow-orchestration #automation

**Problem statement:** For every unit sold without title, estimate the time until a negotiable title reaches the auction and the probability it breaches the auction's title window, so clerks work the queue in order of risk rather than sale date.

**ML task:** Time-to-event modelling (Cox proportional hazards baseline, gradient-boosted survival trees) with censoring for open cases; derived breach probability at the window date.
**Input data:** Sale date and title-window length; issuing state and whether it runs electronic titles; lienholder and payoff status; seller type (dealer, captive, fleet, lender) and seller's title history; whether the sale was announced title-absent; days since payoff; prior contact outcomes.
**Target:** Days from sale to title received; breach (buyer returned the car, or the window passed) as a binary outcome.
**Evaluation metric:** Concordance index for the ranking, and Brier score at the window date. Operationally, the share of eventual breaches that sat in the top fifth of the morning list.
**Scope:** Modest modelling on data the auction system already timestamps. Most of the work is cleaning title events and lienholder names. 1 data scientist, 2–3 months; value from the first month as a ranked list.
**Data availability:** Held by each auction's title department. Lienholder behaviour generalises across auctions, but no shared dataset exists.

---

## 4. Adjustment Estimation From Claim Evidence
#k-nearest-neighbors #linear-regression #regularization #large-language-models #worker-facing #workflow-orchestration

**Problem statement:** When a buyer files a claim, propose a fair price adjustment the buyer can accept instead of unwinding the sale, from the claim's photos, repair estimate and scan codes and from how similar past claims settled.

**ML task:** Retrieval of nearest past cases (embedding of claim text and category, vehicle, price band) plus a regularised regression or quantile model for the settled adjustment; LLM extraction of line items from repair estimates.
**Input data:** Claim text, photos and video; buyer repair estimates (PDF); trouble codes; vehicle and price; past claims with outcome (adjusted, unwound, denied) and amount.
**Target:** Settled adjustment amount; probability the buyer accepts an adjustment rather than returning the car.
**Evaluation metric:** Median absolute error of the proposed adjustment against the settled amount, and the share of proposals accepted on first offer. Unwinds cost far more than over-adjusting by $100, so the acceptance rate leads.
**Scope:** Retrieval works from the first week. The regression needs a few thousand settled claims per major category. 1 ML engineer and 1 arbitration lead, 3–4 months.
**Data availability:** Each auction's arbitration system. Repair-estimate PDFs vary by shop and need extraction.

---

## 5. Sale-Day Move Forecasting and Driver Sequencing
#time-series-forecasting #optimization-fundamentals #gradient-boosting #worker-facing #automation

**Problem statement:** Forecast which units must move where, and when, on a sale day — to the lane, back to rows, to inspection, to transport — and sequence each driver's moves to cut walking and lane gaps.

**ML task:** Short-horizon forecasting of move demand by zone and 15-minute slot, with a gradient-boosted model on run lists and history, then a vehicle-routing-style assignment that minimises walking distance subject to lane timing.
**Input data:** Run lists and lane schedules; historical move logs with timestamps and locations; no-sale and rerun rates by lane; transport pickup bookings; weather.
**Target:** Moves per zone per slot; realised walking distance and lane-gap minutes.
**Evaluation metric:** Forecast error (MAPE) per slot; reduction in lane-gap minutes and in walking distance per driver in a controlled trial on comparable sale days.
**Scope:** The hard part is accurate locations, which needs phone or tag capture of where each car is left. Without it the forecasts route drivers to wrong rows. 1 data scientist and 1 engineer, 4–6 months including the capture pilot.
**Data availability:** Move logs exist at large auctions but locations are unreliable; must be improved before modelling.
