# The Reputation Score That Penalises Hard Tasks

**Niche:** [[niches/data-labeling-services/the-annotator/profile|The Annotator]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** A contributor's score falls because they worked on ambiguous items where disagreement is expected, so the rational strategy is to avoid the hardest work, which is the work the vendor most needs done.
**Tags:** #bayesian-inference #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #revenue-impact
**Contested on:** Every serious competitor that takes this seriously is fighting to make rejection explicable and contestable for the person whose pay depends on it — and whoever does that keeps the capable contributors, which at the expert tier is the whole business.

## The Problem
A contributor's reputation score is computed from acceptance and agreement rates. They take the hard items — the ambiguous reasoning traces, the edge cases — because they are capable of them. Those items have lower agreement by nature, so their score falls relative to a contributor who takes the straightforward ones. Their access to well-paid work narrows. The rational response is to stop taking the hard items, which every capable contributor eventually works out, and the vendor is then unable to staff exactly the tasks that justify their expert-tier pricing.

## Why It's Still Broken
The score is computed from raw outcomes because that is what is available without modelling item difficulty, and the confounding with task difficulty is the same problem the expert-quality niche describes — solving it once fixes both. The contributor's adaptation is invisible to the vendor, who sees hard items going unclaimed and attributes it to capacity rather than to their own incentive. And the score is used for routing and for access, which makes the distortion consequential rather than cosmetic.

## What a Fix Looks Like
Score ability rather than outcomes. Adjust for item difficulty and ambiguity, so a contributor is assessed against what other capable contributors achieved on the same items rather than against an absolute rate — which is the same ability estimation the quality niche needs and removes the distortion entirely. Report the score's basis to the contributor, since an unexplained score that governs their income is both unfair and unlearnable. Reward hard work explicitly, with a difficulty premium, since the current structure penalises it twice — lower pay per minute and a lower score. Detect the avoidance behaviour, since capable contributors declining hard items is observable and is currently read as unavailability. Separate the routing signal from the access signal, because using one number for both means a temporary dip narrows somebody's access for months. Show contributors which items were ambiguous, so a disagreement on a contested item does not read to them as a personal failure. And monitor whether the hardest items are being claimed, since that is the operational consequence and is the first thing to degrade.

## Who Feels the Pain
Capable contributors penalised for doing the difficult work; vendors unable to staff the tasks their pricing depends on; and customers whose hardest items are annotated by whoever was willing rather than by whoever was best.

## Impact If Fixed
Difficulty-adjusted ability estimation removes a distortion that currently drives capable contributors away from exactly the work that matters most, and it is the same modelling the quality niche already requires. A difficulty premium aligns pay with the effort the task demands rather than penalising it twice.
