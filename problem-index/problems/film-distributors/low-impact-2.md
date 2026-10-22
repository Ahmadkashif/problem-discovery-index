# Film Rent Settlement Theatre by Theatre

**Industry:** [[film-distributors|Film Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Accounts-receivable software tracks invoices; a theatrical release generates hundreds of separate settlements, each on its own terms, and the specialty distributor reconciles them against box office reports by hand.
**Tags:** #large-language-models #gradient-boosting #feature-engineering #evaluation-metrics #data-integration #automation #workflow-orchestration #revenue-impact

## The Problem
A specialty film opens in six theatres and expands over eight weeks to ~250 (estimate). Each engagement is a separate licence. Exhibitors license films "on a film-by-film and theatre-by-theatre basis", in AMC's words, usually as a share of box office that slides by week or by gross, sometimes as a fixed settlement rate negotiated after the run, occasionally as a flat amount. Film rent across the industry comes to roughly half of admissions. When the run ends, the distributor's sales and accounting staff agree a settlement with each circuit's film buyer and each independent theatre, check the gross against Comscore's reported figures, issue the invoice, and chase payment. Small independent theatres pay late. Circuits net disputed amounts against other films. Settlement for a single release runs for weeks after the film has left screens.

The people doing it are a booker or two and an accountant. The data arrives as Comscore reports, exhibitor box office statements in PDF and spreadsheet form, and emails confirming terms that were agreed by phone.

## What Already Exists
General ledgers and AR tools (NetSuite, Sage Intacct, QuickBooks with add-ons) handle invoicing and collections. Comscore reports theatre-level grosses. The largest studios have in-house theatrical distribution systems. Exhibitors run booking and film-rent modules inside their own theatre management systems, which see the exhibitor's side only.

## The Customisation Gap
Specialty distribution needs:
- a terms model per engagement that captures the original deal (week-by-week percentages, aggregate terms, floors, house allowances, fixed settlements) and the settlement actually agreed, which often differs;
- automatic reconciliation of exhibitor-reported grosses against box office reports by theatre and day, with discrepancies flagged before settlement rather than after;
- a settlement worksheet generated per engagement, plus a collections queue that ages independent theatres separately from circuits;
- a record of each film buyer's settlement history, so that the distributor knows which circuits routinely settle below terms and by how much.

Language models can read the exhibitor statements and confirmation emails. The rest is domain logic generic AR does not carry.

## Impact If Solved
Settling in days rather than weeks shortens the distributor's cash cycle on its largest early-window receipt. Systematic reconciliation recovers the small per-engagement shortfalls that are never chased by hand, which can come to a percent or two of film rent on a wide specialty run (estimate). A settlement history by buyer gives the sales team evidence in the next negotiation.
