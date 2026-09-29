# Build: Verdicts Joined Back to Indicators

**Niche:** Precision Verification
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A feedback loop carrying alert dispositions back to the indicators that produced them, at population scale, so precision becomes a measured property of a feed rather than an implied one.
**Tags:** #evaluation-metrics #confidence-intervals #bayesian-inference #logistic-regression #hypothesis-testing #data-integration #compliance #automation
**Contested on:** Whether, when an indicator fires, anyone can establish that the activity it flagged was genuinely malicious.

## The Problem

Every security operations centre generates the ground truth this industry needs and throws it away.

An alert fires because an indicator matched. An analyst investigates and records a disposition: true positive, false positive, benign, duplicate. The ticket closes. That verdict is the single most informative piece of data about the indicator that produced it, and it goes into a case management system and stays there.

It is not joined back to the indicator. It is not sent to the vendor. It is not aggregated across organisations. So the feed that produced the alert learns nothing, the vendor cannot compute precision, and the next customer receives the same indicator with the same confidence score derived from how it was collected rather than from how it has performed.

The scale available is substantial. A vendor bundled with endpoint telemetry sees alerts across tens of thousands of organisations. If even a fraction of those dispositions returned, the resulting precision estimates would be the first real measurement of feed quality anyone has produced.

What stands in the way is partly a plumbing problem — the join between the alert and the indicator, and the channel back to the vendor — and partly that the dispositions themselves are noisy in specific and correctable ways.

## Why Nobody Has Built This

**Dispositions are recorded for ticket closure, not for measurement.** An analyst under time pressure picks the category that closes the case. False positive and benign are used interchangeably. Genuinely ambiguous cases are recorded as whatever is defensible, which is usually not a true positive.

**The join is missing.** Alert records frequently do not retain which indicator and which feed produced the match, particularly after deduplication, so the disposition cannot be attributed even within one organisation.

**No channel back to the vendor exists.** There is no standard mechanism, format or expectation for returning disposition data to an intelligence provider, and no contractual basis in most subscriptions.

**Customers have no incentive to contribute.** Returning disposition data helps the vendor improve a product the customer already paid for, and reveals what the customer's analysts concluded about their own environment.

**Precision estimates would be unflattering.** Against a very low base rate of malicious traffic, even a good indicator produces mostly false positives, and the honest number will look poor to anyone unfamiliar with the arithmetic.

**Ambiguous cases dominate.** A large share of alerts are closed without a firm conclusion, and how those are treated determines the resulting precision figure — which makes the measurement genuinely contestable.

## What to Build

**Retain the join.** Every alert records the indicator and the feed that produced it, retained through deduplication. This is a provenance change in the matching pipeline and it is the prerequisite for everything.

**Improve the disposition taxonomy where the analyst works.** Separate false positive from benign-true-match from unresolved, and make the distinction cheap to record. Most of the noise in this data comes from a taxonomy that does not fit what analysts actually conclude.

**Weight by investigation depth.** A disposition reached after a thorough investigation is stronger evidence than one recorded in ninety seconds. Capturing investigation effort alongside the verdict lets the estimate weight accordingly, which handles much of the noise without asking analysts to do more.

**Build the contribution channel with real reciprocity.** Customers contribute dispositions and receive, in return, precision figures for every feed in their stack and early warning derived from the aggregate. Contribution has to be worth something to the contributor, which is the lesson from every voluntary reporting scheme that succeeded.

**Handle the ambiguous cases explicitly.** Report precision under several treatments of unresolved alerts — counted as false, excluded, or apportioned — and state the sensitivity of the result to that choice. Concealing it would make the measurement attackable; stating it makes it credible.

**Calibrate vendor confidence scores against observed precision.** Vendors assign confidence based on collection method. Checking whether high-confidence indicators actually perform better is a direct test of an assertion every vendor makes and nobody verifies.

**Publish with intervals and sample sizes.** Precision for a feed segment with forty observations is a different claim from one with forty thousand, and reporting the uncertainty honestly is what separates this from marketing.

## Target Customer

Vendors with large telemetry footprints, who can aggregate dispositions across an installed base and for whom a substantiated precision claim is a position no pure-play competitor could reach.

Security operations leadership, who would contribute dispositions in exchange for precision figures on their own stack — which is a trade most would take.

An independent body or consortium as the neutral aggregator, since a vendor computing precision for its own feed alongside competitors' is not a credible arrangement without external governance.

## Impact If Built

The category's central implied claim — that its indicators flag real threats — becomes measurable rather than asserted.

Improving the disposition taxonomy and capturing investigation depth would clean up the ground truth at the point it is generated, which is the cheapest possible improvement and helps the analyst as well.

And calibrating vendor confidence scores against observed precision would test an assertion made on every indicator in every feed, which nobody has ever checked.
