# Two Products, One Category Name

**Niche:** [[niches/customer-data-platforms/the-platform-architecture/profile|The Platform Architecture]]
**Industry:** [[industries/customer-data-platforms|Customer Data Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A buyer evaluates four vendors in the same category, two of which store their data and two of which never see it, and compares them on a feature matrix.
**Tags:** #evaluation-metrics #compliance #descriptive-statistics #workflow-orchestration #quick-win #data-integration #confidence-intervals #revenue-impact
**Contested on:** This niche is not terminal — the packaged platform and the warehouse-native stack compete on different things for different buyers, and they are stated separately in the sub-niches.

## The Problem
A procurement process lists four customer data platform vendors. Two collect, store and activate the organisation's customer data in their own infrastructure. Two activate from the organisation's warehouse and never hold the data. These have different cost structures, different governance implications, different failure modes, different skills requirements and different things that can go wrong at three in the morning. The evaluation compares them on a matrix of features — destination count, identity capability, real-time support — which obscures the one decision that actually matters, and the buyer chooses on a score.

## Why It's Still Broken
The category name was established before the architectural split and nothing renamed it, so a shared label implies a shared comparison — the vocabulary is doing the damage. Analysts cover both in one quadrant. Vendors on each side present their architecture as an implementation detail rather than as the decision. And buyers do not know there is a decision to make.

## What a Fix Looks Like
Make the architecture the first question. Ask where the data will live and who is accountable for it before any feature is compared, which is the fix and reorders the evaluation around the decision that determines everything else. Separate the requirements that follow from each model, since a warehouse-native choice implies a data team and a packaged choice implies paying for storage twice. Compare total cost properly, including the duplicate storage, the pipeline engineering and the internal capability each model assumes. Assess governance explicitly, as data leaving the organisation's boundary is a different risk posture and is frequently the deciding factor once someone asks. Evaluate identity capability independently of the architecture, since it is the hard part and each model handles it differently. Establish the organisation's own readiness honestly, because the composable model is cheaper and is not viable without the team to run it. Trial with a real workload rather than a demonstration, since the differences appear in operation. Keep an exit path in view, because organisations are moving between these models and a choice that cannot be reversed is a larger commitment than it appears. Publish a plain buyer's guide, which nobody with standing in the category will write. And name the two models distinctly, because a shared label is what prevents the buyer from seeing the choice at all.

## Who Feels the Pain
Buyers choosing an architecture without knowing they are choosing one; vendors whose genuine strengths are invisible in a shared feature matrix; and organisations that discover the implications during implementation.

## Impact If Fixed
The category name predates the architectural split and a shared label implies a shared comparison, which is where the damage is done. Asking where the data lives before comparing features reorders the evaluation around the decision that determines cost, governance and capability.
