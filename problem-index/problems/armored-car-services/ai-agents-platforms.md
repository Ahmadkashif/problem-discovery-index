# AI Agents & Platform Opportunities — Armored Car Services

**Industry:** [[armored-car-services|Armored Car Services]]

---

## 1. Stop-Risk Memory Platform
#ai-platform #cnns #object-detection #gradient-boosting #tacit-knowledge-ml #worker-facing

**Concept:** A platform that turns every truck's approach video, route context and crew decision into a site-by-site risk memory for the carrier. It re-identifies vehicles and people that recur near a carrier's stops across trucks and days, scores each approach before arrival from veterans' past decisions, and gives new messengers a briefing on how veterans handle each site. Security directors get a map of where pre-attack surveillance and aborted stops cluster.
**Inputs:** Truck camera feeds, telematics and route schedules; one-tap crew decisions and voice notes; incident and near-miss reports; local crime and calls-for-service data where licensed.
**Outputs / Actions:** In-cab pre-arrival alerts at a fixed alert budget; recurring-entity alerts for security analysts; site briefings for crews; quarterly evidence packs on risk controls for underwriters and bank customers.
**Why now:** Edge inference on vehicle cameras is now cheap enough to run on the truck, vision models re-identify vehicles across cameras well, and armored-carrier attacks — including ambushes of ATM technicians tracked by the FBI since 2022 — have made security a board-level topic at the carriers.
**Market:** The three national carriers first, as enterprise buyers, then regional independents through their insurers; adjacent to fleet-camera vendors, which record but do not learn crews' decisions. A small number of large buyers, so the sale is long and the reference value of the first carrier is high.

---

## 2. Cash Replenishment Agent
#ai-agent #time-series-forecasting #temporal-fusion-transformers #markov-decision-processes #automation #data-integration

**Concept:** An agent working for an ATM owner or a bank's cash operations team that forecasts every machine's and branch's cash needs, plans loads against the carrier's route days and value limits, places orders with the carrier and the Fed on time, and explains each order. It watches live dispense data and holiday or event calendars, and re-plans when a machine trends towards a cash-out, choosing between an earlier scheduled visit and an emergency run on cost.
**Inputs:** Dispense and deposit data by machine and denomination; branch cash positions; carrier route calendars, cut-offs and contract prices; Fed order windows and the recirculation fee policy; paydays, holidays and local events; cost of funds.
**Outputs / Actions:** Replenishment orders by machine, denomination and date; branch and vault orders; emergency-visit recommendations with the cost trade-off; monthly reports of cash-outs, idle cash and visits against contract.
**Why now:** Higher interest rates made idle cash a visible cost, cash's share of payments has settled at a floor (14% in 2024) rather than vanishing, and LLM interfaces let a small cash team supervise thousands of machines by exception.
**Market:** Banks, credit unions and independent ATM deployers; competes with forecasting vendors such as Morphis and OptiCash and with carriers' own managed services, and differentiates by planning against the truck rather than the machine alone.

---

## 3. Custody Exception Investigator
#ai-agent #bayesian-inference #large-language-models #data-integration #compliance #worker-facing

**Concept:** An agent that opens on every count discrepancy — deposit bag, ATM cassette or smart-safe cassette — pulls the scan trail, seal photos, vault-count clip, device logs and customer history, estimates where the difference arose, drafts the customer claim response or the internal investigation summary, and tells the affected crew where the case stands.
**Inputs:** Discrepancy events from vault systems; handheld scan logs; seal photos; vault and truck-door camera indexes; safe and ATM event logs; customer declarations and claim correspondence; investigation history.
**Outputs / Actions:** Evidence packs; origin probabilities; recommended resolution (close as customer miscount, adjust, claim against counterfeit, escalate to investigations); customer letters; crew status notices; monthly discrepancy analytics by customer, station and route.
**Why now:** LLMs can assemble and summarise mixed evidence quickly, carriers already capture most of the underlying scans and video, and provisional-credit programmes have multiplied the number of three-way counts that must agree.
**Market:** Carriers' vault operations and security departments; also retailers' cash offices and banks' cash-vault teams, which run the same disputes from the other side.

---

## 4. Branch Dispatch Copilot
#ai-agent #optimization-fundamentals #monte-carlo-methods #workflow-orchestration #worker-facing #automation

**Concept:** A copilot for the branch route supervisor that rebuilds the day's routes from call-outs, vehicle status, emergency orders and ATM alerts before crews arrive, respecting licences by state, truck value limits, customer windows, cut-offs and route variation rules, then updates customers' expected windows and logs every change for the security team.
**Inputs:** Rosters and licences; vehicle inspection status; route plans; emergency orders; ATM monitoring alerts; customer windows and penalties; traffic; learned stop-time distributions.
**Outputs / Actions:** Proposed rebuilt routes with reasons and expected lateness; customer notifications; overtime forecasts; a variation audit showing that no site's service time has become predictable.
**Why now:** Route optimisation is mature and cheap to run; what was missing is encoding armored-specific rules and accepting voice and chat instructions from a supervisor at 4:30 a.m., which language models now make practical.
**Market:** Branch operations at national and regional carriers; regional independents (86 of the 92 employer firms have fewer than 500 employees) are the natural buyers of a packaged version because they cannot build one.
