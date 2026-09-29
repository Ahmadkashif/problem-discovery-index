# Fix: Green Means Whatever the Integration Could See

**Niche:** Control State Normalisation
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A passing control means the platform's integration checked something and was satisfied, and nobody is told what it checked or how much of the estate it covered.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #data-integration #worker-facing #hypothesis-testing
**Contested on:** Whether "this control is implemented" means anything comparable across two organisations, or describes configurations with nothing in common.

## The Problem

A control shows green. What the customer concludes is that the control is implemented. What actually happened is that an integration queried a system, received a response, applied a rule, and was satisfied.

The distance between those two statements is where the problems live. The integration may have checked one of the organisation's three cloud accounts, because that is the one connected. It may have verified that a setting is enabled at the tenant level without checking whether it is enforced per user. It may be reading a policy document's existence rather than any technical state. It may have checked a sample. It may be evaluating a rule written for a different provider's terminology.

None of this is disclosed. The dashboard says passing, the readiness percentage counts it, the auditor is shown the evidence, and the certificate issues.

The customer's security team frequently knows the control is thinner than the dashboard suggests — they know about the unconnected account, the group with the standing exception, the subsidiary outside the tenant. But the platform's output is the artefact that travels, and it says green.

## Why It's Still Broken

**The product's appeal is simplicity.** Green means done is what makes these platforms pleasant to use and easy to sell. Every qualification added to that reduces the clarity that is the product's main attraction.

**Disclosure looks like a weakness.** A platform that states what its integration did not check is describing the limits of its own coverage, while a competitor's dashboard shows the same control green with no caveat. The buyer comparing them sees a worse product.

**Coverage gaps are usually the customer's doing.** The unconnected account, the subsidiary outside the tenant, the shadow estate — these are the customer's environment. A platform that surfaced them prominently would be telling paying customers that their setup is incomplete, which is correct and unwelcome.

**Auditors accept the artefact.** If the platform's evidence satisfies the auditor, there is no external pressure to qualify it. The audit is the forcing function and it is not forcing this.

**Nobody measures verification depth.** There is no metric anywhere for what a control check actually established, so the variation between a thorough check and a nominal one is invisible even inside the platform.

## What a Fix Looks Like

**State what was checked, on every control.** Which systems, which accounts, what proportion of the population, by what method, when. A single line per control. This is the fix and it requires no new data — only surfacing what the integration already knows about its own scope.

**Report estate coverage prominently.** What fraction of the organisation's actual cloud accounts, identity tenants, repositories and endpoints the platform can see. A readiness percentage computed over sixty per cent of the estate should say so next to the number, every time.

**Distinguish observed from asserted.** Controls verified by technical observation, controls verified by a document's existence, and controls attested by a person. Three categories, plainly labelled. Many customers would be surprised by how many of their green controls are in the second and third.

**Surface unconnected systems as a finding.** Detected accounts, tenants and repositories not connected to the platform, raised as a gap rather than silently excluded. This is discoverable from the connected systems themselves and is currently invisible.

**Alert on integration staleness loudly.** A check that has not returned fresh data should not display as passing. This is the specific failure where continuous monitoring reports green because nothing is being monitored, and it is the most dangerous version of the whole problem.

**Give the auditor the verification detail.** Audit evidence packages should include what was checked and what was not, so the auditor's judgement is informed rather than deferred to the platform's rule.

## Who Feels the Pain

The organisation, which believes a control is in place across its estate and has it in place across the part that happened to be connected.

The security engineer, who knows the dashboard overstates reality and finds their own platform's output being quoted back at them as evidence.

The enterprise buyer and the insurer, treating a certificate as a statement about an organisation when it is a statement about a subset of systems of undisclosed size.

And the auditor, whose independent judgement is quietly replaced by a vendor's rule whose scope they were never shown.

## Impact If Fixed

Stating what was checked, per control, costs one line and converts an opaque verdict into an inspectable claim. It is the cheapest meaningful improvement in this category.

Estate coverage reported alongside readiness would immediately reveal the most common and least discussed failure — a compliance programme covering the systems that were easy to connect.

And loud alerting on stale integrations would close the specific gap where the monitoring says everything is fine because the monitoring stopped, which is the failure mode this entire product category is supposed to prevent.
