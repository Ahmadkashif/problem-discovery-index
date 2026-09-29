# Nobody Knows Whether Network Visits Displace Paying Members

**Niche:** [[niches/fitness-wellness-software/network-funded-fitness/profile|Network-Funded Fitness]]
**Industry:** [[industries/fitness-wellness-software|Fitness & Wellness Software]]
**Type:** Fix (Pain Point)
**One-liner:** A studio joins a network to fill empty classes and cannot tell whether the network members are filling empty spots or taking spots that direct members wanted, which is the difference between incremental revenue and a discount on revenue it already had.
**Tags:** #descriptive-statistics #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor serving network-participating studios is fighting to let a small studio see, verify and reconcile what a fitness network actually owes it — and whoever makes network revenue legible takes those studios.

## The Problem
The Saturday 9am is full. A third of the spots were taken by network members at a fraction of the drop-in rate. Some of those spots would have gone unsold; some would have been bought by direct members who checked, saw the class full, and went elsewhere — and a few of those will not come back. The studio sees a full class and a payment from the network and concludes participation is working. Whether it is depends entirely on how much of that capacity was genuinely spare, which nobody has computed and which varies enormously by class and by hour.

## Why It's Still Broken
Displacement is invisible by construction: a member who saw a full class and did not book generates no record in most systems. The studio's own data shows bookings and not attempted bookings, so the counterfactual is missing. And the framing has never been applied — network participation is discussed as a marketing channel rather than as a capacity allocation decision, which is what it actually is.

## What a Fix Looks Like
Capture the missing signal and compare the hours. Record waitlist entries and, where the booking interface allows, attempts to book a full class — which is a small instrumentation change and produces the demand signal the studio has never had. Compare classes and hours with high network participation against comparable ones with low participation, within the studio and, where a platform can, across comparable studios, to estimate whether network visits substitute for or add to direct bookings at each hour. The answer will be different for a Tuesday afternoon and a Saturday morning, and that difference is the actionable output: restrict or reduce network allocation in the hours where displacement is real, and expand it in the hours where it is genuinely incremental. Most networks permit some allocation control, and almost no studio exercises it deliberately because no studio has the analysis.

## Who Feels the Pain
Studio owners who cannot tell whether their busiest classes are their most or least profitable; direct members who could not get into a class they pay full price for; and the studio's own economics, which may be quietly converting full-price demand into network-rate revenue.

## Impact If Fixed
Distinguishing incremental from displaced network visits is the single question that determines whether participation helps a studio, and it is answerable from booking data plus a small instrumentation change. The hour-level answer turns network participation from an all-or-nothing decision into a managed allocation, which is a materially better position for the studio than the one it has now.
