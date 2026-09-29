# A Success Rate That Means Nothing Per Target

**Niche:** [[niches/web-data-extraction-firms/proxy-and-access-infrastructure/profile|Proxy & Access Infrastructure]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Networks advertise a headline success rate averaged across every target, and a buyer only cares about the handful of targets they actually need, where the rate may be a fraction of the advertised one.
**Tags:** #evaluation-metrics #descriptive-statistics #confidence-intervals #convex-optimization #hypothesis-testing #automation #revenue-impact #time-series-forecasting
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver successful requests against evolving detection at the lowest cost per success — and whoever does that takes the account, because the buyer meters exactly that and switches on it.

## The Problem
A network advertises a very high success rate. A buyer needs three specific targets, all of which run serious detection. Their observed success rate is far below the headline, because the average is dominated by millions of requests to undefended sites. They discover this after integrating and burning through a commitment. The network knows the per-target rate precisely — it is a direct consequence of their own request logs — and publishes an aggregate that is technically accurate and predicts nothing about the buyer's workload.

## Why Nobody Has Built This
Per-target disclosure would show every network's weaknesses precisely, and no one will publish first. The aggregate is flattering and universal, so it is the industry's default claim. Buyers cannot verify before committing, which removes the pressure. And publishing per-target performance arguably helps the targets improve their detection, which is a genuine if convenient objection.

## What to Build
Report performance where the buyer's workload lives. Provide per-target success rates from the network's own logs, at minimum to prospective buyers under agreement, which turns the purchase from a gamble into a measurement and is available to any network willing to be specific. Offer a trial against the buyer's actual target list before commitment, which is the fully convincing version and costs the network very little. Report the trend per target, since detection evolves and a target that worked last quarter may not now. Route adaptively per target rather than by a global policy, since the address type, rotation behaviour and pacing that work differ by target and a single strategy is wrong for most of them. Report cost per successful request rather than per request, which is the buyer's actual unit and which the current metering obscures. Detect and report when a target's defences change, giving buyers warning before their pipeline degrades. Manage pool health per target, retiring addresses already blocked there rather than continuing to spend them. And publish a target difficulty index, which is genuinely useful to buyers planning what to collect and which any network can produce from its own logs.

## Target Customer
Extraction engineers and firms procuring access, and the networks willing to compete on specificity rather than on an average.

## Impact If Built
The headline rate is dominated by undefended targets and predicts nothing about a buyer's actual workload. Per-target rates from the network's own logs turn a gamble into a measurement, and adaptive per-target routing is a real performance gain the global policy leaves on the table.
