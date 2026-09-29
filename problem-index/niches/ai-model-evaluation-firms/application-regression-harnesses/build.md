# A Test Set Written Once and Never Maintained

**Niche:** [[niches/ai-model-evaluation-firms/application-regression-harnesses/profile|Application Regression Harnesses]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A product team writes an evaluation set during the first sprint, production drifts away from it over the following year, and the suite keeps passing while the application gets worse.
**Tags:** #large-language-models #evaluation-metrics #k-means-clustering #dbscan #change-point-detection #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to tell a product team whether their change made their own application better, per commit, at a cost that fits a tooling budget — and whoever does that takes the account, because that is the only question an application team is asking.

## The Problem
The evaluation set was written in week three by two engineers who imagined what users would ask. A year later the product serves a different user base with different phrasing, a new feature area nobody anticipated, and a long tail of requests the original set does not resemble. The suite runs on every commit and passes. Support tickets tell a different story. Nobody has updated the set because it is not anybody's job, and adding cases requires deciding what the right answer is, which is the expensive part.

## Why Nobody Has Built This
Test set maintenance is unglamorous, uncredited work that competes against shipping features. Deciding the expected output for a new case requires domain judgement, which is the bottleneck. Production traffic contains customer data that frequently cannot be used as test material without handling. And the suite passing is interpreted as good news rather than as a signal that it has stopped discriminating, which is the same failure the software testing world named decades ago.

## What to Build
Grow the evaluation set from production. Cluster production traffic and compare its coverage against the evaluation set, surfacing the regions of real usage the suite does not represent — which is a direct, computable answer to a question no team currently asks and is the core of this build. Propose new test cases from underrepresented clusters, selecting for informativeness rather than volume, so a team adds ten cases that discriminate rather than a thousand that do not. Mine production failures — thumbs-down, escalations, retries, abandoned sessions — into candidate cases, since those are the highest-value items available and they are already labelled by user behaviour. Make expected-output authoring cheap with a judge proposing and a human approving, because the judgement bottleneck is what stops maintenance. Handle customer data properly: redact, synthesise or keep the set inside the team's boundary, since the data problem is the reason many teams never start. Report suite coverage and discriminative power over time, so a suite going stale is visible rather than reassuring. Retire cases that every version passes, which is what keeps the suite informative and small enough to run per commit. And version the set alongside the application, so a score is interpretable against the suite it came from.

## Target Customer
Engineering teams shipping model-based applications, and the evaluation platform vendors whose product currently ends at running the set the customer typed in.

## Impact If Built
A suite that always passes has stopped measuring, and teams read it as good news. Comparing production traffic coverage against the evaluation set answers that directly, and mining production failures supplies the cases that discriminate.
