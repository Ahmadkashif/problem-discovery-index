# Work Location as an Address Field

**Niche:** [[niches/hr-tech-platforms/multi-jurisdiction-compliance/profile|Multi-Jurisdiction Employment Compliance]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Which jurisdiction's employment rules apply to an employee depends on where they actually work, and HR systems record a home address and an office assignment that may both be wrong.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in employment compliance content is fighting to detect a leave, sick time, pay transparency or classification rule change before an employer is configured wrongly against it — and whoever holds detection latency lowest takes the account.

## The Problem
An employee is recorded against a headquarters location because that is the office they were hired into. They moved two states away during remote working and told their manager but not HR. They spend a week a month at a client site in a third state. Their sick leave accrual, their minimum wage floor, their tax withholding and their pay transparency entitlements all depend on where they actually work, and the system holds a location that has been wrong for three years. Multiply across a distributed workforce and the employer's entire jurisdictional footprint — the list of rule sets it needs to comply with — is derived from a field nobody maintains.

## Why It's Still Broken
Work location was a trivial field when everyone worked at an office, and remote work made it a compliance determinant overnight without anyone changing the data model. Employees have no incentive to report a move and frequently do not realise it matters. Employers are ambivalent about asking, because establishing that employees work in new jurisdictions creates obligations — registration, withholding, compliance — that are easier not to have discovered. That ambivalence is the least defensible part of the situation and is worth naming.

## What a Fix Looks Like
Make work location a maintained, dated attribute rather than a static field. Ask employees directly and periodically, in a way that makes clear why it matters to them — their entitlements depend on it, which is true and is a better framing than a compliance request. Reconcile against signals the employer already has where it is proportionate to do so: payroll tax withholding jurisdiction, expense claims, device network location at a coarse level. Be explicit and narrow about what is used, because location monitoring of employees is a serious matter and a compliance justification does not license continuous tracking. Record location as a history with effective dates, so entitlement calculations use where the employee worked at the time rather than where they are now. Surface the employer's derived jurisdictional footprint as a standing report — here are the forty-one jurisdictions your workforce currently triggers, and here are the eleven you are not configured for — which is the artefact that connects this to the rest of the sub-niche and which most distributed employers have never seen.

## Who Feels the Pain
Employees accruing entitlements under the wrong jurisdiction's rules; HR compliance teams who cannot state their own footprint; and employers discovering registration and withholding obligations retroactively.

## Impact If Fixed
The jurisdictional footprint report is a query over a properly maintained location field and it typically reveals obligations the employer did not know it had, which is uncomfortable and is far cheaper to discover internally than through an agency. Dated location history is the schema change that makes retroactive entitlement calculation correct rather than approximate.
