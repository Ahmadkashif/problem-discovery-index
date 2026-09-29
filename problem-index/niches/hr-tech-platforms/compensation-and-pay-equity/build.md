# The Equity Check at the Moment of Decision

**Niche:** [[niches/hr-tech-platforms/compensation-and-pay-equity/profile|Compensation & Pay Equity]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Pay disparities are created one decision at a time all year and detected once at year end by an external analysis, which means the check runs twelve months after the only moment it could have changed anything.
**Tags:** #linear-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #causal-inference #descriptive-statistics #compliance #revenue-impact
**Contested on:** Every serious competitor in compensation software is fighting to check a pay decision for equity and market position before it is made rather than after — and whoever moves the check to the point of decision takes the account.

## The Problem
A manager makes an offer to a candidate at the top of the range, because the candidate negotiated and the role is hard to fill. The decision is reasonable in isolation. It also places the new hire above three existing employees in the same role with more tenure and stronger performance, two of whom share a protected characteristic. Nobody notices, because the approval sees a budget, a range and a requisition. Eleven months later the annual pay equity analysis identifies an unexplained disparity in that job family, and the remediation costs more than the correct decision would have and does not undo the eleven months.

## Why Nobody Has Built This
Pay equity analysis has been structured as a privileged external exercise precisely so that its findings are protected, which is a defensible legal strategy with an unfortunate consequence: it puts the analysis outside the systems where decisions are made, by design. Building the check into the decision point means the organisation generates a contemporaneous record of having been told about a disparity before creating it, which counsel will identify as a risk. The counter-argument is straightforward and is the one this note takes: an organisation that is told and corrects is in a materially better position than one that was not told and remediates a year later, and the employees affected are better off by a year.

## What to Build
An equity and market check that runs when a pay decision is entered, before approval. The decision's effect is computed against the current population: where it places this person relative to comparable employees on the factors that legitimately explain pay — level, location, tenure, performance, relevant experience — and whether it creates or widens an unexplained gap, with the statistical caveats appropriate to a single decision rather than a population analysis. Market position is shown against the benchmark. Compression effects on existing employees are surfaced explicitly, since that is the most common and least visible consequence of a competitive offer. The approver sees the implication and can proceed with a recorded rationale, which is the correct outcome — sometimes the offer is right and the remedy is adjusting the incumbents. Findings roll up so that the annual analysis becomes a confirmation rather than a discovery, and the organisation's own record shows a pattern of checking rather than a pattern of remediating.

## Target Customer
Compensation platform vendors, HCM incumbents whose planning modules show budgets and not implications, and total rewards functions in organisations facing pay transparency obligations.

## Impact If Built
Moving the check from annual to per-decision is the difference between preventing a disparity and remediating one, and remediation is both more expensive and worse for the employees who were underpaid in the interim. The compression surfacing is the element with the most immediate value, because a competitive external offer that quietly disadvantages three incumbents is the most common way pay inequity is created and the least likely to be noticed.
