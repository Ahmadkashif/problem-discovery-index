# Machine Learning Opportunities — Wired Broadband Providers

**Industry:** [[wired-broadband-providers|Wired Broadband Providers]]
**Derived from:** [[problems/wired-broadband-providers/high-impact|High Impact]], [[problems/wired-broadband-providers/low-impact-1|Low Impact 1]], [[problems/wired-broadband-providers/low-impact-2|Low Impact 2]], [[problems/wired-broadband-providers/worker-life-1|Worker Life 1]], [[problems/wired-broadband-providers/worker-life-2|Worker Life 2]]

---

## 1. Learning the Senior Technician's Impairment Read
#tacit-knowledge-ml #cnns #graph-neural-networks #gradient-boosting #feature-engineering #evaluation-metrics #worker-facing #revenue-impact

**Problem statement:** Senior maintenance technicians look at DOCSIS pre-equalization taps, full-band spectrum captures and OTDR traces and know what kind of impairment it is and which span, tap or connector is failing, a judgement built over years that they cannot specify. Learn that read from telemetry joined to the repairs that cleared it, and rank likely fault locations for whoever is dispatched.

**ML task:** Multi-class classification of impairment type (micro-reflection, ingress, suck-out, low-level, macrobend, dirty connector, splice loss) from signal representations, plus localisation as ranking over plant elements using a graph of the network topology
**Input data:** Pre-equalization coefficients and full-band captures from every modem (DOCSIS PNM), OFDM/OFDMA channel estimates where available; ONT optical levels and OTDR traces on fibre; plant topology and span lengths from the network map; repair records with location, part replaced and photos; telemetry before and after each repair.
**Target:** Impairment class per affected device; a ranked list of plant elements (tap, amplifier, span, closure) most likely to hold the fault; and whether the fault is in shared plant or a single premises.
**Evaluation metric:** Top-3 localisation accuracy against repairs that cleared the signature (signature present before, absent after), measured on later months than training. Recall on shared-plant faults matters more than precision: missing one sends trucks to many houses, while a wrong suggestion costs a maintenance technician a short detour. Report agreement with senior technicians alongside their own test-retest agreement on the same plots, which is the realistic ceiling.
**Scope:** The data collection challenge comes first: the expert's read has to be captured while they work, so the system needs a one-minute repair log on the technician's phone that pins the fix to the map, with telemetry attached automatically, and senior technicians reviewing ranked suggestions during a calibration period so their corrections become labels. The labelling challenge is that experts disagree with themselves and repairs bundle several fixes, so labels should come from before-and-after signature change, with a sample re-labelled blind to estimate intra-rater reliability. The deployment challenge is speed: suggestions must reach the dispatcher before a premises visit is booked and the technician's phone before they climb, faster than a senior glancing at a PNM screen. 2 ML engineers, 1 RF/plant domain lead and access to one region's maintenance team, 9–12 months; first value comes from the "many modems, one tap" localisation before any impairment classifier is trusted. Plant maps with wrong span lengths are the biggest single risk.
**Data availability:** Large cable operators hold PNM telemetry for millions of modems; mid-sized operators can collect it through vendor tools built on CableLabs methods. The decisive asset, repairs tied to locations and to signature change, mostly does not exist yet and has to be built prospectively. Fibre OTDR traces are stored inconsistently, often on the test set itself.

---

## 2. Trouble-Call Dispatch Triage
#gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #automation #revenue-impact

**Problem statement:** When a customer reports a problem, decide whether to send a technician to the premises, route the ticket to a maintenance crew at a known plant location, fix it remotely, or attach it to an impairment already being worked.

**ML task:** Multi-class classification with cost-sensitive decision thresholds
**Input data:** Ticket text and call-centre disposition; the account's modem or ONT telemetry over the past 30 days; neighbouring devices' telemetry on the same tap, splitter or node; open maintenance tickets and outages; the account's repeat and install history; weather.
**Target:** The dispatch that actually resolved the ticket (premises fix, plant fix, remote fix, no fault), derived from the final resolution and whether the account repeated within 30 days.
**Evaluation metric:** Expected cost per ticket under a cost matrix (a wasted premises visit, a repeat, a missed outage) compared with current practice, plus the repeat rate within 30 days. Calibrated probabilities matter because the call centre will act on thresholds.
**Scope:** A standard tabular problem once tickets and telemetry are joined; the hard part is that the "resolved" label is polluted by wrong resolution codes, so labels should lean on repeat behaviour and signature change. 1–2 data scientists, 4–6 months for a pilot in one market.
**Data availability:** Tickets, dispositions and telemetry are internal and abundant at any operator above ~50,000 subscribers (estimate); small operators need pooled models through a vendor.

