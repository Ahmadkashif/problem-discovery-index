# Division Orders and the Owner Who Calls About Their Check

**Industry:** [[oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every operator keeps a decimal interest for every owner in every well, puts payments in suspense when title or addresses are unclear, and answers owners' calls about their check stubs, using revenue software and a help-desk tool that know nothing about title opinions, state payment statutes or escheat.
**Tags:** #large-language-models #bert #k-nearest-neighbors #feature-engineering #compliance #automation #data-integration

## The Problem
When a well goes on production, the operator owes a share of every sale to each royalty, overriding royalty and working-interest owner in the unit. The division order analyst turns the drilling or division order title opinion into a decimal for each owner, sends division orders, and sets up each owner in the revenue system. From then on, every change is manual: an owner dies and the heirs send a probate order, a mineral buyer files a deed, a lease is amended, a tract is re-allocated in a unit. Each change means reading a document, recalculating decimals that must still sum to the unit total, and deciding whether to pay, hold or ask for more paper.

Payments that cannot be made go into suspense: unknown owner, bad address, title requirement unmet, no signed division order where one is required. Suspense balances grow quietly until a state's dormancy period runs out; Texas presumes oil and gas proceeds abandoned after three years (search summary). Meanwhile owners call. A retiree with a 0.0015 decimal sees a smaller check and a line called "post-production deduction" and wants to know why. Owner-relations staff answer by pulling the check detail, the lease and the purchaser statement, often over several days.

## What Already Exists
The accounting systems carry division-order and revenue-distribution modules: Quorum, W Energy, PakEnergy (WolfePak), P2 (BOLO) and Excalibur. Owner portals let owners download check detail and 1099s. Help-desk tools such as Zendesk and Salesforce Service Cloud log calls. Unclaimed-property compliance software and outside services handle state escheat filings. Enverus was recruiting an Owner Relations Agent in Austin, Denver or remote US on 25 October 2026 to answer owner calls on revenue, land, division orders and JIB, at $43,000–$58,000 a year.

## The Customisation Gap
The generic tools store decimals and log calls; they do not do the reading. The industry-specific logic is: extracting ownership changes from probate orders, mineral deeds, affidavits of heirship and lease amendments and turning them into decimal changes that still balance to the unit; tracking which title requirements in the opinion each suspense item is waiting on; applying each state's payment-timing statute and its interest penalties (Texas sets the first payment at 120 days after the month of first sale, recalled); scheduling escheat by state and dormancy period; and explaining a check stub line by line, with gross volume, price, taxes and deductions tied back to the lease's deduction clause. Each operator builds parts of this in spreadsheets and staff memory.

## Impact If Solved
A mid-size operator paying ~20,000 owner interests (estimate) could cut division-order change processing from days to hours and owner-call handling time by roughly half (estimate). It could also clear stale suspense before it escheats, where each dollar released to the right owner is a dollar not sent to the state with an audit trail the operator must later defend.
