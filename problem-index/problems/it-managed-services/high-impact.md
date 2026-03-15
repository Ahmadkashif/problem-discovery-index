# Ticket Triage, Routing, and Automated Resolution for L1 Issues

**Industry:** [[it-managed-services|IT Managed Services]]
**Type:** High Impact
**One-liner:** 60-70% of MSP tickets are L1 issues that could be resolved without a human technician, and automating them transforms the entire service delivery margin.
**Tags:** #llm #bert #text-classification #nlp #automation #revenue-impact

## The Problem
MSP help desks receive a relentless stream of tickets — password resets, printer connectivity, VPN configuration, basic Office 365 issues — that consume L1 technician hours at scale. A 500-endpoint MSP may process 800-1,200 tickets per month, with the majority being repetitive L1 issues that follow predictable resolution paths. Technicians spend their days on these low-skill tasks instead of the L2/L3 work that actually prevents client churn. The result: bloated labor costs, slower SLA response times, and technician burnout that drives 30-40% annual turnover at the L1 level.

## Why It's Unsolved
Simple keyword-based routing rules in ConnectWise and Datto miss context: "can't print" could be a driver issue, a network issue, a permissions issue, or a hardware failure, each requiring different resolution paths. LLM-based classification needs to parse unstructured ticket descriptions that mix technical jargon with end-user language ("the thing on my screen won't go to the printer"). Automated resolution requires safe execution of remediation scripts on client endpoints, which demands tight integration with RMM agents and careful guardrails to avoid breaking production environments. MSPs also face a trust problem: clients paying for managed services expect human accountability, not a chatbot.

## What a Solution Looks Like
Inbound tickets are classified by an NLP model that identifies the issue category, urgency, affected system, and likely resolution path. For tickets matching known L1 patterns with high confidence (>95%), the system executes a pre-approved remediation script via the RMM agent — resetting a password, restarting a print spooler, flushing DNS — and closes the ticket with a resolution summary. Ambiguous or multi-symptom tickets are routed to the appropriate technician tier with a pre-populated diagnosis. The technician reviews automated resolutions in a daily digest, building a feedback loop that improves classification accuracy over time.

## Impact If Solved
Automating 40-50% of L1 tickets at a mid-size MSP saves 1.5-2 FTEs of technician labor annually (~$90-120K), while reducing average first-response time from 30 minutes to under 2 minutes for resolved tickets. The freed capacity lets MSPs take on more endpoints without hiring, directly improving per-endpoint margins from the industry-typical 8-12% to 18-22%.