---

## 3. Fabric Reconciliation and Availability-Claim Validation
#k-nearest-neighbors #large-language-models #feature-engineering #evaluation-metrics #compliance #data-integration

**Problem statement:** Match an operator's passings and billing addresses to FCC Fabric location IDs, and flag availability claims likely to be wrong before the semiannual filing.

**ML task:** Record linkage (address normalisation, geospatial nearest-neighbour candidate generation, pairwise match classification) plus a classifier for claim validity
**Input data:** Fabric location files with coordinates and unit counts; the operator's network map passings and drop lengths; billing and service addresses; prior filings and challenge outcomes; crowdsourced speed tests where licensed.
**Target:** Fabric location ID per operator address (or "no match"); per location, whether the claimed technology and speed are supportable within ten business days.
**Evaluation metric:** Match precision and recall on a hand-verified sample stratified by rural, multi-unit and new-build locations; for claims, the rate of sustained challenges in the following cycle. False positive claims cost credibility and subsidy eligibility; false negatives cede territory.
**Scope:** Address normalisation with a language model plus geospatial candidate search handles most cases; multi-unit buildings and rural addresses without street numbers are the hard tail. 1 engineer and 1 analyst, 3–4 months, reusable each filing cycle.
**Data availability:** Fabric files are licensed from CostQuest to filers; the national map's provider-level availability is public; operator records are internal.

---

## 4. Uplift-Targeted Save Offers at Promo Roll-Off
#causal-inference #survival-analysis #gradient-boosting #hypothesis-testing #evaluation-metrics #revenue-impact

**Problem statement:** For each household whose promotion expires, estimate how much each retention offer changes its probability of staying, given the alternatives actually available at its address.

**ML task:** Uplift modelling (conditional average treatment effect per offer) on top of a time-to-churn survival model
**Input data:** Promo calendar and price history; tenure, usage, outage and ticket history; bundle status; address-level competitor availability from public FCC map data, fixed wireless eligibility checks and fibre construction footprints; past offers made and outcomes; randomised holdouts where they exist.
**Target:** Churn within 90 and 180 days of roll-off under each offer versus no offer; retained revenue net of discount.
**Evaluation metric:** Qini coefficient and incremental retained margin on a randomised holdout. Without a holdout the model learns which customers save desks favour, not which offers work, so a standing randomised control group is part of the build.
**Scope:** 2 data scientists, 6 months, plus the operational change to run holdouts. Address-level competition data is the differentiating feature and needs refreshing every map cycle.
**Data availability:** Internal billing and CRM data are rich; competitive availability per address is public through the FCC National Broadband Map, with fixed wireless capacity the noisiest input.

---

## 5. Outage Detection and Customer Messaging From Device Telemetry
#change-point-detection #time-series-forecasting #large-language-models #worker-facing #automation #workflow-orchestration

**Problem statement:** Detect an outage within minutes from simultaneous device drops behind a shared element, estimate its extent and likely cause, and draft customer updates before the phones ring.

**ML task:** Online change-point detection over device-status counts per topology node, cause classification (power, fibre cut, upstream, equipment) and restoration-time forecasting, with an LLM generating customer messages from field notes
**Input data:** ONT and modem online status and alarms; cabinet power and battery alarms; topology; historical outages with cause and duration; technician field notes.
**Target:** Outage start and affected set; cause class; restoration time; message drafts.
**Evaluation metric:** Detection latency and false-alarm rate per week; share of affected customers notified before they call; restoration-time error. A false outage message erodes trust quickly, so precision at the notification threshold is the binding constraint.
**Scope:** Straightforward for operators with device status polling; topology accuracy again decides quality. 1 engineer, 3 months for detection and notification; cause and ETA models follow.
**Data availability:** Device status and alarms are already collected by OLT, CMTS and element managers; historical outage causes are recorded unevenly and need cleanup.
