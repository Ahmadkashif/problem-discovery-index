# Build: Evidence Assembly and Consistency Measurement for Disputes

**Niche:** [[niches/freelance-marketplaces/dispute-resolution/profile|Dispute Resolution]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Assemble the dispute record into a structured timeline against the contract's own terms, and measure whether agents given the same facts decide the same way.
**Tags:** #large-language-models #transformers #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #worker-facing #workflow-orchestration
**Contested on:** Whether the decisive facts can be extracted from a message thread reliably enough that an agent works from a record rather than an impression.

## The Problem

A dispute arrives as a support ticket pointing at a contract. The agent opens a message thread that may run to two hundred messages over six weeks, a file history with a dozen uploads and no clear versioning, a milestone log, a contract description written by the client at posting time, and two long statements from parties who each believe they are obviously right.

The agent has a queue and reads until they form a view. The decisive facts in most of these disputes are few and specific: what the contract said was in scope, what was delivered and when, what was requested after the contract started, what each party acknowledged. Those facts are in the record. Finding them is a reading task performed under time pressure, over and over, on material designed for none of this.

## Why Nobody Has Built This

Dispute volume is a cost centre, and cost centres get headcount and macros rather than engineering. The disputed sums are small enough that the obvious business case — reducing per-dispute handling time — is modest, and the larger case, which is that inconsistent adjudication drives away the supply side, has never been quantified because the inconsistency has never been measured.

There is also an understandable fear of appearing to automate a judgement about who is telling the truth. That fear is well-founded and has been allowed to block the part of the work that is not a judgement at all: assembling the evidence. The two got conflated and the whole area went untouched.

## What to Build

A dispute workbench that does the reading and leaves the deciding alone.

The extraction layer produces a structured timeline from the contract record: scope as originally written, each deliverable with its upload time and whether it was acknowledged, each change request with who made it and whether the other party agreed, each milestone with its funding and release state, and the points at which the parties' accounts diverge. Language models handle this well — it is extraction and alignment over documents, with every claim anchored to a specific message or file so the agent can check it in one click. Nothing is summarised without a citation.

On top of that, the comparison the agent actually needs: what the contract said should be delivered against what was delivered, with the gaps and the additions both listed. Most disputes in this industry are scope disputes wearing other clothes, and laying the two lists side by side resolves the factual question in a large share of cases without anyone forming a view about credibility.

Then measure consistency, which is the half nobody does. Build a set of resolved disputes into a calibration corpus and route each one, blind, to multiple agents. Measure agreement. Report it by agent, by dispute type, by disputed amount and by which party was the freelancer's tenure cohort. Inter-agent agreement on identical facts is the single most important quality number in this function and no platform currently knows its value.

Use the consistency data to produce precedent. Where agreement is high, the decision rule is stable and can be written down as guidance — which is what a policy should be and mostly is not. Where agreement is low, that dispute type needs a policy decision made once at the top rather than re-litigated by each agent. Surfacing similar resolved disputes with their outcomes gives the agent a precedent set, which is both a consistency mechanism and a training one.

Keep the determination with the human, and be explicit about it in the product. The system never recommends an outcome. It presents the record, the comparison and the precedents, and the agent decides — which is both the right design and the only version that survives contact with the legal team.

## Target Customer

Platform operations leadership at marketplaces where dispute volume has outgrown the queue, and trust leadership at platforms facing supply-side complaints about arbitrary decisions. The consistency measurement is also the artifact that satisfies a regulator asking how work-allocation and payment decisions are made.

## Impact If Built

Agents decide from a record rather than an impression, in less time, with precedent visible. The platform learns for the first time how consistent its own adjudication is, and the dispute types where it is not consistent become policy questions answered once instead of coin flips answered daily. And the freelancer who loses a dispute loses it on a documented basis, which is a different experience from losing it to whoever read the thread that afternoon.
