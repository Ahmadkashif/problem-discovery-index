# Paying the Last Click, Which Is Usually the Party That Did the Least

**Industry:** [[affiliate-networks|Affiliate Networks]]
**Type:** High Impact
**One-liner:** A commission rule written before smartphones pays whoever touched the shopper closest to checkout, which is reliably a coupon extension firing on a payment page the shopper had already reached.
**Tags:** #causal-inference #hypothesis-testing #bayesian-inference #confidence-intervals #survival-analysis #evaluation-metrics #revenue-impact #compliance

## The Problem
Affiliate commission is awarded on last click. A shopper reads a review, clicks through, browses, leaves, returns directly a week later, adds to basket, reaches the payment page, and a browser extension offers to find a coupon. It sets a click and a cookie in the act of searching for codes. The sale completes. The extension is the last click and takes the commission; the publisher who wrote the review gets nothing.

This is not an edge case, it is the dominant pattern in the channel's economics. Coupon, cashback and loyalty extensions are among the largest publishers on every major network. Trademark bidders — partners who buy search ads on the merchant's own brand name, intercepting shoppers already heading to the site — are another large category paid the same way. Both are structurally positioned to be last and structurally unlikely to have caused anything.

The merchant pays a commission on a sale they would overwhelmingly have made anyway, and reports affiliate as their best-performing channel because the attributed revenue divided by the commission produces a spectacular ratio. That ratio is the reason budgets stay, and it is very nearly unfalsifiable without a holdout that almost nobody runs.

The people losing are content publishers and creators — the partners who actually introduce products to people who had not heard of them, whose contribution appears early in the path and is therefore never the last click. Their share of the channel's payouts has been declining for years and the mechanism is well understood by everyone in the industry.

## Why It's Unsolved
The rule is simple, auditable and contractually embedded in tens of thousands of merchant-publisher agreements. Changing it means renegotiating all of them, and the partners who lose are the networks' largest, loudest and most sophisticated — several of which are large enough to move their merchants to a competitor that keeps the old rule. A network that unilaterally moves to incremental commissioning takes an immediate revenue hit on its biggest accounts in exchange for a fairer distribution among smaller ones.

The measurement problem is tractable but genuinely nontrivial. Establishing that an extension is non-incremental requires withholding it for a randomised subset of sessions, which requires cooperation from the party being tested, or a merchant-side implementation that the merchant must build. Multi-touch attribution models — the usual answer — are correlational and will happily assign credit along a path in whatever proportion the model was specified to; they do not answer the causal question and are frequently used to avoid it.

There is also a definitional fight. An extension argues, not unreasonably, that a found coupon prevents an abandoned basket and that its presence increases conversion at the margin. That claim is testable. It has been tested rarely and never published in a form merchants can check, which is itself the finding.

## What a Solution Looks Like
Measure by partner class, not by path. The question is not *how much credit does this click deserve* but *what happens to merchant revenue when this class of partner is switched off for a random subset of sessions*. That is a clean experiment: randomise at the shopper or session level, suppress the affiliate tracking for the treated arm, observe completed revenue. It answers the extension question and the trademark bidding question directly, and the answer is a number per partner class per merchant.

Commission on measured contribution. Once incrementality is estimated per class, commission rates become a policy rather than a rule — content partners paid at a rate that reflects introduction, extensions paid at a rate that reflects whatever marginal conversion lift they genuinely produce, which may be small but is not necessarily zero. The important shift is that the rate is derived from an experiment the merchant can inspect.

Model the introduction. A path where a publisher introduced a product the shopper had never encountered is different from one where a shopper searched the exact product name, and the network can tell the difference from its own data — prior exposure, search terms, time to conversion, whether the shopper visited the merchant before. Paying differently for introduction versus interception is the practical form of the fix and does not require abandoning path-based logic entirely.

And publish the methodology. The channel's credibility problem is that its headline metric cannot be checked; a network that lets merchants audit the experiment turns that into a differentiator at a moment when the whole category is under scrutiny.

## Impact If Solved
Roughly $12B of US commission is allocated annually by a rule that pays proximity rather than contribution. Reallocating even a modest share toward partners who genuinely introduce products changes the economics of content publishing and creator commerce, which is where the channel's actual value to merchants comes from and where its supply has been eroding. For a network, it is the one available basis for differentiation in a category where every competitor offers the same tracking, the same dashboards and the same rule — and the scrutiny that arrived with the extension controversy makes this the moment where a challenger can move before the incumbents, who cannot.
