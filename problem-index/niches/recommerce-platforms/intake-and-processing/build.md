# Two Judgements With Nothing in Common

**Niche:** [[niches/recommerce-platforms/intake-and-processing/profile|Intake & Processing]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Grading and authentication are performed at the same station by the same operation under the same quota, and one is a consistency problem with no opponent while the other is an adversarial call with severe asymmetric costs.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #worker-facing #cnns #automation #descriptive-statistics
**Contested on:** Not terminal — the contest differs by whether there is an adversary, and the decomposition is recorded in the profile.

## The Problem
An intake operation runs one pipeline, one quota and one set of quality metrics over two judgements with opposite properties. Grading errors are small, frequent, correctable and cost margin at the aggregate level; authentication errors are rare, severe, hard to correct and cost either a fraud loss or a wronged seller. Measuring both as accuracy against a sample, staffing both to a throughput target and training both through the same programme produces an operation that is slightly wrong at grading constantly and occasionally catastrophically wrong at authentication, and cannot tell which of those is happening from the metrics it reports.

## Why Nobody Has Built This
The two judgements happen on the same physical item at the same station, which makes one pipeline the obvious design. Authentication is only relevant in some categories, so it was added into an existing grading operation rather than designed separately. Quota and quality metrics came from the warehouse. And the asymmetry of the authentication error is understood by the authenticators and not by the operating model around them.

## What to Build
Separate the pipelines and their measurement. Route items by whether authentication is required, so authentication is a distinct step with its own time allowance, its own staffing and its own metrics rather than a task inside a graded quota — which is the structural change and everything else follows from it. Measure grading on consistency and authentication on error rates by direction, because they are different failure types and a single accuracy figure describes neither. Give the authentication step a time allowance set by the decision rather than by the throughput target, since a quota on an adversarial judgement is how a false accept happens. Build the shared substrate properly: the photography, the item record, the attribute capture and the audit trail serve both and should be excellent for both. Capture the observations rather than only the conclusions, since the grader's detailed observations and the authenticator's specific checks are the inputs to every model downstream and are currently compressed into a grade and a yes. Record escalation and second-opinion paths explicitly for authentication and make them normal rather than exceptional. Report the two cost lines separately, since they scale differently with volume and category mix. And staff and train them as different skills, because they are.

## Target Customer
Managed platform operations leadership, the graders and authenticators, and the resale-as-a-service providers running both for brand clients.

## Impact If Built
One pipeline, one quota and one accuracy metric over two judgements with opposite failure economics produces an operation that cannot tell which kind of error it is making. Capturing the detailed observations rather than the conclusions is what feeds every downstream model in the category.
