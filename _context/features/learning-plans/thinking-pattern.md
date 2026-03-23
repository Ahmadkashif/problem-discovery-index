# Learning Plans — How to Execute

## Step 1: Map the Topic to Tags

The user says "I want to learn linear regression." DO this:

1. IDENTIFY the primary tag: `#linear-regression`
2. IDENTIFY co-occurring tags that expand the search: `#gradient-boosting` (often paired), `#time-series-forecasting` (common application)
3. IF the topic doesn't map to an existing tag → tell the user. Do NOT invent tags.

## Step 2: Find Vault Problems

RUN: `grep -r "{target-tag}" problem-index/problems/*/ml-opportunity.md`

Each match gives you a pre-scoped ML problem with input data, target, metric, and scope.

- IF fewer than 3 exact matches → expand to co-occurring tags
- IF still fewer than 3 → frame those as "build {technique} as baseline, compare to the recommended approach"

## Step 3: Select 3 Projects with Progressive Difficulty

APPLY these criteria strictly:

**Beginner:** Clear input/output, tabular data, well-known evaluation metric. The technique is the natural first choice.
- ASK: "Could a student with basic Python complete this in a weekend?"

**Intermediate:** Messier data, feature engineering required, possibly multi-step pipeline. Requires tuning and domain knowledge.
- ASK: "Does this require the learner to make non-obvious decisions about data preprocessing?"

**Advanced:** The technique alone isn't enough — needs ensemble methods, careful feature selection, or comparison with more sophisticated approaches.
- ASK: "Does this force the learner to understand the technique's limitations?"

**RULE: No two projects from the same industry.** CHECK this before proceeding. IF violated → swap one project for a different industry.

## Step 4: Write Foundations

Structure `foundations.md` in this exact order:

1. **Intuition first** — what is this technique doing conceptually? DO NOT start with equations.
2. **Math** — minimal formal treatment needed to understand what's happening
3. **Key hyperparameters** — what knobs exist and what they control
4. **Common pitfalls** — what goes wrong and why
5. **When NOT to use it** — the technique's limitations

**IF you catch yourself writing a textbook chapter → STOP. Focus ONLY on theory needed for the 3 selected projects.**

## Step 5: Write Project Files

For each `project-{N}.md`, INCLUDE all of these — no exceptions:

1. **Wiki-link** to the source `ml-opportunity.md` entry
2. **Concrete dataset recommendations** — name specific public datasets (Kaggle, UCI, etc.). Include synthetic data generation as fallback.
3. **4-phase implementation walkthrough:**
   - Exploration: load data, EDA, understand distributions
   - Baseline: simplest possible model (e.g., mean prediction, logistic regression)
   - Primary Model: implement the target technique
   - Iteration: tune, compare, evaluate against the source metric
4. **Evaluation criteria** with the metric from the source `ml-opportunity.md` + thresholds:
   - Beginner: achievable with minimal tuning
   - Good: requires thoughtful feature engineering
   - Excellent: competitive with more complex approaches

**IF you can't find a public dataset → STOP. Write a synthetic data generation recipe instead. "Find a suitable dataset" is never acceptable.**

## Step 6: Write Deployment and Resources

`deployment-guide.md` — practical, not theoretical. Cover: API serving, monitoring, retraining triggers. Keep it actionable.

`resources.md` — curated, not exhaustive. Libraries the learner will actually use. Papers that actually explain the technique well. Communities where they can get help.

## Failure Modes

- **IF you're picking toy problems** → STOP. The whole point is real vault problems. Iris and MNIST are banned.
- **IF all projects are the same difficulty** → STOP. There MUST be clear progression. Re-evaluate complexity.
- **IF two projects share an industry** → STOP. Swap one for a different industry.
- **IF foundations reads like a textbook** → STOP. Focus on what's needed for the 3 projects.
- **IF dataset recommendations are vague** → STOP. Name the exact dataset, not "find a dataset."
