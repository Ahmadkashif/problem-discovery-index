# Fix: The Connector Broke and the Dashboard Stayed Green

**Niche:** Evidence Collection & Continuous Monitoring
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An integration stops returning data and the control it verified keeps displaying its last known state, which was passing.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing
**Contested on:** Whether continuous monitoring reports the state of the estate or the state of the integrations.

## The Problem

Someone rotates a service account credential during an infrastructure cleanup. The compliance platform's connector to that system starts failing. The failure appears in a log, and possibly in an email nobody routes anywhere.

The controls that connector verified keep showing their last observed state. They were passing when it broke, so they show passing. The readiness percentage counts them. The evidence package includes their last observation, dated three months before the audit period ended. And the organisation's security team believes, because their dashboard tells them, that multi-factor authentication is enforced across the estate.

Three months later something changes in that system — a group is created without the policy applied, an exception is granted and forgotten — and nothing detects it, because nothing is looking. The dashboard is still green.

This is the specific failure the product exists to prevent. Continuous monitoring is the entire value proposition over periodic audit, and a monitoring system that cannot distinguish "checked and fine" from "could not check" has silently reverted to being a point-in-time snapshot with a misleading interface.

## Why It's Still Broken

**Stale and passing render identically.** The data model holds a control status and a last-updated timestamp, and the interface shows the status. Distinguishing them requires treating staleness as a state rather than as metadata, which is a deliberate product decision nobody has made.

**Alerting on broken connectors is noisy.** Connectors fail transiently, all the time. Alerting on every failure trains people to ignore the alerts, so platforms tune the alerting down, which is how a persistent failure disappears into the noise.

**Nobody is on call for compliance.** Production monitoring failure gets a page. Compliance monitoring failure gets an email to a shared mailbox, and the compliance manager who receives it may not have the access to fix an integration anyway.

**The customer broke it, usually.** Credential rotation, permission changes, account restructuring. Platforms are reluctant to alarm customers repeatedly about the customer's own changes, so the messaging is soft.

**Auditors have not caught it.** Evidence dates are visible in the audit package and are rarely scrutinised against the period. If the audit does not catch it, there is no consequence, so there is no pressure.

**Showing red loses deals.** A product that honestly displays fifteen controls in an unknown state looks worse in a demonstration than one that shows everything green, and procurement compares demonstrations.

## What a Fix Looks Like

**Add an explicit unknown state.** Not passing, not failing — unverified since a date. Displayed distinctly, excluded from the readiness percentage, and shown in the audit package as what it is. This is the fix, it is a data model change, and everything else follows from it.

**Define a freshness threshold per control and enforce it.** Beyond the threshold, the control moves to unknown automatically. The threshold can be conservative; what matters is that it exists and is applied without anyone deciding.

**Escalate persistent failures to a person with access.** A connector down for more than a short window should reach the engineer who can fix it, not the compliance mailbox. Routing by the system involved rather than by the compliance function is a small change with a large effect.

**Watch for scope contraction, not just failure.** A connector that still succeeds and returns fewer resources than before is the more dangerous case, because it looks healthy. This is detectable by tracking the observed population per check and is currently detected by nobody.

**Put connector health on the audit package.** A summary of integration uptime and evidence freshness across the period, included in what goes to the auditor. Auditors would use it if it were there, and its presence would immediately make this a competitive dimension.

**Report it honestly in demonstrations.** The product that shows unknown states accurately is the better product, and the way that becomes a selling point rather than a liability is by explaining what the competitor's all-green dashboard is concealing.

## Who Feels the Pain

The organisation, which believes a control is enforced and stopped verifying it months ago — and which may discover the gap through an incident rather than through the dashboard that was supposed to prevent one.

The security engineer, whose actual estate has drifted while the compliance view says it has not.

The auditor, presented with evidence that is technically dated and presented as current, whose scrutiny is the only remaining check and who is not looking for this.

And the enterprise buyer and insurer at the end of the chain, relying on a certificate issued partly on observations that stopped being made.

## Impact If Fixed

An explicit unknown state is a small change that prevents the category's defining failure. A monitoring product that cannot say it has stopped monitoring has a defect, not a limitation.

Routing persistent failures to someone with access to fix them would resolve most of these within days rather than at the next audit.

And including connector health in the audit package would create the external pressure that makes every platform fix this, because the moment auditors compare evidence freshness across vendors it becomes a competitive requirement.
