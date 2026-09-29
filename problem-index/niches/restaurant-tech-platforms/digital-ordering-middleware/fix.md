# Nobody Measures Menu Drift

**Niche:** [[niches/restaurant-tech-platforms/digital-ordering-middleware/profile|Digital Ordering & Channel Middleware]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A restaurant's menu disagrees with itself across channels constantly — wrong prices, unavailable items, missing modifiers — and no vendor publishes a fidelity figure, so operators discover each discrepancy through a customer complaint.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #change-point-detection #automation #quick-win #revenue-impact
**Contested on:** Every serious competitor in ordering middleware is fighting to keep one menu correct across five channels that each model a modifier differently — and whoever requires the fewest manual rebuilds takes the account.

## The Problem
The kitchen eighty-sixes the salmon at seven. It comes off the point of sale immediately and off one marketplace ten minutes later, stays on the second until someone remembers, and never comes off the restaurant's own website because that is managed separately. Orders continue to arrive for it. Each one becomes a refund, a substitution call, or an angry review. Separately, a price increase applied last month reached three of five channels. Nobody knows about any of this until a customer complains, because no system compares the channels to each other.

## Why It's Still Broken
Each vendor owns a subset of the channels and reports on its own sync status, which is not the same as fidelity — a sync that ran successfully can still have produced a divergent menu, and a channel managed outside the middleware is invisible entirely. Publishing a fidelity number is also commercially unattractive: it quantifies exactly how imperfect the product is, in a market where everyone competes on integration count and nobody competes on correctness. And the operator has never asked, because they experience drift as a series of individual incidents rather than as a measurable rate.

## What a Fix Looks Like
Read the channels back and compare. Pull each channel's live menu as a customer would see it — which every channel exposes, since it has to render — and diff it against the point of sale's current state on the axes that matter: item presence, price, modifier availability, and eighty-six status. Report a fidelity figure per channel, continuously, with the specific discrepancies listed. Alert on the ones with immediate revenue consequence, above all availability, since an order for an unavailable item is a guaranteed loss. Track time-to-propagate per channel per change type, which is the diagnostic that shows whether a channel is slow or a sync is broken. None of this requires cooperation from the channels or new integration work; it requires reading what is already public and comparing it to what the restaurant intends.

## Who Feels the Pain
Managers refunding orders for items that ran out two hours ago; guests who ordered something the restaurant does not have; and operators whose prices are stale on channels they cannot see.

## Impact If Fixed
Availability drift is a direct, measurable revenue loss that is eliminated the moment it is visible, and fidelity measurement takes a read of public data rather than a new integration. Publishing the figure also changes the basis of competition in this niche from how many channels a vendor connects to how correct those connections are, which is the axis operators actually care about.
