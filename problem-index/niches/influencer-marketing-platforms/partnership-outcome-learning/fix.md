# The Discount Code as the Only Evidence

**Niche:** [[niches/influencer-marketing-platforms/partnership-outcome-learning/profile|Partnership Outcome Learning]]
**Industry:** [[industries/influencer-marketing-platforms|Influencer Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** The campaign is judged on redemptions of a discount code, which measures who wanted a discount rather than who was persuaded, and everyone treats the number as the result.
**Tags:** #descriptive-statistics #evaluation-metrics #causal-inference #confidence-intervals #hypothesis-testing #quick-win #revenue-impact #survival-analysis
**Contested on:** Every serious competitor in this niche is fighting to turn a corpus of thousands of past partnerships into the answer to the only question the category is asked — and whoever closes that loop makes every subsequent selection better than the last.

## The Problem
Every creator gets a unique discount code. The campaign is evaluated on how many times each code was redeemed. That number is the only creator-level outcome data most brands ever produce, and it measures something quite specific: people who saw the content, wanted a discount, remembered the code and used it. It misses everyone who bought without the code, everyone who bought later, and everyone who bought through a different channel after seeing the content. It over-credits creators whose audiences are deal-seeking and under-credits creators who build preference. Selection decisions for the next year are made on it.

## Why It's Still Broken
The code is the only creator-level signal that is trivially available, so it became the metric — measurement follows availability rather than relevance. Codes are cheap to issue and produce a clean number. Everyone understands them. And the bias is systematic rather than random, which means it does not average out and does quietly distort every comparison.

## What a Fix Looks Like
Use the code as one signal, not as the answer. Report code redemption alongside an estimate of what it misses, which is derivable from the ratio of coded to uncoded sales in the campaign window and is the fix — the correction factor is computable and nobody computes it. Add creator-level links and landing pages, which capture a different and partly overlapping population and are cheap to deploy. Measure the uplift in overall sales during and after the campaign window against a baseline, since that is the quantity that matters and the code is only a proxy for it. Track post-window purchase, because persuasion has a delay and a redemption window of seven days systematically favours impulse over preference. Correct for audience deal-seeking behaviour explicitly, as some audiences use codes far more than others and that is a property of the audience rather than of the creator's persuasiveness. Run occasional holdouts by suppressing a creator's content region or cohort, which is the only real evidence and is rarely attempted at this scale. Combine code, link, uplift and survey signals rather than choosing one, since each is biased differently and the combination is far better than the best single measure. Report the measured share of attributable sales so brands know how much of the picture the code represents. Use the same method across campaigns so comparisons are valid over time. And publish the correction, because a category whose headline creator metric is known to be biased and is used anyway will keep selecting the wrong creators.

## Who Feels the Pain
Creators who build preference and are ranked below those with deal-seeking audiences; brands selecting on a biased signal for years; and the category, whose only widely used outcome metric measures the wrong thing.

## Impact If Fixed
Measurement followed availability rather than relevance, and the bias is systematic so it never averages out. The ratio of coded to uncoded sales in the campaign window gives a correction factor that is computable today and that nobody computes.
