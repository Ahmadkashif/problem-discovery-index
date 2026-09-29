# The Blocklist That Blocked the News

**Niche:** [[niches/programmatic-ad-platforms/cohort-and-contextual-targeting/profile|Cohort & Contextual Targeting]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A keyword blocklist defunds serious journalism because the word appears in the article, while the actual unsuitable inventory has no keyword at all.
**Tags:** #bert #transformers #evaluation-metrics #descriptive-statistics #hypothesis-testing #quick-win #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bid well on an impression where nothing about the person is known — and whoever extracts the most from the page, the moment and the aggregate wins the majority of inventory that is no longer addressable.

## The Problem
A brand's blocklist contains a few hundred words. Those words appear in almost every serious news article, so the brand's advertising is systematically withheld from reported journalism and delivered instead to listicles, aggregators and inventory built to carry advertisements, which contain none of the words. The blocklist was intended to keep the brand away from content that would embarrass it. What it actually does is defund the highest-quality inventory in the market, raise the brand's effective cost, and shift spend toward pages nobody reads. Everyone in the chain knows this and the lists keep growing, because a list is what the tooling accepts.

## Why It's Still Broken
Blocklists are the only control most buying interfaces expose, so every concern becomes a keyword — the interface determines the behaviour. A blocked impression has no visible cost while an embarrassing placement has a visible one, which makes over-blocking the safe personal choice for whoever maintains the list. Nobody measures what the list excludes. And lists accumulate through incidents and are never pruned.

## What a Fix Looks Like
Replace matching words with judging pages. Evaluate suitability from the page's meaning rather than its vocabulary, which is the fix and is well within the reach of standard language models — the distinction between an article about a tragedy and an article endorsing one is obvious to a model and invisible to a list. Report what the blocklist costs — reach lost, quality of inventory excluded, price paid elsewhere — which is the number that changes behaviour and is never calculated. Make suitability graded and advertiser-specific, since brands genuinely differ and a universal safety standard serves none of them well. Separate genuine unsuitability from ordinary difficult subject matter, which is the specific failure and the one that defunds journalism. Prune lists automatically by testing each term's actual effect, since most terms in a mature list exclude nothing unsuitable and a large amount of good inventory. Show the buyer examples of what a rule excludes before it is applied, which prevents the worst additions at the moment they are made. Target the made-for-advertising inventory the lists currently steer spend toward, connecting this to the supply quality niche. Give publishers a route to contest exclusion, which currently does not exist and which surfaces errors nobody else will find. Track exclusion rate by publisher as a monitored metric, so systematic defunding becomes visible. And run the comparison — a campaign on suitability judgement against one on the blocklist — since the performance difference is usually decisive and is the only argument that moves a brand team.

## Who Feels the Pain
Publishers of serious journalism systematically defunded; advertisers paying more for worse inventory; and audiences whose quality media loses its revenue to pages built for advertisements.

## Impact If Fixed
The list excludes articles about tragedies and admits pages built to carry advertisements, because it matches words rather than meaning. Reporting what the blocklist costs in reach, quality and price is the calculation nobody runs and the one that changes the behaviour.
