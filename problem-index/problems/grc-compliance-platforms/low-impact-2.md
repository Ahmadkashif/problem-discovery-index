# Evidence Integrations and Control Drift

**Industry:** [[grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Continuous monitoring reports that a control is passing until an integration silently stops returning data, and then it reports that too.
**Tags:** #change-point-detection #time-series-forecasting #gradient-boosting #graph-neural-networks #confidence-intervals #evaluation-metrics #data-integration #compliance

## The Problem
The automated tier of this category rests on integrations: cloud provider APIs, identity systems, device management, ticketing, code repositories, HR systems. Each supplies evidence that a control is operating, continuously, which is genuinely better than the annual screenshot it replaced.

Integrations break. Credentials expire, permissions are narrowed during a cleanup, an API version is deprecated, a resource moves to an account the integration cannot see, a new region is opened and never connected. The failure modes are quiet: the platform receives less data or none, and a control that is evaluated over what it can see reports passing.

Coverage is the deeper version. An integration connected to one cloud account in an organisation with fourteen reports on one account, and nothing in the interface distinguishes a control that is passing everywhere from one that is passing where the platform happens to be looking. Auditors rarely probe this, so the gap persists through certification.

And exception handling accumulates. Controls have documented exceptions — a legacy system that cannot support a requirement, a service account that cannot use multi-factor authentication — recorded with a justification and an expiry that nobody revisits. Over years the exception set becomes a second, undocumented compliance posture.

## What Already Exists
Integration catalogues are the core of the automated platforms and are extensive and well-maintained. Continuous control monitoring with alerting is the category's headline feature. Evidence is timestamped and retained for audit. Exception workflows exist with approval and expiry fields. Cloud security posture management vendors cover adjacent ground with better cloud-native coverage and weaker framework mapping.

## The Customisation Gap
Coverage must be a first-class reported quantity. A control's status should be qualified by what the platform can actually see — this many of your accounts, this share of your endpoints, this fraction of your repositories — and passing on partial coverage should look different from passing on full coverage. That single change would surface a great deal of currently invisible risk and is a presentation decision as much as a technical one.

Integration health needs monitoring against expectation rather than against errors. An integration returning data is not the same as an integration returning the right data, and forecasting expected evidence volume per integration — then flagging departures — catches the silent degradation that error monitoring misses entirely.

Estate discovery is the missing input. The platform knows what it is connected to and not what exists, and reconciling against independent discovery — cloud organisation structures, DNS, device inventories, code hosting — would identify the accounts, regions and repositories nobody connected.

And exceptions need lifecycle management with risk context. An exception that has been renewed four times is a permanent state misdescribed as temporary, and surfacing the aggregate exception posture — what it excludes, what risk it carries, how long it has persisted — turns an accumulating shadow into something governable.

## Impact If Solved
The automated compliance model's credibility rests on evidence that is continuous and complete, and it is quietly neither. Coverage as a reported quantity, integration health monitored against expected volume, reconciliation against independent estate discovery and exception lifecycle management address the gap between what these platforms report and what they actually observe — which is the difference between continuous assurance and a dashboard that is confident about a subset.
