# Indicator Decay and Feed Precision

**Industry:** [[threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** An address that hosted malicious infrastructure last month may host a customer's supplier this month, and feeds rarely say how confident they are or how old the observation is.
**Tags:** #survival-analysis #change-point-detection #gradient-boosting #bayesian-inference #confidence-intervals #time-series-forecasting #evaluation-metrics #probability-distributions

## The Problem
Indicators of compromise — addresses, domains, file hashes, certificates — are observations about a moment. Infrastructure is rented, reassigned and sinkholed; addresses are reallocated to unrelated services; domains expire and are re-registered by someone else; a hash identifies a file that may appear legitimately in other contexts.

Feeds ship indicators with variable metadata about when they were observed, in what context, and with what confidence. Many carry little. Downstream, they are loaded into blocking and detection systems where a stale indicator produces alerts against legitimate traffic, or blocks a service the business depends on — which is the failure that makes security teams distrust feeds and either tune them out or restrict them to detection rather than prevention.

Decay rates differ enormously by indicator type and context. A file hash for a specific malware sample stays valid indefinitely; an address used by a commodity botnet may be meaningless in days; a domain registered specifically for a campaign is reliable while the campaign runs. Treating these alike, which the common formats encourage, is the source of most of the practical problem.

And precision is rarely published. A customer cannot compare two feeds on accuracy because no vendor states theirs, and measuring it independently requires telemetry analysis most customers do not perform.

## What Already Exists
Structured formats support confidence and validity fields and they are populated inconsistently. Threat intelligence platforms provide ageing rules, deduplication and scoring across feeds, generally with customer-configured decay periods rather than learned ones. Some vendors publish confidence levels. Sinkhole and passive DNS data sources make reassignment observable. Reputation services maintain scores with their own ageing. Community efforts have produced guidance on indicator ageing that is not widely implemented.

## The Customisation Gap
Decay should be modelled per indicator type and context rather than configured as a global ageing rule. How long an indicator remains predictive is a survival problem with observable outcomes — an indicator that stops matching malicious activity and starts matching benign traffic has decayed, and that transition is detectable in aggregate telemetry across an installed base.

Reassignment detection is the specific high-value case. Infrastructure moving from malicious to legitimate use is observable through passive DNS, certificate changes, hosting changes and the character of the traffic matching it, and detecting it promptly is what prevents the block that takes down a business service.

Precision measurement requires telemetry and is the most valuable thing a feed could publish. Match rate and true positive rate per feed, per indicator type, per customer segment — computable by any vendor with telemetry access and published by none.

And the per-customer calibration matters. An indicator's practical precision depends on the environment matching it; the same address produces different false positive rates at an organisation whose users browse widely and one whose traffic is narrow, and a confidence score that ignores this is generic where it could be specific.

## Impact If Solved
Stale and imprecise indicators are the reason security teams distrust feeds and confine them to low-consequence uses, which wastes the category's entire value proposition. Learned per-type decay, prompt reassignment detection and published precision would make indicators usable for prevention rather than only detection — which is the difference between intelligence that stops something and intelligence that adds to an alert queue.
