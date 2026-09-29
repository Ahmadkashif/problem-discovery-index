# Build: Exposure as a Managed Quantity

**Niche:** Reviewer Exposure Management
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An exposure accounting layer that measures what each reviewer actually saw, at what severity, and routes and presents work against a cumulative budget rather than a throughput target.
**Tags:** #gradient-boosting #cnns #confidence-intervals #evaluation-metrics #markov-decision-processes #worker-facing #compliance #automation
**Contested on:** Whether the amount and intensity of distressing material a reviewer is exposed to is a managed quantity or an incidental by-product of a queue someone else composed.

## The Problem

Every other industry that exposes workers to a cumulative hazard measures the dose. Radiation workers wear dosimeters. Noise exposure is integrated over a shift against a statutory limit. Chemical exposure is monitored, logged and capped, and the employer can produce the record.

Content moderation exposes tens of thousands of people to a hazard that litigation has established is real, and measures nothing. A reviewer's day is recorded as decisions completed, average handling time and quality score. What they actually saw — how many items at what severity, how many involving children, how many depicting death, whether the severe items arrived in a run or spread across eight hours — exists nowhere. The vendor cannot state it for one reviewer on one day, let alone across a career.

The consequences are immediate and practical. There is no threshold to enforce because there is no quantity. There is no way to spread severe material across a team rather than concentrating it on whoever happened to be fast. There is no evidence when a claim arrives, so the vendor litigates blind on the exact question the claim turns on. And no vendor can demonstrate to a client, a regulator or a prospective employee that its operation is meaningfully safer than a competitor's, which means the market cannot reward one that is.

## Why Nobody Has Built This

**Measuring creates a record.** The moment a vendor can state how much severe material a reviewer saw, that record is discoverable. Counsel's instinct is that the safest position is not to know — and it is a coherent short-term position, which is why it has prevailed. It is also wrong over any longer horizon, because the absence of a record is itself becoming the finding in these cases, and a vendor with a dosimetry record and an enforced cap is in a far stronger position than one with neither.

**The severity label has to come from somewhere.** Scoring an item's psychological severity before a human sees it means classifying it, which means either the platform's classifier output — which the vendor usually cannot see — or the vendor's own models running on the client's content, which the contract may not permit. The data access problem sits upstream of everything.

**Capping exposure reduces throughput.** A cap means a reviewer stops or switches queues while work remains. Under a per-decision contract that is directly costly, and the client did not agree to it. Any vendor moving first bears the cost alone in a market that competes on price.

**The client owns the queue.** Routing decisions that would spread severe material across a team require control over assignment the vendor may not have, because in many arrangements reviewers pull from a platform-managed queue.

**Nobody has defined the units.** Radiation has sieverts. There is no accepted unit of psychological exposure, no established dose-response curve, and no threshold anyone can cite. Building the measurement means proposing the metric, which is scientifically uncertain and commercially exposed in a way that invites attack.

## What to Build

**A severity model and an exposure ledger.** Every item routed to a person carries a severity vector before it is shown — category, intensity, victim characteristics, whether the material is real or depicted — sourced from the classifier where available and from the vendor's own model where not. Every assignment writes to a per-reviewer ledger: what was shown, at what severity, at what fidelity, for how long, and whether it was escalated. The ledger is the product; everything else is what the ledger makes possible.

**A cumulative budget, enforced.** Per shift, per week, per quarter, with separate budgets for the categories that evidence and reviewer testimony consistently identify as worst. When a reviewer approaches the budget, routing changes: they move to lower-severity queues, to appeals, to quality audit, or to training work. This is the intervention, and it requires nothing from the client except the right to assign within the queue.

**Spread rather than concentrate.** Assignment that accounts for what each reviewer has already absorbed today, deliberately distributing severe items across the team instead of letting them pool with whoever is fastest. The current system concentrates the hazard on the best workers, which is both harmful and precisely backwards.

**Recovery scheduling that is structural, not discretionary.** Mandatory lower-intensity work after a severe run, scheduled automatically rather than requested by a reviewer who has to identify themselves as struggling. Discretionary breaks are taken least by the people who need them most, which is the consistent finding wherever this has been studied.

**Publish the methodology, keep the model.** The unit definition, the severity taxonomy and the budget rationale should be open, developed with occupational health clinicians and offered to the industry. A vendor that defines the standard and can demonstrate compliance with it converts an unpriced liability into a competitive credential, and the standard is worth more shared than held.

**Evidence, deliberately.** The ledger, the enforced caps and the clinical outcomes tracked alongside them form exactly the record a vendor needs in front of a client, a regulator or a court. Build it knowing that is what it is for.

## Target Customer

The vendors themselves — Teleperformance, TaskUs, Concentrix, Majorel and the specialist tier — sold to the operations leadership and the general counsel jointly, because the argument is simultaneously operational and about liability that is already crystallising.

Platforms are the second buyer and an increasingly motivated one, since supply-chain labour conditions have become a reputational and regulatory exposure for them regardless of who employs the reviewer.

## Impact If Built

The hazard becomes manageable because it becomes measurable, which is the entire history of occupational health in every other industry that has one.

The vendor gets something to compete on other than price. A demonstrable exposure standard is the first non-price differentiator this industry has had, and it is the kind clients under public scrutiny will pay for.

And the concentration effect reverses. Today the fastest, most capable reviewers absorb the most severe material because throughput routing sends it to them, which is a mechanism for destroying exactly the people the operation most depends on.
