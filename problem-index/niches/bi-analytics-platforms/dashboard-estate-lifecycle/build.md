# Eleven Thousand Dashboards and Four Hundred Used

**Niche:** [[niches/bi-analytics-platforms/dashboard-estate-lifecycle/profile|Dashboard Estate Lifecycle]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Analytics estates only ever grow, because creating an asset takes a click and deleting one requires a certainty nobody can obtain, and no product supplies that certainty.
**Tags:** #survival-analysis #k-means-clustering #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #automation #quick-win
**Contested on:** Every serious competitor in analytics governance is fighting to make retiring an asset safe enough that an organisation will actually do it — and whoever does that takes the governance account, because every estate grows monotonically and every governance programme has failed to stop it.

## The Problem
A governance lead is asked to clean up the analytics estate. Eleven thousand assets. They pull a usage report and find that four hundred were opened last month. They cannot delete the other ten thousand six hundred, because among them are the quarterly board report, the annual audit extract, the seasonal planning workbook and an unknown number of things that matter rarely and enormously. Deleting one of those is a career-visible failure and keeping all of them is invisible. So nothing is deleted, the clean-up is declared complete with forty archived assets, and the estate is larger again in six months.

## Why Nobody Has Built This
The asymmetry is the whole problem and no product addresses it: vendors ship usage reports, which are necessary and not sufficient, and stop at the point where a human must take a risk. Making retirement safe requires infrequent-but-important usage to be distinguishable from dead, which needs more than a thirty-day view — it needs periodicity detection and an understanding of who the users are. It also requires a reversible path, which is a platform capability nobody has built because deletion was modelled as permanent. And governance is a programme with a deadline rather than a continuously running function, so each campaign restarts from the same position.

## What to Build
Retirement as a safe, reversible, continuous process. Classify every asset using more than recency: periodicity, so an asset opened four times a year on the same week is recognised as seasonal rather than dead; audience, since an asset with two executive viewers outranks one with forty casual ones; downstream dependencies, including the spreadsheet connections the last-mile niche describes; and duplication, since an asset with a near-identical and more-used sibling is retirable regardless of its own usage. Produce a recommendation per asset with the evidence, rather than a report the human must interpret. Make the path reversible: soft-retire with a notice period, keep the asset restorable on demand for a year, and tell the owner and recent viewers before it happens — which is what converts an unmakeable decision into a routine one, since a wrong soft-retirement costs an inconvenience rather than a career. Then run it continuously with a default policy, because the campaign model has failed everywhere and a standing process is the only thing that holds an estate flat. And measure creation alongside retirement, since an estate that retires two hundred assets a quarter and creates four hundred is still losing.

## Target Customer
Data governance leads and platform owners, BI vendors whose customers' estates degrade their own product's usability, and catalogue vendors for whom this is the action their inventory has always lacked.

## Impact If Built
Every estate has this problem, every governance campaign fails at it, and the failure is entirely about the asymmetry of consequence rather than about missing data. Periodicity-aware classification and a reversible retirement path are the two things that make the decision safe enough to take.
