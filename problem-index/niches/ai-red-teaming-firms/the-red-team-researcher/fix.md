# Reading Every Output by Hand

**Niche:** [[niches/ai-red-teaming-firms/the-red-team-researcher/profile|The Red Team Researcher]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher probing a model reads every response to judge whether it crossed a line, including the overwhelming majority that clearly did not, which multiplies their exposure for no research value.
**Tags:** #worker-facing #automation #evaluation-metrics #large-language-models #descriptive-statistics #confidence-intervals #quick-win #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to keep skilled researchers able to do this work for years rather than months — and whoever does that holds the scarce input the entire industry runs on.

## The Problem
A researcher runs two thousand probe variations over a day. Perhaps forty produce something worth examining. They read all two thousand, because judging whether a response crossed a line requires reading it, and the tooling presents results as a list. Their exposure is fifty times what the research required. The judgement they are paid for concerns the forty; the other nineteen hundred and sixty are a cost paid for the absence of a filter that could be built in a week.

## Why It's Still Broken
The tooling was built to run probes and show results, and a triage layer looked like a nicety rather than a safety measure. Automated classification of harmful output is imperfect, and the correct response to imperfection was assumed to be reading everything rather than reading everything a classifier flagged plus a sample of the rest. Researchers are conscientious and default to reading all of it. And nobody has measured exposure, so the multiplier is invisible.

## What a Fix Looks Like
Filter before the human. Classify every response automatically and present the researcher with the flagged results plus a sample of the unflagged, which cuts exposure by an order of magnitude and preserves the ability to catch classifier misses — this is a week of work and is the highest-return intervention in this niche by a wide margin. Tune the classifier for recall rather than precision, since the cost of a false negative is a missed finding and the cost of a false positive is one more response read, and that asymmetry should be explicit. Show a summary or a classification before the full text, so the researcher chooses to look rather than being shown. Default to obscured presentation with an explicit reveal for the categories where that matters. Order the review queue so the clearly-harmless are not presented at all and the borderline come first while attention is fresh. Track and report exposure reduction, which is what demonstrates the intervention is working and is the measurement the build note needs. Let a researcher hand a category to a colleague mid-engagement without it being a failure. And keep the classifier's misses visible as a sampled check, so the filter is trusted on evidence rather than on hope.

## Who Feels the Pain
Researchers reading nineteen hundred harmless responses to find forty; firms losing experienced people to cumulative exposure they never measured; and clients whose assessments depend on a capability being spent down unnecessarily.

## Impact If Fixed
Classifier-first triage with a sampled check cuts exposure by an order of magnitude for about a week of work, which makes it the highest-return intervention available here. Tuning for recall makes the asymmetry between a missed finding and one extra response explicit.
