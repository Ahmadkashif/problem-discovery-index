# Configured Rules Checked Against Current Law

**Niche:** [[niches/hr-tech-platforms/multi-jurisdiction-compliance/profile|Multi-Jurisdiction Employment Compliance]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An employer's accrual and leave configuration is a snapshot of what somebody understood the law to be when they set it up, and nothing compares it to what the law says today.
**Tags:** #bert #large-language-models #transformers #change-point-detection #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in employment compliance content is fighting to detect a leave, sick time, pay transparency or classification rule change before an employer is configured wrongly against it — and whoever holds detection latency lowest takes the account.

## The Problem
A city passes a paid sick leave ordinance with an accrual rate, a carryover cap and a covered-employee definition. The employer has eleven people there. Nobody in HR operations learns about it, because the ordinance was reported locally and the compliance content provider covers the state. The accrual engine continues applying the employer's default policy, which is less generous. Two years later the divergence surfaces — through an employee complaint, an audit or an agency inquiry — and the remediation covers two years for eleven people, plus whatever penalty applies. Every element of the failure is a detection problem.

## Why Nobody Has Built This
Content maintenance is a cost centre sized to the coverage sold, so coverage has a ceiling at the jurisdictions most customers care about, which is exactly the wrong prioritisation for a problem whose growth is in small jurisdictions. Comparing configuration to law requires representing the law in a form comparable to a configuration, which nobody has done — the content is delivered as guidance documents and the configuration is a set of accrual parameters, and the two never meet. And the liability framing discourages a vendor from asserting what the law requires, which is the same dynamic that keeps small-landlord and screening products shipping templates and disclaimers.

## What to Build
Jurisdictional rules as executable, versioned content, and a continuous comparison against each employer's configuration. Each rule set carries its scope — which employers, which employees, from which date — and the parameters that an accrual engine needs: rate, cap, carryover, waiting period, covered reasons, documentation limits. Employers resolve to their applicable jurisdiction stack from where employees actually work, which is the fix note's subject and is load-bearing. The comparison runs continuously and reports divergence with the affected population, the effective date and the magnitude, which is what makes it actionable rather than alarming. Where a rule requires interpretation, it routes to a human with the provision cited rather than being decided silently. And the remediation path is part of the product, including retroactive entitlement calculation, because an employer that discovers a two-year divergence needs to know what it owes and to whom.

## Target Customer
HCM vendors, compliance content providers, professional employer organisations and the distributed employers who acquired forty jurisdictions when they went remote.

## Impact If Built
The exposure is personal and accumulating: employees in covered jurisdictions are under-accruing entitlements they are legally owed, silently, for as long as the divergence runs. Continuous comparison converts that into a list with a date and a population, which is both a compliance correction and the only way the affected employees ever get what they were owed.
