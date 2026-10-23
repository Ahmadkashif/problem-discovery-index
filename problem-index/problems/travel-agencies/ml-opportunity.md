# Machine Learning Opportunities — Travel Agencies

**Industry:** [[travel-agencies|Travel Agencies]]
**Derived from:** [[problems/travel-agencies/high-impact|High Impact]], [[problems/travel-agencies/low-impact-1|Low Impact 1]], [[problems/travel-agencies/low-impact-2|Low Impact 2]], [[problems/travel-agencies/worker-life-1|Worker Life 1]], [[problems/travel-agencies/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Advisor's Fit Judgement
#tacit-knowledge-ml #large-language-models #transformers #gradient-boosting #word-embeddings #evaluation-metrics #revenue-impact

**Problem statement:** Senior leisure advisors hear a client's description and "just know" which properties, ships and ground operators will suit them — a judgement built over hundreds of trips that they cannot specify and that leaves with them. The ML problem is to learn that judgement from the options senior advisors offered, the option chosen and the outcome, and to propose a ranked shortlist with reasons to a junior advisor during the discovery conversation.

**ML task:** Learning to rank over candidate products conditioned on a client profile extracted from conversation, plus a calibrated probability that the client rebooks within 12 months given the match
**Input data:** Discovery call transcripts and message threads (with consent); structured preferences extracted by an LLM (pace, budget signals, past dislikes, party composition, accessibility needs); proposals with all options offered and the one chosen; product attributes from supplier content and consortium listings; post-trip outcome signals (amenity confirmed, complaint, refund, post-trip rating, rebooking).
**Target:** Ranking of candidate products matching senior advisors' choices; outcome composite (rebook, no complaint, rating ≥ threshold).
**Evaluation metric:** NDCG@5 against held-out senior-advisor shortlists, reported against senior advisors' agreement with each other on the same anonymised briefs as the ceiling. Outcome model: Brier score and calibration of the rebook probability, measured out of time. A confident wrong match (a large resort for a client who said they hate crowds) costs a client; a missed good option costs little, so precision at the top of the list matters more than coverage.
**Scope:** The data collection challenge is the hardest part: the expert's reasoning must be captured while they work, so the system needs zero-effort capture — transcripts and messages parsed automatically, a one-tap "why this one" confirmation, and outcome signals collected by a two-question post-trip check-in rather than advisor notes. The labelling challenge is that outcomes are noisy (weather and flights spoil good matches) and advisors disagree with themselves after a bad recent experience, so each composite label needs reliability measured on a re-annotated sample, and senior-advisor shortlists should be collected on standardised briefs to estimate the agreement ceiling. The deployment challenge is speed: suggestions must appear while the call is running or the proposal is being built, faster than the advisor's recall, and must show their basis or senior advisors will reject them. 2 ML engineers, 1 data engineer and an advisor-community lead inside a host or consortium, 9-12 months, with value first as retrieval ("advisors who booked similar clients chose these three") before any ranker is trusted.
**Data availability:** Booking records exist at hosts and consortia; proposals with rejected options exist in itinerary tools but are rarely kept; outcome signals must be built going forward. Transcript capture needs client consent and the advisor's agreement, since independent advisors regard client knowledge as theirs.

---

## 2. Expected-Commission Matching and Time-to-Payment
#large-language-models #k-nearest-neighbors #survival-analysis #evaluation-metrics #data-integration #automation #revenue-impact

**Problem statement:** Match each commission payment line from clearing houses, cruise and tour statements to the booking it pays, compute the variance against what the booking should have paid, and predict which open commissions will never arrive without a chase, so the back office works the right claims before suppliers stop responding.

**ML task:** Entity resolution between payment lines and bookings (fuzzy record linkage), plus survival modelling of time to payment by supplier, chain, booking channel and amount
**Input data:** Booking records with change history (dates, rates, cancellations) from Trams, ClientBase or host systems; supplier statements as CSV, PDF and email; clearing-house remittance files; historical payment dates; supplier commission rules; ASTA watch-list and recovery outcomes.
**Target:** Match / no-match per payment line and booking pair with confidence; expected commission per booking; hazard of payment over days since checkout or sailing.
**Evaluation metric:** Match precision at the auto-post threshold (a wrong match silently closes a real debt) and recall of true matches; for the survival model, concordance index and calibration of the 90-day non-payment probability, judged by recovered dollars per chase hour against the current fixed age-based chase rule.
**Scope:** Matching is the bulk of the work and the easier part: LLM extraction of statement PDFs plus a blocked, learned similarity on name, dates, property and amount. 1 ML engineer and 1 back-office analyst for 4-6 months at one host. The survival model needs a few years of payment history to estimate supplier-level behaviour.
**Data availability:** Hosts and larger agencies hold years of bookings and payments; statement formats vary by supplier but are repeated. Labels come from the historical reconciliation the back office already did by hand.

---

## 3. Group Block Pickup Forecasting
#survival-analysis #gradient-boosting #time-series-forecasting #bayesian-inference #feature-engineering #revenue-impact

**Problem statement:** For each contracted room or cabin block, forecast final pickup at the supplier's release and name-in dates from the booking curve so far, so the advisor releases or extends space before attrition charges apply.

**ML task:** Final-pickup forecasting from partial booking curves (hierarchical Bayesian or gradient-boosted model on curve features), with time-to-booking survival modelling per invited guest where guest lists exist
**Input data:** Historical blocks with contract terms and daily or weekly pickup; group type (wedding, cruise, alumni, faith, sports); destination and season; lead time; guest-list size and RSVP data; deposit and payment-plan status; marketing touches.
**Target:** Rooms or cabins picked up at cut-off, with an interval; probability of breaching the attrition allowance.
**Evaluation metric:** Mean absolute error in rooms at the release date, and interval coverage; the decision metric is attrition dollars paid plus commission lost on prematurely released rooms, against the advisor's own release decisions.
**Scope:** Modest modelling on small data per advisor; the value appears only when pooled across a host's or consortium's groups. 1 data scientist, 3-4 months, with Bayesian pooling by group type to handle sparse histories.
**Data availability:** Pickup histories live in supplier group portals and advisor spreadsheets; hosts that run group desks have the cleanest records. Contract terms must be extracted from PDFs.

---

## 4. Disruption Re-Accommodation Ranking
#gradient-boosting #logistic-regression #monte-carlo-methods #optimization-fundamentals #large-language-models #worker-facing #automation

**Problem statement:** When flights cancel or misconnect, generate and rank re-accommodation options for each affected corporate traveller by their realistic chance of success — connection made, seat held, hotel available — within the client's travel policy, before the traveller calls.

**ML task:** Probability of successful connection per option (binary classification on minimum-connection, terminal, historical delay and irregular-operations features), Monte Carlo simulation of itinerary completion across legs, and constrained ranking against policy and cost
**Input data:** Traveller PNRs and profiles; client travel policies; schedule and live flight-status feeds; historical on-time and cancellation data by route and hour; seat availability; fare rules for exchanges; hotel availability near alternate airports; past rebookings and whether travellers completed them.
**Target:** Success probability per option; ranked option list; flag for options that breach policy or fare rules.
**Evaluation metric:** Share of travellers whose first-ranked option is completed as booked, and agent handling time per disrupted traveller; misconnect probability calibration matters most, because an option that looks valid and fails sends the traveller back into the queue at a worse hour.
**Scope:** 2 ML engineers and 1 GDS/NDC integration engineer, 6-9 months, inside a TMC. The hard part is integration — live availability, NDC changes, policy engines — not the models.
**Data availability:** TMCs hold PNRs and servicing logs; schedule and flight-status data are licensable; completion outcomes can be read from ticket usage and later segments.

---

## 5. Exchange and Debit-Memo Risk Screening
#gradient-boosting #logistic-regression #large-language-models #bert #evaluation-metrics #compliance #automation

**Problem statement:** Before an exchange, refund or reissue is ticketed, predict whether it will draw an agency debit memo from the airline, and point to the fare-rule clause or fare calculation that will trigger it.

**ML task:** Binary classification of transactions at risk of a debit memo, with fare-rule text classification to identify the violated condition
**Input data:** Exchange and refund transactions with fare basis, fare calculation lines and fare rules text (categories for penalties, advance purchase, combinability); agent and channel; historical debit memos with airline reason codes; ARC settlement records.
**Target:** Debit-memo occurrence within ~90 days (estimate of the typical window); reason category.
**Evaluation metric:** Recall at a fixed review rate — the agency can afford to re-check perhaps 5% of transactions (estimate), so the model must catch most future debit memos inside that slice; dollars of debit memos avoided per review hour.
**Scope:** 1 ML engineer and a senior ticketing agent for 4 months at a mid-size TMC or consolidator. Fare-rule text is semi-structured and well suited to transformer classification; the base rate is low, so historical memos across several years are needed.
**Data availability:** Agencies hold their own debit-memo history and transaction records; reason codes are inconsistent across airlines and need normalising.
