# A Coverage Prediction Before the Sample Is Run

**Niche:** [[niches/clinical-laboratories/molecular-genetic-coverage-prior-auth/profile|Molecular & Genetic Test Coverage and Prior Authorization]]
**Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A molecular lab spends hundreds of dollars running a test before it knows whether anyone will pay for it, and has the history to predict the answer.
**Tags:** #gradient-boosting #large-language-models #feature-engineering #survival-analysis #revenue-impact #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to get each high-dollar molecular or genetic test paid, through authorization, Z-code, coverage evidence and appeal, and whoever collects on the highest share of tests performed takes the account.

## The Problem
When a hereditary cancer panel, a tumour profile or a prenatal screen arrives, the lab must decide whether to run it now, hold it for authorization or contact the patient about cost. The decision is usually made by rule ("run everything, chase later") because nobody knows the odds. A share of tests is then never paid, and patients receive surprise bills that damage the ordering relationship.

## Why Nobody Has Built This
Coverage logic is spread across payer policies, benefit-manager criteria, MolDX articles and the patient's clinical history, and changes often. The history that would train a model sits in billing, while the run decision sits in lab operations. Vendors sell submission tools, not predictions.

## What to Build
A model trained on the lab's own orders and outcomes that predicts, per test and patient, the probability of payment and the expected time to payment. Inputs are payer, plan, test, diagnosis, clinical criteria met according to the requisition and notes, ordering provider history and authorization status. A language model maps each case to the applicable policy clauses. The output is a run, hold or patient-contact decision with the missing evidence listed, and a time-to-payment curve for finance.

## Target Customer
VPs of reimbursement and lab operations at genetic, oncology and transplant testing labs running 1,000+ high-dollar tests a week.

## Impact If Built
Raising the paid share of performed tests by five points on a lab with $300M of molecular revenue is ~$15M a year (estimate), with fewer patients billed for tests their plan rejected.
