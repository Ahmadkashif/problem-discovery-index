# Closing Disclosure Balancing Under TRID

**Industry:** [[title-and-settlement-offices|Title & Settlement Offices]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Lenders and settlement agents reconcile the same closing numbers in two systems by email against a three-business-day clock, and the generic comparison tools available to them know nothing about TRID fee sections, tolerance buckets or how a title premium must be disclosed.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #compliance #workflow-orchestration #automation #data-integration

## The Problem
On a financed closing two parties produce the same numbers. The lender owns the Closing Disclosure and must ensure the borrower receives it at least three business days before consummation; the settlement agent produces the ALTA settlement statement, the seller's figures, prorations, payoffs, commissions, recording fees, transfer taxes and title charges. The escrow officer sends fees to the lender, the lender's closer drafts the CD, the officer marks up the PDF, and the two go back and forth until every line agrees. A late payoff update, a changed commission split or an HOA transfer fee discovered in the estoppel reopens the loop. If a change makes the APR inaccurate, alters the loan product or adds a prepayment penalty, the three-day clock restarts and the closing date moves.

## What Already Exists
Lender-side closing platforms and loan origination systems generate the CD and offer settlement-agent portals for fee entry; production systems (SoftPro, Qualia, RamQuest) generate settlement statements and can export fees; and general PDF comparison and spreadsheet reconciliation tools can diff two documents line by line. Each works inside its own boundary. The lender portal assumes the agent will rekey fees into its form, the production system assumes the agent's numbers are the truth, and a PDF diff flags differences without knowing which ones matter.

## The Customisation Gap
Balancing needs TRID-aware logic layered on top of the generic comparison. The tool must map each settlement-statement line to its CD section (origination charges, services the borrower did and did not shop for, taxes and government fees, prepaids, escrows, other) and tolerance bucket, because a fee that moves sections can turn a compliant file into a tolerance cure. It must apply the disclosure rule for title premiums, under which the lender's policy is shown at the full rate and the owner's policy as the remainder of the simultaneous-issue premium, so the CD's title figures deliberately differ from the agent's invoice. And it must handle state transfer-tax splits, seller credits, per-diem payoff interest to the funding date, and which party's figure governs each line. It also needs to recognise that only some differences trigger redisclosure, and to tell the officer which before the lender's closer does.

## Impact If Solved
A balancing layer that reads both documents and returns a list of material differences, each with the governing figure and the TRID consequence, turns three or four email rounds into one, protects the closing date from avoidable redisclosure, and frees escrow officers from the most repetitive hour of every financed file.
