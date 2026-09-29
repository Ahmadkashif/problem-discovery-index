# Fix: The Assessment Happens After the Decision

**Niche:** Assessments & Documentation
**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The privacy review arrives when the feature is built and the launch is scheduled, at which point it can document the risk or delay the release.
**Tags:** #evaluation-metrics #compliance #worker-facing #workflow-orchestration #confidence-intervals
**Contested on:** Whether an impact assessment changes what gets built, or documents a decision already taken.

## The Problem

A product team designs a feature, builds it, tests it and schedules the launch. Two weeks out, someone remembers the privacy assessment. A request goes to the privacy team with a deadline.

At that point the assessment has two possible outcomes. It can conclude the processing is acceptable, possibly with mitigations that will be implemented later, and the launch proceeds. Or it can identify a problem requiring a design change, which means delaying a launch with commercial momentum, engineering already reassigned, and a marketing plan in motion.

The second outcome happens rarely, and when it does the privacy team is the reason the launch slipped. So the practical function of the assessment is to document the processing and specify mitigations that can be added around a design that is fixed.

The alternative was available and cheap. The same review at design, before the data model was settled, could have narrowed the collection, chosen a different identifier, set a retention period in the schema or picked a vendor with a better transfer position. All of those are nearly free before the build and expensive after it.

Everyone involved knows this. The assessment arrives late because nothing in the product process triggers it earlier, and because the privacy team has no visibility of what is being designed until it is finished.

## Why It's Still Broken

**Nothing triggers the assessment at design.** The trigger is someone remembering, and the moment people remember compliance requirements is when they are preparing to ship.

**The privacy team cannot see the pipeline.** They are not in design reviews, not on product specifications, and not in architecture discussions, so they cannot initiate anything earlier.

**Early involvement looks like friction.** Product teams experience privacy as a blocker, so involving them early feels like inviting delay, when it is precisely what avoids it.

**Capacity forces triage.** A small privacy team cannot participate in every design discussion, so they engage where the process forces them to, which is at the end.

**Late objection is punished.** An assessment that blocks a launch damages the relationship, which teaches the privacy team to find ways to say yes — which teaches product teams that the assessment is a formality.

**The document is what is required.** Regulation requires the assessment to exist. Nothing requires it to have influenced anything.

## What a Fix Looks Like

**Trigger from design artefacts, not from launch readiness.** A new data field in a schema, a new external integration in an architecture document, a new data source in a pipeline definition. These are machine-detectable and they occur at design, which is where the trigger belongs.

**Give the privacy team pipeline visibility.** Access to the product roadmap and design review process, so they can engage selectively and early rather than being handed finished work.

**Use a lightweight screen at design and a full assessment only where needed.** Most designs need a short set of questions, not a formal assessment. Reserving the heavy process for the genuinely high-risk cases lets a small team engage early and often, which is the capacity fix.

**Make it a design input, not an approval gate.** Framed as helping shape the design rather than approving it, early involvement is welcomed. Framed as a gate, it is avoided until unavoidable.

**Publish patterns so teams self-serve.** Common designs with their privacy positions already worked out — how to handle identifiers, what retention to default to, which vendors are pre-approved — so teams can build correctly without an assessment at all. This is the golden-path idea applied to privacy.

**Measure whether assessments change anything.** Track how many resulted in a design change. A programme where assessments never alter a design is running a documentation exercise, and knowing that is the first step to fixing it.

**Do not punish the early objection.** An organisation that treats a design-stage privacy concern as useful input rather than as an obstacle gets them raised early, which is cheaper for everyone.

## Who Feels the Pain

The privacy team, arriving too late to influence anything and then blamed for either delaying a launch or approving something they had reservations about.

The product team, hit with a compliance requirement at the worst moment, which teaches them to see privacy as an obstacle.

The organisation, which builds systems that collect more than necessary and retain longer than needed, because the cheap moment to decide otherwise passed unnoticed.

And the individuals whose data is collected by a design nobody questioned while questioning it was still free.

## Impact If Fixed

Triggering from design artefacts moves the assessment to the moment it can change something, which is the entire difference between a design instrument and a document.

A lightweight screen at design with escalation to full assessment lets a small team engage across the whole pipeline, which is what makes early involvement feasible rather than aspirational.

And measuring how often assessments change a design would tell an organisation whether its privacy programme influences anything — a question most have never asked and most would not like the answer to.
