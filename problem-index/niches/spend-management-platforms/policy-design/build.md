# Which Policies Actually Work

**Niche:** [[niches/spend-management-platforms/policy-design/profile|Policy Design]]
**Industry:** [[industries/spend-management-platforms|Spend Management Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Thousands of companies are running a natural experiment in spend policy on one platform and nobody has read the results.
**Tags:** #causal-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #gradient-boosting #k-means-clustering #descriptive-statistics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to say which spend policies actually produce better outcomes rather than merely more exceptions — and whoever can answer that across thousands of companies sells policy instead of a rule builder.

## The Problem
Does a lower transaction limit reduce wasteful spend or just generate approvals? Does requiring receipts below a threshold change behaviour or only create work? Does routing approvals through a second manager catch anything? These are empirical questions, and the platform hosts thousands of companies with different answers configured, whose spend patterns, exception rates, and financial outcomes it observes continuously. The best practice templates it ships were assembled from convention and nobody has ever checked whether any of them do anything.

## Why Nobody Has Built This
Policy is the customer's to set, so the platform positioned itself as a tool rather than as an authority — and a tool has no reason to develop an opinion. The comparison requires defining a spend outcome, which nobody has done. Confounding is real, since companies that choose strict policies differ from those that do not. And a finding that a popular control does nothing would be commercially awkward.

## What to Build
Compare the configurations and then experiment. Define what a good spend outcome is — waste, policy violations that mattered, spend per unit of revenue, employee friction — which is the core and is the definitional work nobody has done. Compare outcomes across policy configurations at scale, since the customer base is a natural experiment of a size no consultancy could assemble. Handle confounding seriously with matching and sensitivity analysis, because companies choosing strict policies differ systematically and naive comparison will produce nonsense. Run actual experiments where customers consent, as small randomised changes to thresholds are low-risk and settle questions comparison cannot. Measure the cost side as well as the benefit, since a policy's friction is quantifiable in exception hours and is never counted. Segment by company size, sector and growth stage, because the right policy for a fifty-person company is not the right one for a thousand. Ship evidence-based templates rather than conventional ones, which is the product and is a genuine differentiator. Tell customers when a policy they have is doing nothing, as that is valuable, credible and costs nothing to deliver. Publish what is learned, since it would establish the platform as the authority on the question. And revisit as behaviour changes, because policy effects are not permanent.

## Target Customer
Product and customer success leadership, finance leaders choosing policies from convention, auditors assessing control design, and consultancies selling policy advice with no evidence base.

## Impact If Built
Positioning as a tool meant never developing an opinion, so the templates encode convention. Thousands of companies running different configurations on one platform is a natural experiment in control design that nobody has read.
