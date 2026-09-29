# Benchmark Integrity

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to produce a score that survives the question "was this in the training data?" — and whoever does that takes the account, because every number the industry currently sells is an upper bound of unknown looseness.

## Profile
**Market Size:** ~$290M US attributable to integrity rather than to running the evaluation
**Share of Parent Industry:** ~36% of category revenue
**Digital Adoption:** None — contamination is unmeasured and reported around
**Target Buyer:** Anyone making a decision on a published score: labs, enterprises, regulators, procurement
**Automation Potential:** High for detection, structural for prevention

## What Makes This a Distinct Niche
Public benchmarks are plausibly inside the training corpora of the models they measure. The extent is unknowable because the corpora are undisclosed, which means every published score is an upper bound whose looseness nobody can quantify. The field's responses — private held-out sets, dynamically generated items, adversarial variants, canary strings — each buy time and none resolve it, because a held-out set is held out only until it is used enough to leak, and a generated item is only as good as the generator. This is the industry's structural crisis and it is also its largest commercial opportunity: a score that comes with credible evidence about contamination is a different product from a score, and nobody sells it.

## Current Tools & Gaps
Private held-out evaluation sets, dynamic and procedural item generation, adversarial perturbations of existing benchmarks, canary strings, and membership inference attempts against model outputs. The gaps: no standard contamination measure accompanies any published score; no accounting for a held-out set's decay as it is used; no distinction between memorisation and genuine capability in the reported number; and no independent custody of the evaluation material, so the party running the test and the party with an interest in the result are frequently the same.

## Problems
- [[niches/ai-model-evaluation-firms/benchmark-integrity/build|🔨 Build: Every Score Is an Upper Bound of Unknown Looseness]]
- [[niches/ai-model-evaluation-firms/benchmark-integrity/buy|🛒 Buy: Held-Out Custody From Competition and Assessment]]
- [[niches/ai-model-evaluation-firms/benchmark-integrity/fix|🔧 Fix: The Private Set That Decays Every Time It Is Used]]
