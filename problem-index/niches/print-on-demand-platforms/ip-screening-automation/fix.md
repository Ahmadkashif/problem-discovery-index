# A Queue Full of False Positives

**Niche:** [[niches/print-on-demand-platforms/ip-screening-automation/profile|IP Screening Automation]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The screening flags every design containing a common word that happens to be a trademark, the review queue fills with obvious non-infringements, and reviewers learn to approve quickly — which is exactly the habit that lets the real ones through.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #worker-facing #compliance #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to catch the infringing uploads that exact matching misses — and whoever does that manages the exposure, because the obvious cases are already handled and the liability lives entirely in what gets through.

## The Problem
The brand list contains ordinary words that are registered marks in some class. Every design using those words in their ordinary sense is flagged. The reviewer's queue is dominated by designs that plainly infringe nothing, they clear them at speed, and the rhythm of rapid approval carries through to the case that actually needed attention. The screening's recall was never the binding constraint on the reviewer's accuracy; its precision was, and nobody measures precision because the metric reported is items screened.

## Why It's Still Broken
Recall is the safe direction for a screening system's designer and precision costs nothing visible. Nobody measures the reviewer's accuracy as a function of queue composition, so the connection between false positives and missed real cases is not established anywhere. The brand list grows as rights holders request additions and never shrinks. And a flagged design that is approved is recorded as a screening success rather than as a false positive.

## What a Fix Looks Like
Improve precision and measure its effect. Contextualise the match rather than flagging on the string: a mark used descriptively, in an ordinary sense, or in an unrelated goods class is a different case from a mark used as a mark, and the distinction is largely determinable — this contextualisation is the fix and it removes most of the queue volume. Score confidence and route only the genuinely uncertain to review, since a design with a low score and no other signal does not need a person. Measure and report screening precision, which is currently unmeasured and is the number that governs the reviewer's effectiveness. Track reviewer accuracy against queue composition, which establishes the link between false positives and missed cases and is the evidence for investing in precision. Prune the brand list of terms whose flags are never upheld, and record class and usage context rather than a bare string. Order the queue by risk so the reviewer's attention is fresh on the cases that warrant it. Seed known cases to measure reviewer accuracy directly, which the trust and safety practice elsewhere uses. And report both error directions, since the current reporting describes only volume.

## Who Feels the Pain
Reviewers clearing obvious non-cases at a rhythm that carries into the real ones; creators flagged for using an ordinary word; and platforms whose liability exposure is shaped by a queue nobody has tuned.

## Impact If Fixed
The binding constraint on reviewer accuracy is queue precision, not screening recall, and precision is unmeasured. Contextualising the match by usage and goods class removes most of the volume, and seeded known cases measure reviewer accuracy directly for the first time.
