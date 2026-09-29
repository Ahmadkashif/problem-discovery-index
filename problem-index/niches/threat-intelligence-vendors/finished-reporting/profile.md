# Finished Intelligence Reporting

**Parent Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Category:** Low Digitized
**Contested on:** Whether a finished assessment reaches the person who can act on it in a form they can act on, or is published to a portal and read by nobody in particular.

## Profile

**Market Size:** ~$850M
**Share of Parent Industry:** ~17%
**Digital Adoption:** Very low — a document to a portal
**Target Buyer:** CISOs, intelligence consumers, detection engineering
**Automation Potential:** Moderate — distribution and matching automate, the analysis does not

## What Makes This a Distinct Niche

Finished intelligence is the analytical product: an assessment of an adversary group, a campaign, a malware family, a sector threat landscape. An analyst spends a week or more producing something careful, sourced and considered.

It is published to a portal. Subscribers may receive an email. And then nothing — no vendor can tell an analyst whether a single customer changed anything as a result, because there is no mechanism by which that information would return.

The contest is about reaching the right reader with something actionable. A strategic assessment aimed at a CISO and a technical write-up aimed at a detection engineer are different products for different people, and both arrive as documents in the same portal. The CISO reads the summary of a report they may not need; the detection engineer needs the technical detail extracted into something they can implement and has to do that extraction by hand.

Meanwhile the reporting's relevance to any particular customer is unassessed. A report on an adversary targeting a sector the customer is not in arrives identically to one describing a campaign against their exact stack.

## Current Tools & Gaps

Portals with a report library, search and tagging. Email alerting on new publications. Some sector and adversary filtering. Analyst briefings and advisory calls for larger accounts. ATT&CK mapping in technical reports, increasingly standard and genuinely useful.

The gaps are in targeting, extraction and feedback. Relevance is not assessed per customer, so every subscriber receives everything. Technical content is prose, so a detection engineer extracts the detectable behaviours manually into rules. Nothing links a report to the customer's own environment — whether they run the affected software, whether the described infrastructure appears in their telemetry. Reading is tracked at best as a page view, which says nothing about whether anything changed. And no vendor can report to its own analysts what their work produced, which is the reason the work does not improve.

## Problems

- [[niches/threat-intelligence-vendors/finished-reporting/build|🔨 Build: Reporting That Lands Where It Can Be Acted On]]
- [[niches/threat-intelligence-vendors/finished-reporting/buy|🛒 Buy: Intelligence Requirements Practice From Government]]
- [[niches/threat-intelligence-vendors/finished-reporting/fix|🔧 Fix: Published to the Portal and Nobody Knows]]
