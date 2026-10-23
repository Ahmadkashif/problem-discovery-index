# Machine Learning Opportunities — Armored Car Services

**Industry:** [[armored-car-services|Armored Car Services]]
**Derived from:** [[problems/armored-car-services/high-impact|High Impact]], [[problems/armored-car-services/low-impact-1|Low Impact 1]], [[problems/armored-car-services/low-impact-2|Low Impact 2]], [[problems/armored-car-services/worker-life-1|Worker Life 1]], [[problems/armored-car-services/worker-life-2|Worker Life 2]]

---

## 1. Learning the Messenger's Read of a Stop
#tacit-knowledge-ml #cnns #object-detection #transfer-learning #gradient-boosting #evaluation-metrics #worker-facing

**Problem statement:** Veteran armored crews read the scene around a stop in the seconds before the door opens and decide to proceed, circle, re-sequence or abort, a judgement built over thousands of stops that they cannot specify. The ML problem is to learn that read from recorded approaches and crew decisions, and to detect cross-route surveillance patterns no single crew can see.

**ML task:** (a) Object detection and cross-camera re-identification of vehicles and people recurring near a carrier's stops across trucks and days; (b) stop-level risk scoring, a calibrated probability that a veteran crew would decline or delay the stop, conditioned on detected scene features and route context
**Input data:** Multi-camera video from trucks over the final approach (front, side and rear cameras); GPS and telematics; route schedule, site identity, time of day and day of week; cash value on board; one-tap crew decisions (proceed, circle, delay, re-sequence, abort, backup) with optional voice notes; incident and near-miss reports; police calls-for-service data near sites where available.
**Target:** Crew decision class per approach (veteran crews' decisions as the primary label); incident or attempted attack within the stop window (rare, high-weight label); recurring-entity alerts confirmed or dismissed by security analysts.
**Evaluation metric:** For the risk score, agreement with held-out veteran decisions measured against veterans' own test-retest consistency on re-shown approaches as the ceiling, and recall on the small set of stops that preceded real attacks or confirmed surveillance. The alert rate matters as much as accuracy: crews will ignore a system that flags more than a small share of approaches, so report precision at a fixed alert budget per route day. For re-identification, precision of recurring-vehicle matches confirmed by analysts, because a false "you are being watched" alarm is expensive.
**Scope:** The data collection challenge is first and largest: the expert's read must be captured while it happens, so the cab needs a one-tap decision control and automatic clipping of the approach video joined to the route record, without adding seconds to the stop. The labelling challenge is that robberies are rare (49 armored-carrier violations nationally in the FBI's 2023 Hobbs Act table) and veterans disagree with themselves, so the model must learn mainly from decisions and near-misses, with repeated annotation of a sample of approaches to measure intra-rater reliability. The deployment challenge is speed: the score must reach the cab before the messenger reaches the door handle, faster than their own glance, so inference runs on the truck. 3 ML engineers, 1 computer vision engineer and a security-operations lead embedded with one branch, 9–12 months, with the first value coming from cross-route re-identification and site histories rather than the risk score.
**Data availability:** Truck cameras exist on many fleets but footage is retained for evidence and overwritten; decisions are not recorded at all. A carrier must build the corpus prospectively for 6–12 months. Privacy rules on recording public spaces and on facial recognition vary by state and push the design towards vehicle re-identification first.

---

## 2. Route-Aware ATM Cash Forecasting and Replenishment
#time-series-forecasting #temporal-fusion-transformers #gradient-boosting #markov-decision-processes #dynamic-programming #evaluation-metrics #automation

**Problem statement:** Forecast each ATM's withdrawals and deposits by denomination and set replenishment amounts and dates that minimise idle cash, cash-outs and unscheduled visits subject to the carrier's route days, vault cut-offs and per-truck value limits.

**ML task:** Probabilistic multi-horizon forecasting (quantiles per machine, denomination and day), followed by a stochastic inventory policy solved per machine with route-day and value constraints across a route
**Input data:** Daily dispense and deposit history per machine and cassette; cassette capacities and denomination configuration; host-site hours and type; paydays, benefit payment dates, holidays and local events; nearby machine outages; the carrier's route calendar, vault cut-offs and truck value limits; contract costs of a cash-out and an unscheduled visit; the owner's cost of funds.
**Target:** Withdrawal and deposit quantiles per machine-denomination-day; recommended load per visit; visit dates.
**Evaluation metric:** Out-of-time pinball loss on quantiles, and in simulation or A/B on matched machines the joint outcome that owners pay for: cash-out hours, average idle cash and unscheduled visits per thousand machine-days, priced with the owner's own cost weights. A forecast with lower error that raises emergency visits is worse, not better. Report against the current vendor or desk forecast as the baseline.
**Scope:** Forecasting itself is well understood; the work is the coupling to routes and contracts and the denomination-level data. 2 data scientists and 1 operations-research engineer, 5–6 months for one carrier region or one large ATM owner, with gains concentrated on holiday and payday periods.
**Data availability:** Dispense data belongs to the ATM owner and reaches the carrier under managed-service contracts, so a carrier needs contractual consent to pool it across owners; an owner can do it alone for its own fleet. Route calendars and value limits are the carrier's.

