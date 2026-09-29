# The Security Engineer Receiving the Report

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Underserved Audience
**Contested on:** Whether severity reflects what a finding means in this organisation's architecture, or a rating assigned by someone who has never seen it.

## Profile

**Market Size:** ~$420M
**Share of Parent Industry:** ~7%
**Digital Adoption:** Low — a PDF and a spreadsheet
**Target Buyer:** Client security engineering, application security leadership
**Automation Potential:** High for triage and routing, low for the prioritisation judgement

## What Makes This a Distinct Niche

The report arrives with eighty findings. One security engineer has to turn it into work that other teams — who do not report to them, have their own roadmaps, and did not commission the test — will actually do.

The severities are the immediate problem. They were assigned by a tester who saw the system from outside for two weeks and has no knowledge of what sits behind it: which service holds real customer data and which is a staging remnant, what compensating controls exist at the network layer, which component is being decommissioned next quarter, which team has capacity. A high on an internal tool nobody can reach is a high in the report and a waste of everyone's month. A medium on a payment path may be the most urgent item in the document.

So the engineer re-triages all eighty findings against architecture only they hold, converts them into tickets in the right team's format with enough context that an engineer who has never read a penetration test can act, negotiates priority with teams who have other plans, and chases closure for months. None of this is what they were hired for, none of it is in the engagement, and it is where most of a test's value is won or lost.

## Current Tools & Gaps

A PDF, exported into a spreadsheet, manually turned into tickets. Vulnerability management platforms ingest findings and track them to closure, and are deployed at larger organisations. Some testing firms offer a portal with findings and status. Retesting is a paid add-on on request.

The gaps sit squarely on the receiver's side. Severity arrives without architectural context and there is no structured way to adjust it that survives into the record, so the engineer's re-triage lives in their head or a private spreadsheet. Findings are described for a security audience rather than for the developer who must fix them, so each ticket needs rewriting. Nothing maps a finding to the owning team, which in a large organisation is real work. The same class of finding appears across many services and arrives as many unrelated items rather than one systemic issue. And there is no channel back to the firm to say a severity was wrong, so next year's report repeats the same misjudgement.

## Problems

- [[niches/penetration-testing-firms/the-security-engineer/build|🔨 Build: Severity in Context]]
- [[niches/penetration-testing-firms/the-security-engineer/buy|🛒 Buy: Vulnerability Management for the Manual Report]]
- [[niches/penetration-testing-firms/the-security-engineer/fix|🔧 Fix: Eighty Findings and One Person]]
