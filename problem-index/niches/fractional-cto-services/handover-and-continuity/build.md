# Build: The Decision Record as Deliverable

**Niche:** Handover & Continuity
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A deliverable format that captures each decision's rationale, assumptions and revisit conditions as the engagement produces them, so the direction remains evaluable after its author leaves.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #workflow-orchestration #automation #worker-facing
**Contested on:** Whether the reasoning behind a technical direction survives the departure of the person who set it.

## The Problem

The artefact a fractional CTO leaves behind is a document written to persuade. It states the direction, argues for it, and presents a roadmap. It is good at what it was built for — getting a board to approve a course of action — and structurally unsuited to the job it is actually asked to do for the next two years, which is to let people who were not in the room evaluate a plan as circumstances change.

What is missing is specific and always the same. Why this option and not the others that were considered. What the choice assumes about the business — the growth rate, the funding, the hiring plan, the regulatory position. What would have to become true for the decision to be wrong. What was deliberately deferred and under what conditions it should be picked up. Which parts of the plan are load-bearing and which are convenience.

All of that existed during the engagement. It was discussed in meetings, worked through on whiteboards, and settled in conversations between the practitioner and two or three people. It was never written because writing it was not a deliverable, and the practitioner had a persuasive document to produce instead.

Then the practitioner leaves. Eight months later growth came in at half the plan, and the team is executing an architecture chosen for a scale that is not arriving, with nobody able to say whether that matters — because the assumption was never stated, so its failure is not visible as a failure.

## Why Nobody Has Built This

**The paying artefact is the deck.** Clients buy the recommendation, and the recommendation is judged on clarity and persuasiveness at the moment it is delivered. Nobody at the point of purchase values the thing that will matter in eighteen months, and the practitioner is not paid for it.

**Writing rationale at the end is impossible.** By the time the engagement is closing, the decisions were made weeks ago and the reasoning has compressed into a conclusion. Reconstructing it is slow, unpaid and produces a sanitised version. Capture has to happen at the moment of decision or it does not happen, and nothing prompts it then.

**Stating assumptions is professionally uncomfortable.** "This plan assumes you close the funding round and hire six engineers" is an honest and useful sentence that also reads as hedging, and in a room where the practitioner is being paid for conviction there is a real incentive not to say it.

**Nobody owns the artefact after the handover.** The document goes to whoever is left, who did not commission it, may not agree with it, and has their own work. Adoption on the client side is the unsolved half, and a format nobody reads is not a fix.

**There is no feedback.** The cost of a lost rationale lands on people the practitioner will never speak to again, so no practitioner has ever been told this is a problem.

## What to Build

**Capture during, not after.** A lightweight decision record created at the moment a decision is made, in the meeting where it is made, in five minutes. What was decided, what else was considered, why this one, what it assumes, what would make it wrong, what was deferred. The whole design constraint is that it must be faster to fill in during the conversation than to reconstruct later, which means structure over prose and voice or transcript capture from the meeting itself doing most of the work.

**Assumptions as first-class, checkable objects.** Every assumption recorded with its source, its value, and a threshold at which the decision should be revisited. Growth at 40% or above. Team reaching nine engineers by Q3. No SOC 2 requirement before next year. These are the load-bearing statements, they are the ones that silently become false, and making them explicit and checkable is the single highest-value element of the whole design.

**Revisit triggers with an owner.** Each decision carries the conditions under which it should be reopened and a named person on the client side responsible for noticing. A trigger with no owner is a comment; a trigger with an owner is a mechanism.

**Structured dependencies between decisions.** Which decisions rest on which. When an assumption fails, the affected decisions are identifiable rather than a matter of reconstruction, which is what makes a half-executed plan re-evaluable instead of abandonable.

**Two outputs from one capture.** The persuasive narrative for the board and the decision record for the successors, generated from the same underlying material. The practitioner still produces the deck they are paid for; the record is a by-product rather than an extra deliverable, which is the only way it gets made.

**Hand it to a person, not a folder.** The final session is a structured walkthrough with whoever inherits the plan, recorded, with their questions captured against the decisions they concern. The inheritor is usually the senior engineer described in [[niches/fractional-cto-services/the-senior-engineer/profile|🟣 The Senior Engineer Left Behind]], and they are the actual user of everything above.

## Target Customer

Fractional CTOs and interim technology leaders whose engagements end by design and who differentiate on the quality of what they leave. The format is a competitive credential — a practitioner who can show a prospective client what the handover looks like has an argument nobody else in the pitch is making.

Client-side, the buyer is a board or CEO who has already lived through a stranded plan, which is a large population and an easy conversation.

## Impact If Built

The plan becomes evaluable by people who were not present, which is the entire difference between a direction and a set of instructions. When growth comes in at half, the team can see which decisions that invalidates and which it does not.

The half-executed plan stops being a binary between blind continuation and total abandonment. Most stranded plans are not wrong; they are unevaluable, and they get abandoned for want of anyone able to defend the parts that still hold.

And the practitioner's reputation stops depending on whether the client happened to retain someone capable of carrying the reasoning forward.
