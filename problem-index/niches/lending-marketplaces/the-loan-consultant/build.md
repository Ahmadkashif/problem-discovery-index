# Knowing Who Will Say Yes

**Niche:** [[niches/lending-marketplaces/the-loan-consultant/profile|The Loan Consultant]]
**Industry:** [[industries/lending-marketplaces|Lending Marketplaces]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The consultant is on the phone recommending lenders to a borrower without knowing which of them would approve.
**Tags:** #gradient-boosting #worker-facing #evaluation-metrics #confidence-intervals #logistic-regression #automation #compliance #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to tell a licensed consultant which lenders will actually approve the person they are calling — and whoever supplies that turns a dialling job back into an advisory one.

## The Problem
The consultant has a name, a phone number, a stated loan purpose and amount, and a self-reported credit band. They have a list of lender products. What they do not have is any estimate of which lenders would approve this borrower, what rate they would offer, or which of the four they are about to suggest is a waste of the borrower's time and credit file. So they recommend by heuristic and habit, the borrower applies to several, and most decline.

## Why Nobody Has Built This
Approval prediction does not exist upstream, so there is nothing to deliver to the consultant — the sales floor inherits the same missing feedback loop as the ranking system. Call centre tooling was bought as a dialler and CRM rather than built as a decision surface. Consultants are measured on conversion, so the guidance they get is script rather than analysis. And nobody records which recommendations led to approvals.

## What to Build
Put the match in front of the consultant. Deliver a ranked approval-likelihood view per borrower at call time, which is the core and is the single most useful thing the role could be given. Show expected terms alongside likelihood, since the borrower's question is what it will cost and the consultant currently answers from a rate table. Prioritise the queue by expected value rather than by arrival time, because working a good lead late is the most common avoidable loss. Capture the outcome of every recommendation, as the sales floor is the one place where decisions and results can both be observed and it is producing no data. Learn which framings work for which borrower profiles, since consultants develop this knowledge individually and it never leaves them. Tell the consultant when no lender is likely to approve, because the honest conversation is better for everyone and the role currently has no way to have it. Flag the borrower who has already shopped recently, which changes the conversation and is visible in the marketplace's own data. Handle compliance obligations in the surface rather than in the script, so disclosures are delivered consistently. Measure lead quality separately from consultant performance, which is the fairness problem at the heart of the role. And feed call outcomes back into routing and acquisition, since this is the richest outcome data the marketplace can generate itself.

## Target Customer
Sales and call centre leadership, licensed consultants, borrowers receiving guesses, and sales enablement vendors with no approval intelligence.

## Impact If Built
The sales floor inherits the same missing feedback loop as the ranking system, so there is nothing to hand the consultant. Approval likelihood with expected terms at call time turns a script into advice and produces the outcome data nobody else is collecting.
