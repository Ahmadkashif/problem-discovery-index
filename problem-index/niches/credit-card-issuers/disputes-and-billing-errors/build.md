# A First-Party Misuse Read That Never Auto-Denies

**Niche:** [[niches/credit-card-issuers/disputes-and-billing-errors/profile|Disputes & Billing-Error Resolution]]
**Industry:** [[industries/credit-card-issuers|Credit Card Issuers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Dispute analysts can often tell when a cardholder disputing a charge as fraud actually made it, and the issuer has no way to capture that read without turning it into a denial engine.
**Tags:** #tacit-knowledge-ml #gradient-boosting #transformers #evaluation-metrics #feature-engineering #compliance
**Contested on:** Every serious competitor in this niche is fighting to decide each disputed charge correctly — genuine fraud, merchant error or first-party misuse — inside Reg Z's two-billing-cycle limit and the network's chargeback window, and whoever cuts write-offs without wrongly denying genuine claims takes the account.

## The Problem
A cardholder reports an online purchase as unauthorised. The analyst sees the same device used for a dozen past purchases at that merchant, delivery to the cardholder's own address, and a story that changed between the app and the call. In a Quavo-sponsored 2026 survey nearly four in ten consumers admitted a dispute they later realised may not have been valid. Experienced analysts recognise the pattern; new ones reissue the card and file a fraud chargeback that the merchant wins with compelling evidence.

## Why Nobody Has Built This
Denying a genuine claim is a Reg Z violation and a complaint, so issuers are rightly wary of any model that says "this customer is lying". The analyst's read is never recorded as a label.

## What to Build
A review aid that assembles the cardholder's history with the merchant, device and delivery evidence and the network's compelling-evidence data, scores the likelihood that a fraud claim is first-party, and routes high-scoring claims to a gentle verification step and a reclassification to the correct dispute type — never to an automatic denial. Analysts' conclusions are captured as labels and graded against representment outcomes.

## Target Customer
Heads of disputes at large and mid-size issuers.

## Impact If Built
Fewer lost chargebacks and fraud reissues on purchases the cardholder made, with genuine claims untouched.
