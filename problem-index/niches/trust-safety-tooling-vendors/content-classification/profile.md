# Content Classification

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** High Market Share
**Contested on:** Whether a classifier works where the harm actually concentrates — lower-resource languages, specific communities, context-dependent meaning — or only in the aggregate.

## Profile

**Market Size:** ~$900M
**Share of Parent Industry:** ~30%
**Digital Adoption:** High — capable models across modalities
**Target Buyer:** Platform trust & safety leadership, policy teams
**Automation Potential:** High — and the remaining failures are where automation is hardest

## What Makes This a Distinct Niche

The classifiers are the product: text, image, video and audio models detecting harassment, violence, sexual content, self-harm, extremism, fraud and a long list of category-specific harms, across many languages, at platform scale.

They are genuinely capable, and the capability is uneven in a specific pattern. Performance is strongest in high-resource languages on unambiguous content and weakest exactly where the documented moderation harms concentrate: lower-resource languages, code-switched and transliterated text, reclaimed speech within a community, context-dependent meaning, content that describes harm rather than committing it, and novel harm types.

Every vendor reports an aggregate accuracy figure that conceals all of it. A classifier that performs excellently in English and poorly in a language with forty million speakers reports a good number, and the buyer sees a good number.

Every serious competitor is fighting over the hard cases and none can demonstrate performance on them, because the reporting is an aggregate and the benchmark is the vendor's own.

## Current Tools & Gaps

Multimodal classifiers with broad language coverage, fine-tuning against customer policy, hash matching for known material, and increasingly large language model approaches for context-dependent categories. Confidence scores per classification. Custom category training for customer-specific policies.

The gaps are in the distribution of performance. Results are not reported per language, per community or per content type, so the failures are invisible. Context is handled poorly, so a quotation, a report of harm, a counter-speech post and the harm itself are frequently indistinguishable to a classifier. Reclaimed speech is a documented and persistent failure. Code-switched and transliterated content is covered worst in the languages where it is most common. And no vendor publishes a per-segment breakdown, so a buyer choosing for a specific market is choosing blind.

## Problems

- [[niches/trust-safety-tooling-vendors/content-classification/build|🔨 Build: Performance Where the Harm Is]]
- [[niches/trust-safety-tooling-vendors/content-classification/buy|🛒 Buy: Fairness Evaluation From Machine Learning Research]]
- [[niches/trust-safety-tooling-vendors/content-classification/fix|🔧 Fix: The Aggregate Hides the Languages That Fail]]