---

## 3. Chain-of-Custody Discrepancy Attribution
#bayesian-inference #hypothesis-testing #gradient-boosting #feature-engineering #data-integration #compliance

**Problem statement:** When a deposit, cassette or smart-safe cassette count disagrees with the declared or validated amount, estimate where in the chain the difference most likely arose — the customer's count, the safe, transit or the counting room — and assemble the evidence.

**ML task:** Probabilistic attribution over handoff stages using a hierarchical Bayesian model of discrepancy rates by customer, location, counting station, crew and drop type, plus a classifier that flags discrepancies whose pattern departs from the customer's and station's baseline
**Input data:** Bag-level declared amounts, seal numbers and photos, handheld scan events with time and location, vault count results by station and operator, smart-safe validation logs and jam events, ATM counters, prior discrepancy outcomes and investigation findings.
**Target:** Posterior probability of origin per stage; resolution class (customer miscount, counting error, device error, counterfeit, theft); escalate or close.
**Evaluation metric:** Calibration of origin probabilities against resolved investigations, and time-to-resolution and share of crew-attributed cases later overturned before and after. Recall on true theft cases is the safety constraint: the system must not let a real internal theft close as a customer miscount, so report it separately even though the cases are few.
**Scope:** Most of the build is joining the records; the models are modest. 1 data scientist, 1 data engineer and an investigations lead, 4 months to a first version at one region.
**Data availability:** Scan, vault and investigation records are the carrier's own; customer declarations are supplied with each bag. Investigation outcomes are recorded unevenly and must be cleaned or captured going forward.

---

## 4. Staged-Fault Detection for ATM Service Calls
#lstms-and-grus #hidden-markov-models #gradient-boosting #evaluation-metrics #worker-facing

**Problem statement:** The FBI has tracked schemes since 2022 in which robbers jam an ATM and wait for the technician sent to fix it. Classify incoming fault calls as likely genuine or possibly staged from the machine's own event sequence, so dispatch can send two people, delay, or request an escort.

**ML task:** Sequence classification over ATM device event logs preceding a fault (card reader, dispenser, deposit module, door and sensor events), combined with site and time features in a gradient-boosted risk score
**Input data:** Device journals and status messages from remote monitoring; fault codes; transaction sequences before the fault; site type and hours; prior faults at the site; incident reports of attacks on technicians; local crime data.
**Target:** Staged or suspicious versus genuine fault (labels from incident reports and from technician findings of foreign objects or tampering); recommended dispatch mode.
**Evaluation metric:** Recall on confirmed staged faults at a fixed share of calls flagged, because each flagged call costs a second technician or a delay; secondary metric is mean time to restore for genuine faults, which must not get worse.
**Scope:** Labels are few, so the first version leans on rules and anomaly patterns validated by security staff, with the classifier trained as confirmed cases accumulate across a fleet. 1 ML engineer and 1 field-operations analyst, 4 months.
**Data availability:** Device logs sit with the ATM owner or the managed-service provider under contract; technician findings are recorded in field-service systems in free text and need extraction.

---

## 5. Morning Route Rebuild with Learned Stop Times
#optimization-fundamentals #monte-carlo-methods #gradient-boosting #probability-distributions #workflow-orchestration #automation

**Problem statement:** Rebuild a branch's routes each morning after call-outs, vehicle failures and emergency orders, respecting crew licences by state, truck value limits, customer windows, vault cut-offs and a requirement that sequences and timings vary, using learned rather than assumed stop durations.

**ML task:** Regression of stop service-time distributions per site and time; stochastic vehicle-routing optimisation with randomisation constraints, evaluated by Monte Carlo simulation of service times and traffic
**Input data:** Route history with arrival and departure times per stop; customer windows and penalties; crew rosters and licence states; vehicle status; vault and Fed cut-offs; emergency orders and ATM alerts; traffic data.
**Target:** Service-time distributions per stop; a feasible daily plan with expected lateness by customer.
**Evaluation metric:** Missed customer windows, overtime hours and truck-hours per stop against supervisors' manual plans on the same days; a predictability measure (how often a site is served at the same time and order) that must stay above the security team's threshold; and supervisor time to a confirmed plan.
**Scope:** Vehicle-routing solvers exist; the work is encoding the security and licensing rules and learning stop times. 1 operations-research engineer and 1 data scientist, 4 months to a pilot branch.
**Data availability:** Route history, rosters and licences are the carrier's own and clean enough once extracted from the dispatch system.
