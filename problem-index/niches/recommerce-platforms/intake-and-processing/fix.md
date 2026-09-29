# A Cost Per Item That Ignores the Item

**Niche:** [[niches/recommerce-platforms/intake-and-processing/profile|Intake & Processing]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Every item receives the same processing — the same inspection, the same photography, the same listing effort — whether it will sell for fifteen dollars or five hundred, because the pipeline has one path.
**Tags:** #revenue-impact #evaluation-metrics #convex-optimization #confidence-intervals #descriptive-statistics #workflow-orchestration #quick-win #gradient-boosting
**Contested on:** Not terminal — the contest differs by whether there is an adversary, and the decomposition is recorded in the profile.

## The Problem
A twelve-dollar item and a four-hundred-dollar item go through the same eight-step intake: the same number of photographs, the same inspection depth, the same listing detail, the same storage handling. The processing cost is roughly the same for both. On the twelve-dollar item that cost consumes most of the margin and sometimes exceeds it; on the four-hundred-dollar item it is trivial and the item would have justified far more attention — better photographs, a more detailed condition description, a considered price — all of which would have raised its realised value. One pipeline optimised for average throughput is simultaneously too expensive for the low end and too cursory for the high end.

## Why It's Still Broken
A single pipeline is simpler to design, staff and measure, and warehouse operations naturally optimise for uniform flow. The value of an item is not known with confidence at the point where the routing decision would have to be made, which is used as a reason for uniformity. Differential handling complicates the quota system. And the cost is averaged in reporting, which hides that it is fatal at one end and inadequate at the other.

## What a Fix Looks Like
Route by expected value. Estimate the item's likely realised value at the earliest point possible — from the brand, category and a first photograph — and assign a processing tier accordingly, which is a routing decision using the pricing model's output and is the fix. Give the high-value tier more of everything that raises realised price: better photography, detailed condition description, considered pricing, and a second opinion where it matters, since the return on that effort is measurable and positive. Strip the low-value tier to the minimum that will still sell, or decline it entirely, which the acceptance niche develops. Measure processing cost and realised margin per tier, so the tiering is tuned on evidence rather than on intuition. Allow items to be re-routed when the first assessment was wrong, since the early estimate is uncertain and a cheap correction path is better than a confident misroute. Report the margin distribution by value band, which typically shows a large loss-making tail that a blended figure conceals. Test the effect of extra effort on realised price at the high end, since the assumption that better photographs raise value is testable and would justify the tier. And design the quota per tier rather than globally, because a uniform throughput target is what forces the uniform pipeline.

## Who Feels the Pain
Platforms losing money on a large tail of low-value items; sellers of high-value items whose goods were processed cursorily; and operations teams measured on a throughput number that averages two incompatible objectives.

## Impact If Fixed
One pipeline is simultaneously too expensive for the low end and too cursory for the high end, and the blended cost figure hides both. Routing by estimated value is a decision the pricing model can already inform, and margin by value band typically reveals a loss-making tail nobody has seen.
