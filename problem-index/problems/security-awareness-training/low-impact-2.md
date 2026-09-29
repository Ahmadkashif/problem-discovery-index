# The Reporting Pipeline Nobody Resourced

**Industry:** [[security-awareness-training|Security Awareness Training]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The programme trains people to report suspicious messages, they do, and the reports arrive as an unmanageable queue at a security team that never asked for them.
**Tags:** #bert #transformers #gradient-boosting #k-nearest-neighbors #dbscan #confidence-intervals #evaluation-metrics #automation

## The Problem
The genuinely valuable behaviour an awareness programme can produce is reporting. An employee who reports a message that reached them gives the security team something the gateway missed, in real time, against a live campaign.

The consequence of success is a queue. A large organisation generates hundreds or thousands of reports a day, and the overwhelming majority are legitimate mail — marketing, newsletters, unusual but genuine internal messages, and the simulations the programme itself sent. Each must be assessed, because the one that matters is in there.

That queue lands on a security operations team already at capacity and is frequently the lowest-priority work, which means slow response. Slow response is exactly what destroys reporting behaviour: an employee who reports something and hears nothing for a week concludes it does not matter, and the programme's most valuable output degrades.

Campaign detection is the part being lost. Several reports of the same message across an organisation is a live attack in progress, and identifying that in minutes rather than days is the difference between blocking it and investigating it afterwards.

And the simulations pollute their own pipeline. A substantial share of reports are the programme's own tests, which consume triage capacity to no end.

## What Already Exists
Reporting buttons integrated into mail clients are standard and route to the platform, the security team or both. Some platforms auto-resolve reports of their own simulations. Email security vendors offer report triage with automated analysis of headers, links and attachments. Threat intelligence lookups on reported indicators are commonly integrated. Larger organisations have built their own triage automation with varying sophistication.

## The Customisation Gap
Clustering is the immediate unbuilt capability. Multiple reports of the same or similar message should collapse into one campaign object with the recipient list attached, which converts hundreds of individual triage tasks into a handful of campaign decisions and surfaces the live attack that is currently buried in volume.

Classification needs to be organisation-specific. What constitutes unusual mail depends on the organisation's normal traffic, its vendors, its internal conventions and its language, and a generic classifier will flag ordinary business correspondence as suspicious in some organisations and miss targeted lures in others.

Feedback to the reporter is the piece that sustains the behaviour and is the cheapest to build. An automatic acknowledgement with an outcome — this was a simulation, this was legitimate, this was malicious and has been blocked — takes a reporting programme from a void into a loop, and the reporting rate is the metric the programme should be optimising.

And the recipient list is the actionable output. When a report is confirmed malicious, everyone else who received it is identifiable, and remediating them before they act is the response that prevents harm — which requires the clustering and the mail system integration together.

## Impact If Solved
Employee reporting is the one output of an awareness programme with direct defensive value, and it is systematically undermined by a triage pipeline nobody resourced. Campaign clustering, organisation-specific classification, automatic reporter feedback and recipient-list remediation convert a burden into a detection capability — and sustaining the reporting behaviour is the thing that would make the whole programme worth running.
