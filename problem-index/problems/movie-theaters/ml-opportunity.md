# Machine Learning Opportunities — Movie Theaters

**Industry:** [[movie-theaters|Movie Theaters]]
**Derived from:** [[problems/movie-theaters/high-impact|High Impact]], [[problems/movie-theaters/low-impact-1|Low Impact 1]], [[problems/movie-theaters/low-impact-2|Low Impact 2]], [[problems/movie-theaters/worker-life-1|Worker Life 1]], [[problems/movie-theaters/worker-life-2|Worker Life 2]]

---

## 1. Learning the Film Buyer's Local Read
#tacit-knowledge-ml #gradient-boosting #bayesian-inference #time-series-forecasting #causal-inference #feature-engineering #evaluation-metrics #revenue-impact

**Problem statement:** Experienced film buyers "know" how a film will hold in a particular market (which audiences turn out, which weekend collapses, which daypart carries a film) and act on it in Monday holdover calls without writing it down. The ML problem is to learn each market's pattern from the circuit's own history and the buyer's past overrides, and to forecast next week's net theatre profit per film per theatre under alternative screen and showtime allocations, so the read is available to a junior buyer or a booking agent covering many small towns.

**ML task:** Hierarchical regression of next-week admissions by theatre, film and daypart (theatres nested in markets, films in genre and rating groups), with a learned adjustment layer that models where and how the senior buyer departed from the national-trend forecast and whether those departures paid off; calibrated predictive intervals for each allocation option
**Input data:** Theatre-by-film-by-showtime admissions and gross from the point-of-sale system over several years; auditorium capacities and formats; showtime schedules; presales by day before the show; concession sales by transaction; film attributes (genre, rating, runtime, distributor, opening gross nationally, week of run); competing openers each week; local demographics by trade area; the buyer's booking history and, going forward, the one-line expectation recorded at each call; settled film rent terms by week.
**Target:** Next-week admissions and concession revenue per film per theatre; net theatre margin (admissions minus film rent at the settled scale, plus concession margin); for the adjustment layer, the residual between the buyer's choice and the base forecast's preferred choice, labelled by realised outcome.
**Evaluation metric:** Out-of-time error on next-week admissions (weighted MAPE by theatre size) against two baselines: the national week-over-week drop applied locally, and the buyer's own recorded expectation. The decision metric is net margin per screen-week under the recommended allocation, estimated on held-out weeks with off-policy correction because only the booked option is observed. Under-forecasting a strong holdover costs more than over-forecasting a weak one, because the dropped film's cheap late weeks are lost for good.
**Scope:** The data collection challenge comes first: the buyer's reasoning must be captured as they decide, so the system needs a near-zero-effort way to record an expectation during the Monday calls, and past decisions must be reconstructed from booking histories and emails. The labelling challenge is that buyers disagree with themselves, and the outcome is confounded by competition, weather and marketing, so a sample of decisions needs repeated blind judgements to measure the buyer's own consistency, and the counterfactual must be estimated from comparable theatres that made the other call. The deployment challenge is speed: the forecast must land Sunday night, read faster than a glance at the grosses, and respect commitments already made to distributors. 2 ML engineers and a programming analyst embedded with a circuit's film department, 6–9 months, with value appearing first as retrieval ("the last five films like this in this market held 70% into week three").
**Data availability:** Every circuit holds years of point-of-sale history in Vista, Veezi or a similar system, and that data is clean. Terms and settled rent sit in accounting records and emails and must be joined by hand at first. The buyer's expectations don't exist and have to be captured from now on. Independents' histories are scattered across separate systems unless a booking agent or ticketing vendor pools them with consent.

---

## 2. Showtime Scheduling Under Turn-Time and Crew Constraints
#optimization-fundamentals #dynamic-programming #monte-carlo-methods #markov-decision-processes #workflow-orchestration #worker-facing #automation

**Problem statement:** Given the week's booked films, auditoriums and a demand forecast by daypart, build each day's showtime grid to maximise expected net margin while respecting cleaning turn times, staggered let-outs the crew can clear, projector and playlist constraints, distributor commitments (minimum showtimes, auditorium size) and the ticketing system's publishing deadline.

**ML task:** Constrained combinatorial optimisation over start times and auditorium assignments, with stochastic demand sampled from the forecast and a simulation of crew turn capacity; re-optimisation as presales arrive
**Input data:** Film runtimes plus trailer and ad reel lengths; auditorium capacities, formats and seating type; demand forecasts by film, day and hour (entry 1); presales curves; crew rosters and observed turn durations by auditorium type; distributor commitments; historical schedules and their outcomes.
**Target:** A showtime grid per theatre per day, with a feasibility report on turn collisions and the expected margin difference from the manually built grid.
**Evaluation metric:** Expected net margin per day against the human schedule in a simulation calibrated on historical weeks, with hard-constraint violations (turns the crew cannot clear, missed commitments) counted separately and required to be zero. Late starts per weekend after deployment is the operational check.
**Scope:** The optimisation itself is standard. The work is in the constraints buyers and managers apply without stating them, which must be elicited and encoded. 1 operations-research engineer and 1 engineer integrating with the ticketing system's scheduling API, 4–5 months for a pilot circuit.
**Data availability:** Schedules, runtimes and sales are in the ticketing system. Turn durations are not measured and need a few weeks of timestamping by crew. Commitments are in the buyer's notes.

