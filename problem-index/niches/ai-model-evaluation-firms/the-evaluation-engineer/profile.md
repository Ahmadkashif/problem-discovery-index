# The Evaluation Engineer

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to answer "did the model change or did the measurement change?" without a person spending a day on it — and whoever does that takes the account, because that question consumes most of an evaluation engineer's week.

## Profile
**Market Size:** ~$130M US in loaded engineering cost
**Share of Parent Industry:** ~16% of category revenue equivalent
**Digital Adoption:** None — debugging by hand
**Target Buyer:** Evaluation engineering teams and their leads
**Automation Potential:** Very High — every source of movement is recorded

## What Makes This a Distinct Niche
The evaluation engineer's job is nominally to measure models and actually to establish, over and over, whether a score moved because the model changed or because the grader was non-deterministic, the output parser broke on a formatting change, the rubric was interpreted differently this run, an API returned differently, or the item set was silently edited. This is the category's own internal tax, it consumes most of a skilled engineer's time, and every source of the ambiguity is something the platform recorded and did not attribute. It is the same problem the category sells to its customers, unaddressed inside the firms selling it.

## Current Tools & Gaps
Harness logs, manual comparison of run outputs, ad hoc scripts, and re-running things until the pattern is clear. The gaps: no decomposition of score movement into its causes; no versioning that covers all five moving parts at once; parsers that fail silently and are counted as model failures; no regression tests on the graders themselves; and no measure of how much of the team's time goes to this, so it is never prioritised.

## Problems
- [[niches/ai-model-evaluation-firms/the-evaluation-engineer/build|🔨 Build: Did the Model Change or Did the Grader?]]
- [[niches/ai-model-evaluation-firms/the-evaluation-engineer/buy|🛒 Buy: Build Reproducibility and Bisection Tooling]]
- [[niches/ai-model-evaluation-firms/the-evaluation-engineer/fix|🔧 Fix: The Parser That Failed Silently]]
