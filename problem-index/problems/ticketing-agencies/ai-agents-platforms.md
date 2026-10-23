# AI Agents & Platform Opportunities — Ticketing & Reservation Agencies

**Industry:** [[ticketing-agencies|Ticketing & Reservation Agencies]]

---

## 1. Onsale Decision Ledger and Scaling Platform
#ai-platform #tacit-knowledge-ml #gradient-boosting #survival-analysis #evaluation-metrics #revenue-impact

**Concept:** A platform for the people who own the onsale decision (promoters, teams and large venues) that records every scaling, hold and release decision with its reason, grades each one after the show against sell-through and resale prices, and recommends price levels and release timing for the next show within the artist's price ceiling. It keeps a departing ticketing director's record available to whoever scales the next tour.
**Inputs:** Seat maps, scaling sheets and hold plans; seat-level sales exported from the primary system; presale and queue counts; resale listings and sold prices; artist and market demand signals; the artist's price and fee constraints.
**Outputs / Actions:** Structured decision records; section-level sell-through and resale-premium forecasts; release-timing alerts during the onsale; post-show grading reports for the promoter and the artist's manager.
**Why now:** Rotating mobile tickets and marketplace data now make the resale price of almost every seat observable within days, the DOJ settlement's 15% fee cap pushes value back into the face price, and language models can draft decision records from scaling sheets and emails cheaply enough that capture no longer depends on discipline.
**Market:** Promoters, major-league and college ticket offices, and arena and theatre operators. The primary ticketers are both the obvious incumbents and conflicted. Venues opened to rival ticketers under the settlement need an independent record of yield to compare them.

---

## 2. Broker Inventory and Delivery Agent
#ai-agent #time-series-forecasting #gradient-boosting #data-integration #workflow-orchestration #automation

**Concept:** An agent that runs a broker's inventory across every resale marketplace. It keeps one seat-level record per ticket, delists everywhere within seconds of a sale, reprices against forecast price paths and state resale caps, schedules mobile transfers against each venue's transfer window and each marketplace's deadline, and reconciles payouts net of fees and penalties.
**Inputs:** Broker POS inventory and costs; marketplace listing, sale and payout APIs; primary-platform transfer status; venue transfer restrictions; jurisdiction rule tables; price forecasts.
**Outputs / Actions:** Listing creation, repricing and delisting; transfer execution and alerts; penalty-risk warnings; daily profit and loss by event and marketplace.
**Why now:** Mobile transfer flows and marketplace APIs are now standard enough to automate end to end, and new state caps make manual repricing a compliance risk as well as a cost.
**Market:** Thousands of small and mid-sized brokers who pay for POS and pricing tools today (estimate). Competes with marketplace-owned tools (SkyBox, TradeDesk) and differentiates by being neutral across marketplaces.

---

## 3. Ticket Pricing Compliance Agent
#ai-agent #large-language-models #bert #compliance #data-integration #automation

**Concept:** An agent that maintains a dated jurisdiction rule table from statutes and guidance, checks every listing and price display against it before publication, blocks speculative or over-cap listings, generates compliant all-in price displays and keeps an audit record of what each buyer saw.
**Inputs:** Federal and state statutes, bills and guidance; listing feeds with venue, event date, face value and fees; marketplace display templates.
**Outputs / Actions:** Listing approvals and blocks with reasons; fee display text; alerts on new laws and effective dates; regulator-ready audit exports.
**Why now:** The FTC fees rule (in force since May 2025), Executive Order 14254's push on BOTS Act enforcement and a wave of state caps such as Vermont's Act 109 have turned ticket compliance from a policy page into a per-listing control, and language models can read statutes into schemas with human review.
**Market:** Resale marketplaces, primary ticketers, brokers' POS vendors and affiliate sites. Regulatory-change and tax engines are adjacent sellers, but none handles listing-level resale rules.

---

## 4. Cancellation and Refund Resolution Agent
#ai-agent #large-language-models #logistic-regression #workflow-orchestration #worker-facing #automation

**Concept:** An agent that takes over when an event is cancelled, postponed or relocated, or a ticket fails at the gate. It reads each order's full state, applies the organiser's and marketplace's policy, issues refunds, credits or replacement seats within policy, contacts likely chargeback cases before they dispute, and assembles evidence packs for the disputes that arrive.
**Inputs:** Event status changes and organiser authorisations; order, payment, delivery and scan records; marketplace guarantees; support contacts; card dispute notifications.
**Outputs / Actions:** Automated refunds, credits and transfers; proactive outreach; agent handoff summaries; dispute responses filed within the network deadline.
**Why now:** Language models can resolve policy-bound contacts reliably when grounded in order data, and card-network alert programmes let merchants refund before a dispute becomes a chargeback.
**Market:** Primary ticketers, resale marketplaces, timeshare and park reservation services. Competes with general support automation and chargeback vendors, and differentiates on knowing event-status policy.
