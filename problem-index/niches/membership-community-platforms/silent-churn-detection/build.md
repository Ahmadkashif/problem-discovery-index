# Acting on an Absence

**Niche:** [[niches/membership-community-platforms/silent-churn-detection/profile|Silent Churn Detection]]
**Industry:** [[industries/membership-community-platforms|Membership & Community Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The member left in week three and cancelled in month five, and the platform noticed in month five.
**Tags:** #survival-analysis #change-point-detection #gradient-boosting #evaluation-metrics #confidence-intervals #revenue-impact #causal-inference #automation
**Contested on:** Every serious competitor in this niche is fighting to reach the member who stopped showing up months before they cancel — and whoever detects the silence early enough to act recovers revenue that is currently written off as inevitable.

## The Problem
The cancellation is a formality. The decision was made months earlier, when the member stopped opening the app, and the intervening period was inertia and a payment that kept going out. Everything about the disengagement was observable in real time: the lengthening gaps, the unopened notifications, the posts not read, the events not attended. The platform's first response is a cancellation confirmation and a win-back email to someone who left in spirit a quarter ago.

## Why Nobody Has Built This
Churn is defined by the billing event, so the system detects the payment stopping rather than the person leaving — a business that defines its outcome as a cancellation cannot see the departure that preceded it. Absence is a negative signal and systems fire on events. The member does not complain, so no ticket exists. And the long interval makes the disengagement feel historical rather than current.

## What to Build
Detect the silence and intervene while it is warm. Model disengagement from declining visit frequency, reading, reaction and posting against each member's own baseline, which is the core and gives months of warning. Detect the change point rather than a threshold, since members have very different normal levels and a fixed rule catches the wrong people. Distinguish a temporary lapse from a departure, as many members go quiet for a fortnight and return and pressing them is counterproductive. Intervene while the member still recognises the community, because a message at week four and one at month four are completely different acts. Make the intervention a connection rather than a message, since the cause is usually that nobody knows them and a personal contact from a member is what works. Ask what happened, as a quiet member will often say and nobody asks. Report the disengaged-but-paying population, which is a number every community has and none computes, and which is both a revenue risk and an ethical one. Distinguish the contented lurker from the departed, because they look identical in activity and are opposite. Test interventions against renewal, which is the clean outcome. And measure the interval between disengagement and cancellation, since compressing it is what converts silent churn into a recoverable event.

## Target Customer
Product and revenue leadership, founders and operators, members who drifted away, and retention vendors.

## Impact If Built
A business that defines its outcome as a cancellation cannot see the departure that preceded it by months. Change-point detection against each member's own baseline turns a formality at renewal into a recoverable event in week four.
