# Machine Learning Opportunities — Ticketing & Reservation Agencies

**Industry:** [[ticketing-agencies|Ticketing & Reservation Agencies]]
**Derived from:** [[problems/ticketing-agencies/high-impact|High Impact]], [[problems/ticketing-agencies/low-impact-1|Low Impact 1]], [[problems/ticketing-agencies/low-impact-2|Low Impact 2]], [[problems/ticketing-agencies/worker-life-1|Worker Life 1]], [[problems/ticketing-agencies/worker-life-2|Worker Life 2]]

---

## 1. Learning the Ticketing Director's Scaling and Release Read
#tacit-knowledge-ml #gradient-boosting #survival-analysis #bayesian-inference #causal-inference #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Experienced ticketing directors look at a venue map, an artist's history and a market and "know" how each section will sell, how many seats to hold and when to release them, a judgement built over hundreds of onsales that they cannot write down. The ML problem is to learn that read from past scaling decisions and seat-level outcomes and put it in front of whoever scales the next show.

**ML task:** Seat- and section-level time-to-sale modelling (survival analysis with censoring for unsold seats) plus regression of the first-week resale premium, conditioned on the price level and hold plan; a recommendation layer that proposes price levels and release timing within the artist's price ceiling.
**Input data:** Venue seat maps with sightline and section attributes; historical scaling sheets and hold plans; seat-level sale timestamps, prices and channels from the primary system; presale registration and queue counts; artist streaming and prior-tour sales by market; day of week and competing events; resale listings and sold prices from marketplace feeds; the director's annotated release decisions where they exist.
**Target:** Probability a seat sells by each hour after onsale and by show day; realised price; resale premium over face in the first seven days; agreement between the model's proposed scaling and the expert's.
**Evaluation metric:** Concordance index and calibration of time-to-sale curves, measured strictly on onsales after the training window. Error in predicted resale premium by section, reported against a naive "same as last tour" baseline. Overpricing costs unsold seats, discounts and a fan backlash; underpricing costs the resale spread. Report both errors separately and weight them by the artist's stated tolerance, not symmetrically.
**Scope:** The data collection challenge comes first. The expert's reasoning has to be captured at scaling and during the onsale, so the system needs a near-zero-effort way to log a hold release or price change with a reason. Historical decisions have to be reconstructed from scaling sheets and inventory logs. The labelling challenge is that resale price is a biased label: it reflects the seats brokers chose to list, and fee rules and state caps shift it. Unsold seats are censored, not zeros, and directors scale similar shows differently depending on recent memory, so repeated blind scaling of past shows is needed to measure the expert's own consistency. The deployment challenge is speed. The recommendation must land inside the first minutes of an onsale, faster than the director reads the sales map, or it is ignored. Expect 2 ML engineers, 1 data engineer and a ticketing director seconded part-time, 6-9 months. Value appears first as retrieval ("the last five times this building sold this genre on a Tuesday") before any recommendation is trusted.
**Data availability:** Seat-level sales sit with the primary ticketing company, but under agreements with the venue or promoter, so a promoter, team or large venue is the natural owner of the project. Resale prices are observable from marketplace feeds and listing scrapes. The decision ledger does not exist and building it is most of the work.

---

## 2. Linked-Account Cluster Detection at Onsales
#graph-neural-networks #dbscan #graph-theory #gradient-boosting #evaluation-metrics #compliance #automation

**Problem statement:** Find groups of buyer accounts controlled by one broker that together exceed an onsale's per-person purchase limit, the conduct the BOTS Act and the FTC's 2025 complaint target, without blocking real fans who share a household, card or office network.

**ML task:** Graph construction over accounts, devices, payment instruments, addresses, phone numbers and transfer recipients; community detection plus a supervised classifier scoring each cluster as one controlling buyer or independent fans.
**Input data:** Account registration and login telemetry; device and network fingerprints; payment tokens and billing addresses; queue and checkout events; post-sale ticket transfers and resale listings matched back to purchasing accounts; past enforcement actions and manual review outcomes.
**Target:** Cluster label (single controller or not); estimated tickets controlled per cluster; whether those tickets later appeared on resale within 72 hours.
**Evaluation metric:** Precision at the review queue's capacity, since every flagged cluster is a human review and a wrongly cancelled fan order is a public complaint. Recall is measured on the share of first-week resale listings traced back to flagged clusters. False-block rate on verified-fan accounts is a hard constraint set with the artist.
**Scope:** Graph features and community detection give a strong baseline in 2-3 months for 2 engineers. The supervised layer needs review labels, which arrive slowly, and adversaries adapt within weeks, so the model must be retrained per major onsale. Expect a standing team, not a project.
**Data availability:** Held by each primary platform; resale matching needs marketplace cooperation or listing scrapes. Labels come from trust-and-safety reviews and, increasingly, from enforcement records.

