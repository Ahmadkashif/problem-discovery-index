# Guidelines Written in English and Translated

**Niche:** [[niches/data-labeling-services/low-resource-domains/profile|Low-Resource Domains]]
**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Type:** Fix (Pain Point)
**One-liner:** The annotation guideline is written for English, translated, and applied to a language whose relevant distinctions it does not describe — so the annotators improvise and the disagreement is attributed to them.
**Tags:** #bert #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor here is fighting to produce quality data in languages and specialisms where the contributor pool is small enough that every standard quality mechanism fails — and whoever does that takes the coverage contracts, because nobody can currently deliver them reliably.

## The Problem
A guideline defines a set of categories with English examples, developed on English data, and is translated. In the target language, two of the categories collapse into one distinction that speakers do not naturally make, one category needs to split because the language marks something English does not, and the examples do not correspond to anything an annotator will encounter. The annotators do their best, disagree, and are reported as having low agreement — which is read as low quality and is in fact the guideline being wrong. Their attempts to raise this go through a project manager who does not speak the language.

## Why It's Still Broken
Guidelines are authored once by the customer or a taxonomy specialist working in English, and translation is treated as a delivery step rather than as an adaptation. The contributors who know the guideline is wrong are at the bottom of the communication chain and their feedback passes through people who cannot evaluate it. Agreement statistics attribute the resulting disagreement to annotators, which makes the guideline's failure look like a workforce problem. And nobody has treated guideline adaptation as a design activity requiring native expertise.

## What a Fix Looks Like
Adapt the guideline with the contributors rather than translating it to them. Run a pilot with native experts before the main batch, specifically to find where the categories do not fit, which is a small cost and prevents the systematic error — and is the standard practice in survey translation that this industry has not adopted. Give the contributors a direct channel to raise guideline problems, in their own language, reaching somebody who can evaluate it — since they are the only people who can see the problem and currently cannot report it. Analyse disagreement for structure, because disagreement concentrated on particular categories is a guideline signal and disagreement spread evenly is an annotator signal, and the distinction is computable and is not made. Document the adaptations, so the language's version of the taxonomy is explicit rather than improvised, which also makes the delivered data interpretable. Treat the adapted guideline as a deliverable, since the customer needs to know their categories mean something different in this language. And feed it back to the taxonomy, since a distinction one language forces is frequently one the original guideline should have made.

## Who Feels the Pain
Annotators applying a taxonomy that does not fit their language and being marked down for the resulting disagreement; customers receiving data whose categories mean something they do not expect; and the speakers of those languages, whose representation in the resulting models is degraded by a translation step.

## Impact If Fixed
A native-expert pilot before the main batch is cheap and prevents a systematic error that currently propagates through an entire delivery. Analysing disagreement for structure distinguishes a guideline problem from an annotator problem, which is a distinction the current statistics cannot make.
