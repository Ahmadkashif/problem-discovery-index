# Build: Test the Translation

**Niche:** Policy Configuration & Deployment
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A policy test suite — examples with the policy's intended outcome — run against the configuration, so the gap between what the policy says and what the system does is measured rather than assumed.
**Tags:** #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #automation #workflow-orchestration #data-integration
**Contested on:** Whether a written policy becomes a classifier configuration that faithfully implements it.

## The Problem

A platform's policy on harassment runs to several pages. It defines the harm, sets out what is prohibited, and states exceptions — quotation of harassment in order to report it, discussion in an educational context, reclaimed use within a community, satire.

The configuration is a category selection and a threshold. Possibly a custom-trained category for a platform-specific rule.

Whether the second implements the first is unknown. The exceptions in particular are conditions a classifier may not honour at all — a quotation of a harassing message and the message itself look similar, and whether the system distinguishes them is an empirical question nobody has asked.

Testing it is straightforward. Assemble a set of examples that the policy clearly covers, with the intended outcome for each, including the exceptions. Run them through the configuration. Compare. The disagreements are the translation gap.

Nobody does this. The policy team writes the policy, the solutions engineer configures the system, and the two artefacts are never compared. When a policy is updated, the configuration is adjusted and nobody checks whether the adjustment implements the change.

It is the most directly testable thing in the whole industry and it is not tested.

## Why Nobody Has Built This

**The two artefacts have different owners.** Policy is written by a policy team; configuration is set by an engineer or a solutions consultant. Neither owns the correspondence.

**Building the test set requires policy examples.** Assembling examples with intended outcomes requires policy judgement applied to specific cases, which the policy team can do and has not been asked to.

**The gap is uncomfortable.** A test showing that the system does not honour the policy's exceptions is a finding about both the policy and the vendor, and neither party has an interest in producing it.

**Exceptions are hard for classifiers.** Quotation, education and reclaimed use are exactly the context distinctions classifiers handle worst, so the test would mostly confirm a known weakness in an uncomfortably specific way.

**Nobody asks.** No regulator or buyer has asked a platform to demonstrate that its configuration implements its published policy.

**Configuration is treated as an integration task.** It is scoped as getting the product running rather than as implementing a policy faithfully.

## What to Build

**Build the policy test suite with the policy team.** Examples per policy provision, with the intended outcome, including the exceptions. A few hundred items per major category, assembled by the people who wrote the policy.

**Run it against the configuration and report the disagreements.** Where the system's decision differs from the policy's intended outcome, that is the translation gap, and it is the output that matters.

**Report exception handling separately.** Whether the system honours quotation, education, reclaimed use and satire is the part most likely to fail and most consequential for the users affected, and it should be reported on its own.

**Regression test on every change.** A policy update or a configuration change re-runs the suite, so a change that breaks an exception is caught before deployment.

**Record what cannot be represented.** Where a policy provision has no configuration equivalent, record the gap explicitly rather than approximating it silently. This is what makes the policy honest about what is enforced.

**Version policy and configuration together.** A configuration should reference the policy version it implements, so a policy change without a configuration change is visible.

**Put the policy team in the loop.** The people who wrote the policy should see what the configuration does with their examples, which is the connection that currently does not exist.

## Target Customer

Platform policy teams, who write the policy and have never seen evidence that the system implements it.

Vendors, for whom a policy conformance test is a differentiator that also protects them — a documented gap between a customer's policy and what the product can represent is better for the vendor than an unexamined assumption.

Regulators, who increasingly require platforms to publish policies and will eventually ask whether the enforcement matches them.

## Impact If Built

The most directly testable claim in the industry — that the system implements the published policy — becomes tested, and it is currently assumed.

Reporting exception handling separately would reveal the failures that most affect users who are discussing harm rather than causing it, which is where the documented over-removal harm concentrates.

And recording what cannot be represented would make a platform's published policy honest about what is actually enforced, which is a gap that currently sits entirely unexamined between two teams.
