# The Returning Borrower Nobody Recognises

**Niche:** [[niches/lending-marketplaces/cross-lender-intelligence/profile|Cross-Lender Intelligence]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** The borrower shopped here eight months ago and was declined everywhere, and today they are treated as a brand new lead.
**Tags:** #quick-win #evaluation-metrics #automation #descriptive-statistics #gradient-boosting #data-integration #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn the view of the same borrower shopping across many lenders over years into answers no individual lender can produce — and whoever organises it owns the only empirical picture of how credit is actually priced and granted.

## The Problem
A consumer submits a form. They submitted one eight months ago with a similar profile, were routed to four lenders, and came back twice more in the interim, which strongly suggests none of it worked. The marketplace treats today's submission as a fresh lead, routes them to substantially the same lenders, sells the lead at the same price, and the cycle repeats. Their own history is in the database and nothing consults it.

## Why It's Still Broken
Each submission is processed as an independent event because the pipeline was built around the lead rather than the person — and identity resolution across submissions was never required to sell a lead. Repeat submissions look like volume, which is what the business counts. The history's implication is unflattering to the routing. And nobody measured the repeat rate.

## What a Fix Looks Like
Recognise the person. Match submissions to prior ones and build a borrower history, which is the fix and is straightforward identity resolution on data already held. Report the repeat submission rate, since it is one query and will reveal how much of the volume is people who were not helped the first time. Use the history in routing, because sending a borrower to the same four lenders that already declined them is the clearest waste in the system. Detect the improved profile, as a borrower returning with better credit is a genuinely good lead and is currently indistinguishable. Tell the consultant the borrower has shopped before, which changes the call entirely. Flag the borrower who has been declined everywhere repeatedly, since continuing to route them is harmful and there are better things to offer them. Price repeat leads honestly to lenders, because selling a lender the same declined borrower three times damages the relationship and is currently invisible. Respect the consent and privacy boundaries on reusing prior submissions, which is a real constraint and is manageable. Measure outcomes for repeat versus first-time borrowers, as the difference will be large. And use the repeat pattern as an outcome proxy where funding data is missing, since it is the best free signal available.

## Who Feels the Pain
Borrowers cycled through the same declines; lenders repeatedly sold applicants they already rejected; consultants calling people with an unacknowledged history; and a marketplace counting its own failures as volume.

## Impact If Fixed
The pipeline was built around the lead rather than the person, so identity resolution was never required. Matching submissions to prior ones is simple, exposes how much volume is unhelped repeat shoppers, and supplies the best free outcome proxy in the business.
