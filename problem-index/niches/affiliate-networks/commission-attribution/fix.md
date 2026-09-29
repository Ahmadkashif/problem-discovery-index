# The Extension That Fires on the Payment Page

**Niche:** [[niches/affiliate-networks/commission-attribution/profile|Commission Attribution]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Fix (Pain Point)
**One-liner:** A browser extension activating on a checkout page the shopper had already reached is recorded as a click, and the entire commission follows.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #quick-win #revenue-impact #confidence-intervals #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to pay partners for what they contributed rather than for who was last — and whoever measures that moves a substantial share of twelve billion dollars from extensions and trademark bidders to content and creators.

## The Problem
The tracking model has one event type: a click that sends a shopper to the merchant. A browser extension activating on a page the shopper is already on is not that. It produces the same tracking signal, is recorded identically, and collects the commission as though it had delivered the visitor. The system cannot distinguish a referral from an interception because it has no field for the difference, and a substantial share of the category's commission flows through that gap. The distinguishing information — that no navigation occurred, that the shopper was already deep in a session, that the merchant page was already loaded — is present in the data and is not examined.

## Why It's Still Broken
The event model predates extensions and has one shape, which means the distinction has nowhere to live — a data model gap rather than a detection problem. The extensions are among the networks' largest publishers by volume. Merchants see a converting partner and a low-looking commission rate. And the trade press described this for a decade before anyone looked at it systematically.

## What a Fix Looks Like
Record what actually happened. Classify the touch by type — a genuine referral navigation, an on-site activation, a post-click injection — which is the fix, is determinable from signals already collected, and gives every downstream decision something to work with. Report on-site activations separately from referrals, so merchants can see the split for the first time; most are surprised by their own number. Require partners to declare their mechanism, and verify it, since self-declaration alone is worthless but a declaration that can be checked is enforceable. Set different commission terms by touch type, which is the natural remedy once the distinction exists and needs no attribution modelling at all. Run the suppression test — disable extension commission on a shopper sample and observe conversion — which settles the contribution question in a fortnight and is the evidence merchants need. Detect activations triggered by arrival at checkout specifically, as that pattern is the clearest case and is trivially identifiable. Give merchants the control, since it is their commission policy and many will make a different choice once they can see the data. Extend the same treatment to trademark bidding, which is the same interception in a different form. Publish the taxonomy as an industry standard, because a single network acting alone loses its largest publishers to a competitor. And report the share of commission paid on non-navigational touches, because that one number reframes the entire category.

## Who Feels the Pain
Content publishers and creators who created demand and were paid nothing; merchants paying commission on sales they had already made; and the category's credibility as a performance channel.

## Impact If Fixed
The event model has one shape, so an interception and a referral are indistinguishable by construction rather than by difficulty. Classifying touch type from signals already collected lets merchants set different terms without any attribution modelling at all.
