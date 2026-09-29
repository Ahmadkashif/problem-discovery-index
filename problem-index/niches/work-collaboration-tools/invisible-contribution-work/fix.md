# Nobody Measures How the Load Is Distributed

**Niche:** [[niches/work-collaboration-tools/invisible-contribution-work/profile|Invisible Contribution Work]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** Review, mentoring, incident response, documentation and coordination are distributed very unevenly across every team, the distribution is a single query away, and no organisation computes it.
**Tags:** #descriptive-statistics #graph-theory #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #worker-facing #quick-win
**Contested on:** Every serious competitor that takes this seriously is fighting to make the work that produces no ticket — reviewing, unblocking, mentoring, responding, coordinating — visible in whatever the organisation uses to judge contribution, and whoever does it changes who gets promoted.

## The Problem
On a team of nine, one person performs a substantial majority of the code reviews, another answers most of the questions in the team channel, and a third has onboarded every new joiner for two years. Nobody assigned any of it; it accumulated because they were willing and good at it. The team's manager has a general sense that these people are helpful. What they do not have is the distribution — that one person is doing sixty percent of the reviews — and without it they cannot rebalance, cannot recognise it in a promotion case, and cannot see that the same pattern of who does the supporting work repeats across every team in the organisation with a skew that is visible the moment anyone looks.

## Why It's Still Broken
The data is available in every tool's history and nobody has run the query, because nobody's job includes it. Managers form impressions rather than measurements, and impressions systematically favour visible output. And the finding is uncomfortable in a specific way — the distribution of this work within teams frequently correlates with gender and with other characteristics, in a pattern documented in the research literature, which means computing it produces a result the organisation then has to do something about.

## What a Fix Looks Like
Compute the distribution and show it to the manager and the team. Reviews performed, questions answered, incidents handled, documentation maintained and new joiners supported, by person, over a period — each derivable from existing tool histories and none requiring new instrumentation. Present it as a distribution rather than a ranking, since the purpose is to see the shape of the load rather than to rank people, and the shape is the finding. Report the correlation with role, level and tenure, since some concentration is appropriate — a senior person should review more — and the question is whether the actual distribution matches the intended one. Look at the demographic distribution deliberately rather than avoiding it, because the pattern is well documented in the literature and an organisation that declines to check is choosing not to know. And use it to rebalance: assignment of reviews, rotation of onboarding, and explicit recognition of the load in workload planning, which is the practical change and which is impossible without the number.

## Who Feels the Pain
The people carrying a disproportionate share of the supporting work, who are also disadvantaged by every measurement system that ignores it; teams that lose a load-bearing person and discover what they were doing; and organisations whose promotion outcomes reflect an undercount they have never examined.

## Impact If Fixed
The distribution is a query over data every organisation already has, and the result is consistently more skewed than managers expect. Rebalancing follows directly, and the demographic check — which is the part organisations are most tempted to skip — is the one most likely to reveal something that matters.
