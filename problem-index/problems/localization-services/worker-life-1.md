# The Post-Editor Paid by the Discount

**Industry:** [[localization-services|Localization Services]]
**Type:** Worker Life Changing
**One-liner:** Machine output is paid at a fraction of translation rates on the assumption that editing is proportionally less work, and nobody has ever measured whether it is.
**Tags:** #transformers #gradient-boosting #confidence-intervals #evaluation-metrics #bert #worker-facing #revenue-impact #hypothesis-testing

## The Problem
Post-editing machine translation is now the dominant production model. A linguist receives machine output and brings it to publishable quality, and is paid a per-word rate discounted substantially against full translation, on the premise that the machine has done part of the work.

Linguists across the industry dispute that the discount matches the effort, and the dispute has no data behind it because effort per segment is not measured. The distribution matters more than the average: most segments require light touching and some require complete rework, and the difficult ones take longer than translating from scratch because the editor must first identify that a fluent, confident, plausible machine output is wrong. Fluency without accuracy is the specific hazard of modern machine output, and detecting it is cognitively harder than translating an empty segment.

The rate is applied flat across the file regardless of that distribution. A document of easy segments and a document of hard ones pay the same per word. Quality estimation exists and could route or price by difficulty, and where it is deployed it is generally used to reduce vendor cost rather than to adjust the linguist's rate.

Underneath sits a professional shift. People trained as translators now spend their days correcting a machine, which is different work with less autonomy, and the career path that led from translator to specialist to reviewer has narrowed.

## Why It Matters to the Worker
This is a large, distributed, mostly freelance workforce whose compensation model rests on an unmeasured assumption, in a market where the assumption is set by the buyer. Individual linguists have very little negotiating position, and the effort data that would support their argument is not collected by anyone.

The effort is also genuinely underestimated in ways that are specific rather than vague. Reviewing fluent-sounding output requires sustained attention because errors do not announce themselves; that is more tiring per hour than translating, and it produces the fatigue effects that make late-file quality worse, which is then attributed to the linguist.

And the shift in the work has changed what the job develops. Correcting output does not build the domain expertise and voice that translation did, which narrows where a career can go at exactly the moment the rates have fallen.

## What a Solution Looks Like
Measure the effort. Keystroke, timing and edit distance data per segment is collectible in the editor and would establish the actual relationship between machine output quality and post-editing effort — which is the empirical basis the pricing argument has never had. It should be collected transparently, with the linguist seeing their own data, and used for pricing rather than for surveillance, which is the distinction that determines whether it is an improvement or another instrument against them.

Price by difficulty. Quality estimation at segment level already predicts how much work a segment needs, and applying it to the rate as well as to the routing is the straightforward fix to the flat-rate problem. A file of hard segments should pay more per word than a file of easy ones.

Surface the confident errors. The specific hazard is fluent wrongness, and flagging segments where the machine is likely to be confidently incorrect — terminology deviation, number and entity mismatches, source ambiguity, unusual constructions — directs attention where it is actually needed and reduces the scanning burden that makes the work tiring.

Give linguists their own record. Throughput, quality outcomes and the difficulty mix they have handled belong to the linguist and would let them negotiate on evidence rather than on assertion.

## Impact If Solved
A large professional workforce is paid against an assumption nobody has tested, in a production model that has restructured the industry's economics within a decade. Measured effort, difficulty-based pricing and confident-error flagging address the compensation argument with data and reduce the specific cognitive burden that makes post-editing harder than its price implies — and the data to do it is generated continuously in every editor and discarded.
