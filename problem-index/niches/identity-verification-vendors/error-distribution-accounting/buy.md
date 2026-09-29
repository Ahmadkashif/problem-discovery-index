# Fairness Assessment From Model Governance

**Niche:** [[niches/identity-verification-vendors/error-distribution-accounting/profile|Error Distribution Accounting]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Lending developed disparate impact testing and proxy methodology under regulatory pressure, and identity verification has the same decision shape with none of the apparatus.
**Tags:** #compliance #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #causal-inference #logistic-regression #cross-validation
**Contested on:** Every serious competitor in this niche is fighting to be the first to publish how its error rates are distributed across the populations it decides about — and whoever produces that number defines the standard everyone else is then measured against.

## The Problem
Lending built a whole practice for this: disparate impact testing, proxy methodologies for inferring demographics where they are not collected, less discriminatory alternative analysis, documentation standards and supervisory examination. It exists because credit decisions affect access and the law requires the testing. Identity verification makes a decision that gates access to credit itself, and the practice was never extended to it.

## What Already Exists
Disparate impact testing methodology; demographic proxy estimation techniques; less discriminatory alternative search; fair lending documentation and examination standards; and remediation programme design.

## The Customization Gap
The adaptation is to an access decision made by a vendor rather than a lender. It requires: (1) testing a technical pipeline rather than a credit policy, where the drivers are capture quality and data coverage rather than underwriting variables — this is the substantive translation; (2) the outcome being an inability to complete rather than a denial, which is not currently framed as a decision at all; (3) the vendor rather than the regulated institution holding the model, so responsibility must be allocated between them; (4) rejections with no outcome, which makes the error rate harder to establish than a lending approval rate; and (5) no clear regulatory requirement in many use cases, making adoption voluntary and therefore a positioning choice.

## Target Customer
Data, policy and compliance leadership, regulated institutions carrying access obligations, regulators and advocates, and fairness assessment vendors.

## Impact If Solved
Lending's apparatus exists because the law required it, and the decision that gates access to lending itself has none of it. Translating disparate impact testing onto a technical pipeline is the adaptation, and the proxy methodology transfers directly.
