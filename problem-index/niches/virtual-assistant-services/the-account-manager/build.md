# Build: Diagnosis and a Ladder of Interventions

**Niche:** [[niches/virtual-assistant-services/the-account-manager/profile|The Account Manager]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Give the account manager a view of the working relationship, a diagnosis of what is actually wrong, and interventions between a phone call and a replacement.
**Tags:** #gradient-boosting #change-point-detection #descriptive-statistics #confidence-intervals #evaluation-metrics #large-language-models #worker-facing #workflow-orchestration
**Contested on:** Whether the cause of a failing placement can be identified without watching the work.

## The Problem

An account manager holds thirty to sixty placements and finds out one is failing when the client says so. At that point they have three data points — a satisfaction score, an hours report and two accounts of the situation — and none tells them what is wrong.

The candidate causes are distinct and call for opposite responses. A briefing problem, where the executive hands over tasks too tersely, is fixed by coaching the client and costs the assistant nothing. An execution problem is fixed by training or, eventually, replacement. A scope problem — the executive delegated something that requires context nobody has yet — is fixed by re-scoping. A match problem is fixed by replacement. Applying the replacement remedy to the first three costs an assistant their placement and leaves the cause in place for their successor.

The evidence that would distinguish them is in the correspondence between executive and assistant, which the account manager cannot see.

## Why Nobody Has Built This

Account management in this industry is relationship work, and the tooling is a CRM inherited from sales. The idea that account health could be measured from the work itself has not arisen, because the work happens in someone else's systems.

Visibility also requires the access conversation. An account manager reading the client's correspondence is a step beyond what anyone has proposed, even though the assistant is already in it and the aggregate signals — message volume, round trips, response times — do not require reading content at all.

And the guarantee, commercially, works. It resolves the client's complaint quickly, which protects the account, which is what account management is measured on. The costs fall on the assistant and on the next placement.

## What to Build

An account health signal, a diagnosis and an intervention ladder.

**Build the health signal from metadata, not content.** Message volume between executive and assistant and its trend. Round trips per task. Response latencies both ways. Task completion times. Escalation frequency. Hours utilised against hours contracted. None of this requires reading anything, all of it is available with modest consented access, and together it is a strong leading indicator — deterioration shows up here weeks before a complaint.

**Diagnose from the pattern.** High pre-execution clarification points at briefing. High post-delivery revision points at execution. Rising task completion times with stable round trips points at scope or capacity. Falling message volume with stable hours points at disengagement, which is the most dangerous pattern and the quietest. The mapping from pattern to cause is learnable from the agency's own resolved cases.

**Alert early.** A change-point on the health signal at week three or six is an intervention opportunity; a client complaint at month four is a salvage operation. This single capability changes the role.

**Build the intervention ladder.** A briefing coaching session with the executive, using specific examples. A scope conversation to move a task type back. Additional training or a targeted resource for the assistant. A structured three-way conversation with stated expectations and a review date. Partial re-scoping. Additional support hours. Replacement last. Each is proportionate to a different diagnosis and currently only the first and last exist.

**Record what was tried and what worked.** Interventions and outcomes, accumulated across an agency's accounts, is the dataset that tells the next account manager which remedy fits which pattern. Nobody keeps it.

**Handle the access properly.** Metadata only by default, scoped to the assistant's working channels, consented by the client at onboarding and visible to both parties. The distinction between metadata and content is what makes this acceptable and it should be stated plainly.

## Target Customer

Agency operations leadership, where the case is replacement rate and client retention — the two largest costs in the business and both currently driven by a role with no instruments.

## Impact If Built

The account manager finds out a placement is failing in week three rather than month four, knows which of four distinct problems they are looking at, and has a proportionate response to each. Replacements fall because most of the causes were never assistant problems. And the agency accumulates a record of which remedies work, which nobody currently has.
