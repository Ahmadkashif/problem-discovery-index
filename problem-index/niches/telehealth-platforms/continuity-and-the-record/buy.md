# Buy: EHR and Interoperability Products Adapted to a Platform With No Panel

**Niche:** [[niches/telehealth-platforms/continuity-and-the-record/profile|Continuity & the Fragmented Record]]
**Industry:** [[industries/telehealth-platforms|Telehealth Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** EHRs are built around a practice's panel of patients seen over years; a telehealth platform has millions of patients it may see once each.
**Tags:** #data-integration #compliance #workflow-orchestration #evaluation-metrics #large-language-models #confidence-intervals #automation #descriptive-statistics
**Contested on:** Whether panel-oriented clinical software can serve a platform whose patients have no panel.

## The Problem

Electronic health records and the interoperability layer around them are mature, heavily regulated and widely deployed. Charting, e-prescribing, orders, results, document exchange and patient portals all work, and several vendors offer configurations aimed at virtual care.

The design centre is a practice: a defined patient panel, a care team, a longitudinal chart built over years, and a clinician who knows the patient. A telehealth platform has an enormous patient population most of whom appear once, contractor clinicians who see any patient in a licensed state, and a chart that consists of one encounter. The software's assumptions about who is responsible for what do not hold.

## What Already Exists

Ambulatory EHRs with telehealth modules, virtual-care-specific EHR products, the interoperability frameworks and FHIR APIs, Direct secure messaging, provider directories, e-prescribing networks, and patient portal infrastructure. Document exchange between organisations is a solved, regulated problem.

## The Customization Gap

**There is no care team and no panel, so responsibility has to be modelled differently.** EHR workflows route results, messages and follow-ups to a responsible clinician. Here the clinician who saw the patient may not work today, so routing has to go to a team or a queue with defined ownership — a workflow redesign rather than a configuration.

**The chart is an episode and the useful object is a thread summary.** EHRs present a chart for a clinician who knows the patient. A telehealth clinician needs a generated summary surfacing what matters for this encounter, which is a different primary view and is what virtual-care EHR products mostly do not provide.

**Write-back to an external provider is not a standard workflow.** EHRs exchange records with organisations that request them. Proactively pushing every encounter to a primary care provider the platform identified from a patient's answer is a routing problem involving directory lookup, delivery confirmation and failure handling, and no product does it as a default.

**Patient identity is weak.** A practice knows who its patients are. A platform has self-registered identities with no institutional verification, which makes deduplication, record matching and external exchange all riskier. A deliberate identity strategy is the platform's own work and underpins everything else.

**Volume and cost per encounter are different by an order of magnitude.** Per-provider EHR licensing and workflows designed for twenty patients a day fit poorly against a platform doing tens of thousands of encounters with contractor clinicians working variable hours across many states.

## Target Customer

Telehealth platforms selecting or replacing their clinical system, who need to know what a virtual-care EHR still leaves them to build. Also the EHR and interoperability vendors, for whom panel-less episodic care is a growing deployment pattern their products fit awkwardly.

## Impact If Solved

The charting, prescribing, exchange and portal infrastructure gets bought, and the team-based routing, thread summary view, proactive write-back, identity strategy and volume economics get designed. Concretely: a clinician opens a summary rather than an empty chart, and the encounter reaches the patient's own doctor without anyone doing anything.
