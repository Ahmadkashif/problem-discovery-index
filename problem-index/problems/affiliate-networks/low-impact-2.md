# Fraud and Compliance Monitoring

**Industry:** [[affiliate-networks|Affiliate Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Cookie stuffing, trademark bidding and incentivised traffic are policed by rules and manual spot checks, which catch the tactics that were common five years ago.
**Tags:** #change-point-detection #dbscan #graph-neural-networks #gradient-boosting #k-means-clustering #evaluation-metrics #compliance #feature-engineering

## The Problem
Affiliate fraud is old, varied and adaptive. Cookie stuffing sets tracking cookies for users who never clicked. Trademark bidding buys search ads on the merchant's own brand terms, intercepting traffic the merchant already owned. Coupon code leakage sees exclusive codes published publicly, turning a targeted incentive into a universal discount and a commission on every order. Typosquatting, forced clicks in iframes, incentivised traffic from reward apps, and outright transaction fabrication all persist.

Detection is largely rules-based: click-to-conversion ratios outside a band, sessions with implausible durations, traffic spikes, brand terms appearing in referring URLs. Compliance analysts run periodic manual reviews, searching for the merchant's brand terms themselves to see who appears. Merchants discover problems when they notice their own paid search costs rising for terms they were winning free.

The costly failure is not the fraud that is caught. It is the ambiguity: a partner whose numbers look odd but whose traffic may be legitimate, investigated for weeks, with commission held and a relationship damaged whether or not the finding sticks.

## What Already Exists
BrandVerity monitors trademark bidding and paid search compliance; TrafficGuard and similar vendors filter click fraud. The networks run their own compliance teams and maintain policy frameworks, and the larger ones have genuinely effective processes for the known tactics. Browser vendors' restrictions on third-party cookies have incidentally killed some of the older stuffing techniques. Merchant-side tools flag code leakage by scraping coupon sites for their own codes.

## The Customisation Gap
The detections are per-partner and per-rule; the fraud is structural and relational. Fraud rings operate across many publisher accounts, sharing infrastructure, traffic sources and conversion patterns, and the signal that identifies them is the relationship between accounts rather than any single account's metrics. A network sees all of those accounts and analyses each one separately.

Thresholds are the second gap. A click-to-conversion ratio that is normal for a cashback partner is alarming for a content site, and a rule set globally will either miss the first or bury analysts in false positives on the second. Normal behaviour is partner-class-specific, merchant-specific and seasonal, and it drifts — which makes this a change-detection problem against a learned baseline rather than a threshold problem.

And the tactics adapt faster than the rules. A rule-based system encodes yesterday's fraud; what a network needs is a description of normal that updates continuously, so a new tactic shows up as a departure rather than as a miss. The network has the corpus to learn that description and the cross-merchant view to see a ring — both of which a per-merchant tool structurally cannot.

## Impact If Solved
Fraud losses in affiliate are real but the larger cost is the tax on legitimate partners: held commissions, slow investigations, and the reputational damage of a channel merchants half-suspect. Cross-account relational detection catches the organised end, which is most of the money, and learned per-class baselines reduce the false positives that consume analyst time and poison partner relationships. It is also the compliance story a network needs when a merchant's finance team asks what exactly they are paying for.
