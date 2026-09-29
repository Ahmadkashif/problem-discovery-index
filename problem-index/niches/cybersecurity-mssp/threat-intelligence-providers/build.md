# Intelligence Assessments Scored Against What Actually Happened

**Niche:** [[niches/cybersecurity-mssp/threat-intelligence-providers/profile|Threat Intelligence Providers]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Analysts publish thousands of assessments a year with explicit confidence language, most of them resolve within months, and the firm keeps no record of which ones were right.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #time-series-forecasting #causal-inference #descriptive-statistics #bert #transformers #data-integration #revenue-impact

## The Problem
Finished intelligence is full of assessments that resolve: this vulnerability will be exploited at scale, this actor will target this sector, this infrastructure belongs to this group, this campaign will continue. The tradecraft even prescribes confidence language, which is a commitment to a probability. Events then settle most of them within weeks or months, and nobody scores them. So the firm cannot tell a client how often its high-confidence assessments hold, cannot identify which analysts or intelligence types are reliable, and cannot detect that its collection is systematically producing a biased picture of a threat space. Clients meanwhile prioritize patching and defensive investment on assessments whose track record is unknown to everyone including the people who wrote them.

## Why Nobody Has Built This
Assessments are written as prose within reports rather than as structured claims, so extracting them retrospectively is real work and there was never a forward-looking capture step. Resolution is genuinely harder than in most forecasting domains — an assessment that exploitation will occur is unfalsifiable on a short horizon and requires a stated observation window and source to settle. The intelligence profession also has a longstanding discomfort with scoring, partly on the reasonable ground that a correct assessment can be followed by a wrong outcome, and that discomfort has been allowed to prevent measurement rather than to inform how it is done.

## What to Build
A claim register capturing assessments as structured, resolvable predictions at the point of writing: the subject, the assertion, the confidence, the horizon, and the resolution rule agreed then rather than argued later. Resolution draws on the firm's own subsequent collection, on exploitation observed in the wild, and on public incident reporting, with unresolvable assessments explicitly marked as such rather than quietly dropped — a category that is itself informative about how much of the product is checkable. The accumulated record supports calibration by analyst, intelligence type, threat category, and horizon, which is how a research organization learns where it is systematically over- or under-confident. It supports detecting collection bias, since assessments that fail in one threat space consistently usually indicate a coverage gap rather than an analytical one. And it supports the commercial claim nobody in this market can currently make: demonstrated calibration, in a category where every vendor asserts analytical rigour and none evidences it.

## Target Customer
VPs of intelligence and chief research officers at intelligence providers running 300-1,500 analysts, and the security leaders who prioritize defensive investment on these assessments with no accuracy history available.

## Impact If Built
Gives an intelligence business the one asset it structurally should have and does not. Internally it turns analytic tradecraft from doctrine into measurement, which is the only route to improving it. Externally, calibration is the strongest differentiator available in a market where collection breadth is increasingly matched and every competitor claims rigour.
