# Adverse Impact Auditing

**Parent Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether the instrument passes groups at different rates, and whether the audit that establishes this is capable of detecting a problem.

## Profile
**Market Size:** ~$448M — 40% of the validity and bias niche
**Share of Parent Industry:** ~11% of US pre-employment assessment
**Digital Adoption:** Growing fast under regulatory pressure
**Target Buyer:** Employers' legal and compliance functions; vendors; audit providers
**Automation Potential:** Very high — the computation is a set of ratios

## What Makes This a Distinct Niche

This is the half with a legal driver, and that is what determines its shape. New York City's Local Law 144 requires annual independent bias audits of automated employment decision tools with published results — the first regime of its kind — and the broader regulatory direction is toward more of this.

The consequence is a functioning market. Audit providers exist, vendors offer audit support, employers procure it, and the artefact gets produced and published. It is bounded, computable from pass-rate data the vendor already holds, and it does not require the client's performance data or eighteen months of waiting.

It is also, in its minimum compliant form, the least informative version of the measurement available. Annual, aggregate, on categories the regulation specifies, reported as ratios without intervals, conducted to produce a document rather than to find a problem. The floor has become the practice.

## Current Tools & Gaps

Impact ratio calculations against the conventional thresholds. Bias audit service providers, a growing category. Vendor-supplied demographic pass-rate reporting. Published audit summaries where required. Fairness metric libraries from the ML community, of variable applicability.

The gaps are granularity, frequency and inference. Aggregate annual ratios conceal disparities that appear in specific roles, locations or requisitions. No confidence intervals are reported, so a ratio from a small sample is presented as a finding. Intersectional analysis is rare. And demographic data is frequently incomplete, which is treated as a data problem rather than as a potential source of bias in the audit itself.

## Problems
- [[niches/talent-assessment-platforms/adverse-impact-auditing/build|🔨 Build: Continuous, Segmented Impact Monitoring With Honest Inference]]
- [[niches/talent-assessment-platforms/adverse-impact-auditing/buy|🛒 Buy: Fairness Libraries Adapted to a Statutory Standard]]
- [[niches/talent-assessment-platforms/adverse-impact-auditing/fix|🔧 Fix: An Annual Aggregate Ratio With No Interval]]
