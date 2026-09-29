# Orchestration and Step-Up Routing

**Industry:** [[identity-verification-vendors|Identity Verification Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Customers stack several verification vendors behind routing rules written by hand, and nobody measures which path actually verifies which kind of applicant.
**Tags:** #gradient-boosting #causal-inference #k-nearest-neighbors #confidence-intervals #evaluation-metrics #feature-engineering #workflow-orchestration #data-integration

## The Problem
Serious identity programmes use several vendors. A database check first because it is cheap and frictionless; document and selfie verification if that is inconclusive; a knowledge-based or phone-based check as an alternative; manual review at the end.

The routing is rules. If the database check scores below X, request a document. If the document fails, offer a retry, then a different method, then review. The rules were written during implementation and adjusted when something broke.

Each step costs money and costs applicants. Every additional step loses a meaningful share of genuine users, and the loss is concentrated among people for whom the step is hardest — someone without a passport, without a current licence, without a phone contract in their own name, without a thick credit file.

Vendor performance varies by segment in ways no customer measures. One vendor is better on younger applicants with thin files; another handles non-US documents better; a third is stronger on device signals. Customers choose a primary vendor on an aggregate benchmark and route everyone through it.

And the whole flow is evaluated on pass rate and fraud rate, neither of which reveals whether a particular path was the right one for a particular applicant.

## What Already Exists
Orchestration platforms — Alloy, Persona, Sardine and several others — provide multi-vendor routing with configurable rules and unified reporting. Vendors expose granular sub-scores. Step-up flows are standard practice. Some platforms offer basic A/B testing of flows.

## The Customisation Gap
Routing is not personalised. Which verification path is most likely to succeed for a given applicant is predictable from what is already known at the first step — device, geography, thin-file indicators, document availability signals — and every applicant instead walks the same decision tree.

Vendor performance by segment is not measured, despite orchestration platforms holding exactly the data to measure it: the same applicant population sent to different vendors with outcomes attached. This is the single most valuable analysis an orchestration layer could run and it is essentially unexploited.

Abandonment is not attributed to steps. Every added step has a dropout cost that varies by population, and flow design is done on cost per check rather than on genuine applicants lost.

And nothing runs proper experiments. Comparing routing policies requires randomised assignment, orchestration platforms are perfectly positioned to run it, and almost none do — so flow changes are evaluated on aggregate pass rate, which conflates the policy with whoever happened to apply that month.

## Impact If Solved
Orchestration exists to handle the applicants a single vendor cannot verify, and it is configured with static rules and evaluated on metrics that cannot see its actual effect. Personalised routing, segment-level vendor measurement and randomised policy comparison improve both conversion and fraud detection, and they specifically help the applicants whose verification is hardest — which is the reason orchestration exists in the first place.
