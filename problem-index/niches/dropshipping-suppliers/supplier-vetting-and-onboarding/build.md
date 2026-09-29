# Approved and Never Reviewed

**Niche:** [[niches/dropshipping-suppliers/supplier-vetting-and-onboarding/profile|Supplier Vetting & Onboarding]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A sourcing analyst approves suppliers onto the platform from documents, a sample order and a video call, then never learns whether the approval was right.
**Tags:** #logistic-regression #gradient-boosting #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to predict whether a supplier will perform before any orders have been routed to them — and whoever does that well controls who gets into the marketplace and therefore what it is worth.

## The Problem
An analyst reviews forty supplier applications a week. Each one gets a registration document, a photograph of a warehouse, a sample order that arrived reasonably, and a call. They approve or decline. Eighteen months and two hundred thousand orders later, nobody has told them which of their approvals turned out to be excellent suppliers and which produced a year of disputes. They are making a prediction repeatedly, at volume, with the outcome fully observed by their own employer, and receiving no feedback of any kind. Whatever skill exists in the role is unmeasurable and untransferable.

## Why Nobody Has Built This
Onboarding and performance sit in different teams with different systems, and nobody owns the join — this is the entire reason the loop is open and it is organisational rather than technical. Outcomes arrive months after decisions, past any natural review cycle. The decision record is a free-text assessment that cannot be analysed. And analyst throughput is the metric, which rewards speed over calibration.

## What to Build
Close the loop between the approval and the outcome. Record every vetting decision as structured evidence — what was checked, what was found, what the analyst weighted — so decisions can be analysed at all, which is the prerequisite and is absent today. Join approvals to downstream supplier performance and report it back to the analyst who made the call, which is the whole of the fix and turns a repeated blind judgement into a learnable one. Learn which pre-approval signals actually predict performance, since the platform now has thousands of decisions with observed outcomes and this is a well-posed supervised problem with a real label. Gather external evidence automatically — registration records, shipping records, trade data, other platforms' presence, complaint history — which is the work the analyst does manually and slowly, and is where most of the available signal is. Verify the sample order against the catalogue rather than treating it as a formality, which is the fix note's subject. Calibrate analysts against each other on the same applications, since inter-rater agreement is currently unknown and probably poor. Tier approvals rather than deciding binary, so a marginal supplier can enter with volume limits and a monitored trial instead of being admitted outright or refused. Re-vet on triggers rather than never, because ownership, factories and staff change and approval is currently permanent. And measure the vetting function on downstream supplier performance rather than on applications processed.

## Target Customer
Supplier operations and sourcing teams at dropshipping and sourcing platforms, marketplace trust teams, and the analysts themselves.

## Impact If Built
An analyst makes the same prediction forty times a week with the outcome fully observed by their employer and never learns anything. Joining approvals to downstream performance makes the judgement learnable and turns thousands of past decisions into a well-labelled supervised problem.
