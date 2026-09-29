# A Save Rate That Counts Deferrals

**Niche:** [[niches/subscription-commerce/the-retention-agent/profile|The Retention Agent]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** A subscriber who accepts a discount and cancels three months later is recorded as a save, which makes the retention function's headline metric a measure of delay rather than of retention.
**Tags:** #survival-analysis #evaluation-metrics #causal-inference #confidence-intervals #revenue-impact #hypothesis-testing #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to move the retention conversation earlier than the cancel page — and whoever does that takes the saves, because by the time the agent is involved the decision has been made and a discount is the only tool left.

## The Problem
The retention team reports a forty percent save rate. Of those saves, a large share cancel within three months, most at a reduced price in the interim, and some would have stayed anyway without any offer. The reported number counts the moment the cancellation was not completed, which is a measure of the conversation's immediate outcome rather than of anything the business cares about. Budget and staffing are set against it, offers are optimised for it, and the function is being steered by a metric that rewards delay and discounting over anything that would actually retain somebody.

## Why It's Still Broken
The immediate save is measurable at the moment of the conversation and the twelve-month outcome is not, so the fast metric became the operating one. Distinguishing a genuine save from a deferral requires waiting, which nobody wants to do for a performance metric. Counting the ones who would have stayed anyway requires a holdout, which means deliberately not offering to some cancelling customers and feels wasteful. And a lower, truer number would make the function look worse.

## What a Fix Looks Like
Measure the save over a horizon and against a counterfactual. Report retention at twelve months post-save rather than the immediate acceptance, which is computable from history today and reframes the whole function's performance — this is the fix and the data to do it retrospectively already exists. Hold out a random share of cancelling subscribers from any offer and compare, since some would have stayed regardless and the difference is the only honest measure of what the offers achieve. Report the revenue of a save net of the discount given, since a subscriber retained at half price for six months may be worth less than the cancellation. Distinguish save types — discount, pause, operational fix, cadence change — and measure each separately, because they almost certainly differ enormously and are pooled. Track whether the underlying problem was fixed, since an operational remedy that works should show a durable retention effect and a discount should not. Reward the agent on the durable outcome, which changes what they try. Report the deferral rate explicitly, because it is the difference between the reported and the real number and naming it is what forces the change. And use the honest figure in the business case for earlier intervention, since it is the evidence that the cancel page is the wrong place to spend.

## Who Feels the Pain
Operators steering a function by a metric that rewards delay; agents coached toward discounts that do not retain; and the customers offered a price reduction for an operational problem.

## Impact If Fixed
The reported metric measures the conversation's immediate outcome and the business cares about twelve-month retention, which is computable from existing history. A holdout on cancelling subscribers is the only honest measure of what the offers achieve and nobody runs one.
