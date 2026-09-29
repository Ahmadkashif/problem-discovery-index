# Alerts Fire Millions of Times a Day and Nobody Measures Which Ones Matter

**Niche:** [[niches/pharmacy-independents/drug-compendia-pricing-publishers/profile|Drug Compendia & Pricing Content Publishers]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The publisher's interaction content interrupts pharmacists millions of times a day, most of the interruptions are dismissed, and the publisher never sees a single dismissal.
**Tags:** #gradient-boosting #evaluation-metrics #causal-inference #transformers #tacit-knowledge-ml

## The Problem
Every time a prescription is entered anywhere in the country, the pharmacy system screens it against the publisher's knowledge base: drug-drug interactions, allergy cross-sensitivity, duplicate therapy, dose range, disease contraindications. When something matches, the system stops and makes a person decide.

Alert fatigue in this setting is one of the best-documented findings in clinical informatics. Override rates for interaction alerts routinely run above ninety per cent. A pharmacist filling two hundred prescriptions a day dismisses alerts continuously, which means the alerts that matter are dismissed at the same rate as the ones that do not, because attention does not survive that volume.

The content publisher is the party that decides what fires. It grades severity, sets the pairs, and defines the logic. And it is structurally blind to the consequence: the alerts fire inside the customer's system, the pharmacist's response happens there, and no signal returns. Severity grades are assigned by clinical editors reading the literature — which is the right basis for whether an interaction is real, and no basis at all for whether an alert is worth interrupting someone over.

The result is a product whose central quality attribute has never been measured by the company that makes it.

## Why Nobody Has Built This
The business model puts a wall exactly where the feedback would flow. Content is licensed to system vendors, who embed it in software used by pharmacies. Override data belongs to the pharmacy, sits under HIPAA, and reaches neither the system vendor nor the publisher. Nobody designed this to be opaque; it is the natural consequence of a three-party licensing chain.

Severity grading is also a defensive act before it is a clinical one. An interaction downgraded and later implicated in a patient harm is a liability event for the publisher. Grading conservatively is individually rational and collectively produces the noise.

And the customers have never demanded it. System vendors buy content on coverage and currency — how many interactions, how fast updated — because those are the attributes procurement can compare. Nobody has ever been asked for a specification of alert precision.

## What to Build
A feedback loop the licensing chain currently prevents, and the models it enables.

**Instrument overrides at the source.** Negotiate with system vendors for de-identified alert-and-response telemetry: what fired, in what context, what the pharmacist did, and what reason they gave. This is a commercial and contractual project as much as a technical one, and it is the precondition for everything else. De-identified alert events are not protected health information and the pathway is well established.

**Model whether an alert will be acted on.** Given the alert type, the drug pair, the patient's regimen shape, the dispensing context and the prescriber, predict whether this alert changes what happens. That is a supervised problem with millions of labels a day once the telemetry exists.

**Grade severity and interruptiveness separately.** The clinical severity of an interaction and whether it warrants stopping a pharmacist are different questions currently answered by one field. Splitting them lets the content stay clinically conservative while the delivery becomes selective — which resolves the liability tension rather than fighting it.

**Use the override reasons as evidence.** When a pharmacist dismisses an alert as clinically irrelevant for a specific patient, they are stating an expert judgment the literature does not contain. Aggregated across the country these are the largest body of practising pharmacist reasoning that exists anywhere, and they are currently discarded a second after being produced.

**Publish the measurement.** Precision and action rate by alert class, reported. In a market where content is bought on coverage counts, being the first vendor with a measured signal-to-noise figure changes what procurement compares on.

## Target Customer
Chief Clinical Officer or VP of Content at a drug knowledge base publisher. The strategic argument is that coverage and update speed are now matched across the main vendors, and clinical decision support quality is the only remaining axis — and it is unmeasured by everyone.

## Impact If Built
Alert fatigue is a recognised patient safety problem, and the party best positioned to fix it is the one that has never seen the data. Closing that loop would improve the safety performance of a system that touches essentially every prescription dispensed in the United States, and would give the publisher a defensible product claim no competitor could answer.
