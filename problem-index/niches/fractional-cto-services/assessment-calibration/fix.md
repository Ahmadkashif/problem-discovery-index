# Fix: The Recommendation Nobody Follows Up

**Niche:** Assessment Calibration
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Fix (Pain Point)
**One-liner:** The engagement ends at the recommendation, so nobody — advisor, client or firm — ever learns whether it was executed or whether it worked.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference #data-integration #workflow-orchestration #revenue-impact
**Contested on:** Whether an advisory practice retains its own assessments and their outcomes well enough to know which of its judgements have historically been right.

## The Problem

A fractional CTO concludes an engagement with a set of recommendations, presents them, and leaves. That is the contractual end of the work and, in practice, the end of all information flow. Eighteen months later the company either rebuilt the platform successfully, rebuilt it badly, started and abandoned it, or never started — and the advisor does not know which.

This is not an edge case; it is the standard shape of the profession. Advisors accumulate impressions from the minority of clients who stay in touch, which is a biased sample in the obvious direction: happy clients keep calling. The pattern library a twenty-year practitioner carries is built substantially on engagements whose results they never saw and on a subset whose results were good enough to produce a continuing relationship.

The waste is specific. At the moment the engagement ends, the firm holds a detailed, structured prediction about a real company. Eighteen months later, that company holds the result. Connecting the two costs one phone call, and the call is never made — not because anyone refuses, but because it is nobody's job and there is nowhere to put the answer.

## Why It's Still Broken

**The commercial model ends at delivery.** Fees attach to the engagement. A follow-up is unbilled time against a dormant relationship, and in a utilisation-driven business unbilled time is the thing that does not happen.

**Asking feels like exposure.** "Did our recommendation work?" is a question with a possible answer the advisor does not want, delivered to a client who may not have executed and may feel judged by the asking. The social awkwardness is real in both directions and is enough to prevent the call on its own.

**The relationship has gone dormant.** The sponsor may have left. The champion may have been the person the restructuring recommendation displaced. Reopening contact after eighteen months of silence is a small act requiring a reason, and "I would like to score my own prediction" is not a reason most practitioners will offer.

**Execution confounds everything.** Clients rarely execute a recommendation as given — they do part of it, modify the rest, and the business changes underneath. Attributing the outcome is genuinely hard, and the difficulty is used as a reason not to collect the data, when in fact recording execution fidelity alongside the outcome resolves most of it.

**There is nowhere to put the answer.** Even a practitioner who does follow up has no system expecting the information. It becomes a memory, which is exactly the biased pattern library the follow-up was supposed to correct.

## What a Fix Looks Like

**Put it in the engagement letter.** A scheduled check-in at six and eighteen months, written into the contract at signing as part of the deliverable, at no additional fee. This removes every obstacle at once: it is not a favour, not an awkward reopening, not unbilled discretionary time, and the client agreed to it when they were most positively disposed. It also reads as confidence — a firm that contracts to come back and ask whether its advice worked is making a statement about its advice.

**Make it valuable to the client.** Frame the check-in as a free reassessment rather than a survey. Fifteen minutes on where the plan stands, what changed, what is now the constraint. Clients accept this readily because it is useful to them, and it reliably surfaces new work, which is the commercial argument that gets it approved internally.

**Record execution fidelity separately from outcome.** Which recommendations were executed, partially executed, modified or dropped, and why. This is the field that makes the whole record interpretable — a missed estimate on a recommendation that was never executed says nothing about the estimate, and without the fidelity field it looks identical to a genuine miss.

**Collect what is cheap and objective.** Where the client is willing, a repeat of the [[niches/fractional-cto-services/evidence-extraction/profile|🎯 Evidence Extraction]] derivation at eighteen months gives a measured before-and-after on the same estate — did effort concentration move, did the coupling loosen, did flow improve — which is far stronger evidence than a recollection and costs an afternoon.

**Assign it.** One person in the practice owns the follow-up calendar and the record. It is an operations function, not a practitioner function, and treating it as practitioner discretion is why it has never happened.

## Who Feels the Pain

The practitioner, who has spent a career making consequential judgements and receiving almost no feedback on any of them, and whose confidence is therefore built on a sample selected for agreement.

The client, twice: once in buying advice from someone with an uncalibrated pattern library, and again in never receiving the check-in that would have caught the half-executed plan before it settled into permanence.

The practice owner, who cannot demonstrate value to prospects beyond testimonials, and cannot tell which of their practitioners are actually good — because there is no measure, only reputation, and reputation inside a firm is mostly a function of who presents well.

The senior engineer left holding the plan feels it most sharply of all, and is the subject of [[niches/fractional-cto-services/the-senior-engineer/profile|🟣 The Senior Engineer Left Behind]].

## Impact If Fixed

The feedback loop closes. Within two or three years a practice knows the distribution of its estimates against actuals, the hit rate on its risk flags and the execution rate on its recommendations — and practitioners who see that begin giving different advice, because calibration responds to feedback.

The check-in itself generates revenue. A structured conversation eighteen months after an engagement, with a client who executed part of a plan and is now facing the consequences, converts to follow-on work at a rate that pays for the entire programme several times over — which is what makes this the rare knowledge-capture initiative that survives its first budget review.

And the sample stops being biased. The practitioner who hears from the engagements that went badly, as a matter of routine, is a materially better advisor than the one who hears only from the ones that went well.
