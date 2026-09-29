# Failures Treated as Absence Rather Than Signal

**Niche:** [[niches/online-marketplaces/unmet-demand-intelligence/profile|Unmet Demand Intelligence]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Marketplaces hold the complete record of demand that went unmet and analyse conversion on the transactions that happened, treating every failure as an absence rather than as the most actionable signal they have.
**Tags:** #k-means-clustering #word-embeddings #descriptive-statistics #evaluation-metrics #revenue-impact #confidence-intervals #time-series-forecasting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to turn every search that found nothing and every listing that expired into a map of where supply and demand fail to meet — and whoever does that takes the market, because that map is the operating instruction for a matching business.

## The Problem
Eleven thousand buyers searched for a particular kind of item last quarter, found nothing they wanted, and left. Four hundred sellers listed items that never received an impression. Supply acquisition spent the quarter recruiting sellers in the categories where the marketplace already has the most inventory, because those categories generate the most revenue and therefore look most attractive in every report anybody runs. The eleven thousand unmet searches and the four hundred invisible listings were both logged, neither was analysed, and the business that exists to match supply and demand made its supply decisions without looking at where they fail to meet.

## Why Nobody Has Built This
Analytics are built around transactions because transactions are revenue, and a failed session produces no revenue event to hang analysis on. Zero-result searches are treated as a search quality bug rather than as a demand signal. Supply acquisition is measured on sellers recruited and works from category revenue, which reflects existing supply rather than latent demand. And the buyer who leaves is invisible by definition.

## What to Build
Build the unmet demand map. Cluster searches that returned nothing, returned nothing clicked, or ended in an abandoned session, into interpretable demand segments with volumes attached — which is ordinary analysis on data already logged and produces the artefact this business is missing. Infer intent from behaviour where no query exists, since the largest group of failures is browse sessions that ended without a click and they carry a trajectory even without words. Join unsold inventory to the unmet searches, since the most common outcome is that both existed and did not find each other, and separating the supply gap from the matching failure is the finding that tells you whether to recruit sellers or fix search. Report a supply gap ranking to acquisition — these are the categories and attributes where demand exists and supply does not — which redirects the function from where revenue is to where it could be. Estimate the value of each gap, so the ranking is by opportunity rather than by volume. Detect demand that the marketplace could serve at a different price, which is a pricing gap rather than a supply gap and is remedied differently. Feed the map to sellers, telling them what buyers are looking for and not finding, which is the most useful thing a marketplace can tell its supply side and almost nobody does. And report unmet demand alongside gross merchandise value, because a matching business that reports only successful matches is measuring half of its own performance.

## Target Customer
Marketplace operators and their supply acquisition functions, the sellers who would list what buyers want, and the buyers who left.

## Impact If Built
A matching business makes supply decisions from category revenue, which reflects the supply it already has. The unmet demand map is ordinary analysis on data already logged, and telling sellers what buyers cannot find is the most useful signal a marketplace can send its supply side.
