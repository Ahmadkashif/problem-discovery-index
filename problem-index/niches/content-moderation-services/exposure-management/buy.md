# Buy: Occupational Health Monitoring for a Digital Hazard

**Niche:** Reviewer Exposure Management
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Industrial occupational health has a century of practice in dose measurement, exposure limits and surveillance, and none of it has been pointed at a hazard delivered through a screen.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #survival-analysis #compliance #worker-facing #data-integration
**Contested on:** Whether the amount and intensity of distressing material a reviewer is exposed to is a managed quantity or an incidental by-product of a queue someone else composed.

## The Problem

The discipline this industry needs already exists and is mature. Occupational health and safety has spent a century developing exactly this apparatus: identify a hazard, define a unit of dose, establish a dose-response relationship, set an exposure limit, measure individual cumulative exposure, enforce the limit through work rotation, and run medical surveillance to catch harm early. It is embedded in regulation, in software, and in the professional practice of industrial hygienists.

Content moderation has a hazard that litigation has established, a workforce of hundreds of thousands, and none of the apparatus. It has counsellors. The entire response sits at the medical surveillance end — support after harm — with nothing at the measurement and limitation end that does the actual work in every other industry.

The adaptation is not conceptual. It is that the hazard arrives through a screen rather than through air or noise, so nobody has thought of it as an industrial hygiene problem, and the software category serving that discipline has never been asked to model it.

## What Already Exists

Environmental health and safety platforms — Cority, Enablon, Intelex, VelocityEHS, Sphera, Gensuite — handle exposure monitoring, dose tracking against occupational exposure limits, incident management, medical surveillance scheduling and regulatory reporting. Cority and VelocityEHS in particular have well-developed industrial hygiene modules with sampling, exposure group modelling and cumulative dose tracking.

Adjacent practice: radiation dosimetry services with personal badge monitoring and lifetime dose registries; noise dosimetry integrating exposure across a shift; fatigue risk management systems in aviation and rail, which model cumulative cognitive load against rostering and are the closest structural analogue, since they constrain scheduling on the basis of accumulated strain rather than a chemical.

Clinical: PTSD and trauma screening instruments with established psychometrics; occupational mental health surveillance programmes in emergency services, which is the profession whose exposure profile most resembles this one.

## The Customization Gap

**No unit, no limit, no curve.** Every EHS platform assumes a defined dose unit, a published occupational exposure limit and an established dose-response relationship. Psychological exposure to distressing media has none of the three. Defining them — in collaboration with occupational health clinicians, and with enough rigour to survive challenge — is the adaptation's hardest and most valuable part, and it is research before it is software.

**The measurement is upstream, not on the worker.** Industrial hygiene measures the environment around a person with a badge or a pump. Here the dose is determined by what the routing system decided to show, which means exposure measurement has to live inside the work assignment system rather than beside the worker. No EHS platform integrates with a work queue, because no hazard has ever been delivered by one.

**Real-time control, not retrospective reporting.** EHS platforms report exposure after the fact for compliance. This hazard can be controlled at the moment of assignment — the item is about to be shown and the decision to show it is still available — which is a real-time routing integration nothing in the category has.

**Emergency-services surveillance is closer than industrial.** The clinical instruments that fit are the trauma-exposure ones used with first responders, not the respiratory and audiometric screening EHS platforms schedule by default. The surveillance module needs a different clinical content set.

**Fatigue risk management is the better template.** Aviation's model — cumulative load constraining the roster, with enforced recovery — maps far more closely than chemical exposure does, and no vendor has carried it across.

**Discoverability shapes the requirements.** A vendor adopting this creates a record that will be read in litigation. The platform must support defensible methodology documentation, versioned limits and auditable enforcement, because a partial or inconsistently applied record is worse than none.

## Target Customer

Cority or VelocityEHS are the plausible adapters — mature industrial hygiene modules, enterprise reach, and a strategic interest in extending beyond physical hazards as knowledge work develops recognised occupational exposures.

The buyers are the moderation vendors, purchased jointly by operations and legal. Beyond them the same adaptation fits every workforce with routine trauma exposure through a screen: emergency dispatch, child protection investigators, insurance claims handlers on catastrophic loss, and the trust and safety teams platforms staff in-house.

## Impact If Solved

A century of occupational health practice reaches a hazard that has been treated as an unavoidable feature of the work. The single most consequential idea in that tradition is that a hazard you can measure is a hazard you can limit, and this industry has never taken the first step.

A defined unit and a published limit would change the market's structure. Clients could specify it, regulators could reference it, and vendors could compete on it — none of which is possible while exposure remains unquantified.

And the adaptation generalises immediately to every other screen-delivered trauma exposure, which is a substantially larger population than content moderation alone.
