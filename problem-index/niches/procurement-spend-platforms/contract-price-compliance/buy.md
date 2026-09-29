# Recovery Audit Methodology Run Continuously

**Niche:** [[niches/procurement-spend-platforms/contract-price-compliance/profile|Contract Price Compliance]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recovery audit firms have refined the methodology for finding overpayments in historical spend over decades and are paid a share of what they find, which is proof both that the money is there and that nobody is preventing it.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #evaluation-metrics #confidence-intervals #automation #revenue-impact #compliance
**Contested on:** Every serious competitor in procurement controls is fighting to check the invoiced price against the contracted price at the moment of payment — and whoever closes that gap takes the savings the organisation already negotiated.

## The Problem
A recovery audit firm examines several years of accounts payable data and finds duplicate payments, missed discounts, unclaimed rebates, pricing errors, unapplied credits and tax overpayments. They are paid a contingent share, which is substantial, and the same firm returns two years later and finds a comparable amount. The methodology is well developed, the findings are repeatable, and the organisation treats the exercise as a periodic recovery rather than as a description of controls that are absent.

## What Already Exists
Recovery audit methodology is mature and documented: duplicate detection across varying invoice representations, discount and rebate entitlement checking, price variance analysis, credit application verification and statement reconciliation. Data analytics tooling implements all of it trivially. Continuous controls monitoring is an established internal audit discipline with commercial products. Everything the recovery auditors do can be run continuously against current transactions rather than annually against history.

## The Customization Gap
The adaptation is from a retrospective sweep to a preventive control. It requires: (1) running the tests before payment rather than after, which changes the economics entirely — a prevented overpayment is worth more than a recovered one because recovery costs a contingent fee and a supplier relationship conversation; (2) duplicate detection tuned to the real patterns, which are not identical invoices but the same charge arriving under a different invoice number, through a different entity or split across lines, and which is a matching problem rather than a comparison; (3) entitlement checking against contract terms, which requires the structured terms this niche's build note produces and is the largest category of finding; (4) false positive management, since a preventive control that blocks correct payments is worse than a retrospective one, which argues for flagging and routing rather than blocking and for measuring precision from the outset; and (5) the finding rate tracked over time, because a control that is working should find less each period and a recovery audit engagement that keeps finding the same amount is evidence that nothing was fixed.

## Target Customer
Finance and internal audit functions, accounts payable organisations, procurement platform vendors, and the recovery audit firms themselves, for whom continuous monitoring is a better business than periodic sweeps.

## Impact If Solved
The methodology is proven by the existence of a contingent-fee industry built on it, which is the clearest possible evidence that the money is there and that nobody is checking. Moving the tests before payment converts a shared recovery into a full prevention, and the declining finding rate is the measure of whether the controls are actually working.
