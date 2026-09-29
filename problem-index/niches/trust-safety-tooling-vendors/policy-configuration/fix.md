# Fix: The Policy Changed and the Configuration Did Not

**Niche:** Policy Configuration & Deployment
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A policy is revised, published and communicated, and the classifier continues enforcing the previous version because nobody changed anything.
**Tags:** #evaluation-metrics #compliance #change-point-detection #workflow-orchestration #confidence-intervals #automation
**Contested on:** Whether a written policy becomes a classifier configuration that faithfully implements it.

## The Problem

The policy team revises a definition. A category boundary moves, an exception is added, a term is redefined. The policy is approved, published and communicated to the workforce and to users.

The classifier configuration is unchanged. Nobody told the engineer who maintains it, or they were told and the change did not obviously map to anything in the configuration, or they adjusted a threshold and nobody checked whether that implemented the change.

So the platform is publishing one policy and enforcing another. The gap may be small or may be substantial, and nobody knows which because nothing compares them.

The same happens in reverse. A vendor updates a model, a category's behaviour shifts, and the enforcement changes without any policy decision. The published policy is unchanged and the enforcement is different.

This is invisible by construction. The policy lives in a document, the enforcement lives in a system, and there is no artefact connecting them. Nothing raises an alert when they diverge because nothing knows they are supposed to correspond.

And the published policy is what users, regulators and courts will be shown as the platform's stated position.

## Why It's Still Broken

**Policy and configuration are in different systems with different owners.** No process connects a policy approval to a configuration review.

**Not every policy change maps to a configuration change.** Some revisions are clarifications that the classifier's behaviour already covers, which makes the review feel unnecessary until one does not.

**Nobody tests correspondence.** Without a policy test suite there is no mechanism that would notice, which is the underlying cause.

**Model updates change enforcement silently.** A vendor model update can shift behaviour without any configuration change, which is a divergence nobody initiated.

**The policy team does not see the system.** They write policy and have no visibility of what the classifier does, so they cannot notice the gap.

**Nobody asks.** No regulator has asked a platform to demonstrate that its enforcement matches its published policy, though the question is obvious and increasingly likely.

## What a Fix Looks Like

**Make policy approval trigger a configuration review.** Every policy change routes to whoever maintains the configuration, with an explicit decision recorded — configuration changed, or no change required and why. Two minutes and it closes the most common gap.

**Version the configuration against the policy.** The configuration records which policy version it implements. A policy version ahead of the configuration is visible immediately.

**Build the policy test suite.** Examples with intended outcomes, run against the configuration on every policy or configuration change, which is the mechanism that would detect divergence automatically.

**Review configuration on vendor model updates.** A model update can move enforcement without a configuration change, so the policy correspondence should be re-checked when the model changes.

**Give the policy team visibility.** The people who write the policy should be able to see what the system actually does with examples, which is the connection that would surface divergence without any process.

**Audit correspondence periodically.** Even without a test suite, a periodic check of a sample of policy provisions against the system's behaviour would find the gaps.

**Publish honestly where enforcement differs.** Where a published policy provision is not enforceable with the available tooling, saying so is more defensible than publishing a position the system does not implement.

## Who Feels the Pain

Users, who read a published policy and experience enforcement of a different one, in either direction.

The policy team, whose carefully revised definition is not in force and who have no way to know.

The platform, whose published policy is the document a regulator or a court will examine and which does not describe what the system does.

And the engineer maintaining the configuration, who is implementing a policy they did not write, may not have been told about, and has no test that would tell them whether they got it right.

## Impact If Fixed

Routing every policy approval to a configuration review with a recorded decision is two minutes per change and closes the most common divergence.

Versioning the configuration against the policy makes the gap visible immediately, and it is a field.

And a policy test suite run on every change is what would detect divergence automatically — including the divergence caused by a vendor model update, which nobody initiated and which nothing currently notices at all.
