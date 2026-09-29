# Decision Quality Measurement

**Parent Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Category:** High Market Share
**Contested on:** Whether decision quality means agreement with an auditor applying the policy literally, or linkage to what actually happened after the decision.

## Profile

**Market Size:** ~$2.0B
**Share of Parent Industry:** ~17%
**Digital Adoption:** Low — sampled manual audit
**Target Buyer:** Vendor quality leadership, platform trust and safety
**Automation Potential:** High — the outcome data exists and is not returned

## What Makes This a Distinct Niche

A vendor makes hundreds of millions of decisions a year. Its entire commercial standing rests on the quality of those decisions. And the only quality signal it receives is whether a small sample matched an auditor applying the policy document.

That metric has a specific, well-understood pathology. An auditor grading against a written policy will mark the literal reading correct, because that is what the document says. So reviewers learn to apply the policy literally — and the hardest cases, the ones where the policy's language fails to anticipate the situation and contextual judgement is the entire value a human adds, are exactly the cases where literal application is wrong and gets scored right. The metric teaches people to stop doing the thing they were hired for.

What would fix it exists and does not come back. Whether the decision was upheld on appeal. Whether the enforcement was later reversed. Whether the content, if left up, caused the harm it was assessed for. Whether the account went on to violate repeatedly. All of it sits with the platform, and none of it returns to the vendor — so a business built on decision quality has no measure of decision quality beyond internal agreement.

## Current Tools & Gaps

Quality audit programmes are universal and broadly similar: a sampled subset of each reviewer's decisions re-reviewed by an auditor, scored against the policy, aggregated into an accuracy figure that feeds contractual service levels and individual performance management. Some contracts specify calibration sessions where auditors align on contested cases. Client-side audits run in parallel and occasionally disagree with the vendor's own.

The gaps are structural. Inter-rater reliability is rarely computed properly, so nobody knows how much of the measured error is reviewer variance and how much is auditor variance. Sample sizes are set by contract rather than by what would actually distinguish one reviewer from another, which means much of what is reported as individual performance is noise. Appeal outcomes, the single most available external signal, are almost never returned. Nothing distinguishes an error of policy application from a case where the policy itself was inadequate, so policy failures are recorded as reviewer failures and the policy never learns. And no vendor can demonstrate to a prospective client that its decisions are better than a competitor's by any measure a client would find meaningful.

## Problems

- [[niches/content-moderation-services/decision-quality/build|🔨 Build: Quality Measured Against Outcomes]]
- [[niches/content-moderation-services/decision-quality/buy|🛒 Buy: Inter-Rater Reliability From Clinical Research]]
- [[niches/content-moderation-services/decision-quality/fix|🔧 Fix: The Metric That Punishes Judgement]]
