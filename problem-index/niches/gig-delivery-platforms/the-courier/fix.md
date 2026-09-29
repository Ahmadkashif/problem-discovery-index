# Fix: Gross Is Shown, Net Is Never Computed

**Niche:** [[niches/gig-delivery-platforms/the-courier/profile|The Courier]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The app reports a weekly earnings total with no deduction for the miles that produced it, so the number couriers plan their lives around overstates their income by a large and unknown factor.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #feature-engineering #compliance #worker-facing #quick-win #data-integration
**Contested on:** Whether the platform will subtract from the headline the cost it already knows the courier incurred.

## The Problem

A courier finishes the week and the app shows a total. That total is gross. It does not deduct fuel, maintenance, depreciation, insurance or the self-employment tax that will be due, and it does not account for the miles driven between deliveries that produced no revenue at all.

The gap is not marginal. Independent estimates of gig courier net hourly earnings vary widely — which is itself the symptom, since nobody outside the platforms can compute it — and the consistent finding is that net is substantially below gross. A courier planning on the app's number is planning on a figure that will be corrected, painfully, by a transmission repair or a tax bill.

The platform has the route distances. It has the engaged time. The only missing input is a per-mile cost figure, which the courier could supply in one setting or which could default to a standard rate.

## Why It's Still Broken

A net figure is a smaller figure, and the gross number is what recruits couriers and what appears in earnings claims. There is no incentive to publish a number that makes the work look worse.

The stated reason is that the platform cannot know an individual's costs — vehicle, efficiency, insurance, tax situation all vary. That is true and it does not justify showing zero. A range, or a figure based on a user-supplied per-mile rate with a standard default, is straightforwardly better than a gross total presented as earnings, and the same objection would prevent any business from ever reporting a margin.

There is also the classification shadow again: computing and presenting a worker's net income looks like something an employer does, and platforms have been advised to avoid resembling one.

## What a Fix Looks Like

Subtract the cost. The distance is already in the system.

Let the courier enter a per-mile cost, defaulted by vehicle class, with a short explanation of what it should include. Then report net alongside gross everywhere gross appears: per delivery, per day, per week. Also report net per engaged hour and per online hour, which are the two rates that govern whether the work is worth doing and which differ substantially.

Include the deadhead miles. The distance between the last drop-off and the next pickup is driven for the platform's benefit and is currently in nobody's accounting. The app records it. Attributing it to the delivery that caused it is the single largest correction available and the one most likely to be resisted.

Set aside the tax. A running estimate of self-employment tax and quarterly obligation, shown alongside the net figure, is simple arithmetic and prevents the most common financial shock in this workforce. Several third-party tools do this and the platform is better positioned to do it accurately.

Show the annual mileage log. The platform has every route it dispatched. Producing a deduction-ready log costs nothing and is worth real money to every courier at tax time — one of the few purely positive-sum changes available here.

And when making earnings claims in recruitment, state which figure is being quoted. A gross per-hour figure presented without qualification is the origin of most of the disappointment in this workforce and increasingly of the regulatory attention.

## Who Feels the Pain

Couriers, who plan around a number that overstates their income, and most severely newer ones who have not yet been corrected by a repair bill. Couriers in higher-cost vehicles, for whom the gap is largest and least visible. And the broader argument about gig work, which is conducted with estimates of net earnings that vary by a factor of two because the only party who can measure it declines to.

## Impact If Fixed

The number couriers plan their lives around becomes the number they actually take home. Deadhead mileage enters the accounting, which is where the largest unrecognised cost sits. And the platform can state what its couriers net — a question it will be asked with increasing force, and one it currently answers by changing the subject.
