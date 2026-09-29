# Hours Viewed Is Not Value

**Niche:** [[niches/streaming-video-platforms/content-economics/profile|Content Economics]]
**Industry:** [[industries/streaming-video-platforms|Streaming Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The renewal decision is made on a viewing threshold whose relationship to retention nobody has ever checked.
**Tags:** #descriptive-statistics #quick-win #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact #survival-analysis #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to know what a title is worth before and after it exists — and the contest splits cleanly enough that it is not terminal.

## The Problem
A series is renewed or cancelled based on whether its viewing exceeded a threshold. The threshold is a number set internally, applied across very different titles, and its relationship to subscriber retention has never been tested. A show watched by two million subscribers who were never leaving may clear it; a show watched by four hundred thousand who joined for it may not. The decision is made, the consequence appears in churn months later, and nobody connects the two.

## Why It's Still Broken
The threshold is the only decision rule available, so it is applied rather than validated — a rule that provides a defensible answer stops being questioned about whether the answer is right. Retrospective analysis of past renewal and cancellation decisions requires connecting them to churn, which nobody has done. Decisions are attributed to judgement rather than to the rule. And the outcome is confounded by everything else happening.

## What a Fix Looks Like
Check the rule against what happened. Analyse past cancellations against subsequent churn among their viewers, which is the fix and is directly computable from the record. Report the viewer overlap for each title — how many of its viewers watch nothing else — since a title whose audience has no other reason to stay is worth far more than the threshold suggests. Show viewing concentrated in newly acquired subscribers separately, as that is the closest available proxy for acquisition contribution. Report signups occurring near a title's release, which is crude, confounded and still more informative than hours viewed alone. Test the threshold against outcomes retrospectively, because it has never been validated and may be badly wrong. Segment the analysis by title type, since one threshold across documentaries, dramas and reality is obviously wrong. Track what happened to viewers of cancelled titles, which is the single most informative retrospective available. Flag titles whose audience is narrow and loyal, as they are systematically undervalued by the current rule. Say plainly what hours viewed does and does not measure, so the room reads the number correctly. And commission the causal work, since these fixes are improvements and not the answer.

## Who Feels the Pain
Subscribers whose reason for staying is cancelled; commissioners defending decisions with a number they distrust; creators whose narrow, loyal audience does not count; and a business allocating billions on an unvalidated rule.

## Impact If Fixed
A rule that provides a defensible answer stops being questioned about whether the answer is right. Analysing past cancellations against their viewers' subsequent churn is computable today and tests the threshold the business has never checked.
