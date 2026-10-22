# Purchase Suspense Predicted Before Shipping

**Niche:** [[niches/mortgage-lenders/post-closing-delivery-trailing-docs/profile|Post-Closing, Delivery & Trailing Documents]]
**Industry:** [[industries/mortgage-lenders|Mortgage Lenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Lenders learn that an investor will suspend a loan when the suspense notice arrives, days after shipping, though the same defects recur by closer, title agent and loan type.
**Tags:** #gradient-boosting #large-language-models #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to move a closed loan from the closing table to investor purchase and final documents with no suspense items in the fewest warehouse days, and whoever shortens dwell and clears trailing documents fastest takes the account.

## The Problem
An investor's purchase review finds a mismatch between the note and the closing disclosure, a missing signature or initial, a power of attorney not approved in advance, or an unacceptable title commitment exception. The loan goes into suspense, the post-closer chases a fix, and the loan sits on warehouse for days or weeks longer.

## Why Nobody Has Built This
Post-closing checklists exist, but they apply the same checks to every loan. Investors' suspense reasons arrive in free text through separate portals, so lenders have never built a labelled history of which loans get suspended and why.

## What to Build
A pre-shipping model trained on the lender's suspense history (normalised from every investor's portal) that scores each closed loan by suspense risk and likely reason, using closer, title and settlement agent, state, product, investor and document-check results; plus document AI that checks the high-risk loans' packages against the specific investor's purchase conditions before they ship.

## Target Customer
Post-closing and secondary operations leaders at lenders selling 1,000+ loans a month to several investors.

## Impact If Built
Each suspension avoided removes days of dwell; on a busy lender's book that is millions of dollars of haircut cash and line capacity freed (estimate), and fewer aged loans sold at a discount.
