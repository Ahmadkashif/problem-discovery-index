# Three Hundred Models and Nobody Knows Which Matter

**Niche:** [[niches/data-platform-integrators/estate-utilisation/profile|Estate Utilisation]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The platform has hundreds of models, everyone suspects most are unused, and nobody has run the query that would say.
**Tags:** #quick-win #data-integration #descriptive-statistics #evaluation-metrics #automation #revenue-impact #graph-theory #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to establish which of the models and dashboards it has built are actually used, when the query log holds the answer and nobody has ever run it — and whoever answers it takes the account.

## The Problem
Every mature data platform owner believes their estate is mostly inventory and none of them can demonstrate it. The query history is retained by the platform, the asset list is in the catalogue, and a join between them takes an afternoon. It is not run, so every conversation about rationalisation, cost, migration scope and team capacity happens without the one fact that would inform all of them.

## Why It's Still Broken
Nobody owns the question — a report that would embarrass several parties and is nobody's responsibility does not get run, however easy it is. The answer implicates past delivery. The platform makes the data available and does not surface the report. And the estate's growth is not anyone's problem yet.

## What a Fix Looks Like
Run the join, which is an afternoon on any of these platforms. Query the access history against the asset inventory and report last-queried date and query count per asset, which is the fix and names the estate immediately. Separate human queries from scheduled pipeline reads, since a model read only by another model is a different case. Report by consumer as well as by asset, which shows whether an asset has an audience of one. Include dashboards and downstream tools, as those are where the proliferation is worst. Look at ninety days rather than a week, which is the horizon that distinguishes unused from occasional. Attach the cost of running each unused asset, which converts the report into a business case. Share it with the asset owners rather than only with leadership, as they are the ones who can agree to retirement. Repeat it quarterly, since the estate regrows. Use it to scope the next migration, which is where it saves the most. And publish the headline proportion internally, because the number is usually startling and it is what creates the will to act.

## Who Feels the Pain
Data teams maintaining assets nobody opens; platform owners paying to run them; engineers whose change work is slowed by the accumulation; and every migration, which carries the whole estate forward.

## Impact If Fixed
A report that would embarrass several parties and is nobody's responsibility does not get run, however easy it is. An afternoon's join between query history and the asset inventory names the estate for the first time.
