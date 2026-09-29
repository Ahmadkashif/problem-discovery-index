# The Worst Listings at the Deciding Moment

**Niche:** [[niches/online-marketplaces/seller-onboarding/profile|Seller Onboarding]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Listing flows are polished and well tested, and new sellers produce their worst listings during the exact window in which they decide whether the marketplace works for them.
**Tags:** #cnns #large-language-models #gradient-boosting #evaluation-metrics #automation #survival-analysis #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get a new seller to their first sale before they decide the marketplace does not work — and whoever does that takes the supply, because the first weeks decide whether a seller stays for years.

## The Problem
A new seller lists three items over a fortnight. The photographs are taken on a kitchen table in poor light, the titles read like conversation, the category is approximately right, half the attributes are blank and the prices are guesses. All three rank near the bottom of any result they appear in, receive almost no impressions, and do not sell. The seller concludes the marketplace has no buyers for their kind of item and stops. Every defect in those listings was detectable at the moment of creation and each was fixable in under a minute with the right prompt, and the flow said only that the required fields were filled.

## Why Nobody Has Built This
Onboarding is owned by a growth function measured on sellers acquired and listings created, both of which the current flow maximises. Listing quality is owned by nobody. Telling a seller their listing is poor is friction at the moment they are least committed, which product teams avoid. And the causal chain from a bad first photograph to a churned seller eight weeks later is long enough that nobody has drawn it.

## What to Build
Make the first three listings succeed. Score listing quality at creation from the photograph, the title, the attributes, the category fit and the price, predicting the impressions and sell-through it will get — which is a well-posed problem with abundant labelled history and is the foundation of everything else here. Fix rather than flag: rewrite the title for retrieval, suggest the correct category, extract attributes from the photograph and the description, and propose a price from comparable sales, with the seller approving rather than authoring. Assess the photograph and say specifically what to change, since image quality is the single largest determinant of performance in visual categories and a seller who is told to move to a window and remove the background will do it. Show the seller what comparable successful listings look like in their category, which teaches faster than any guideline. Predict and warn when a listing will not sell, at the moment it is created rather than ninety days later. Track time-to-first-sale as the retention metric it is, since it predicts seller survival better than any other available signal and is not on most operators' dashboards. Intervene actively on sellers approaching the point of giving up, since they are identifiable and the cost of an intervention is trivial against acquisition cost. And measure the quality of listings a cohort creates over time, because a seller who never learns is a seller who will eventually leave.

## Target Customer
Seller growth and operations functions, the new sellers themselves, and the operators whose supply acquisition spend is being wasted downstream.

## Impact If Built
Every defect in a failing first listing is detectable at creation and fixable in a minute, and the flow checks only that fields are filled. Time-to-first-sale predicts seller survival better than anything else available and is on almost no operator's dashboard.
