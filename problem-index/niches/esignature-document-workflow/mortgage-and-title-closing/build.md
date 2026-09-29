# Predicting the Closing That Falls Back to Paper

**Niche:** [[niches/esignature-document-workflow/mortgage-and-title-closing/profile|Mortgage & Title Closing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A closing scheduled as fully digital collapses to paper two days out, and every factor that caused it — the county, the investor, the lender overlay, the notary's jurisdiction, a missing document — was knowable at application.
**Tags:** #gradient-boosting #logistic-regression #random-forests #survival-analysis #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance
**Contested on:** Every serious competitor in closing technology is fighting to get a loan to fund and an instrument to record without the parties being in a room — and whoever can do that across the widest set of counties, investors and lender overlays takes the volume.

## The Problem
A closing is set up as fully digital. Forty-eight hours out, the title agent discovers the county will not accept an electronically recorded deed of trust in the required format, or the investor who has committed to purchase the loan will not take an electronic note, or the borrower has moved and the notary is not commissioned in the new state. The closing reverts to paper: a room is booked, a courier arranged, the borrower takes a morning off, and funding slips. Every one of those constraints was determinable weeks earlier from the property county, the loan product, the investor commitment and the borrower's location.

## Why Nobody Has Built This
The constraints live in four different organisations and nobody assembles them. Counties publish recording capability inconsistently and change it without announcement. Investor and lender overlays are commercial documents distributed by email, not data. Each participant tracks the fragment it needs, so the title agent knows their counties and the lender knows their investors and neither knows the combination until the file is in flight. The fallback is also normalised — falling back to paper is annoying rather than fatal, which is why a problem everyone complains about has never been anybody's project.

## What to Build
Digital-eligibility determination at application, maintained as a live matrix and scored per file. The deterministic core is the acceptance matrix: county recording capability and format, investor electronic note acceptance, lender overlay permissions, and state remote notarisation authority with effective dates — assembled once, maintained continuously, and queried per loan. On top of it, a risk score for the files where the matrix is silent or stale, learned from historical fallbacks, since the matrix will never be complete and a probability with a reason attached is better than silence. The output is a decision at application rather than a discovery at closing: this file can close fully digitally, this one is hybrid and here are the two documents that need ink, this one cannot and here is why — and for the hybrid and paper cases, what would have to change, which is often something a lender can actually influence such as an investor choice. Then track the fallbacks that happen anyway and feed them back, since each one is a labelled example of a gap in the matrix.

## Target Customer
Lenders, title agents and closing platform vendors; and the investors and warehouse lenders whose own acceptance policies are the constraint and who currently cannot see their effect on closing efficiency.

## Impact If Built
Fallback to paper is the single largest brake on digital closing adoption and its causes are almost entirely knowable in advance. Determining eligibility at application rather than at closing removes the cost and moves the decision to the point where something can still be done about it.
