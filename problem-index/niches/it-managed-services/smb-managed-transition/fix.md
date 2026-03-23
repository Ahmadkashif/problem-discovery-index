# Hybrid Break/Fix and Managed Service Delivery Confusion

**Niche:** [[niches/it-managed-services/smb-managed-transition/profile|SMB Break/Fix-to-Managed Transition MSPs]]
**Industry:** [[industries/it-managed-services|IT Managed Services]]
**Type:** Fix (Pain Point)
**One-liner:** Technicians working on both break/fix and managed clients in the same day apply the wrong service model — spending 2 hours on a break/fix ticket that should have been a 15-minute band-aid, or band-aiding a managed client issue that should be root-caused.
**Tags:** #workflow-orchestration #automation #worker-facing #revenue-impact

## The Problem
MSPs in transition maintain two service delivery models simultaneously: managed clients receive proactive monitoring and flat-rate support (every hour spent is a cost), while break/fix clients are billed hourly (every hour spent is revenue). Technicians context-switch between these models throughout the day without clear differentiation in the PSA. On a managed ticket, the correct behavior is to fix the root cause and prevent recurrence (reducing future ticket volume). On a break/fix ticket, the correct behavior is to resolve the immediate issue efficiently (the client is paying by the hour but the MSP wants throughput). Without clear service model tagging and workflow differentiation, technicians default to one mode: some over-invest in break/fix tickets (spending 3 hours root-causing when the client only authorized 1), while others under-invest in managed tickets (band-aiding issues that recur weekly).

## Why It's Still Broken
PSA platforms do not differentiate ticket workflow by service model. A ticket is a ticket — same priority levels, same routing rules, same SLA definitions. The distinction between "this client pays per incident, keep it efficient" and "this client pays flat rate, invest in prevention" exists only in the technician's memory and the service manager's verbal reminders. When the MSP has 60% managed clients and 40% break/fix, the confusion creates measurable margin impact: over-servicing break/fix clients without billing, and under-servicing managed clients leading to recurring tickets.

## What a Fix Looks Like
A service model layer in the PSA that tags every ticket with its delivery model (managed vs. break/fix vs. project), applies model-specific workflow rules (managed tickets trigger root-cause analysis prompts, break/fix tickets show authorized hours and budget remaining), and surfaces model-appropriate metrics to the technician (managed: "this client has had 3 similar tickets this month — investigate root cause" vs. break/fix: "client authorized 1 hour — estimate before proceeding"). The service manager dashboard shows per-model profitability and flags technicians who are systematically over-investing in one model.

## Who Feels the Pain
Technicians who waste effort applying the wrong service approach, service managers who see inconsistent delivery quality, and MSP owners who cannot understand why their managed contract margins are lower than expected.

## Impact If Fixed
Improves managed contract margins by 3-5 percentage points through proper root-cause investment, and increases break/fix billing capture by 10-15% through better scope management — together adding $50K-$150K annually to a 15-person MSP's bottom line.
