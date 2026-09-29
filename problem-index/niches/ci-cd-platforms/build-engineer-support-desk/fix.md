# Nobody Measures the Pipeline Support Queue

**Niche:** [[niches/ci-cd-platforms/build-engineer-support-desk/profile|The Build Engineer Support Desk]]
**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A platform team spends most of its capacity answering pipeline questions and cannot say what share, on what topics, or how much is repeat.
**Tags:** #descriptive-statistics #k-means-clustering #bert #hypothesis-testing #confidence-intervals #evaluation-metrics #quick-win #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to let a developer resolve their own pipeline failure without a build engineer — and whoever does that takes the platform team's time back, which is currently spent supporting pipelines they did not write.

## The Problem
A platform lead is asked why the caching project has not shipped. The reason is that the team spends most of its time in the support channel, but they cannot say most — they can say it feels like most. There is no count, no categorisation, no repeat rate and no time attribution. The conversation becomes a matter of impression against a stakeholder who also has impressions, no capacity is added, the project slips again, and the support volume — which the project would have reduced — stays exactly where it is.

## Why It's Still Broken
Questions arrive in a chat channel because that is convenient for the asker, and instrumenting chat as a work system is nobody's assigned task. Ticketing has been tried and abandoned in most organisations, because a form adds friction for the asker and the asker is frequently under time pressure with a broken build. Platform engineers also resist measuring their interruptions, reasonably fearing the number becomes a target. And the load is genuinely hard to attribute, since a two-minute answer costs far more than two minutes in context switching.

## What a Fix Looks Like
Measure it passively, which is the only approach that has ever worked here. Classify messages in the platform channels as support requests or not, which is ordinary text classification requiring no behaviour change from anyone. Categorise by failure class using the same taxonomy the diagnosis capability uses, so the support data and the failure data speak the same language. Compute the repeat rate by clustering semantically similar requests over a year, which is usually the most persuasive single number available and typically shows that a handful of causes account for most of the volume. Estimate time including context switching with a stated multiplier rather than a hidden one, since the credibility of the exercise depends on not overstating. Report it as capacity — this share of the team's time, on these causes, of which this proportion is repeat — which is the form a leadership conversation needs. And frame it as a measure of the platform rather than of the engineers, which is both accurate and the only framing under which the team will support being measured.

## Who Feels the Pain
Platform engineers whose work is interrupt-driven and unacknowledged; platform leads negotiating capacity on impressions; and organisations whose platform improvements are permanently blocked by the support load those improvements would reduce.

## Impact If Fixed
Passive classification over the chat channels requires nothing of the askers, which is why it succeeds where request forms have failed. The repeat rate and the cause breakdown are the two numbers that change the capacity conversation and neither exists today.
