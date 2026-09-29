# Performance Evaluation & Benchmarking

**Parent Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Category:** Low Digitized
**Contested on:** Whether two products can be compared at all, given that every vendor grades its own exam on a test set nobody has seen.

## Profile

**Market Size:** ~$450M
**Share of Parent Industry:** ~15%
**Digital Adoption:** Very low — self-administered exams
**Target Buyer:** Platform buyers, regulators, researchers, civil society
**Automation Potential:** Moderate — the technical part is easy, the coordination is not

## What Makes This a Distinct Niche

Every vendor publishes accuracy figures computed on internal test sets whose composition is not disclosed. A buyer comparing two products is comparing two self-administered exams with different questions.

This is the field's defining gap. It prevents buyers from choosing on quality, which means the market competes on price, integration and coverage claims. It prevents regulators from verifying platform accuracy reporting, which is increasingly required. And it allows the per-language and per-community failures that cause most documented moderation harm to remain invisible inside an aggregate.

Building a shared benchmark is a coordination problem rather than a technical one. The technical work — a held-out test set, a submission protocol, a leaderboard — is ordinary. The obstacles are that a benchmark requires labelled data in the sensitive categories these products address, that vendors currently leading on unverifiable claims have no interest in being measured, and that no institution owns the problem.

It is the single change that would most improve outcomes across every platform these tools are deployed on, and it has not been built.

## Current Tools & Gaps

Vendor-published accuracy figures on internal test sets. Customer proof-of-concept evaluations, which are the only real comparison and are conducted on the buyer's own data at their own cost with no methodology standard. Academic datasets for some categories, frequently small, dated or narrow. Some regulatory reporting requirements now emerging.

The gaps are everything. No shared benchmark exists in any category. Test set composition is not disclosed by any vendor. Proof-of-concept evaluations are conducted without a methodology, so two buyers evaluating the same products reach different conclusions. Disaggregated results are not reported. And there is no institution positioned to hold a benchmark — the technical barrier is low and the institutional one is total.

## Problems

- [[niches/trust-safety-tooling-vendors/performance-evaluation/build|🔨 Build: The Benchmark Nobody Owns]]
- [[niches/trust-safety-tooling-vendors/performance-evaluation/buy|🛒 Buy: Benchmark Governance From Machine Learning and Testing]]
- [[niches/trust-safety-tooling-vendors/performance-evaluation/fix|🔧 Fix: Every Buyer Runs Their Own Evaluation Badly]]
