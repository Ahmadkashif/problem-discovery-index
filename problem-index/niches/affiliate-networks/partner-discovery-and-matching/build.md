# Everyone Recruits the Same Two Hundred Partners

**Niche:** [[niches/affiliate-networks/partner-discovery-and-matching/profile|Partner Discovery & Matching]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Finding the publishers who could sell a merchant's products is done by browsing a marketplace directory sorted by size, which is how every merchant ends up recruiting the same two hundred partners.
**Tags:** #matrix-decompositions #gradient-boosting #word-embeddings #evaluation-metrics #confidence-intervals #revenue-impact #k-nearest-neighbors #transformers
**Contested on:** Every serious competitor in this niche is fighting to predict which publishers would actually sell a given merchant's products — and whoever does that from the network's own cross-merchant record ends the era of everyone recruiting the same two hundred partners.

## The Problem
A merchant joins a network and needs partners. They open the directory, sort by size, and contact the biggest names in their category — the same names every competitor contacted, who are already saturated with offers and will take the merchant only on terms that suit the partner. Meanwhile there are publishers whose audience is an exact match, whose content already covers this product type, and who convert well for comparable merchants, sitting unfound on page forty. The network knows all of this with precision. It presents a list sorted by size.

## Why Nobody Has Built This
The directory was built as a listings page and never reconsidered as a matching problem, which is a framing gap rather than a capability one. Networks earn on volume and the large publishers deliver volume, so the incentive to surface smaller better-fitting partners is weak. Cross-merchant performance data is commercially sensitive to expose directly, even though it can be used in a model without being shown. And nobody measures recruitment outcomes, so the current method cannot be shown to be poor.

## What to Build
Turn the directory into a prediction. Model the expected value of a merchant-publisher pairing from the network's full history of such pairings, which is a well-posed problem with abundant observed outcomes and is the reason this should work better here than in almost any matching context. Represent the merchant by catalogue and category and the publisher by content, audience and demonstrated performance, so the match is about fit rather than about size. Use cross-merchant performance without disclosing it, since the model can rank on what a publisher achieves for comparable merchants while showing only the recommendation. Predict incremental rather than total value, connecting to the attribution work, because a partner who intercepts existing demand is a cost dressed as a match. Handle the cold start on both sides, as a new merchant and a new publisher are the cases that matter most and a pure history model serves neither. Surface capacity, since a publisher already carrying forty competing merchants is a poor match regardless of fit, and saturation is observable to the network. Recommend in both directions, because a publisher choosing programmes is the same problem and connects to the publisher side. Measure recruitment outcomes — who was contacted, who joined, what they produced — which is the feedback loop that makes the model improve and which nobody currently records. Diversify recommendations deliberately, since recommending the same top partners to everyone reproduces the problem inside a better-looking interface. And report the performance of recommended partners against self-selected ones, since that comparison is the entire case.

## Target Customer
Merchant recruitment and partnership teams, affiliate networks differentiating their marketplace, and the publishers who are a good fit and never found.

## Impact If Built
The network observes the outcome of every match it has ever made and presents a list sorted by size. Modelling pairing value from that history is a well-posed problem with abundant labels, and it surfaces the fitting publishers currently sitting on page forty.
