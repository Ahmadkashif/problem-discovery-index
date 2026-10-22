# Move Prediction for the Servicing Book

**Niche:** [[niches/mortgage-lenders/portfolio-recapture-retention/profile|Portfolio Recapture & Retention]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Recapture tools find borrowers when rates drop, which every competitor sees the same day; the borrowers who leave in a high-rate market leave because they move.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #data-integration
**Contested on:** Every serious competitor in this niche is fighting to reach a servicing-book borrower with a credible refinance or purchase offer before a competitor's rate alert or credit-trigger lead does, and whoever identifies the borrower's moment first takes the account.

## The Problem
With 30-year rates expected above 7% through 2027 (MBA), most of the servicing book is out of the money for refinancing. Payoffs come from home sales, and the borrower who sells usually takes a purchase loan from whoever their agent recommends. The servicer learns of the move when the payoff request arrives, weeks after the new lender was chosen.

## Why Nobody Has Built This
Recapture tools were built in the 2020–21 refinance wave around rate incentive. Move signals (listings, escrow and insurance changes, school-year timing, equity and family-size proxies) sit in different data sources and need permissible-use review.

## What to Build
A time-to-move model on the servicing book using listing feeds matched to serviced properties, equity, tenure, escrow and payment changes, borrower contact history and local market turnover, delivering a ranked list of borrowers likely to list within 90 days, with a pre-approval offer timed before they choose an agent's lender.

## Target Customer
Heads of consumer direct and retention at independent lenders retaining servicing.

## Impact If Built
Each recaptured purchase loan keeps a borrower who would otherwise pay off the MSR and generates a new gain on sale; at today's rates that is most of the recapture opportunity left.
