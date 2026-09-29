# Memberships Sold Without Modelling the Capacity They Consume

**Niche:** [[niches/fitness-wellness-software/wellness-recovery-services/profile|Wellness & Recovery Services]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Fix (Pain Point)
**One-liner:** Recovery studios sell unlimited or high-credit memberships priced on an assumption about how often members will come, and nobody checks the assumption until the schedule is congested and walk-in revenue has disappeared.
**Tags:** #descriptive-statistics #time-series-forecasting #confidence-intervals #evaluation-metrics #hypothesis-testing #optimization-fundamentals #revenue-impact #quick-win
**Contested on:** Every serious competitor in recovery and wellness software is fighting to keep practitioners and rooms utilised when service durations vary and no-shows are costly — and whoever raises utilisation per available practitioner hour takes the account.

## The Problem
A studio launches a membership at $199 a month for unlimited recovery services, priced on the belief that members will come about four times a month. The membership sells well. Heavy users come three times a week, consume a disproportionate share of the evening capacity, and crowd out the single-session clients paying $60 a visit. Six months in, the schedule is full, revenue per available hour has fallen, and the owner cannot tell whether the membership is a success or the thing that is destroying the business — because nobody modelled the capacity a membership consumes or measured it afterwards.

## Why It's Still Broken
Membership pricing in this category has been copied from fitness, where marginal capacity is nearly free because a class has a fixed headcount and cost, and imported into a business where every visit consumes a practitioner hour with a real cost. That is a fundamental difference and it is rarely articulated. The measurement that would catch it — utilisation by member, revenue per available practitioner hour by segment — requires the resource model that this niche's build note describes, so the diagnostic depends on the capability the studio does not have.

## What a Fix Looks Like
Measure consumption per member and price against it. Visit frequency distribution by membership tier is computable from booking history immediately, and the distribution — not the average — is what matters, because a small group of heavy users typically drives the congestion. Compute contribution per member against the practitioner cost their visits consume, which converts an argument about whether memberships are good into an arithmetic question per tier. Model the capacity implication before selling more: how many members at this consumption profile can this practitioner roster support before displacement begins, which is the question nobody asked at launch. Then the options are ordinary — credit-based rather than unlimited tiers, peak and off-peak entitlements, a cap, or a higher price — and the studio can choose with evidence rather than after congestion. Report revenue per available practitioner hour as the standing metric, since it is the only number that reflects both sides of the trade.

## Who Feels the Pain
Owners whose busiest schedule coincides with their worst economics; walk-in clients who can no longer get an evening appointment; and practitioners working full days on the lowest-yield bookings.

## Impact If Fixed
Membership consumption modelling is arithmetic on existing booking data and is the difference between a membership programme that builds a business and one that quietly converts high-margin revenue into capacity congestion. Doing it before launching a tier is straightforward; doing it afterwards is the more common case and is still recoverable.
