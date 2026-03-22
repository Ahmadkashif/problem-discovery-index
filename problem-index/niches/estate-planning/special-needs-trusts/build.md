# SNT Distribution Compliance Checker

**Niche:** [[niches/estate-planning/special-needs-trusts/profile|Special Needs Trusts]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Trustees verify that proposed trust distributions won't disqualify the beneficiary from SSI or Medicaid before making the payment — replacing hours of POMS research with a real-time compliance check.
**Tags:** #large-language-models #decision-trees #feature-engineering #evaluation-metrics #tacit-knowledge-ml #compliance

## The Problem
A special needs trust trustee receives a request: "Can the trust pay for a new computer for the beneficiary?" The answer depends on: Is this a first-party or third-party SNT? What is the beneficiary's current SSI amount? Would this be considered "in-kind support and maintenance" (ISM) under SSA rules? If so, does it fall under the "one-third reduction rule" or the "presumed maximum value" rule? Has the beneficiary already received other ISM this month? Would the distribution push the beneficiary's countable resources over the $2,000 SSI limit? Experienced SNT trustees and attorneys develop intuition for which distributions are safe and which are dangerous — they "just know" that paying for a vacation is fine but paying rent directly triggers ISM. This tacit knowledge takes years to develop, and mistakes during the learning period can cost beneficiaries their benefits.

## Why Nobody Has Built This
SSA's rules on what constitutes income, resources, and ISM for SNT beneficiaries are spread across thousands of pages of POMS (Program Operations Manual System), Social Security Rulings, and case law. The rules interact in complex ways — a distribution that's fine in one context (trust pays a store directly for clothing) is problematic in another (trust gives the beneficiary cash to buy clothing). Regional SSA offices sometimes interpret rules differently. Building a reliable compliance engine requires encoding not just the rules but the interpretive layer that experienced practitioners apply — the judgment calls about how SSA field offices will actually treat a distribution vs. how the rules technically read.

## What to Build
A distribution compliance platform where the trustee enters: trust type (first-party/third-party), proposed distribution (amount, payee, purpose, payment method), beneficiary's current SSI amount and Medicaid status, and any other distributions made this month. The system checks the distribution against SSA rules and returns: (1) compliant/non-compliant/needs review, (2) if ISM, the SSI reduction amount, (3) if resource-affecting, the impact on the $2,000 resource limit, (4) recommended payment structure to minimize benefit impact (e.g., "pay the vendor directly rather than reimbursing the beneficiary"), and (5) documentation language for the trust records explaining the distribution rationale. An ML layer trained on distribution decisions from professional trustees captures the tacit knowledge of experienced practitioners — learning which distribution patterns experienced trustees approve vs. refer for legal review.

## Target Customer
Professional trust companies and individual trustees managing 20-200+ SNTs who currently research each distribution request manually using POMS and attorney consultations. Also: SNT attorneys who advise trustees on distribution compliance.

## Impact If Built
Reduces per-distribution compliance research from 30-60 minutes to 2-5 minutes. Prevents benefit-disqualifying distributions that cost beneficiaries $11K-$60K/year in SSI and Medicaid benefits. Enables less experienced trustees to manage SNTs safely, expanding the pool of qualified trustees for a growing population of SNT beneficiaries.
