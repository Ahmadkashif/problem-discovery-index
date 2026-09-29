# Maintenance Triage and Vendor Dispatch

**Industry:** [[proptech-platforms|Proptech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Work order systems are universal and competent, and the two decisions they leave to a busy site manager — what is this actually, and who should go — are the ones that determine cost and resident satisfaction.
**Tags:** #bert #large-language-models #word-embeddings #gradient-boosting #feature-engineering #evaluation-metrics #workflow-orchestration

## The Problem
A resident submits a work order: "kitchen sink leaking." That text is the input to a triage decision. Is it a supply line, a drain, a disposal, or a failing faucet cartridge? Is it urgent — water reaching a unit below is an emergency, a slow drip is not? Can the in-house maintenance technician handle it or does it need a licensed plumber? Which vendor, at what rate, and how fast will they actually come?

A site manager makes this call many times a day across a portfolio of units, from a sentence, with no equipment history and no evidence about vendor performance beyond who answers the phone. Getting it wrong costs in both directions: sending a plumber for a disposal reset is a wasted invoice, and treating an escalating leak as routine is a flood claim.

Vendor selection is decided almost entirely by relationship. Who is responsive, who has done work here before, who the previous manager used. Nothing in the stack records whether a vendor's work held, whether they charged what they quoted, or how long they actually took.

## What Already Exists
Every property management platform ships work orders with categories, priorities, assignment and status tracking. Resident portals and mobile submission are standard. Vendor marketplaces and dispatch networks (Lula, Property Meld, SMS Assist) exist and are growing. Photo and video attachment at submission is common. Preventive maintenance scheduling is available.

## The Customisation Gap
Categorisation is left to the resident, who selects from a dropdown they do not understand, or to a manager reading free text. Predicting the actual problem from the resident's description plus the unit's history is a well-shaped classification task on data every platform holds and none uses.

Urgency is the sharper gap. The difference between an emergency and a routine ticket is currently the resident's own priority selection, which is systematically unreliable in both directions. Predicting escalation risk — this description, in this building, with this plumbing age, has a meaningful chance of becoming a water damage claim — is exactly the kind of thing the platform's own claim history could support.

Vendor performance is the third and the most neglected. The platform sees every invoice, every completion time, every repeat work order on the same unit and component. Whether a vendor's repairs hold is directly measurable from recurrence, and nobody computes it. Dispatching on measured outcomes rather than on relationship is available to any vendor that decides to look.

## Impact If Solved
Maintenance is the largest controllable operating expense in rental housing and the primary driver of resident satisfaction and renewal. Better triage removes wasted trade visits; escalation prediction prevents the small number of claims that dominate the loss ratio; vendor scoring converts a relationship purchase into an evidence-based one.
