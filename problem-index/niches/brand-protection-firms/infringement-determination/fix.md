# Fix: The Appeal Goes to the Platform, Not the Filer

**Niche:** Infringement Determination
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Fix (Pain Point)
**One-liner:** When a determination is reversed on appeal, the platform knows and the firm that filed the notice does not, so the clearest evidence of error never reaches the party who made it.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #worker-facing #data-integration #workflow-orchestration
**Contested on:** Whether a flagged listing is actually infringing, which is a legal judgement that no image match settles.

## The Problem

A seller is actioned. They appeal to the platform, because that is the only route available. The platform reviews, concludes the listing was legitimate, and restores it.

That reversal is the strongest possible signal that a determination was wrong. It came from a different party, with the seller's evidence in front of them, reaching the opposite conclusion.

It goes nowhere. The platform restores the listing and closes the appeal. The firm that filed the notice is not told. The reviewer who made the determination never learns. The detection pipeline that surfaced the candidate receives no correction. And the same seller may be actioned again next month by the same firm on the same basis.

The consequence is that the industry's precision cannot improve, because the feedback that would improve it is routed to a party who has no reason to pass it back. Firms genuinely do not know their own error rate, not because they are avoiding the question but because the answer is held by someone else.

Meanwhile the seller, who was right, absorbed the lost income during the appeal and has no reason to believe it will not happen again.

## Why It's Still Broken

**The appeal is the platform's process.** It exists to resolve a dispute on the platform, not to inform the notice sender, and there is no mechanism in it for doing so.

**Firms do not ask.** Requesting appeal outcomes is straightforward and almost no firm does it, because nothing in their metrics would use the answer.

**The outcome is unwelcome.** A reversal rate is a precision measurement, and a firm priced on notice volume has no commercial reason to generate one.

**Platforms have no obligation to report back.** Nothing requires a platform to tell a notice sender that their notice was wrong, and the platform gains nothing from doing so.

**Sellers have no route to the filer.** The affected party cannot reach the party that made the determination, so even a direct complaint does not arrive.

**Nobody aggregates.** Reversal data across platforms would give an industry-level error rate, and it sits in fragments across a dozen platform appeal systems.

## What a Fix Looks Like

**Ask platforms for appeal outcomes.** Most have a relationship with high-volume notice senders and would provide it if asked. This is the cheapest fix available and no firm has made the request part of its standard integration.

**Feed reversals back into review and detection.** A reversed determination should correct the seller's record, inform the reviewer, and mark the detection pattern that produced it. Currently none of the three happens.

**Give sellers a direct channel to the filer.** An affected seller able to contact the firm that filed the notice is both fairer and the fastest route to the firm learning about its own errors — and most firms are not contactable by the people they action.

**Publish a reversal rate.** A firm that reports its own precision is making a claim no competitor currently can, and it is the number a brand should be asking for.

**Platforms should report it as standard.** Returning the outcome to the notice sender costs a platform almost nothing and would create the feedback loop the whole notice system lacks.

**Track repeat wrongful actions against the same seller.** A seller actioned, restored and actioned again is the clearest possible evidence that the correction is not propagating, and it recurs.

**Brands should require it at renewal.** A client asking for the reversal rate changes what the firm measures, and it is a question any brand can ask.

## Who Feels the Pain

The seller, whose reversal proved they were right and changed nothing, and who can reasonably expect it to happen again.

The reviewer, who made a determination that was overturned and was never told, and therefore cannot calibrate.

The firm, which genuinely does not know its own error rate and is competing in a market where accuracy is invisible.

And the brand, whose enforcement vendor may be repeatedly actioning its own authorised resellers with no mechanism by which anyone would find out.

## Impact If Fixed

Asking platforms for appeal outcomes is a request nobody has made, would be granted in many cases, and would give this industry its first precision measurement.

Feeding reversals back into the seller record would stop the specific and common failure where a legitimate seller is actioned, restored and actioned again.

And a published reversal rate would let a brand choose an enforcement firm on whether its notices are right — which is currently impossible and is the information most relevant to the reputational risk the brand is actually carrying.
