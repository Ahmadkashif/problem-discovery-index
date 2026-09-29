# Probabilistic Matching Practice

**Niche:** [[niches/audio-adtech-networks/attribution-and-independence/profile|Attribution & Independence]]
**Industry:** [[industries/audio-adtech-networks|Audio Adtech Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Record linkage has estimated and published match error rates for decades, and audio attribution matches on an IP address and reports a number.
**Tags:** #bayesian-inference #graph-theory #confidence-intervals #hypothesis-testing #evaluation-metrics #expectation-maximization #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to establish that hearing an advertisement caused something, credibly enough to be believed by a buyer — and whoever does that from a position the sellers do not own becomes the channel's only referee.

## The Problem
Matching records that may refer to the same entity, under uncertainty, with estimated error rates, is a mature statistical discipline — the same practice that underlies the identity problem in customer data platforms and in census linkage. Match weights are estimated, uncertain pairs are treated differently from confident ones, and false match and false non-match rates are reported because the users of the linkage need to know them. Audio attribution performs a linkage on a single weak identifier and reports the result as a count.

## What Already Exists
Probabilistic record linkage with estimated match weights; false match and non-match rate estimation; treatment of uncertain matches distinct from confident ones; blocking and candidate generation; and published linkage quality methodology.

## The Customization Gap
The adaptation is to a single weak identifier and a causal question on top. It requires: (1) linkage on one attribute of low discriminating power, where the practice normally has several fields — an address shared by a household and sometimes by thousands of subscribers gives a match weight that must be estimated rather than assumed; (2) a causal rather than an identity question, since even a correct match does not establish that the advertisement caused the visit, which linkage practice never has to address; (3) validation without ground truth, requiring seeded tests and advertiser-side confirmation to estimate rates at all; (4) a commercial interest in the direction of error, since the party performing the linkage benefits from false positives — a conflict that census linkage does not have; and (5) privacy constraints on what may be linked, which shape the method as much as the statistics do.

## Target Customer
Audio measurement providers, advertiser measurement teams, and record linkage practitioners for whom this is an unserved commercial application.

## Impact If Solved
Linkage practice publishes error rates because users need them, and audio matches one weak identifier and reports a count. A correct match still does not establish causation, and the linker benefiting from false positives is a conflict census practice never faces.
