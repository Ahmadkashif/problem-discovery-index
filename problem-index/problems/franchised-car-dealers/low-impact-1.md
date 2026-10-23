# Warranty Claims Paid on First Submission and Kept Through Audit

**Industry:** [[franchised-car-dealers|Franchised Car Dealers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every franchised store turns covered repairs into claims against its OEM's policy manual, and DMS warranty modules move the claim without checking it against the rules that decide whether it is paid now and kept later.
**Tags:** #bert #transformers #gradient-boosting #evaluation-metrics #compliance #automation #revenue-impact

## The Problem
When a technician repairs a covered failure, the store is paid by the OEM, not the customer, and only if the claim is right. The warranty administrator, usually one person per store or shared across a small group, builds each claim from the repair order: the labour operation code and the OEM's allowed time, the causal part number, the technician's complaint-cause-correction story, diagnostic trouble codes and test results, photos, sublet invoices and the returned part. The OEM's system edits the claim on submission, and its warranty auditors can review paid claims later and charge them back to the store's parts and service account.

Rejections and chargebacks come from small things: a story that names the symptom but not the test that proved the cause, a labour time claimed above the guide without the required approval, a part not retained for return, a repair performed before prior authorisation was logged. The administrator learns each OEM's habits by experience, and a store that changes administrators often sees its rejection rate rise for months (estimate).

## What Already Exists
DMS warranty modules (CDK, Reynolds & Reynolds, Tekion) assemble claims from the repair order and transmit them to the OEM; OEM warranty portals apply submission edits and report status; outsourced warranty administration services work a store's claims remotely; retail-rate submission firms such as Armatus Dealer Uplift file the statutory requests that raise a store's warranty labour and parts rates (Armatus says it has helped over 7,500 dealers to 19,500+ rate increases).

## The Customisation Gap
The generic tools transmit claims; they do not apply the OEM's rules before the OEM does. The missing layer is OEM-specific: each manufacturer's policy and procedures manual, labour time guide, prior-authorisation thresholds, parts-retention rules and story requirements, turned into checks run before submission, plus a reading of the technician's story against the operation code ("does this story show the diagnosis that justifies this op code?"). It also needs the state clock. Statutes such as Virginia § 46.2-1571 set a 30-day payment deadline and limit chargebacks to six months after the claim except for fraud, so each paid claim has a defined audit exposure window that a tool can track and defend. The data to learn this exists in every store: years of claims with OEM response codes, resubmissions and audit outcomes.

## Impact If Solved
A pre-submission check tuned to each OEM's rules cuts first-pass rejections and the administrator's resubmission work, and a claim file built to survive audit reduces chargebacks that arrive months after the money was spent. Take a store paid ~$1M a year in warranty labour and parts (estimate). Cutting the rejected-plus-charged-back share from ~4% to ~2% of those dollars (estimate) keeps ~$20,000 a year of fixed-ops gross. It also makes the administrator's job transferable rather than dependent on one person's memory.
