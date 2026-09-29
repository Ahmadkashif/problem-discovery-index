# Build: The Case, Not the Ticket

**Niche:** Case Management & Workflow
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model a moderation decision as a case with a recorded rationale, a subject who is affected, an appeal that reconsiders with more context than the original, and a record a regulator can follow.
**Tags:** #evaluation-metrics #confidence-intervals #graph-theory #compliance #workflow-orchestration #automation #worker-facing #data-integration
**Contested on:** Whether the workflow around the classifiers routes, records and appeals properly.

## The Problem

A moderation decision is modelled as a ticket. It arrives in a queue, a reviewer makes a call, the ticket closes, and an enforcement action fires.

What the model omits is everything that makes it a moderation decision rather than a support request. There is a person affected by the outcome, who may lose content, reach, income or an account. The decision may be appealed, and the appeal will be evaluated against a rationale that was frequently not recorded. The decision forms part of a pattern for that user, which nobody assembles. And a regulator may ask, in aggregate or specifically, why this decision was made — which requires a record the ticket does not contain.

The practical failures follow. An appeal is reviewed by someone who sees the item and not the reasoning, so they are making a fresh decision rather than reviewing one. A user wrongly actioned three times has three unconnected records. The same item reported by forty people generates forty cases in some deployments. And the audit trail, when a regulator asks, turns out to record the state change and not the basis.

## Why Nobody Has Built This

**Ticketing was the available starting point.** Many platforms built moderation on general ticketing because it existed, and the model carried through.

**Recording rationale costs reviewer seconds.** In a queue with a throughput target, a structured rationale field is friction, and its value appears later and elsewhere.

**Appeals volume is lower, so appeals tooling is thinner.** The main queue got the investment and the appeal path is the afterthought, which inverts the priority given what an appeal is for.

**User-level history raises questions.** Assembling a user's decision history is useful and is also a profile, which needs handling carefully — and the difficulty has meant it is not done at all.

**Audit requirements are recent.** Regulatory obligations to justify decisions have arrived faster than the systems have adapted.

**The affected person is not the customer.** The system serves the platform's operations, and the user experiencing the outcome has no standing in the product's design.

## What to Build

**Record the rationale, structured, at decision time.** The policy applied, the basis, the specific element of the content. Seconds to record and it is what makes an appeal a review rather than a fresh guess.

**Make the appeal see more, not less.** The original rationale, the full context, more time, and where the original was automated, a human. An appeal reviewed with less than the original decision is not a review.

**Assemble the user's decision history.** Every decision affecting one person, visible when reviewing a new one, so a pattern of wrongful action is detectable and a genuine repeat offender is too.

**Deduplicate reports into items.** Forty reports of one piece of content is one decision with a report count, which is both far less work and a stronger signal.

**Build the audit trail properly.** Who decided, on what basis, against which policy version, with what evidence, and what changed on appeal. This is what a regulator will ask for and it is frequently not reconstructable.

**Route by capability, not just by category.** Language, specialism and clearance, with the reviewer's current exposure as a constraint — which is the same routing problem described in [[industries/content-moderation-services|Content Moderation Services]].

**Close the loop with the affected user.** Tell them what was decided, on what basis, and what they can do. A decision communicated as a bare outcome is the source of most of the frustration these systems generate.

## Target Customer

Trust and safety operations leadership, for whom appeals quality and audit adequacy are becoming regulatory requirements rather than optional improvements.

Platforms subject to platform accountability regimes, which impose notice-and-action, redress and reporting obligations that current case systems frequently cannot satisfy.

Case management vendors in the category, for whom the case-versus-ticket distinction is the product argument against general ticketing adapted by a customer's engineering team.

## Impact If Built

Recording the rationale at decision time is seconds per case and is the single change that makes appeals meaningful, audits possible and quality measurable.

Assembling the user's decision history would make a pattern of wrongful action against one person visible, which is currently impossible and is where the most serious individual harms accumulate.

And an audit trail that records the basis rather than the state change is what regulatory obligations increasingly require, and what most systems would currently fail to produce.
