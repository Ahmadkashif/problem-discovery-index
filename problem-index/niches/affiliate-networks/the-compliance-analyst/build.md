# A Rulebook of What Was Common Five Years Ago

**Niche:** [[niches/affiliate-networks/the-compliance-analyst/profile|The Compliance Analyst]]
**Industry:** [[industries/affiliate-networks|Affiliate Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Cookie stuffing, trademark bidding and incentivised traffic are policed by rules and manual spot checks, which catch the tactics that were common five years ago.
**Tags:** #worker-facing #gradient-boosting #graph-theory #dbscan #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to catch tactics that evolve faster than the rulebook, with an analyst who has rules and spot checks — and whoever gives them detection that learns replaces a policing model that is permanently one cycle behind.

## The Problem
The rulebook has forty-one rules. Each was written after a specific abuse was discovered, which means the rulebook is a history of what has already been exploited. The people running the current tactics read the same rules, know exactly what is checked, and operate in the space between. The analyst does spot checks — visiting partner sites, looking at traffic patterns — across a partner base far too large to cover, guided by complaints and intuition. The network holds complete behavioural data on every partner across every merchant, which is the richest possible substrate for detecting anomalous behaviour, and it is used to run string matches.

## Why Nobody Has Built This
Rules are explainable and defensible in a dispute, which matters when the consequence is suspending a partner's income, and that defensibility argument has kept the approach in place. Anomaly detection produces cases an analyst must still adjudicate, so it looks like more work before it looks like less. The largest partners are commercially sensitive to investigate. And the true miss rate is unknown, so the current approach cannot be shown to be failing.

## What to Build
Detect behaviour, not patterns you already know. Model each partner's normal behaviour across merchants and flag deviation, which is the core and works on tactics nobody has named yet — the entire limitation of rules is that they require the tactic to be known first. Use the cross-merchant view, since a partner behaving differently on one merchant than on twenty others is the strongest available signal and is only visible to the network. Cluster partners by behavioural signature to find networks of related accounts, because the same operators run many identities and single-account analysis misses the structure. Detect the specific economic signatures — conversion rates implying interception rather than referral, click timing implying no navigation, traffic sources implying incentivisation — which are measurable properties rather than string matches. Rank the queue by expected loss, so the analyst's limited capacity goes where the money is rather than where the complaint came from. Present every case with its evidence assembled, which is what makes an anomaly actionable and is the difference between a score and a case. Keep the human decision, since suspending income is consequential and a model should not do it alone. Learn from analyst decisions, which are high-quality labels currently discarded. Share signals across networks where possible, as operators move between them and each network sees only its own slice. And measure what is being missed through deliberate audits, because a policing function with no estimate of its own miss rate cannot know whether it is working.

## Target Customer
Network compliance operations, merchant programme teams, and the compliance analysts running spot checks across thousands of partners.

## Impact If Built
A rulebook is a history of what has already been exploited, and the people running current tactics read it. Modelling a partner's normal behaviour across merchants detects tactics nobody has named, and the cross-merchant view is a signal only the network can see.
