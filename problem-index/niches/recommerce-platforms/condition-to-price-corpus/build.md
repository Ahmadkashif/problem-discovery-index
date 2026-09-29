# The Only Dataset Linking Condition to Value

**Niche:** [[niches/recommerce-platforms/condition-to-price-corpus/profile|Condition-to-Price Corpus]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These platforms have built the only large-scale dataset connecting a physical item's observed condition to what someone actually paid for it, and it is used to set a price for the item in front of the grader.
**Tags:** #cnns #gradient-boosting #survival-analysis #confidence-intervals #evaluation-metrics #revenue-impact #transfer-learning #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to turn millions of items' observed condition and realised price into an empirical account of what secondhand value actually is — and whoever does that defines the market, because no other party can produce it.

## The Problem
A platform has processed eleven million items. For each one it holds photographs, a grade, attributes, a listing date, a price history and a realised outcome. That is eleven million labelled examples connecting how something looks to what it is worth — a dataset no manufacturer, retailer, insurer or researcher can construct, because none of them observe both ends. The platform uses it to look up a comparable price for the next item and to draw an operations dashboard. The questions it answers — what condition is worth, how value decays, which brands hold up, what durability is worth in resale — are asked by every brand entering resale and answered by nobody.

## Why Nobody Has Built This
The corpus accumulated as operational exhaust rather than as an asset, and nobody was assigned to it. The photographs are stored for listings and are not treated as training data. The platforms are operations businesses whose engineering goes to throughput. And the questions the corpus answers are asked by parties outside the business, which makes it somebody else's opportunity until the platform notices.

## What to Build
Model the corpus and publish what is publishable. Learn condition-to-value directly from the photographs and realised prices, which is a large supervised problem with abundant labels and which produces a better condition model than any rubric — this is the foundation and it improves grading, pricing, acceptance and markdown simultaneously. Build a value retention index by brand, category and age, updated continuously, which is genuinely useful to the market and which only a platform of this kind can produce. Estimate depreciation curves, so a brand can see what their products are worth at two, four and six years and what that says about durability. Quantify what condition is worth, in currency, per category, which is the question every operational decision in this sector implicitly answers and none answers explicitly. Offer the intelligence to brands entering resale, since resale-as-a-service customers most need to know what their goods will be worth and the provider holds the answer. Feed everything back into acceptance, grading, pricing and markdown, since one corpus serves all four. Publish the indices, since a platform that defines what secondhand value means in a category holds a position no competitor can take without the same corpus. And treat the photographs as the asset they are, which the fix note develops.

## Target Customer
The platforms themselves, the brands entering resale, and the insurers, lenders and researchers who have no other source for what used goods are worth.

## Impact If Built
Eleven million labelled examples linking appearance to realised value exist nowhere else and are used for a comparable lookup. A learned condition-to-value model improves grading, pricing, acceptance and markdown from one build, and the value retention index is something only a platform of this kind can produce.
