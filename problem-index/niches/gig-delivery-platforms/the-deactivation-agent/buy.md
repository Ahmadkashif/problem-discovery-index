# Buy: Trust & Safety Tooling Adapted to Deactivation

**Niche:** [[niches/gig-delivery-platforms/the-deactivation-agent/profile|The Deactivation Review Agent]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Trust and safety platforms review content items; here the reviewed object is a person's livelihood and the decision is increasingly governed by statute.
**Tags:** #evaluation-metrics #confidence-intervals #descriptive-statistics #compliance #large-language-models #workflow-orchestration #automation #worker-facing
**Contested on:** Whether item-review tooling can carry an enforcement decision that removes someone's income under jurisdictional protections.

## The Problem

Trust and safety tooling has matured and is worth buying: case management, queue routing, policy versioning, reviewer interfaces, QA sampling and appeals workflow are all better in the vendor products than in most in-house builds.

The category was shaped by content moderation, where the object is a post, the decision is remove-or-keep, the action is reversible at no cost to anyone's income, and the reviewed party has no economic relationship with the platform. A deactivation is none of those. The object is an account with thousands of deliveries behind it, the action ends a job, reversal does not restore the lost weeks, and in a growing set of jurisdictions the whole process is subject to statutory requirements on notice, evidence and appeal.

## What Already Exists

The dedicated T&S platforms and the fraud-side vendors, discussed in [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]. Queue management with priority routing, policy libraries with versioning, structured reviewer interfaces, decision audit trails, QA sampling and appeal routing. All of it works and none of it should be rebuilt.

## The Customization Gap

**The object is a working history, not an item.** The reviewer needs volume, trend, complaint composition, GPS corroboration, photos and chat across a year, not a flagged artefact plus thin context. The interface has to be built around an entity timeline with statistical context, which is a different product from an item queue.

**Base rates have to be in the interface.** Content moderation rarely needs a population comparison — a policy violation is one regardless of how many posts the author made. Here the same two complaints mean opposite things at twenty deliveries and at six hundred, and no vendor interface has a slot for a percentile. Adding it is the highest-value change and is entirely outside what the products model.

**The action space needs a middle with state.** Warnings with improvement windows, temporary order-type restrictions, review periods with exit criteria, required training — each needs its own state machine, expiry and escalation. Bought tooling models binary enforcement with an appeal.

**Jurisdictional protections are hard requirements now.** Several jurisdictions require a stated specific reason, advance notice for some categories, evidence disclosure and a genuine appeal with a human reviewer and a timeline. That is a compliance workflow with per-jurisdiction variation, auditable at the case level, and it is not in any T&S product because content moderation has no equivalent statutory regime of this shape.

**Money and obligations are in flight.** A deactivated courier may hold an undelivered order, pending earnings and a scheduled shift. Enforcement has to propagate coherently into dispatch and payments and unwind on reinstatement — a coupling the vendor products have no representation for.

## Target Customer

Platform trust and safety teams running or evaluating a T&S platform and finding the account-level, statutorily-governed decision does not fit the item-review model. Also the T&S vendors themselves, for whom platform-work enforcement is a distinct and growing segment with requirements their content-shaped products do not meet.

## Impact If Solved

The bought layer keeps handling queues, policy, audit and QA, and the platform adds the entity timeline, the base rates, the graduated state machine and the jurisdictional workflow. In practice: an agent sees a percentile instead of a raw count, has an action that fits a 60% suspicion, and the case record satisfies a statute rather than being reconstructed for it afterwards.
