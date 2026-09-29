# Judge Model Validity

**Parent Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to state how much a model grader agrees with the humans it replaced, per task and continuously — and whoever does that takes the account, because the dominant grading method in the industry is also the least validated.

## Profile
**Market Size:** ~$170M US
**Share of Parent Industry:** ~21% of category revenue
**Digital Adoption:** Low — universal method, rare validation
**Target Buyer:** Every firm and team using a model as a grader
**Automation Potential:** Very High — validation is a mechanical, repeatable computation

## What Makes This a Distinct Niche
Using a model to grade another model's output has become the dominant automated method because it is the only thing that scales. It inherits the judge's biases, including a documented preference for outputs resembling its own, sensitivity to length and position, and a tendency to reward confident phrasing. These are known and the standard practice is to use a judge anyway with little or no validation against human judgement on the specific task at hand. The contest is validation as a continuous, reported property: how much this judge agrees with these experts on this task, where it systematically diverges, and whether that agreement has moved since the judge model was last updated.

## Current Tools & Gaps
Judge prompts, rubric-in-prompt grading, occasional spot checks against human labels, and published research on judge biases that practice has not absorbed. The gaps: agreement with human judgement is rarely measured and almost never reported alongside the score; judge model updates silently change the measuring instrument; self-preference and length bias are documented and uncorrected; and the judge's non-determinism sets an unreported floor on every result it produces.

## Problems
- [[niches/ai-model-evaluation-firms/judge-model-validity/build|🔨 Build: The Measuring Instrument Nobody Calibrated]]
- [[niches/ai-model-evaluation-firms/judge-model-validity/buy|🛒 Buy: Measurement Validation From Psychometrics and Diagnostics]]
- [[niches/ai-model-evaluation-firms/judge-model-validity/fix|🔧 Fix: The Judge Model That Changed Underneath the Benchmark]]
