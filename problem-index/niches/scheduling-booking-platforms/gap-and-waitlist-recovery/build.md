# Twenty Hours to Sell It Again

**Niche:** [[niches/scheduling-booking-platforms/gap-and-waitlist-recovery/profile|Gap & Waitlist Recovery]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A cancellation leaves a knowably empty slot with hours of selling time remaining, and the standard response is to leave it open.
**Tags:** #gradient-boosting #logistic-regression #k-nearest-neighbors #survival-analysis #evaluation-metrics #confidence-intervals #revenue-impact #automation
**Contested on:** Every serious competitor here is fighting to refill a slot in the hours after it is released, to the right customer, without spamming everyone — and whoever does that takes the operator, because the recovered slot is pure margin on capacity already paid for.

## The Problem
A client cancels Thursday's two o'clock on Wednesday morning. Twenty-eight hours of selling time. The practitioner is still being paid and the room is still rented. The operator, busy, messages two people they can think of, gets no reply, and the slot stays empty. In the platform are eleven clients who tried to book that window in the past fortnight, six whose usual interval has elapsed, and three who have taken a short-notice offer before — and none of them hears about it.

## Why Nobody Has Built This
Waitlists were implemented as a list to display rather than as a recovery mechanism, because the design assumption was that the operator would work it. Automating the offer requires deciding who to ask and in what order, which is a ranking problem nobody framed. The blast approach — telling everyone at once — is the obvious naive alternative and it fails badly in practice, producing a race, several disappointed clients and declining response rates over time, which has discouraged automation generally rather than prompting a better design. And the loss is invisible in the same way the availability loss is: an empty slot generates no record of the revenue that did not happen.

## What to Build
Automatic, ranked, time-aware recovery. On any slot becoming free — cancellation, reschedule, shortened appointment, or a no-show identified early — assemble the candidate set: people who sought that window, clients past their usual interval, the explicit waitlist, and anyone whose pattern fits. Rank by likelihood of accepting this specific slot, which is learnable from every previous offer and response and is a clean supervised problem with accumulating labels. Offer sequentially with short expiries rather than broadcasting, so each person gets a genuine hold and nobody is disappointed by a race — a small design decision that determines whether the mechanism degrades over months or improves. Time the offer for when the person is likely to see it, using their own message response history. Consider a modest incentive where the slot is otherwise unlikely to fill, which is ordinary yield practice and is unavailable here today. And report the recovery rate and the revenue it returned, which is the number that justifies the feature and which no operator currently has in any form.

## Target Customer
Any operator with perishable capacity and fixed costs — clinics, salons, studios, trades — and the platform vendors, for whom this is directly attributable revenue rather than a productivity claim.

## Impact If Built
The economics are unusually favourable because the capacity is already paid for, making a recovered slot close to pure margin. Sequential ranked offers rather than broadcasts are what make the mechanism sustainable rather than self-defeating, and the recovery-rate report is the first time an operator sees this loss at all.
