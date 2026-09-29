# Nobody Asks Whether That Was Worth It

**Niche:** [[niches/ugc-video-platforms/recommendation-and-viewer-value/profile|Recommendation & Viewer Value]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The viewer spent forty minutes, closed the app feeling worse, and that session is recorded as a success.
**Tags:** #quick-win #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #causal-inference #automation #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to optimise for a viewer who is glad they watched rather than one who watched for longer — and whoever measures that instead of assuming it holds the attention everyone else is burning.

## The Problem
Every session is scored by duration and interaction. A session where a viewer found what they wanted and left satisfied and a session where they scrolled for forty minutes and regretted it look similar in the metrics, and the second looks better. The platform has never asked which it was, so the systems optimising these sessions have no way to prefer one, and the difference accumulates into whether people want the product in five years.

## Why It's Still Broken
Satisfaction is not logged and duration is, so the available signal became the definition of a good session — a metric that exists will define success in the absence of one that does not. Asking viewers directly is assumed to be intrusive and low-response. Nobody connected session quality to long-term retention. And no short-term metric would improve from measuring it.

## What a Fix Looks Like
Ask, and use the behaviour that already indicates regret. Survey a sample of sessions about whether the time felt well spent, which is the fix and is a standard research instrument nobody applies at this scale. Use behavioural proxies for regret — rapid exit after a long session, no return the next day, no saves or shares across a long watch — since those are available now and correlate. Report the distribution of session quality rather than average duration, which will show that long sessions are not uniformly good. Correlate session quality with retention over months, because that is the business argument and it has never been made with data. Detect the pattern of a session that went on too long, as it is identifiable and is what viewers themselves complain about. Report it alongside engagement rather than instead of it, so the comparison is available to the people making ranking decisions. Segment by viewer, since the same session length means different things to different people. Test a ranking change on the satisfaction measure over a long horizon, which is the experiment that would settle the argument. Publish what is found, because credibility here is the entire asset. And stop describing duration as engagement, since the word implies a judgement the metric cannot support.

## Who Feels the Pain
Viewers who lose evenings they did not want to lose; product teams optimising a metric they privately distrust; regulators examining recommender effects with no measurement to work from; and platforms whose long-term retention depends on something they do not track.

## Impact If Fixed
A metric that exists will define success in the absence of one that does not, so duration became the definition of a good session. Surveying a sample and using regret proxies already in the logs produces the first measurement of the thing the proxy stands in for.
