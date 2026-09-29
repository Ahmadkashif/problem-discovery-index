# Routing Learned From Outcomes

**Niche:** [[niches/identity-verification-vendors/orchestration-and-routing/profile|Orchestration & Routing]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Several vendors sit behind hand-written rules and nobody knows which one verifies which kind of applicant.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #causal-inference #revenue-impact #automation #workflow-orchestration #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to send each applicant to the verification path that will actually verify them — and whoever measures which path works for which kind of person owns the decision layer above every individual vendor.

## The Problem
A customer runs three verification vendors. Applicants are routed by document type and geography, with a fallback on failure. Which vendor is actually better for an applicant with an older licence on an old device, or a thin-file young adult, or a recently arrived resident, is unknown — the rules were written from vendor marketing and one engineer's judgement two years ago. The orchestration layer sees every applicant, every vendor's response and every eventual outcome, and routes on none of it.

## Why Nobody Has Built This
Orchestration was sold as integration convenience, so it was built to connect vendors rather than to choose between them — a product framed as plumbing does not develop opinions about what flows through it. Outcome data for rejections does not exist, making comparison hard. Vendors have no interest in being compared. And customers lack the volume per segment to conclude anything themselves.

## What to Build
Make routing a learned decision. Model each vendor's verification probability by applicant characteristics — document type and age, device, geography, tenure, file depth — which is the core and is what turns a static rule into a decision. Explore deliberately by sending a sample of each segment to each vendor, since without exploration the routing only confirms its own assumptions. Optimise for verification of legitimate applicants rather than for pass rate, because a lenient vendor will look best on the wrong objective. Sequence the cascade by expected success and cost, as running three vendors when the second was always going to succeed is pure expense and latency. Measure per-vendor performance by segment and report it, which is the asset — no individual customer or vendor can produce it. Attribute failures to the path taken, so a rejection caused by routing rather than by the applicant is identifiable. Track cost and latency alongside accuracy, since a cascade that verifies everyone slowly and expensively is not a success. Test fallback paths continuously, because the untested fallback is the one that fails at the worst moment. Feed the segment-level findings back to the vendors, as that is how the whole category improves. And report to the customer which applicants their configuration fails, which is the conversation nobody is having.

## Target Customer
Platform and policy leadership, customers running multi-vendor stacks, orchestration vendors positioned above the market, and verification vendors whose relative strengths are unmeasured.

## Impact If Built
A product framed as plumbing does not develop opinions about what flows through it, so orchestration connects vendors without choosing between them. Learned routing with deliberate exploration is the only place the comparison can be made.
