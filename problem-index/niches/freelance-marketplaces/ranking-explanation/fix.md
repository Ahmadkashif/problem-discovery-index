# Fix: The Help Article as the Answer to Every Ranking Question

**Niche:** [[niches/freelance-marketplaces/ranking-explanation/profile|Ranking Explanation]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Every question about placement routes to the same generic best-practices page, which is the platform's way of not answering while appearing to.
**Tags:** #large-language-models #evaluation-metrics #descriptive-statistics #confidence-intervals #change-point-detection #worker-facing #workflow-orchestration #quick-win
**Contested on:** Whether the platform can give a freelancer a specific, account-level answer without building the full attribution stack first.

## The Problem

A freelancer writes to support: my proposals stopped getting replies, what changed. The agent has a macro. The macro links to an article that recommends completing your profile, responding promptly, maintaining a high job success score and keeping your availability current. The freelancer already does all of these. The ticket closes as resolved.

This happens at enormous volume, it satisfies nobody, and it is the single most common interaction between a marketplace and the people who supply its labour. The agents know the answer is useless. They send it because it is the only thing the tooling gives them.

## Why It's Still Broken

Because the specific answer requires infrastructure — logged feature vectors, model versions, attribution — that nobody has funded, and because in the absence of that infrastructure the generic answer is genuinely the best available. The failure compounds itself: support cannot demonstrate the value of the attribution work because it has never had an attribution to deliver, so the work stays unfunded.

There is also an organisational gap. Ranking sits with engineering; the freelancer's question arrives at support. The two organisations have no shared artifact, no escalation path that produces a model-level answer, and no mechanism by which the pattern in support tickets reaches the team whose release caused it.

And there is a quiet reason: a specific answer can be wrong in a way a generic one cannot. "Your profile is fine, the category got more competitive" is a falsifiable claim the platform would have to stand behind.

## What a Fix Looks Like

Most of the value here is available without the attribution stack, from data the platform already holds, which is what makes it a fix rather than a build.

Give the support agent a per-account panel before anything else is built. The freelancer's impressions, proposal-to-reply rate and contract rate over the last twelve months as a series. The same three series for the median freelancer in their category over the same window. Their own metrics — response time, completion rate, rating, price percentile — plotted over the same period. Category entrant count. And a marker line for ranking model releases. This is descriptive statistics over existing logs, no modelling, and it converts the conversation entirely: the agent can see whether the drop is account-specific or category-wide, gradual or a step change, coincident with a release or not.

Add change-point detection on the account's own series, seasonally adjusted against its category, so the panel states plainly whether a real change occurred and when. A large share of these tickets are from people whose volume moved within normal variance, and telling someone honestly that nothing changed is a better answer than best practices.

Route the residue properly. When the panel shows a genuine account-specific step change coincident with a release, that is an escalation to the ranking team with evidence attached, not a macro. Track how many of those there are — that count is the first real measurement of how often releases displace individuals, and it is the number that funds the attribution work.

Then replace the macro with generated text grounded strictly in the panel: what changed, when, whether it is specific to them, and what in the data is and is not under their control. Generic advice only where the data genuinely supports it.

## Who Feels the Pain

Freelancers, who get a non-answer at the moment their income drops and conclude, sometimes correctly, that the platform is hiding something. Support agents, who send an answer they know is useless dozens of times a day and absorb the anger it produces. And the platform, which is converting a solvable information problem into supply-side churn and into the public perception of algorithmic arbitrariness that now attracts regulators.

## Impact If Fixed

The most common conversation on the platform stops being a brush-off. Support resolves the majority of ranking questions with evidence in one touch. The genuine displacement cases get separated from the noise and reach the team that caused them, with a count attached. And the platform gets, almost as a side effect, the first honest measurement of how its own releases land on individual incomes.
