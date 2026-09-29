# The Limit Set at Signup

**Niche:** [[niches/spend-management-platforms/credit-underwriting/profile|Credit Underwriting]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The company has tripled its revenue and its card limit is the one it was given eighteen months ago, while the one that halved has the same limit too.
**Tags:** #change-point-detection #quick-win #evaluation-metrics #automation #revenue-impact #descriptive-statistics #confidence-intervals #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to set a corporate card limit for a company with twelve months of history and no credit file — and whoever joins the limit decision to what happened afterwards underwrites a book everyone else is guessing at.

## The Problem
Limits are set at onboarding and then move only when someone asks. A growing customer hits their ceiling, files a request, waits for a manual review, and in the meantime moves spend to another card — which is lost interchange and a weakened relationship. A deteriorating customer keeps the limit they were given when their balances looked healthy, and the exposure grows exactly as their ability to pay declines. The platform sees both situations daily in the bank data it already holds.

## Why It's Still Broken
Limit setting was built as an onboarding step, so the product has an approval flow and no review flow — the decision was modelled as a one-time event. Increases require a request because that is how credit has always worked. Decreases are commercially unpleasant and nobody wants to initiate one. And nobody reports how stale the limits are.

## What a Fix Looks Like
Review continuously from the data already flowing. Recompute limit appropriateness monthly from current bank balances, revenue and payment behaviour, which is the fix and needs no new data at all. Offer increases proactively to customers who have clearly outgrown their limit, since they are the best customers and are currently being pushed to a competitor's card. Flag deteriorating customers for review rather than waiting for a missed payment, because the exposure is growing precisely when it should not. Report the distribution of limit age, which is one query and will show how much of the book is running on stale decisions. Distinguish a temporary dip from a trend, as reacting to one bad month damages good customers. Automate the increase decision where the evidence is unambiguous, since manual review is why the process is slow. Tell the customer what would support an increase, which turns an opaque refusal into a path. Track lost spend from customers who hit their ceiling, as that number quantifies the growth cost of inaction. Handle decreases with notice and explanation, because doing it abruptly destroys the relationship and doing it never destroys the book. And measure utilisation against limit by cohort, which is the simplest available diagnostic and is not produced.

## Who Feels the Pain
Growing customers moving spend elsewhere; credit teams discovering deterioration at the missed payment; customer success managing avoidable friction; and a book whose exposures were sized for a company that no longer exists.

## Impact If Fixed
Limit setting was modelled as a one-time onboarding event, so the product has an approval flow and no review flow. Monthly recomputation from bank data already flowing catches both the outgrown limit and the growing exposure.
