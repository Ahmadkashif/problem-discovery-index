# The Escalation That Carries Its Own Evidence

**Niche:** [[niches/customer-support-platforms/b2b-technical-support/profile|B2B & Technical Support]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A technical case escalates to a specialist who reads a thread, finds it insufficient, and asks the customer for logs and configuration — which is where most of the elapsed time in enterprise support goes.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in technical support software is fighting to make an escalation carry enough for the next person to diagnose without going back to the customer — and whoever makes escalations self-sufficient takes the account.

## The Problem
A customer reports that a scheduled job fails intermittently. The front-line engineer asks for logs; the customer sends a screenshot. Two exchanges later a log file arrives covering the wrong window. The case escalates to a specialist, who reads the thread, determines that the relevant configuration was never captured, and asks the customer again. It escalates to engineering, who need a reproduction that nobody has constructed. Eleven days have elapsed, the service level is breached, and the actual diagnosis — visible in the first log file if the right window had been requested — took forty minutes once the evidence was present.

## Why Nobody Has Built This
Diagnostic data collection has been treated as a conversation because the support platform has no relationship with the customer's environment, and the products that do have that relationship — observability, log management, the vendor's own telemetry — belong to different teams. Each escalation tier has its own idea of what it needs and none is written down, so the collection is negotiated case by case. And the cost falls as elapsed time in someone else's service level rather than as an identifiable line, which keeps it from being anyone's project.

## What to Build
Escalation as a package with defined requirements. Each escalation path declares what it needs — versions, configuration, logs for a specified window around the event, environment details, a reproduction or the evidence that one was attempted — as a checklist the case must satisfy before it moves, which is the single structural change and prevents the most common failure. Collection is automated wherever the product has a telemetry or diagnostic channel, which for most software products is available and unused for support; where it is not, the customer receives one specific request with a tool or a script rather than a conversation. The package is assembled and summarised for the receiving tier: what was reported, what has been established, what has been ruled out, what the evidence shows, and what the previous tier's hypothesis was — which is what a specialist needs and what a thread does not provide. And the measured outcome is escalations returned for insufficient information, which is a number every technical support organisation could compute today and none reports.

## Target Customer
Software and technical product companies with tiered support, support platform vendors serving them, and the engineering organisations receiving escalations they cannot act on.

## Impact If Built
Elapsed time in enterprise technical support is dominated by round trips for evidence, and the requirement is knowable in advance for each escalation path. Declaring it as a checklist and automating collection where the product allows it removes most of the delay, and the returned-escalation rate is the metric that would let an organisation see the problem it currently experiences as slowness.
