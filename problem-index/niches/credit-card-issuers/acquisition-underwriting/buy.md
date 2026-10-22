# Cash-Flow Underwriting Fitted to Revolving Credit

**Niche:** [[niches/credit-card-issuers/acquisition-underwriting/profile|Acquisition & Underwriting Decisioning]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Cash-flow scores were built for instalment loans and small-dollar credit; a credit card is an open-ended line whose risk depends on how the cardholder will use it.
**Tags:** #gradient-boosting #feature-engineering #survival-analysis #evaluation-metrics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to approve, and set the first line for, applicants the bureau file describes poorly — thin files, recent immigrants, near-prime rebuilders — at a loss rate it can predict in advance and explain in an adverse action notice, and whoever does that best takes the account.

## The Problem
Issuers want to approve applicants the bureau cannot score, and bank-transaction data — income regularity, balances, overdrafts, rent — is the most promising source. The scores sold on it predict default on a fixed-payment loan over a set term.

## What Already Exists
Cash-flow attributes and scores from account aggregators and specialist developers, consumer-permissioned data access through Plaid and similar networks, and bureau products that blend cash-flow attributes into traditional scores.

## The Customization Gap
A card needs: (1) a line-assignment output, not only an approve or decline, because loss depends on how much line is granted; (2) prediction of utilisation and revolving behaviour, which drives both revenue and loss; (3) refresh after booking, because cash-flow data can be re-pulled for line management where the cardholder consents; (4) adverse action reasons in terms a consumer recognises ("irregular income deposits") mapped to Reg B; and (5) handling of the applicant who declines to connect a bank account, so the product does not quietly become a second decline path.

## Target Customer
Acquisition risk leaders at issuers targeting thin-file and near-prime segments, including fintech card programmes and their sponsor banks.

## Impact If Solved
Approvals for applicants a bureau score cannot separate, with lines sized to their cash flow rather than set at the minimum.
