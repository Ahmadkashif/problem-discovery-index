# Machine Learning Opportunities — Waste Haulers

**Industry:** [[waste-haulers|Waste Haulers]]
**Derived from:** [[problems/waste-haulers/high-impact|High Impact]], [[problems/waste-haulers/low-impact-1|Low Impact 1]], [[problems/waste-haulers/low-impact-2|Low Impact 2]], [[problems/waste-haulers/worker-life-1|Worker Life 1]], [[problems/waste-haulers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Regular Driver's Route
#tacit-knowledge-ml #lstms-and-grus #gradient-boosting #time-series-forecasting #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Experienced route drivers run their routes in a sequence and manner that differs from the planned route, and "just know" where each cart sits, which customers set out late and which stops need special handling. The ML problem is to learn that knowledge from the regular driver's telemetry and serve it to substitutes as stop-level guidance and miss alerts.

**ML task:** Sequence modelling of the driver's actual stop order conditioned on day, time and conditions; per-stop classification of service attributes (side of street, approach, roll-out needed, late set-out); and real-time probability that an expected lift has been missed
**Input data:** GPS breadcrumbs at 1–5 second intervals; arm-cycle and lift events from the truck body controller; RFID cart reads where fitted; hopper and curb camera frames; planned route sequence from the routing system; customer service tickets for missed pickups, late set-outs and damage; weather and traffic.
**Target:** Next-stop prediction over the regular driver's history; stop-level attributes; a binary "expected service not performed" flag per stop at the time the truck leaves the block.
**Evaluation metric:** For miss alerts, recall on stops later reported as missed and confirmed by camera or go-back, at a precision that keeps alerts to a handful per route-day; a substitute ignores an alert that cries wolf, so precision below ~50% defeats the product. For sequence learning, top-1 next-stop accuracy against the regular driver, reported against the regular driver's own day-to-day agreement as the ceiling. The business metric is missed-stop complaints and route hours on substitute-run days versus the same routes run by regulars.
**Scope:** The data collection challenge comes first: the expert's knowledge must be inferred from what the truck records while he works, because a driver operating an arm cannot annotate, so the system needs weeks of telemetry per route and a near-zero-effort way for the regular driver to confirm or correct a few flagged exceptions at the end of the shift. The labelling challenge is that the expert disagrees with himself — the same driver runs the route in different orders on different days — so the target is a distribution of good sequences, and missed-pickup complaints are noisy labels contaminated by late set-outs that customers report as misses. The deployment challenge is speed and attention: guidance must reach a substitute at the moment of approach, as one short cue, faster than reading a list, and drivers must see it as protection against complaints rather than surveillance. 2 ML engineers and 1 mobile engineer working with one hauler's routes for 6–9 months; value appears first as a learned route book for substitutes before any miss model is trusted.
**Data availability:** Telemetry is held by the hauler and its fleet software or camera vendor and is plentiful on fleets with modern bodies and tablets; small haulers' trucks often lack lift sensors. Ground truth for misses requires joining service tickets to camera frames, which most haulers have never done.

---

## 2. Overflow, Contamination and Battery Detection from Truck Cameras
#cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #compliance #revenue-impact

**Problem statement:** Classify each container service from hopper and curb camera frames as overfilled, contaminated (wrong material in recycling or organics) or carrying a hazard such as a lithium-ion battery, with evidence frames suitable for a customer notice, a billing record or an SB 1383 route-review file.

**ML task:** Multi-label image classification per lift, object detection for prohibited items (bags in recycling, batteries, propane cylinders), and segmentation of the overflow region above the container rim
**Input data:** Frames from hopper and curb cameras triggered by the arm cycle; container size and stream from the customer record; GPS-matched service location; prior notices and charges; reviewer decisions on past flagged events.
**Target:** Labels per lift (overfilled, contaminated by item type, hazard present, clean); bounding boxes for prohibited items; an evidence frame and confidence for each billable or noticeable event.
**Evaluation metric:** Asymmetric by use. For billing, precision on charged overages is binding: a false charge costs a dispute, a credit and possibly the account, and settlements such as WM's in Nevada now require photo evidence. For contamination route reviews, recall on prohibited items at a reviewed sample matters because the jurisdiction must find contamination to notice it. For batteries, recall dominates: a missed battery can start a hopper fire, and Republic reported eight of ten truck fires over two years were caused by rechargeable batteries (search summary).
**Scope:** Detection on hopper images is a solved problem class but a messy domain: night lighting, dust, motion blur, and items that look different crushed. Transfer from general object detectors plus ~20,000–50,000 labelled lifts per stream (estimate) gets a usable model; 2 ML engineers and a labelling team for 4–6 months. The harder work is the decision layer that turns detections into charges or notices under each contract's rules.
**Data availability:** Camera vendors (AMCS, Safe Fleet, Prairie Robotics, Terex's 3rd Eye) and large haulers hold millions of frames; labels exist only where human reviewers have confirmed events. Who may use the images for training depends on vendor terms, which differ.

---

## 3. Commercial Price-Increase Churn and Retention Uplift
#survival-analysis #causal-inference #gradient-boosting #feature-engineering #revenue-impact

**Problem statement:** Estimate, for each commercial account, how the probability of cancellation responds to the size of the annual price increase and to fees, and which retention offer keeps the account at the least cost when the customer calls to complain.

**ML task:** Time-to-cancellation survival model with price-change covariates, plus heterogeneous treatment-effect estimation of increase size and retention offers
**Input data:** Account rate histories and increase letters; fee lines; service level, container size and pickup frequency; overage and credit history; complaints and call logs; cancellations with stated reasons; local competitor presence and broker activity; contract terms and renewal dates.
**Target:** Hazard of cancellation within 3, 6 and 12 months of an increase; incremental retention from each offer type (partial rollback, container downsize, frequency change).
**Evaluation metric:** Calibration of 12-month cancellation probability by decile, measured out of time on the next increase cycle; uplift validated on randomised or quasi-randomised increase sizes. The binding business measure is accounts lost per point of average increase. Overestimating churn risk leaves price on the table across the whole book, and underestimating it loses accounts, so calibration matters more than ranking.
**Scope:** Increases are not randomly assigned; pricing teams choose them by judgement, so causal estimates need either deliberate experimentation or careful adjustment for selection. 1–2 data scientists, 4–6 months, on a hauler with several hundred thousand commercial account-years of history.
**Data availability:** Fully internal to each hauler's billing and CRM systems. Cancellation reasons are poorly coded; competitor prices are largely unobserved.

---

## 4. Franchise Bid Cost-per-Home Estimation
#gradient-boosting #monte-carlo-methods #linear-regression #confidence-intervals #revenue-impact

**Problem statement:** Before bidding a residential franchise, forecast the cost to serve each home over the contract term, including route hours, trucks, disposal tons and tipping fees, carts and contamination, with an uncertainty range the bid team can price.

**ML task:** Regression of route-level cost drivers (homes per route-hour, set-out rate, pounds per home, travel to disposal) from parcel and street features, combined with Monte Carlo simulation of term-level cost under fuel, wage and disposal-fee scenarios
**Input data:** The RFP's household counts and service requirements; parcel density, lot frontage and street network; the hauler's own route performance in comparable areas; disposal site locations and gate rates; historical set-out and tonnage per home; wage and fuel indices named in the contract's rate-adjustment clause.
**Target:** Cost per home per month by service component, with P10–P90 ranges over the contract term.
**Evaluation metric:** Mean absolute percentage error of forecast against realised cost per home in the first contract year on won bids, reported with the coverage of the P10–P90 interval (the realised cost should fall inside about 80% of the time). Underestimating cost locks the hauler into a loss for five years or more; overestimating loses the bid. The error matters more on the low side.
**Scope:** The selection problem is severe: haulers observe realised cost only on bids they won, and bids are won disproportionately when cost was underestimated. 1 data scientist and 1 operations analyst, 3–4 months, using won and lost bids plus existing routes as analogues.
**Data availability:** Route performance is internal; RFP documents and award prices are public records; parcel data is available from counties and commercial providers.

---

## 5. Roll-Off Swap Demand and Dispatch Sequencing
#time-series-forecasting #dynamic-programming #markov-decision-processes #optimization-fundamentals #automation

**Problem statement:** Forecast next-day roll-off demand (drops, swaps, pulls by box size and area) and sequence each truck's hauls against landfill hours and wait times so that more hauls are completed per truck and fewer boxes sit idle.

**ML task:** Count forecasting by box size and zone, plus sequential decision-making for dispatch under stochastic landfill waits and same-day order arrivals
**Input data:** Order history with timestamps and changes; job-site dwell times; contractor and permit data where available; scale-house tickets with arrival and departure times by landfill; truck GPS; box inventory and condition.
**Target:** Orders by size, zone and day; a dispatch policy that maximises completed hauls subject to customer windows and landfill closures.
**Evaluation metric:** Hauls per truck per day and hauls per container per month against the hauler's current dispatch, in a back-test on held-out weeks; forecast weighted absolute percentage error by box size. Same-day changes are the norm, so a policy that re-plans well beats a plan that is optimal at 6 a.m.
**Scope:** Modest data volumes per hauler and heavy dependence on local landfill behaviour. 1–2 engineers, 3–4 months, as a feature inside a roll-off dispatch product rather than a standalone model.
**Data availability:** Held in each hauler's billing and dispatch system, often incomplete at small operators whose orders arrive by phone and are never logged with timestamps.
