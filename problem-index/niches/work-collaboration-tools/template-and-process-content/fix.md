# Nobody Measures Whether a Template Survived

**Niche:** [[niches/work-collaboration-tools/template-and-process-content/profile|Template & Process Content]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** Template galleries report downloads and adoptions, which measure the decision to try, and nobody measures whether the template was still in use a month later — which is the only thing that would tell anyone if it was any good.
**Tags:** #survival-analysis #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #quick-win #automation #cross-validation
**Contested on:** Every serious competitor in onboarding content is fighting to give a team a starting structure that matches how that team actually works — and whoever produces a template teams keep past the first month takes the adoption problem.

## The Problem
A content team publishes forty templates a year and reports adoptions. The most-adopted template is treated as the most successful and is promoted more prominently, which increases its adoptions further. Whether any team that adopted it is still using it, whether they gutted it in week two, and whether they would have been better off starting from a blank workspace are all unmeasured. The content function is optimising for a number that measures the appeal of a title and a screenshot.

## Why It's Still Broken
Adoption is easy to count and survival requires tracking a workspace's structural evolution over months, which nobody has instrumented. The content function's metrics were set when the gallery was built and have not been revisited. And a survival metric would show that most templates are abandoned, which is a finding about the team's own work and is therefore not one they will commission.

## What a Fix Looks Like
Measure survival and modification, which are both computable from workspace history. Survival: what proportion of teams adopting a template are still using a recognisably similar structure after one, three and six months, which is a straightforward analysis over structural snapshots. Modification: what teams change, aggregated — which is simultaneously the quality signal and the improvement instruction, since a field that ninety percent of adopters delete should not be in the template. Report both per template and rank the gallery by survival rather than by adoption, which changes what gets promoted and therefore what gets adopted. Compare against a baseline of teams who started from scratch, since the honest question is whether the template helped at all and some of them will not have. And feed the modification aggregate into the next version automatically, which is the loop the build note describes and which turns the content function from an authoring operation into a curating one.

## Who Feels the Pain
Teams who adopted a structure that did not fit and spent three weeks discovering it; content teams optimising against a metric that measures a thumbnail; and platforms whose principal onboarding mechanism has an unmeasured failure rate.

## Impact If Fixed
Survival measurement is a query over structural history and would immediately reorder the gallery by something meaningful. The modification aggregate is the more valuable half, since it converts the abandonment everyone experiences into a specific instruction about what the template should have contained.
