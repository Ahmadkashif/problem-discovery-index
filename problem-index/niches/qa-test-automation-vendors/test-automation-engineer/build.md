# Repairing Rather Than Designing

**Niche:** [[niches/qa-test-automation-vendors/test-automation-engineer/profile|The Test Automation Engineer]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Test automation engineers spend their weeks repairing tests broken by interface changes rather than designing the tests that would find the defects nobody has thought of.
**Tags:** #bert #k-means-clustering #descriptive-statistics #large-language-models #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to return a test engineer's week from repair to design — and whoever does that takes the quality function, because repair is currently the job and design is what the role was created for.

## The Problem
An engineer joins to design tests. Their first month is spent repairing the existing suite after a design system migration. Their second is spent on a queue of failures from the ongoing interface work. By month six they have designed four new tests and repaired eleven hundred, and the defects reaching production are in behaviours nobody thought to test — which is exactly the work they were hired for and have not done. They can describe several such behaviours from memory, having noticed them while repairing, and have never had the time to act on any of it.

## Why Nobody Has Built This
The repair queue is urgent and the design work is not, which is the standard displacement and requires a structural response rather than a resolution to do better. The tooling addresses authoring and execution and offers nothing for the design activity, because design is judgement and judgement has not been a product category. The repair work is unmeasured, so the displacement is invisible to management until an engineer resigns and explains it. And quality engineering is under-resourced relative to development almost everywhere, which makes the queue permanently larger than the capacity.

## What to Build
Remove the repair and support the design. Automate the repair properly, as the maintenance niche describes, with classification so that the engineer sees only the failures that need judgement — which is the prerequisite and returns most of the week. Repair in bulk, since a single interface change breaking forty tests is one decision and forty edits. Then support the design half, which nothing currently does: surface the behaviours that are unverified and consequential from the coverage analysis; surface the defects that escaped and the behaviours they involved, which is the strongest available input to what should be tested next; surface the areas of the application with the highest change rate and defect density, since that is where design effort returns most; and capture the engineer's own observations as they work, since they notice fragility constantly while repairing and have nowhere to put it. Measure the split between repair and design explicitly and report it, because the displacement is invisible and the number is the argument. And treat the design output as the role's product, since an engineer measured on tests repaired will repair tests.

## Target Customer
Quality engineering leadership, the engineers themselves, and the vendors whose products address the half of the job that requires no skill.

## Impact If Built
The role's valuable half is displaced by its mechanical half, which is invisible because nobody measures the split. Automating repair returns the week and surfacing escaped defects and unverified behaviours gives the design work an input it has never had.
