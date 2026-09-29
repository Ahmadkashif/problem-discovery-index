# Pricing a Contribution to a Model

**Industry:** [[stock-media-marketplaces|Stock Media Marketplaces]]
**Type:** High Impact
**One-liner:** The library is among the most valuable training corpora in existence, the contributors who made it are compensated by a formula nobody negotiated, and no participant has attempted to measure what an individual contribution is actually worth.
**Tags:** #diffusion-models #contrastive-learning #causal-inference #confidence-intervals #dimensionality-reduction #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
A marketplace holds tens or hundreds of millions of images, videos and audio assets, each supplied by a contributor under a licence that predates generative models and says nothing useful about training.

Two things then happened simultaneously. The library became one of the few large visual corpora with clean provenance, making it extremely valuable to model developers who need training data whose origin they can defend. And generative models became capable enough to substitute for a meaningful share of the routine commercial imagery that the library sold.

The marketplaces took two strategic postures. Some licensed their corpora to model developers and built generative tools of their own, establishing contributor compensation funds. Others litigated, with Getty's action against Stability AI the most prominent. Both are defensible; neither answers the underlying question.

That question is what any individual contribution is worth. A contributor fund distributes money by a formula — asset count, historical licensing revenue, download share — that is administratively convenient and has no relationship to how much a given asset influenced the model or its outputs. A contributor with ten thousand generic assets and one whose distinctive work is visibly reflected in the model's outputs are treated the same way, or differently for reasons unrelated to contribution.

Meanwhile the substitution runs in the other direction. Generated imagery competes with the library that trained it, and the contributor's ongoing licensing income falls for reasons they can observe and cannot attribute.

The industry's answer has been the formula, offered as a fait accompli. Contributors have limited leverage — the alternative is withdrawal from the marketplace — and the resulting arrangement is stable rather than legitimate.

Attribution is genuinely hard. A diffusion model's output is not traceable to individual training examples in any simple way, and the honest position is that the question is unsolved rather than merely unaddressed. But unsolved is not the same as unapproachable: influence estimation is an active research area with real methods, and the marketplaces are the only parties holding both the corpus and the provenance required to apply them.

## Why It's Unsolved
The technical difficulty is real. Attributing a generated image to specific training examples is an open research problem, and the available methods — influence functions, training data attribution, similarity-based approaches — are computationally expensive at corpus scale and give approximate answers.

The commercial incentive is weak and points the wrong way. A marketplace that measured contribution precisely would create an obligation to pay accordingly, and the current formula is cheaper and uncontested. There is no competitive pressure because no competitor is doing it either.

Contributors are individually powerless and collectively unorganised. Most are individuals or small studios with no bargaining position and no visibility into the corpus's use.

The legal position is unsettled, which paradoxically discourages measurement: a marketplace that quantified individual contribution might be constructing evidence for a claim against itself, which is a real consideration whatever one thinks of it.

And the substitution effect is even harder to measure than the attribution one. Isolating how much of a contributor's income decline is caused by generated alternatives, rather than by market conditions, search changes or their own catalogue ageing, requires careful work nobody has commissioned.

## What a Solution Looks Like
Apply influence estimation honestly and publish the method. Training data attribution methods exist, they are imperfect, and an imperfect measured attribution with a stated method is a very large improvement on a formula with no relationship to contribution at all. The marketplaces are uniquely able to do this because they hold the corpus, the provenance and the model.

Measure similarity between outputs and the corpus at generation time. When a generated image is close to specific training assets in embedding space, that is a weak but real attribution signal, it is computable per generation, and it would allow compensation to follow use rather than inventory.

Measure the substitution effect. Which categories of asset have lost licensing revenue to generated alternatives is estimable from the marketplace's own search and licensing data, with generated and library results competing in the same result sets. Contributors are currently told their income fell; they could be told why.

Make compensation legible. Whatever formula is used, contributors should be able to see the inputs that produced their share. The current opacity is the thing that makes the arrangement feel imposed regardless of whether the amount is fair.

Give contributors a decision. Whether an asset may be used for training is a choice contributors were mostly not offered, and offering it — with the compensation difference attached — converts a unilateral arrangement into a market.

## Impact If Solved
This determines whether a profession that supplied the visual commons for two decades has a future in it, and it is currently being resolved by formula and by litigation. A marketplace that measures contribution with a published method, reports the substitution effect honestly and gives contributors an actual choice would be the only participant able to claim a licensed corpus is different from a scraped one on grounds other than legal exposure — which is also the strongest commercial argument available to it.
