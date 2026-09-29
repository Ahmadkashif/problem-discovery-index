# Process Mining Applied to Knowledge Work

**Niche:** [[niches/work-collaboration-tools/work-status-inference/profile|Work Status Inference]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process mining reconstructs how a process actually runs from system event logs and is a mature discipline with commercial products, and it has been applied almost entirely to transactional ERP processes while knowledge work is described by people in meetings.
**Tags:** #graph-theory #hidden-markov-models #descriptive-statistics #evaluation-metrics #confidence-intervals #change-point-detection #hypothesis-testing #automation
**Contested on:** Every serious competitor in work management is fighting to say what is actually happening from the activity the tools already captured rather than from what somebody typed — and whoever makes status observed rather than reported takes the category's founding promise.

## The Problem
An organisation wants to know why its product launches take nine months. The answer is assembled from retrospectives and interviews, which produce a narrative. Process mining answers exactly this question for a purchase-to-pay process by reconstructing the real process from event logs, showing the actual paths, the rework loops, the waiting times and the variants — and knowledge work generates event logs of comparable richness in the collaboration tools, which nobody mines.

## What Already Exists
Process mining is a mature commercial category with established vendors, a substantial academic literature and open-source implementations. The core algorithms — process discovery, conformance checking, performance analysis over event logs — are well developed. Event log extraction from systems is standard practice. Every collaboration tool emits a detailed event stream through its audit and activity APIs. The methodology and the tooling are both available and have simply not been pointed here.

## The Customization Gap
The adaptation is to a process that is not a process in the ERP sense. It requires: (1) case identity defined sensibly, since a knowledge work process has no obvious case key and the right one is frequently a piece of work that moves across several tools — which makes the cross-tool identity problem this industry's last niche describes a prerequisite; (2) tolerance for enormous variant diversity, because knowledge work genuinely does not follow one path and a discovery algorithm tuned for structured processes will produce an unreadable spaghetti model — the useful output is the waiting and rework analysis rather than the process map; (3) waiting time attributed to what was being waited for, which is the single most valuable output and requires linking a gap in activity to the dependency that caused it; (4) rework detection, since knowledge work's characteristic waste is a document revised after a review that should have happened earlier, and that loop is visible in the event log; and (5) an explicit boundary against individual surveillance, because the same event data supports measuring a process and measuring a person, and which one gets built determines whether the organisation will tolerate it.

## Target Customer
Work management platform vendors, process mining vendors seeking a new domain, and the operations and transformation functions trying to understand why cross-functional work is slow.

## Impact If Solved
Waiting time and rework analysis over knowledge work event logs would tell organisations where their execution time actually goes, which is currently answered by retrospective narrative. The methodology is mature; the adaptation is case identity and an honest boundary on what the analysis is allowed to be about.
