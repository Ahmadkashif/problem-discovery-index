# Sample Code and Tutorial Maintenance

**Industry:** [[developer-relations-agencies|Developer Relations Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every advocacy programme accumulates dozens of sample applications and tutorials, and a developer's first experience of the product is running one that no longer works.
**Tags:** #gradient-boosting #change-point-detection #large-language-models #bert #graph-neural-networks #evaluation-metrics #automation #workflow-orchestration

## The Problem
Developer relations produces artefacts: sample applications, starter templates, workshop repositories, tutorial series, conference demo code. They are written to be persuasive at a moment and then left, and they rot faster than documentation because they depend on a full dependency tree rather than on a single API.

The rot is total rather than gradual. A sample application with an outdated dependency does not degrade gracefully; it fails on install, and the developer evaluating the product hits that failure in the first five minutes of their first experience. That is the single worst moment for a failure to occur and it is where these failures concentrate.

Discovery is by complaint, usually in a community channel, sometimes publicly. Ownership is unclear — the advocate who built a sample for a conference two years ago may have left, and nobody inherits it. The repositories accumulate, each carrying a small probability of being someone's first impression.

Workshops have an acute version. A workshop built for one event is run again six months later and half the room cannot get past setup, in a room full of people forming an opinion about the product.

## What Already Exists
CI on sample repositories, where it is configured, catches build and test failures automatically and is the effective intervention. Dependabot and Renovate handle dependency updates mechanically. Some platforms provide runnable sandboxes — StackBlitz, CodeSandbox, Gitpod, Codespaces — that remove local environment variance entirely, which is the strongest available fix. Container-based workshop environments do the same for events. Documentation testing frameworks verify embedded examples.

## The Customisation Gap
The gap is inventory and prioritisation rather than technique. Most organisations do not know how many sample repositories exist, which are actually used, which are referenced from documentation or talks, and which are someone's likely first touch. Assembling that inventory with usage signal — clone counts, referral sources, community mentions — identifies the small set where failure is expensive, and almost nobody has it.

Prediction is the second gap. A repository's decay risk is estimable from its dependency freshness, the release cadence of what it depends on, its last update and its CI status, and ranking by risk times exposure tells a small team which twelve of two hundred repositories to fix.

The third is that failure should be detected from the developer's side rather than the maintainer's. Community messages reporting that a sample does not work are a direct signal, and mining them to identify which artefact failed and how is faster than any scheduled check.

And the structural fix is to reduce environment variance — moving samples to sandboxes and workshops to containers — which is a decision about how artefacts are produced rather than how they are maintained, and is the intervention with the largest effect on first-experience failure.

## Impact If Solved
Sample code is frequently a developer's first execution of anything related to the product, and a failure there is disproportionately damaging because it happens before any value has been demonstrated. Inventory with exposure ranking makes maintenance tractable for a small team, decay prediction directs the effort, and moving to variance-free environments addresses the largest cause of first-run failure directly.
