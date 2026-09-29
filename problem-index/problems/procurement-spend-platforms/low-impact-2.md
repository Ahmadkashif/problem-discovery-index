# Supplier Risk and Concentration Monitoring

**Industry:** [[procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Risk data subscriptions supply financial health scores and sanctions screening for any named supplier, and none of them can tell a company which single failure would actually stop its production line.
**Tags:** #graph-neural-networks #gradient-boosting #survival-analysis #change-point-detection #confidence-intervals #evaluation-metrics #compliance

## The Problem
Supplier risk moved from a procurement niche to a board-level concern over a few disrupted years. Companies now screen for financial distress, sanctions exposure, cyber posture, labour practices and geographic concentration, largely by subscribing to external risk data and attaching scores to supplier records.

Those scores describe suppliers in isolation. The question that matters is about the company's own exposure: which supplier failing would halt which product line, how quickly, and with what alternative. That depends on what is bought from whom, which parts have single sources, how much inventory buffers each, and how long qualification of an alternative takes — all internal facts that no external data provider holds.

Concentration is invisible for the same reason the supplier master is broken. A company buying from four suppliers who all source from one sub-tier manufacturer has a concentration it cannot see, because the platform knows tier one and nothing beyond it.

And monitoring is periodic. Risk is reviewed at onboarding and annually, while distress develops over months and is visible in behaviour long before it appears in a rating.

## What Already Exists
Risk data providers (Dun & Bradstreet, Moody's, Craft, Interos, EcoVadis) supply financial, compliance, ESG and increasingly network data. Sanctions and watchlist screening is a mature commodity. Supplier information management modules are standard in the suites. Business continuity planning frameworks are well established. Some platforms map sub-tier relationships from public sources.

## The Customisation Gap
External scores are about the supplier; the exposure is about the buyer. Combining spend, single-source status, inventory cover, lead time and qualification effort into an impact estimate is entirely internal and is what turns a score into a decision. Almost nobody computes it, because the inputs live in the ERP rather than the procurement suite.

Behavioural distress signals are the second gap and are strong. A supplier that has started shipping late, requesting faster payment terms, disputing invoices more often, or whose quoted lead times have crept out, is showing distress the platform observes directly — months before a credit rating moves. Across the platform's whole customer base this signal is far richer than any one buyer sees.

Sub-tier mapping is the third. It is genuinely hard, external providers do it partially from public sources, and the platform has a better route: overlapping supplier behaviour across its customer base reveals common dependencies that no filing discloses.

## Impact If Solved
Supply disruption is now a routine cause of material financial loss and is managed with scores that describe suppliers rather than exposure. Combining internal criticality with behavioural distress signals turns supplier risk from a screening exercise into an early warning system, using observations the platform already collects.
