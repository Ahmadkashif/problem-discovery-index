# Fix: The Same Benign Match, Every Week

**Niche:** The SOC Analyst Receiving the Alerts
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst investigates a match, concludes it is benign, closes it, and the same indicator fires again next week because nothing recorded the conclusion.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration #automation
**Contested on:** Whether the alerts an intelligence subscription generates are worth the analyst's attention.

## The Problem

An indicator matches a connection from an internal host. An analyst investigates: the address belongs to a content delivery network used by a supplier, the connection is routine, the indicator is from a report six months old. Benign. Ticket closed, four minutes.

Next Tuesday the same indicator matches the same traffic and a different analyst does the same investigation. The week after, again.

Nothing carries the conclusion forward. The disposition was recorded on a ticket, and the next alert is a new ticket with no reference to the previous one. Suppression exists as a capability and requires somebody to notice the pattern and write a rule, which requires spare capacity and an owner, neither of which the team has.

So skilled people repeat identical investigations indefinitely. The cost is not only the minutes — it is that the repetition teaches the team that this feed produces noise, and they begin dismissing its alerts faster, which is exactly the adaptation that eventually misses something real.

The information needed to stop it is entirely present. The system knows the indicator, the internal host, the destination and every previous disposition. Connecting them is a lookup.

## Why It's Still Broken

**Alerts are not joined to indicators.** Many deployments do not retain which indicator produced an alert in a form that supports querying previous alerts for the same one, particularly after deduplication.

**Suppression is manual and reactive.** Somebody must notice the pattern, decide it is safe, and write a rule. In a busy queue nobody has the time and nobody owns it.

**Suppression feels risky.** An analyst who suppresses an indicator and is later wrong has made a visible mistake, where one who investigates repeatedly has not. The incentive favours repetition.

**Tuning is nobody's job.** Detection engineering tunes detections. Threat intelligence alert tuning falls between the intelligence function and security operations.

**The repetition is invisible to management.** Alert counts and handling times are reported; how many were repeat investigations of the same benign match is not, so the waste does not appear in any metric.

**Analysts accept it.** It is experienced as the nature of the work rather than as a fixable defect, so it generates no escalation.

## What a Fix Looks Like

**Show prior dispositions on every alert.** Investigated four times in the last two months, dismissed as benign each time, with links. This is a lookup, it costs nothing, and it changes a four-minute investigation into a ten-second confirmation.

**Suggest suppression automatically after repetition.** When an indicator has been dismissed as benign several times against the same destination, propose a suppression rule with an expiry and a named approver. The proposal removes the need for someone to notice, and the expiry removes the fear of suppressing permanently.

**Time-bound every suppression.** A rule that expires and must be renewed means a suppressed indicator is reconsidered periodically, which addresses the risk that makes analysts reluctant.

**Report repeat investigations as a metric.** How much of the queue is re-investigation of previously dismissed matches. This makes the waste visible to the people who could fund fixing it, and it is computable from existing data.

**Give tuning an owner and time.** A named person with an allocation for alert quality, reviewing the repeat-investigation report weekly. Without an owner, tuning is what happens when someone is annoyed enough.

**Send the dismissals to whoever manages the subscription.** An indicator dismissed twenty times is telling the organisation something about the feed, and that information currently stops at the ticket.

## Who Feels the Pain

The analyst, performing the same investigation repeatedly, which is both wasteful and specifically demoralising in a way that general workload is not.

The team, whose learned response to a noisy feed is faster dismissal, which is where a real detection eventually gets missed.

The organisation, paying skilled people to re-derive conclusions their own systems already recorded.

And the vendor, whose feed is being discounted by the people using it, with no mechanism by which they would learn that.

## Impact If Fixed

Showing prior dispositions on the alert is a lookup against data already held and would eliminate most of the repetition immediately.

Automatic suppression proposals with expiry dates address both halves of the problem — nobody has to notice the pattern, and nobody has to fear suppressing something permanently.

And reporting repeat investigations as a metric would make a large, invisible waste visible to the people who allocate analyst time, which is the precondition for any of it being fixed.
