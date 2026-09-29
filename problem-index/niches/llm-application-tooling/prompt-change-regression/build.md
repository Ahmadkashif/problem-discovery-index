# A Deployment With No Regression Test

**Niche:** [[niches/llm-application-tooling/prompt-change-regression/profile|Prompt Change Regression]]
**Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Editing a prompt to fix one case silently changes behaviour across every other case, and there is no regression test — so quality moves in both directions invisibly and teams ship on hope.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #large-language-models #cross-validation #automation #k-means-clustering #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to tell a team whether a prompt change made their application better or worse across the whole input distribution — and whoever does that takes the account, because every team shipping one of these applications is currently guessing.

## The Problem
A support assistant occasionally answers a billing question too tersely. An engineer adds a sentence instructing it to be thorough on billing topics. The reported case is fixed. Three other things change: responses to technical questions get longer and less useful, a safety instruction further down the prompt is now competing with the new one and is followed less often, and a formatting convention the front end depends on breaks for a subset of inputs. None is detected. Two weeks later somebody notices the formatting issue, and the other two are never attributed to anything.

## Why Nobody Has Built This
Building a regression set requires deciding what correct looks like across many inputs, which is the expensive part and which the tooling leaves entirely to the customer. The category's products were built around recording rather than comparing, so the surface is a trace viewer. Teams do not ask for a gate on prompt changes because the ability to change a prompt instantly is felt as a feature. And the failure is invisible and delayed, which means nobody attributes it to the missing control.

## What to Build
Make the comparison automatic. Build the regression set from production traffic automatically — cluster inputs, sample across clusters, capture the current outputs as the baseline — which removes the expensive step that stops teams from starting and is the core of the build. Run a paired comparison on identical inputs between the old and new prompt versions, which removes input sampling error entirely and is dramatically more sensitive than comparing two independent evaluations. Grade with a judge calibrated against the team's own labels on a few dozen cases, so the number means something to them specifically. Report per-cluster results, since the aggregate hides that the change helped billing questions and hurt technical ones — and that segmentation is the finding. Detect unchecked behaviours that changed, by comparing outputs structurally as well as by score, which catches the formatting break and the tone shift that no rubric was watching. Report with uncertainty and refuse to show an arrow on a difference inside it. Gate the deployment, so a prompt change with a significant regression does not ship silently. Grow the set from every reported failure, so the suite improves exactly where the application has been weak. And make it cheap enough to run on every change, which means a small default set and a larger one on merge.

## Target Customer
Every team shipping an LLM application, the platform teams supporting them, and the tooling vendors whose products stop at recording.

## Impact If Built
Building the regression set from production traffic removes the step that stops teams from starting. Paired comparison on identical inputs is far more sensitive than independent evaluation, and structural output comparison catches the behaviours no rubric was watching.
