# Proposal Matching and Unpaid Bidding

**Industry:** [[freelance-marketplaces|Freelance Marketplaces]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Freelancers write tailored proposals, sometimes paying platform credits to submit them, against jobs that are frequently never awarded to anyone — and the platform knows which those are.
**Tags:** #bert #contrastive-learning #gradient-boosting #word-embeddings #k-nearest-neighbors #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
On proposal-based marketplaces, a freelancer finds a job posting, writes a tailored application, and submits it — on some platforms spending credits purchased with real money to do so. A substantial share of postings are never awarded: the client was price-checking, the requirement changed, the budget evaporated, or the posting was speculative from the start.

The freelancer cannot distinguish those postings from real ones. A posting that will never be awarded looks the same as one that will, so proposal effort is spent uniformly across both. Across a marketplace the aggregate unpaid labour is enormous, and it is a cost borne entirely by the supply side while the platform's bid-credit revenue rises with it.

Matching in the other direction is equally coarse. Clients receive dozens of proposals and filter by price, rating and proposal length; freelancers who would genuinely fit are buried. The signals that would predict fit — demonstrated work on comparable projects, domain familiarity, communication style match, prior success with similar client types — are in the platform's transaction history and are not what the interface surfaces.

## What Already Exists
All major marketplaces provide job search with filters and some algorithmic recommendation. Fiverr's catalogue model avoids proposals entirely by having buyers select packaged offerings, which is a genuine structural alternative. Toptal and similar curated platforms replace bidding with vetting and hand-matching. Several platforms show a client's history — hire rate, total spend, prior reviews — which is the closest existing signal of whether a posting is serious. Proposal templates and AI writing assistance have proliferated, which raises volume and lowers signal for everyone.

## The Customisation Gap
The platform can predict award probability and does not surface it. Client hire history, posting completeness, budget realism relative to the stated scope, response behaviour to previous proposals, time since posting and category base rates all bear on whether a posting will result in a hire, and a predicted probability shown before a freelancer spends an evening — or a credit — would redirect effort toward real work.

The obvious objection is that the platform earns from bid credits and from volume, so surfacing this reduces short-term revenue. That is exactly the tension, and it is the reason the feature does not exist rather than a technical obstacle.

Fit prediction is the second gap. Predicting whether a particular freelancer-client pairing will complete successfully and both parties will be satisfied is learnable from the platform's own outcome history, and it would improve client results as well as freelancer allocation — making it the version of this with aligned incentives and therefore the more likely to be built.

And proposal quality assessment now needs rethinking, since generated proposals have made length and polish uninformative. What distinguishes a serious application is specific engagement with the requirement, and that is assessable.

## Impact If Solved
Unpaid proposal labour is a large and invisible transfer from freelancers to the marketplace mechanism, and most of it is spent on postings the platform could identify as unlikely to convert. Award probability surfaced before the effort, fit prediction learned from outcomes rather than filters, and proposal assessment that survives generated text would redirect a great deal of wasted work — the first of those against the platform's short-term revenue interest and in favour of its supply base.
