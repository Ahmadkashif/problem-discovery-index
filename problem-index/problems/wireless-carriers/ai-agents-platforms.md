# AI Agents & Platform Opportunities — Wireless Carriers

**Industry:** [[wireless-carriers|Wireless Carriers]]

---

## 1. RF Optimisation Copilot
#ai-agent #graph-neural-networks #causal-inference #tacit-knowledge-ml #worker-facing #revenue-impact

**Concept:** An agent that works the daily worst-offender list alongside the RF engineer. For each degraded sector it assembles the counters, neighbour changes, alarms and measurements, proposes a likely cause with the closest past cases and their outcomes, drafts the parameter change or ticket, and grades the result two to four weeks later against matched control sectors. Over time it becomes the diagnosis ledger the carrier never had, and a running score of which playbooks and teams fix sectors.
**Inputs:** Performance counters, configuration and change logs, neighbour tables, alarms, drive-test and crowdsourced samples, engineer confirmations.
**Outputs / Actions:** Ranked cause hypotheses with evidence; draft change requests within policy limits; verification reports after each change; playbook and team effectiveness scorecards for managers.
**Why now:** Vendor platforms now expose counters and configuration to third-party apps (O-RAN rApps on service management and orchestration platforms), and language models can draft and explain diagnosis records cheaply enough that capturing them no longer depends on engineer discipline.
**Market:** National carriers' optimisation organisations, reached through the equipment vendors' app ecosystems; regional carriers and managed-services providers directly. Network-automation budgets exist; a graded diagnosis ledger doesn't.

---

## 2. Site-to-Air Agent
#ai-agent #large-language-models #transformers #workflow-orchestration #compliance #automation

**Concept:** An agent that runs each site modification from request to on-air. It checks the lease entitlement, prepares the tower-owner application, requests the structural and mount analysis, drafts the municipal eligible facilities request or small-cell application, and tracks every FCC shot clock and tolling notice. It chases each party and escalates the sites whose critical path is slipping.
**Inputs:** Deployment programme lists, lease and amendment records, site drawings and audit photos, prior structural analyses, municipal requirements, application status from tower-owner portals and permitting offices.
**Outputs / Actions:** Draft applications and permit packages; shot-clock calendars with deemed-granted dates; follow-ups to landlords, tower owners and engineers; a weekly forecast of on-air dates by market.
**Why now:** Language models can assemble application packages from drawings and prior filings, and 5G overlays and FWA capacity adds are pushing modification volumes that site development teams can't staff for.
**Market:** Carrier site development and real estate teams, and the site acquisition and engineering firms that work for them. Sitetracker is the incumbent workflow tool; an agent that does the paperwork rather than track it is the gap.

---

## 3. Port-Out and SIM-Change Guard
#ai-agent #gradient-boosting #autoencoders #compliance #automation #workflow-orchestration

**Concept:** An agent that sits on every port-out request, eSIM transfer and SIM change across store, care, web and app. It scores takeover risk from account, device and behaviour signals, applies the authentication and customer notice the FCC's 2023 order sets out, ahead of its compliance date, steps up verification only where risk warrants, and holds or reverses suspicious changes with an audit trail.
**Inputs:** Port and SIM-change requests, account history, device and session signals, care interaction transcripts, recent credential resets, fraud case outcomes, notification delivery records.
**Outputs / Actions:** Approve, step up or hold decisions; customer notices; fraud cases with evidence; compliance reports on authentication and notification.
**Why now:** eSIM makes a SIM change a software event that can happen in seconds from anywhere, the FCC's 2023 order will make authentication and notice a rule rather than a policy once its deferred compliance date is announced, and banks increasingly check SIM-change status before approving payments.
**Market:** Carrier fraud and identity teams. Identity vendors and bank fraud platforms are adjacent sellers, but none is built around the carrier's own port and SIM workflow.

---

## 4. WISP Qualification-to-Experience Platform
#ai-platform #cnns #time-series-forecasting #feature-engineering #revenue-impact #worker-facing

**Concept:** A platform for small fixed wireless ISPs that qualifies each address from LiDAR, terrain, foliage and sector capacity before the sale, schedules installs with a predicted aiming point, then monitors each subscriber's evening-peak experience and tells the operator which sector, link or interferer is degrading which homes and what to change.
**Inputs:** Tower and sector locations, radio telemetry, LiDAR and imagery, install outcomes, subscriber traffic and latency, plan tiers, support tickets.
**Outputs / Actions:** Address-level qualification with expected speed; install work orders; congestion and interference alerts; upgrade and plan-change recommendations; coverage maps for FCC filings.
**Why now:** Public LiDAR coverage has expanded, cheap inference makes per-address line-of-sight modelling affordable, and WISPs now face T-Mobile, Verizon and AT&T fixed wireless (14.7 million customers after Q3 2025) plus subsidised fibre, so a wrong install or a congested sector loses the customer.
**Market:** About 2,000 WISPs serving roughly 9 million customers. Today they buy point tools (TowerCoverage, Cambium cnHeat, Preseem) separately; nobody joins the pre-sale prediction to the post-sale experience.
