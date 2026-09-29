# Evaluation Discipline the Category Has Not Adopted

**Niche:** [[niches/developer-tools-vendors/ai-coding-assistants/profile|AI Coding Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Code generation has public benchmarks, held-out evaluation and contamination controls in the research literature, and the commercial category reports acceptance rates from telemetry.
**Tags:** #large-language-models #evaluation-metrics #cross-validation #confidence-intervals #hypothesis-testing #transformers #descriptive-statistics #transfer-learning
**Contested on:** Every serious competitor here is fighting to be the assistant an engineering organisation actually runs on — and that contest is decided twice, by the developer and by the security function, which is why this niche is not terminal and is decomposed below.

## The Problem
The research community evaluating code generation has developed functional correctness benchmarks, execution-based testing, contamination detection and increasingly realistic repository-level tasks, with published results and known limitations. The commercial category sells on telemetry metrics that no researcher would accept, and buyers have no way to evaluate a tool against their own code beyond a two-week trial and a vote.

## What Already Exists
Public code generation benchmarks with execution-based grading; repository-level and issue-resolution benchmarks that approximate real work; contamination detection methods; pass-at-k and its variants; and the broader evaluation literature on held-out sets and leakage. Execution sandboxes for running candidate code are commodity.

## The Customization Gap
The adaptation is to a specific customer's codebase. It requires: (1) evaluation tasks derived from the customer's own repository history — take a merged change, reconstruct the state before it, and ask whether the assistant produces something equivalent — which is the only evaluation that answers the buyer's actual question and is entirely constructible from data they have; (2) contamination control against a public model's training data, which matters much less for private code and much more for popular open-source dependencies, and should be stated rather than assumed; (3) grading beyond tests passing, since a change that passes tests and violates the codebase's conventions is a maintenance cost, which means style, dependency and architectural conformance checks alongside correctness; (4) task difficulty stratification, because performance on trivial and on substantial changes differs enormously and a single number averages away the decision; and (5) evaluation as a recurring process rather than a procurement exercise, since the models change underneath the customer continuously and a benchmark from six months ago describes a different product.

## Target Customer
Engineering organisations evaluating assistants, assistant vendors, and the evaluation and benchmarking vendors emerging alongside them.

## Impact If Solved
A rigorous evaluation literature exists and the commercial category reports telemetry, which leaves buyers unable to compare tools on anything but sentiment. Customer-repository-derived tasks are the adaptation that makes evaluation relevant, and recurring evaluation is what keeps it true.
