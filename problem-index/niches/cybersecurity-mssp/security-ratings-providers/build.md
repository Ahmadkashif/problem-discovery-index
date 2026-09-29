# Rating Validity Measured Against Realized Incidents

**Niche:** [[niches/cybersecurity-mssp/security-ratings-providers/profile|Security Ratings Providers]]
**Industry:** [[industries/cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Insurers price on the rating and enterprises gate vendors on it, and the claim that a lower rating means a higher breach probability rests on studies the vendor published itself and has not repeated.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #evaluation-metrics #cross-validation #confidence-intervals #causal-inference #hypothesis-testing #compliance #data-integration

## The Problem
A security rating is a prediction: this organization is more likely to suffer an incident than that one. Consequential decisions follow — premium pricing, vendor rejection, contract terms — and the rated organization frequently has no commercial relationship with the rater and no recourse. The evidentiary basis is typically a small number of vendor-published studies correlating ratings with disclosed breaches, produced at a point in time and not maintained as a standing measurement. Meanwhile disclosed incidents accumulate continuously and are matchable to rated entities, which means the validation the product most needs is available and not being performed as a discipline.

## Why Nobody Has Built This
Breach disclosure is a biased sample — regulated sectors and larger organizations disclose more — so a naive correlation confounds disclosure propensity with incident probability, and doing it properly requires modelling disclosure as well as incidence. There is also a legal dimension the segment feels acutely: ratings have drawn dispute and litigation from rated entities, and a continuous validity record is discoverable in a way a single published study is not. The safe institutional posture has been to publish a study, cite it, and not revisit.

## What to Build
Standing validation as a permanent function rather than a periodic publication. Disclosed incidents are matched to rated entities continuously, with disclosure propensity modelled explicitly using sector, size, and regulatory covariates so that observed incidence can be corrected toward true incidence. Predictive performance is reported as calibration rather than only as discrimination — an insurer pricing on a rating needs the stated risk band to mean what it says. Measurement is broken out by sector, size, and geography, because a rating that predicts well for large regulated firms and poorly for mid-market suppliers is exactly the failure that matters to the vendor management use case, and nobody currently checks. Signal-level attribution shows which observed factors actually carry predictive weight, which directs research at the observations worth collecting and away from those that merely look like security hygiene.

## Target Customer
Chief data officers and heads of research at ratings providers running 100-500 staff, and the insurers and vendor risk teams who price and gate on these ratings with no independent validity evidence.

## Impact If Built
Converts the product's central claim from a cited study into a maintained measurement, which is the only durable answer to the criticism the segment attracts. It is also the strongest commercial claim available: in a market where several vendors publish superficially similar scores, demonstrated calibration by segment is the differentiator, and it can only be built by the party holding both the ratings history and the incident matching.