---

## 3. Resale Price Trajectory and Delivery-Risk Forecasting
#temporal-fusion-transformers #gradient-boosting #time-series-forecasting #survival-analysis #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** For a broker or marketplace holding inventory across hundreds of events, forecast each event's resale price path to show day and the probability that each listing fails delivery, so repricing and buying decisions use evidence rather than the current lowest listing.

**ML task:** Multi-horizon probabilistic forecasting of median and section-level sold prices by days-to-event; a separate survival model for delivery failure per listing.
**Input data:** Listing and sold-price histories by event and section across marketplaces; primary inventory remaining; artist and team signals (streaming, standings, injuries); venue transfer restrictions; broker delivery histories; state cap rules.
**Target:** Price quantiles at fixed horizons before the event; probability of non-delivery or late delivery per listing.
**Evaluation metric:** Pinball loss on price quantiles out of time, compared with a "last sold price" baseline; calibration of delivery-failure probabilities. A forecast that is right on average but misses the final-week collapse is worthless to a broker, so the last seven days are reported separately.
**Scope:** 2 data scientists, 4-5 months for a forecasting service; the delivery model is faster because labels are clean. Fan behaviour shifts with each tour cycle, so expect monthly retraining.
**Data availability:** Marketplaces hold sold prices; brokers hold their own sales and costs; listing data is scrapable but sold prices often are not. Delivery outcomes are logged by marketplaces.

---

## 4. Cancellation Refund and Chargeback Triage
#logistic-regression #gradient-boosting #large-language-models #bert #evaluation-metrics #automation #worker-facing

**Problem statement:** When an event is cancelled, postponed or a ticket fails at the gate, predict which orders will turn into card chargebacks, resolve routine refund and transfer contacts automatically, and assemble evidence for the disputes that arrive anyway.

**ML task:** Order-level chargeback propensity (binary classification with calibrated probability); intent classification and summarisation of support contacts; evidence-pack generation from order, delivery and policy records.
**Input data:** Order and payment records; event status changes and organiser refund authorisations; delivery and scan logs; support transcripts and emails; historical dispute outcomes and reason codes.
**Target:** Chargeback within the card-network window; contact intent and resolution; dispute won or lost.
**Evaluation metric:** Precision-recall on chargeback prediction at the outreach budget, since a proactive refund costs the fee margin and a chargeback costs the order plus a fee and a strike against the merchant account. For contact resolution, share resolved without an agent at a reopen rate below an agreed ceiling.
**Scope:** Propensity models are a 2-3 month build for 1-2 data scientists; contact automation with language models is similar but needs careful policy grounding, because policies change daily during a postponement.
**Data availability:** All internal to the platform or marketplace; reason codes from processors; historical transcripts need light labelling.

---

## 5. Statute-to-Rule Extraction for Ticket Pricing Compliance
#large-language-models #transformers #bert #evaluation-metrics #compliance #data-integration #quick-win

**Problem statement:** Turn federal and state ticketing statutes, rules and amendments into a structured, dated rule table (fee display, resale cap, speculative-listing ban, transfer rights, refund duties) that listing systems can enforce.

**ML task:** Clause extraction and slot filling from legal text into a fixed schema, with change detection between bill versions.
**Input data:** Enacted statutes and session laws, the FTC fee rule and its guidance, attorney-general guidance, and pending bills from legislative feeds.
**Target:** Rule records with jurisdiction, scope, threshold (for example 110% of original price), effective and sunset dates, and citations.
**Evaluation metric:** Field-level accuracy against lawyer-reviewed records, with zero tolerance for a wrong effective date or threshold. A missed rule is worse than a slow one, so every extracted record is reviewed before it goes live.
**Scope:** 1 engineer and a part-time lawyer, 2-3 months for the core states, then maintenance each legislative session.
**Data availability:** Statutes are public; the value is in the reviewed schema and the history of versions.
