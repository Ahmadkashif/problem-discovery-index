# Fix: Retention Is Set by Cost, Not by Dwell Time

**Niche:** Pre-Incident Evidence Readiness
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Log retention is a line in a budget negotiation, intrusions last longer than the retention window, and the two facts are never put side by side.
**Tags:** #survival-analysis #evaluation-metrics #confidence-intervals #compliance #revenue-impact #descriptive-statistics
**Contested on:** Whether an organisation can be told, before anything happens, which of its logging gaps will make the notification question unanswerable.

## The Problem

Log retention is decided commercially. The logging platform charges by volume and duration, the bill is large, and the retention period is negotiated down to what the budget allows. Thirty days is common. Ninety is considered good.

Intrusions routinely last longer. An attacker who gained access four months ago, moved laterally over several weeks and exfiltrated data two months in leaves a trail that begins entirely outside a ninety-day window. The responder arriving after discovery finds telemetry covering the last stretch and nothing covering initial access, lateral movement or the period when the data actually left.

So the investigation can establish the end of the story and not the beginning. Which means it cannot establish how the attacker got in, cannot rule out earlier activity, and cannot bound what left during the unretained period — which is precisely the question notification turns on.

The retention decision and the investigative consequence are made by different people at different times with no connection between them. Nobody presented the security team's retention budget as a choice about whether a future notification would be bounded or total.

## Why It's Still Broken

**Retention is a cost line and investigation is a hypothetical.** The bill arrives monthly; the incident may never happen. That asymmetry decides it.

**Dwell time is not in the conversation.** The organisation does not know the distribution, and the firms that do know it are not in the room when retention is set.

**Detection needs are short and drive the decision.** Detection works on recent data, so a short retention satisfies the people who look at logs daily, and their view prevails.

**Compliance retention requirements are unrelated.** Regulatory retention obligations cover different data for different reasons and are frequently mistaken for sufficient.

**Hot and cold storage tiers are underused.** Long retention in cheap cold storage costs a fraction of hot retention and is adequate for investigation, which needs to search history rather than query it fast. This is well known and inconsistently applied.

**Nobody costs the alternative.** The cost of a broader notification, caused by an unbounded scope, caused by a short retention window, is never computed and compared against the storage bill — which is the comparison that would settle it.

## What a Fix Looks Like

**Put the dwell time distribution in front of the retention decision.** Published incident data and forensics firms' own engagement histories give a realistic distribution. Setting retention below the median dwell time is a decision, and it should be made knowingly.

**Cost the notification consequence.** The expected cost of a notification that must assume everything, because scope could not be bounded, against the cost of the retention that would have bounded it. Both are estimable and the comparison is rarely close.

**Use cold storage for the investigative tail.** Full-fidelity retention in cheap archival storage for a year, with hot retention sized for detection. This is a fraction of the cost of extending hot retention and is adequate for forensic search.

**Retain the sources that answer scope, not everything.** Authentication, egress, file and object access, and administrative activity matter far more for scope than the bulk of ingested telemetry. Selective long retention of the investigative sources is cheap and is the practical fix.

**Snapshot on detection.** When something suspicious is detected, immediately preserve a wide window of telemetry before it expires. This is straightforward automation and it catches the common case where discovery happens with days of retention left.

**Get the forensics firm into the retention conversation.** A retainer provider is well placed to say which sources they will need and for how long, before the incident, and is almost never asked.

## Who Feels the Pain

The responder, arriving to find that the intrusion began before the telemetry did, and having to say so.

The organisation, notifying far more broadly than necessary because scope could not be bounded, at a cost that dwarfs the retention saving many times over.

The individuals notified unnecessarily, and the ones not notified because the evidence to establish their inclusion had expired.

And the security team, who negotiated a retention period down under budget pressure with no view of what it would cost later.

## Impact If Fixed

Putting the dwell time distribution next to the retention decision costs nothing and makes visible a trade that is currently made blind.

Selective long retention of the handful of sources that answer scope questions, in cold storage, captures most of the investigative benefit for a small fraction of the cost — which makes this one of the better-value security investments available and one nobody frames that way.

And automatic telemetry preservation on detection is simple automation that would rescue the evidence in the common case where discovery arrives just before expiry.
