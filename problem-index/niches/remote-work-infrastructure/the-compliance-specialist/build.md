# Build: Tooling for the Person Holding the Jurisdictions

**Niche:** [[niches/remote-work-infrastructure/the-compliance-specialist/profile|The Compliance Specialist]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Route the changes, draft the determinations, track the currency and make the knowledge transferable, so the role stops depending on one person having read the right thing.
**Tags:** #large-language-models #compliance #data-integration #workflow-orchestration #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #worker-facing
**Contested on:** Whether generative drafting can support a determination without producing confident wrong answers.

## The Problem

A compliance specialist covering eight jurisdictions is doing three jobs simultaneously: keeping current with eight bodies of law, answering a queue of determination requests, and maintaining the guidance others rely on. All by reading, with a wiki and an inbox.

The failure modes follow. Currency slips because reading eight jurisdictions continuously is not possible alongside a queue. Determinations get made from guidance whose vintage nobody knows. Guidance goes unwritten because the queue is urgent and the wiki is not. And the knowledge concentrates personally, so a departure or a leave of absence removes a jurisdiction's coverage.

Nearly all of the week is retrieval, drafting and tracking — the parts that are now automatable — and very little is the judgement that requires the specialist.

## Why Nobody Has Built This

Compliance is a cost centre in a platform whose engineering goes into the customer-facing product. The specialists are few and their productivity has never been a roadmap item.

There is also a reasonable caution about generative assistance in legal work — a drafted determination that is confidently wrong is worse than a slower correct one. That caution is right about autonomous drafting and wrong about assisted drafting, and the distinction has not been made.

## What to Build

Assistance across the three jobs, with the judgement left with the specialist.

**Route the changes to the owner.** Monitoring of each jurisdiction's primary sources, filtered for relevance by a model, routed to the specialist who owns that country, with a tracked disposition — relevant and actioned, relevant and queued, not relevant. This converts continuous reading into a triaged queue and is the largest single time recovery.

**Draft the determination, do not make it.** Given structured engagement facts and the current rule version, a drafted analysis with the reasoning and the citations, for the specialist to correct or reject. Drafting is most of the time cost; judging is the value. Every draft must cite its rule version so the specialist can check what it relied on.

**Draft the guidance update.** When a change lands, a proposed edit to the affected guidance pages with the diff and the source, rather than a blank editor. Guidance goes stale because updating it is unpaid work competing with a queue, and reducing it to a review makes it happen.

**Show the currency map.** Which jurisdictions and rule areas are verified, when, and which are overdue — as the specialist's own dashboard. The specialist currently has no way to see their own coverage state.

**Measure consistency and feed it back.** Blind double determinations on a sample, with the disagreements returned as guidance defects. This is the professional feedback the role entirely lacks.

**Make the jurisdiction transferable.** The structured rule base, the determination history and the guidance with provenance together constitute a handover artefact, so covering a jurisdiction for someone on leave is possible and a departure is survivable.

**Protect the judgement.** Every drafted output is a proposal requiring a named specialist's acceptance, recorded. The risk is a specialist under queue pressure accepting drafts unexamined, and the design — citations, confidence, mandatory review of the reasoning rather than the conclusion — is what prevents it.

## Target Customer

Platform compliance leadership, for whom specialist capacity is the constraint on jurisdictional expansion and key-person risk is the exposure nobody has quantified. The productivity argument is direct: most of the week is automatable and the judgement is not.

## Impact If Built

The specialist spends their week on judgement rather than on retrieval, drafting and tracking. Currency becomes visible to the person responsible for it. Guidance gets updated because updating it is a review. And a jurisdiction stops being one person's memory, which is the industry's least examined risk.
