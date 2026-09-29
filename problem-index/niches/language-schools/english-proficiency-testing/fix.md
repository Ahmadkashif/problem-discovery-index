# Raters Carry the Standard and It Drifts

**Niche:** [[niches/language-schools/english-proficiency-testing/profile|English Proficiency Testing Organizations]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Fix (Pain Point)
**One-liner:** What a band score means lives in the trained judgment of thousands of raters, and the organization measures their agreement without capturing their reasoning.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #text-classification #worker-facing #transfer-learning

## The Problem
A rubric says a band-7 writing performance shows "good operational command with occasional inaccuracies." What that means in practice is carried by raters — thousands of them, trained through benchmarked samples and certification, monitored for agreement, recertified periodically.

Experienced raters know things the rubric does not say. Which errors are typical of a proficiency level and which signal something else. How to weigh a performance that is fluent and empty against one that is halting and precise. What a particular first-language transfer pattern looks like at each band. Where a specific prompt tends to pull performances upward.

The scoring record captures the score and the agreement statistics. The reasoning is captured only in training materials, which are static and were written years ago from a small set of benchmarked samples. When an experienced rater leaves — and rating is often part-time work with real turnover — their calibration goes with them, and the standard drifts a little.

## Why It's Still Broken
Psychometrics has a strong answer to rater variation — measure agreement, monitor drift, recertify — and it works, in the sense that it detects a problem. It does not capture what the good raters know, so remediation is retraining against the same static materials.

The scoring interface is also built for throughput. A rater assigns a band and moves on, because turnaround is a promise and rating capacity is the constraint. Asking for reasoning is asking for time nobody has.

And there is a defensible caution about recording rater commentary on individual candidates in a process that gets appealed.

## What a Fix Looks Like
Capture rater reasoning where it is cheap and where it generalizes.

**Structured rationale on borderline and double-rated performances only.** Not every score — a small, targeted subset where the judgment is actually hard. Typed features from the rubric plus a short note, which is seconds of work on a case the rater is already thinking about.

**Build a living benchmark library.** Performances with expert commentary explaining precisely why they sit at a boundary, accumulating continuously and indexed by first language, prompt type, and the specific feature in contention. Today's benchmark sets are static and small; this makes them large and current.

**Analyze disagreement by feature, not just by rate.** When two raters differ, what did each see? Aggregated, that is a map of where the rubric is ambiguous — the single most useful input to a rubric revision and the thing no agreement statistic reveals.

**Feed it back at the point of rating.** A rater facing a difficult performance should be able to see comparable benchmarked cases with commentary. This is the calibration mechanism that currently only exists in periodic training.

**Use it as the training corpus for automation.** Rated performances with explicit rationale are exactly what an automated scoring system needs to be construct-valid rather than correlation-driven — and that corpus only exists if the reasoning is captured.

## Who Feels the Pain
Raters, especially new ones, calibrating against static materials. Assessment managers, who can detect drift and cannot explain it. And candidates, whose score depends on which rater drew their performance in a process where the difference between bands changes what they are allowed to do next.

## Impact If Fixed
Score meaning is the organization's entire asset, and it is maintained in the trained judgment of a part-time workforce with turnover. Capturing the reasoning on the cases that are actually hard makes the standard transmissible, gives rubric revision an evidence base, and produces the labelled corpus that any defensible automated scoring depends on.
