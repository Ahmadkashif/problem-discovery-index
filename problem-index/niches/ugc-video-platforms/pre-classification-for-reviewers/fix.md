# Showing the Whole Video by Default

**Niche:** [[niches/ugc-video-platforms/pre-classification-for-reviewers/profile|Pre-Classification for Reviewers]]
**Industry:** [[industries/ugc-video-platforms|UGC Video Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The reviewer is shown the material at full size with sound on, when a blurred still and a transcript line would have supported the decision.
**Tags:** #quick-win #worker-facing #cnns #automation #evaluation-metrics #confidence-intervals #semantic-segmentation #compliance
**Contested on:** Every serious competitor in this niche is fighting to decide automatically everything that does not need a person, so the queue that reaches a human is as small and as bearable as it can be — and whoever does it reduces a documented harm with capability already in the building.

## The Problem
The review interface presents the item. For a large share of decisions the reviewer does not need to see or hear the whole thing — a blurred frame, a still at the flagged timestamp, a transcript excerpt or a description would support the same judgement. The default is full presentation because the interface was built to show content, and the reviewer's exposure is therefore determined by a design choice nobody revisited.

## Why It's Still Broken
The interface was built to display the item under review, so presentation defaults to complete — a tool designed to show something shows all of it unless someone decides otherwise. Minimisation features exist in some tools as options rather than defaults, and an option under a throughput target is not used. Nobody measures what proportion of decisions required full viewing. And the interface is built by a team that does not use it.

## What a Fix Looks Like
Invert the default. Present the minimum by default — blurred, muted, still-framed, with the flagged segment identified — and let the reviewer escalate to more, which is the fix and is the single largest exposure reduction available in the interface. Show the transcript and a description first, since a large share of decisions can be made from them. Point directly at the flagged timestamp rather than requiring a scan. Remove audio by default, as audio is disproportionately distressing and is frequently unnecessary. Measure how often reviewers escalate to full presentation, which will show how much of the exposure was avoidable. Make the minimisation settings sticky rather than per item, because a per-item choice under time pressure defaults to whatever is fastest. Consult the reviewers about the interface, since they know exactly what they do and do not need to see and are rarely asked. Do not count escalation to full view against throughput, as a target that penalises care produces exposure. Apply the strongest defaults on the highest-harm categories. And measure exposure per decision, which is the metric that would let any of this be evaluated.

## Who Feels the Pain
Reviewers seeing more than the decision required; vendor operators managing an avoidable harm; platforms carrying a documented occupational exposure; and the decision quality, which suffers alongside the people making it.

## Impact If Fixed
A tool designed to show something shows all of it unless someone decides otherwise, so full presentation is the default. Inverting it to minimum-first with escalation is an interface change and is the largest exposure reduction available without touching a model.
