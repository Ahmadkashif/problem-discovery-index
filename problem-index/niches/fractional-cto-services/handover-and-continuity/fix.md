# Fix: The Assumption Nobody Recorded

**Niche:** Handover & Continuity
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** Every technical direction rests on assumptions about the business that are true when it is set and frequently false a year later, and because they were never stated, nobody notices when they break.
**Tags:** #change-point-detection #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing
**Contested on:** Whether the reasoning behind a technical direction survives the departure of the person who set it.

## The Problem

A recommendation to build for multi-tenant scale assumes the enterprise deals close. A recommendation to defer the data platform assumes the analytics need stays modest for a year. A recommendation to hire two senior engineers rather than restructure assumes the budget. A recommendation to stay on the current cloud assumes the committed-spend agreement holds.

Each assumption is reasonable when made, discussed openly during the engagement, and entirely absent from the deliverable, which presents the recommendation as a conclusion. The practitioner knows the plan is conditional. The deck does not say so, because a deck aimed at approval does not foreground its own fragility.

Then the conditions move, as they always do. The enterprise deals slip two quarters. The analytics need triples when a new investor starts asking for cohort reporting. The budget is cut. And the organisation keeps executing, because nothing connects the business change to the technical plan. The people who would notice the connection are the people who left.

The failure is quiet and expensive. Nobody makes a wrong decision; a right decision simply continues being executed after the conditions that made it right have gone, and by the time anyone re-examines it, eighteen months of engineering have been committed to it.

## Why It's Still Broken

**Stating conditions undercuts the sale.** A recommendation presented as conditional is a weaker recommendation in the room where it is presented, and the practitioner is paid for conviction. The incentive to leave the assumption implicit is real and operates on people acting in good faith.

**The assumptions are tacit even to the practitioner.** Much of what a plan depends on is not consciously held. An experienced advisor reasons from a model of the business that includes dozens of implicit conditions, and enumerating them requires deliberate effort against an intuition that feels like a single judgement.

**Nobody is watching both sides.** The business facts live with the CEO and CFO; the technical plan lives with engineering. The person who held both was the fractional CTO, and they are gone. This is the structural heart of it — the role that existed to connect the two is the temporary one.

**Silence is the failure signal.** A broken assumption produces no event. No alert fires when growth comes in under plan and an architecture decision quietly becomes wrong. It surfaces, if at all, as a vague sense months later that the plan no longer fits.

**Re-examining is politically expensive.** Reopening a direction approved by the board, championed by an expensive advisor and already half built, requires someone to argue that a settled question should be unsettled. Junior people will not. The person who would have is not there.

## What a Fix Looks Like

**Write the assumptions down as a short list.** Not buried in a document — a single page attached to the recommendation, five to ten statements, each specific enough to be checked. "This plan assumes ARR reaches $8M by Q4." "This assumes no SOC 2 requirement before next year." "This assumes the team reaches nine engineers." Costs a practitioner twenty minutes and is the whole intervention; everything else is refinement.

**Give each assumption a threshold and a check date.** Not "growth continues" but "growth at or above 40% year on year, checked quarterly." A threshold makes the assumption falsifiable; a date makes someone look.

**Name an owner on the client side.** One person — usually the CEO or the senior engineer inheriting the plan — responsible for reviewing the assumption list quarterly. Fifteen minutes, four times a year, against a one-page list. The entire mechanism is that cheap, and its absence is the reason the problem persists.

**Map assumptions to the decisions they support.** When one fails, the affected decisions should be identifiable immediately rather than reconstructed. This is what makes the response proportionate — usually one or two decisions need revisiting, not the whole direction, and without the map the organisation cannot tell the difference and defaults to abandoning everything.

**Contract a review point.** A paid half-day at six or twelve months, written into the original engagement, where the practitioner returns and walks the assumption list. This solves the structural problem directly: it puts the person who held both sides back in the room, briefly, at the moment the conditions have moved. It is cheap relative to the engagement, clients accept it readily when it is part of the original scope, and it reliably generates follow-on work — which is what makes it the version practices will actually adopt.

**Frame conditionality as rigour.** The professional reframe matters. An advisor who states what their plan depends on is demonstrating that they have a model rather than an opinion, and the practitioners who present it that way find it strengthens the recommendation rather than weakening it.

## Who Feels the Pain

The senior engineer executing a plan whose conditions have changed, who suspects it no longer fits and has no standing to say so and no record of what it assumed.

The CEO, who watches engineering deliver something that made sense a year ago and cannot articulate what went wrong, because nothing did.

The practitioner, whose reputation rests on outcomes determined by conditions they explicitly did not control and never documented — the assumption list protects them more than anyone.

The board, which approved a plan on a confidence that was, correctly, conditional, and was never told the conditions.

## Impact If Fixed

A one-page assumption list with thresholds and an owner is close to free and prevents the most expensive quiet failure in the entire profession. There is no other intervention in this vault with that ratio.

It converts a catastrophic re-evaluation into a routine one. Checking a list quarterly means a broken assumption surfaces within three months rather than eighteen, when the correction is cheap and the sunk investment is small.

And it changes what a plan is. A direction with its conditions attached is an instrument the organisation can operate. A direction without them is an instruction the organisation can only obey or abandon.
