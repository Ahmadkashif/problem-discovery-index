# AI Agents & Platform Opportunities — Wired Broadband Providers

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]

---

## 1. Plant Fault Localization Platform
#ai-platform #cnns #graph-neural-networks #gradient-boosting #tacit-knowledge-ml #worker-facing #revenue-impact

**Concept:** A platform that keeps a fault ledger of every repair pinned to the plant map with downstream telemetry before and after, learns from it which impairment signatures point to which plant elements, and ranks likely fault locations for every new impairment and trouble call. It routes plant faults to maintenance crews with the location attached, keeps premises dispatches for genuine premises problems, and gives installers an evidence snapshot at closeout so repeats are attributed to the right cause.
**Inputs:** DOCSIS PNM telemetry, ONT optical levels and OTDR traces; plant topology and span lengths; trouble tickets and dispositions; repair logs with photos and locations; install closeout snapshots.
**Outputs / Actions:** Ranked fault locations per impairment; dispatch recommendations (premises, plant, remote, none); maintenance work orders; repeat attribution with evidence; a coverage view of which nodes are degrading.
**Why now:** DOCSIS 3.1 and 4.0 modems and modern OLTs report far richer health data than a decade ago, CableLabs has published the localisation methods, and the senior technicians who can read the data unaided are retiring.
**Market:** Cable operators below the top three, and fibre and copper telcos, who lack in-house PNM data science; sold directly or embedded in the network vendors and billing/OSS platforms the ~1,600–3,000 smaller operators already use (estimate). The largest MSOs build their own.

---

## 2. BDC and Subsidy Filing Agent
#ai-agent #large-language-models #k-nearest-neighbors #compliance #data-integration #workflow-orchestration

**Concept:** An agent that prepares each semiannual Broadband Data Collection filing and each subsidy milestone report: it reconciles plant and billing records to the current Fabric, explains changes since the last cycle, drafts Fabric challenges before the deadline, assembles location-level evidence for RDOF, A-CAM, ReConnect and BEAD milestones, and drafts responses when an availability claim is challenged.
**Inputs:** Fabric licence files from CostQuest; network map passings; billing addresses and speed tiers; prior filings and challenge outcomes; subsidy obligation lists and milestone dates; install and speed-test records.
**Outputs / Actions:** Draft BDC availability files ready for engineer certification; Fabric challenge submissions; milestone evidence packs; challenge rebuttals; a calendar of every federal and state deadline the operator carries.
**Why now:** The BDC replaced Form 477 with location-level reporting twice a year, BEAD added four-year buildout obligations in all 56 jurisdictions, and language models can now do the address normalisation and narrative drafting that made this consultant work.
**Market:** Small and mid-sized facilities-based providers, roughly 2,000–3,000 filers (estimate), who today pay regulatory consultants per filing; consultants themselves are also buyers.

---

## 3. Outage Communication Agent
#ai-agent #change-point-detection #large-language-models #worker-facing #automation

**Concept:** An agent that detects outages from device telemetry, maps the affected area, updates the status page and phone greeting, texts affected customers, briefs customer service representatives with cause and estimate for each caller's address, drafts updates from field notes as the repair progresses, and calculates bill credits when service returns.
**Inputs:** ONT and modem status, cabinet power alarms, topology, customer contact preferences, technician field notes, credit policy.
**Outputs / Actions:** Outage records; customer notifications; IVR and status-page updates; representative briefing panel; credit lists for billing.
**Why now:** Telemetry is already polled by element managers; cheap language models make well-written customer updates from terse field notes practical for a four-person care team.
**Market:** Rural telcos, co-ops, municipal systems and small fibre ISPs with small care teams; adjacent to billing/OSS vendors (NISC, Sonar, gaiia), who could bundle it.

---

## 4. Retention Offer Desk Agent
#ai-agent #causal-inference #survival-analysis #gradient-boosting #revenue-impact

**Concept:** An agent that, for every household approaching promo roll-off or calling to cancel, looks up which alternatives are actually available at the address, estimates the uplift of each offer, recommends the cheapest offer likely to retain, runs and reports a standing randomised holdout, and for telcos retiring copper sequences migration outreach by wire center.
**Inputs:** Billing and promo calendar; usage, outage and ticket history; FCC map competitive availability per address; fixed wireless eligibility and fibre construction footprints; offer catalogue and past outcomes; copper wire-center retirement plans.
**Outputs / Actions:** Per-account offer recommendations to the save desk or to automated outreach; holdout design and incrementality reports; migration outreach sequences.
**Why now:** Public location-level availability data from the BDC makes address-level competitive context cheap to build for the first time, and fixed wireless and fibre overbuild have made roll-off churn the industry's main commercial problem.
**Market:** Cable operators and telcos with retention teams; buyers are heads of retention and customer lifecycle; competes with churn modules in Amdocs and CSG and differentiates on address-level alternatives and measured uplift.
