# The Merchant Who Is Never Told Why

**Niche:** [[niches/retail-pos-platforms/pos-payments-merchant-services/profile|POS Payments & Merchant Services]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A merchant declined at onboarding, placed in reserve, or terminated receives a generic notice citing terms of service, and has no way to know what triggered it, whether it was an error, or what they could do about it.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #compliance #workflow-orchestration #worker-facing #quick-win
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A small retailer's payouts stop. An email cites a risk review and the terms of service. Support cannot say more. The merchant has payroll on Friday and inventory on order, and has no idea whether the trigger was a single large transaction, a customer dispute, a mismatch in their business registration, or a model output nobody can explain. Some of these merchants are genuinely fraudulent. Many are not, and for them the consequence of an unexplained hold can be the end of the business — a substantially worse outcome than the loss the platform was protecting itself against.

## Why It's Still Broken
The standard justification is that explaining a risk decision teaches adversaries how to evade it, which is a real consideration and is applied far more broadly than it warrants — most of these decisions could be explained at a level that helps a legitimate merchant without providing a map. Beyond that, explanation requires the platform to know its own reason, and where the decision came from an opaque model combined with a manual review, a specific reason may genuinely not exist in a retrievable form. And the merchant has no leverage, which removes the pressure that would otherwise force the practice to improve.

## What a Fix Looks Like
Record a reason and give the merchant a path. Every risk action logs the specific triggers, which is a requirement on the decisioning system rather than a communication feature, and is also what makes the decisions auditable internally. Merchants receive a statement of the category of concern and, where applicable, what documentation would resolve it — which is enough to help the legitimate and rarely enough to instruct the fraudulent. There is a defined appeal with a human, a stated timeframe, and an outcome. Appeals and their results are tracked as data, because the appeal reversal rate is the platform's own measure of how often it is wrong, and no platform publishes or seemingly computes it. Where funds are held, the amount and the release condition are stated rather than left open-ended, since an indefinite hold on a small merchant's revenue is the most damaging version of this and is frequently disproportionate to the exposure.

## Who Feels the Pain
Small merchants whose businesses are suspended without explanation and who cannot make payroll; support staff who cannot answer; and the platform, which is destroying legitimate customers at a rate it does not measure.

## Impact If Fixed
Reason capture makes the platform's own decisions auditable, which improves them independently of anything the merchant sees. The appeal reversal rate is the metric that would tell a platform how often its risk operation is wrong, and the fact that it is not computed anywhere is the most telling thing about this niche.
