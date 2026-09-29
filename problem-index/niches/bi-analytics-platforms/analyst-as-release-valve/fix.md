# Nobody Measures the Queue

**Niche:** [[niches/bi-analytics-platforms/analyst-as-release-valve/profile|The Analyst as Release Valve]]
**Industry:** [[industries/bi-analytics-platforms|BI & Analytics Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Data teams spend a large share of their capacity on ad hoc requests and almost none of them can say what share, what the requests are about, or how much is repeat.
**Tags:** #descriptive-statistics #k-means-clustering #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make the estate answer the question so the analyst does not have to — and whoever measurably shrinks the ad hoc queue takes the analytics account, because that queue is the visible cost of everything the platform failed to deliver.

## The Problem
An analytics leader is asked why the strategic project is late. The honest answer is that the team spends most of its time on requests that arrive in a chat channel, but they cannot say most — they can say it feels like most. There is no count, no categorisation, no repeat rate and no time attribution, so the conversation becomes a matter of impression against a stakeholder who also has impressions. The team gets no extra capacity, the project slips again, and an analyst resigns citing the work not being what they were hired for.

## Why It's Still Broken
Requests arrive in chat because chat is convenient for the asker, and instrumenting chat as a work system requires effort nobody has assigned. Ticketing systems have been tried in most organisations and abandoned, because a form adds friction for the asker and the asker is usually more senior than the analyst. Analysts also resist measuring their own interruptions, reasonably fearing that a number becomes a target. And the load is genuinely hard to attribute, since a four-minute answer costs far more than four minutes and nothing captures the context switch.

## What a Fix Looks Like
Measure it passively. Classify messages in the request channels as requests or not, which is ordinary text classification and requires no behaviour change from anyone — this is the whole unlock, because every attempt that requires the asker to do something has failed. Categorise by subject area, by asker's function and by whether an existing asset covers it, which gives the composition rather than just the count. Compute the repeat rate by clustering semantically similar requests over a year, which is usually the most persuasive single number available. Estimate time including the interruption cost using a defensible multiplier stated openly rather than hidden, since the credibility of the whole exercise depends on not overstating. Report it as capacity — this share of the team's time, on these subjects, of which this proportion was previously answered — which is the form a leadership conversation needs. And present it as a measure of the estate rather than of the analysts, which is both accurate and the only framing under which the team will support being measured.

## Who Feels the Pain
Analysts whose work is interrupt-driven and unacknowledged; analytics leaders negotiating capacity on impressions; and organisations concluding they need more analysts when they have a discoverability problem.

## Impact If Fixed
Passive classification over the chat channels requires nothing of the askers, which is why it succeeds where request forms have failed everywhere. The repeat rate and the coverage share are the two numbers that change the conversation, and neither exists in any organisation today.
