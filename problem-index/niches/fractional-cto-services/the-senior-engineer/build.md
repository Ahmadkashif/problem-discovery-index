# Build: Owning a Plan You Did Not Write

**Niche:** The Senior Engineer Left Behind
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reconstruction tool for the inheritor of a technical direction — recovering rationale from the record that does exist, marking what cannot be recovered, and giving them a defensible account of a plan they did not author.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #confidence-intervals #workflow-orchestration #worker-facing
**Contested on:** Whether the person who inherits a half-executed technical direction can reconstruct enough of its reasoning to own it.

## The Problem

Four months after the fractional CTO left, the CFO asks in a leadership meeting why the company is spending six figures on a platform migration. The senior engineer who inherited the plan knows the migration is in flight, knows roughly what it is for, and cannot produce the argument — because the argument was made in a meeting they attended eight months ago by someone who is no longer employed, and the deck says what will be done rather than why.

So they say something approximately right and visibly unconvincing, and the migration's political position weakens. Repeat this across a dozen decisions over a year and the direction dies by attrition, having consumed most of its budget.

What makes this particularly wasteful is that the reasoning is partially recoverable. It is distributed across Slack threads where the options were debated, pull request discussions where the architecture was worked out, meeting recordings if any were kept, the tracker where work was scoped and descoped, and the recollections of three or four people still in the building. Nobody assembles it, because assembling it is days of archaeology and the inheritor is already doing two jobs.

## Why Nobody Has Built This

**The person who needs it does not buy software.** The senior engineer has no budget. The company's leadership does not perceive the problem — from their side the plan is simply becoming less convincing, which reads as a problem with the plan or with the person defending it.

**It reads as an admission of a bad handover.** Buying a reconstruction tool says the engagement did not leave what it should have, which implicates a practitioner the company chose and paid and may still want to re-engage. The purchase is socially awkward in a way that suppresses it.

**Reconstruction is genuinely uncertain.** Inferring why a decision was made from surrounding discussion produces plausible reasoning that may be wrong, and a confidently wrong rationale is worse than a gap — it will be cited in a leadership meeting and collapse under a question from someone who was there. Being reliably clear about what cannot be recovered is the hard requirement.

**The source material is scattered across systems with awkward access.** Slack history behind a retention policy, pull request discussion in a repository, recordings that were mostly never made. Assembling it requires broad read access an individual contributor may not have.

**The obvious fix is upstream.** The right answer is that the engagement should have produced the decision record in the first place, per [[niches/fractional-cto-services/handover-and-continuity/profile|🟠 Handover & Continuity]]. A tool for the inheritor is remediation, and remediation products are harder to sell than prevention — except that the population needing remediation right now is vastly larger.

## What to Build

**Reconstruct from what exists.** Ingest the deliverables, the Slack history for the relevant period, pull request and issue discussion, meeting recordings where they exist, and any documents. Assemble a decision inventory: what was decided, when, by whom, and every trace of the reasoning that survives anywhere in the record.

**Grade the confidence, loudly.** Each reconstructed rationale marked as directly evidenced (someone wrote it down), inferred (assembled from surrounding discussion), or unrecoverable. The unrecoverable list is the most valuable output, because it tells the inheritor precisely where they must not improvise and where they need to find a human who remembers. A tool that quietly fills gaps with plausible reasoning would do real damage.

**Surface the assumptions the plan rested on, and test them.** Even where rationale is lost, the conditions a plan depended on are often visible in the material — growth targets, headcount plans, funding assumptions. Extract them, show them against what actually happened, and the inheritor can say which parts of the plan still hold, which is the single most useful sentence they can say in a leadership meeting.

**Separate load-bearing from incidental.** Which decisions depend on which. The inheritor's hardest judgement is what can be changed without unravelling the rest, and a dependency map answers most of it.

**Produce the defence pack.** For each significant in-flight commitment, a one-page account: what was decided, why as far as can be established, what it assumed, what remains true, what has changed, and what the options now are. This is exactly what is needed in the meeting where the CFO asks, and it is the deliverable that justifies the whole product.

**A route back to the author.** A structured short engagement — two hours, paid, scheduled — where the departed practitioner answers the unrecoverable list. Cheap, effective, and currently impossible to arrange because there is no mechanism and asking feels like a favour. Making it a normal, priced, bookable thing is a large part of the fix.

## Target Customer

The buyer is the CEO or CTO of the client company, sold on the plan's survival rather than on the engineer's comfort — "you spent six figures on this direction and it is dissolving because nobody can defend it" is the argument that opens the budget.

The user is the senior engineer, and the acquisition route is almost certainly through them: a free or cheap individual tier that makes the case internally, converting to a company purchase.

Secondary and possibly larger: any engineering leader inheriting a direction after a departure, a reorganisation or an acquisition, which is a far broader population with an identical problem.

## Impact If Built

The plan gets evaluated on its merits rather than dying because nobody could speak for it. Most stranded directions are not wrong — they are undefended, and the distinction costs companies enormous sums.

The inheritor gets standing. Walking into the meeting with a documented account of what was decided, what it assumed and what still holds is a completely different position from "the consultant recommended it."

And the organisation can make a real decision about what to keep. A half-executed plan that can be partially defended and partially abandoned, deliberately, is a far better outcome than the usual binary of grinding on or writing it all off.