---

## 3. Showtime-Level Concession Demand Forecasting
#temporal-fusion-transformers #gradient-boosting #time-series-forecasting #feature-engineering #regularization #evaluation-metrics #quick-win #revenue-impact

**Problem statement:** Forecast item-level concession demand (popcorn sizes, fountain drinks, candy, hot food, bar) for each theatre by day and daypart from the booked film slate and presales, to set orders, par levels, prep quantities and counter staffing.

**ML task:** Multi-horizon probabilistic forecasting of item quantities with known future covariates (films, showtimes, presales, formats, discount nights)
**Input data:** Concession transactions linked to ticket transactions (per-capita spend by film and daypart); film attributes and audience mix proxies (rating, genre, family share); presales by showtime; promotions and loyalty offers; weather; local school calendars; supplier delivery schedules.
**Target:** Item quantity distributions by theatre-day-daypart; derived order quantities and prep plans.
**Evaluation metric:** Weighted quantile loss at the order-relevant quantiles, with asymmetric weights: stock-outs of the high-margin core items (popcorn, fountain) on peak nights cost more than modest over-ordering of shelf-stable stock, while over-prepping perishables carries direct waste cost. Report waste and stock-out rates in pilot theatres against manager-ordered controls.
**Scope:** A well-trodden forecasting problem made specific by the film slate. 1–2 data scientists, 3–4 months to a pilot. The transaction link between ticket and concession purchase is the most useful feature and is available in most cinema point-of-sale systems.
**Data availability:** Point-of-sale data is the exhibitor's own and complete. Recipes and item masters need cleaning. Supplier delivery calendars come from the distributor.

---

## 4. Film Rent Terms Extraction and Settlement Reconciliation
#large-language-models #transformers #seq2seq #feature-engineering #evaluation-metrics #automation #data-integration

**Problem statement:** Extract engagement terms (sliding scale by week, floors, house allowances, firm terms, aggregate deals) from booking confirmations and emails into structured records, compute accruals from weekly grosses, and reconcile distributors' settlement invoices, flagging each difference with its likely cause.

**ML task:** Information extraction from semi-structured documents into a terms schema; rule-based computation; classification of reconciliation differences by cause (wrong week, wrong gross, wrong percentage, renegotiated, unrecorded)
**Input data:** Booking confirmations, distributor emails, settlement statements (PDF and spreadsheet), point-of-sale grosses by engagement, previous settlements.
**Target:** Structured terms per engagement; accrual per week; matched invoice lines with difference category and amount.
**Evaluation metric:** Field-level extraction accuracy on terms with zero tolerance for silent errors in percentages and floors, measured on a hand-checked sample; recall on invoice discrepancies above a materiality threshold, because a missed overcharge is lost money and a false flag costs a minute of review.
**Scope:** 1 ML engineer and 1 engineer with a film accountant as subject-matter lead, 4 months. The hard tail is terms changed by phone and never written down, which the system can only surface as unexplained differences.
**Data availability:** Documents and grosses are held by the exhibitor. Labels come from past settlements worked by the film accountant.

---

## 5. Booth Health Monitoring: Projectors, Keys and Accessibility Devices
#autoencoders #change-point-detection #survival-analysis #evaluation-metrics #worker-facing #automation

**Problem statement:** Detect projector, server and sound faults before they darken a show, predict laser or lamp end-of-life, verify that every scheduled show has a valid key, and track the charge and failure history of captioning and audio description devices that the ADA rule requires to be "fully operational."

**ML task:** Unsupervised anomaly detection on multivariate device telemetry; change-point detection on light output and temperature trends; time-to-failure modelling for lamps, lasers and device batteries; deterministic key-coverage checks
**Input data:** Projector and media server logs (light output, temperatures, fan speeds, error codes), theatre management system playlists and KDM inventory, service tickets with failure causes, captioning device check-out and charge logs.
**Target:** Fault risk per screen per day with a probable cause; remaining useful life per light source; key gaps per show; device units to retire.
**Evaluation metric:** Recall on failures that caused a cancelled or late show, with alerts delivered at least 24 hours ahead; false alerts per screen per month kept low enough that managers keep reading them. For devices, the share of check-outs that failed in use.
**Scope:** Telemetry formats differ by manufacturer (Christie, Barco, NEC, Sony) and server (Dolby, GDC). Failure labels are few per theatre, so models must pool across a circuit or a service vendor's fleet. 1–2 engineers, 4–6 months, best built by a service vendor or the theatre management system provider.
**Data availability:** Logs exist on the devices and in remote monitoring systems run by integrators. Failure causes sit in service tickets. Captioning device logs mostly don't exist and would start as a checklist.
