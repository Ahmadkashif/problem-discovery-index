# Living Taxability Matrix with Jurisdiction Change Propagation
**Niche:** [[niches/accounting-firms-smb/salt-research-units/profile|State & Local Tax Research Units]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A taxability matrix that is a live object rather than a spreadsheet — every cell carries its authority and reasoning, and when a state amends a rule the system identifies every client determination that just became questionable.
**Tags:** #bert #transformers #large-language-models #transfer-learning #evaluation-metrics #data-integration #compliance #tacit-knowledge-ml #revenue-impact

## The Problem
A SALT practice maintains taxability matrices for every client with multistate activity — a grid of product or service categories against jurisdictions, each cell holding a taxability determination. The matrices are spreadsheets. The reasoning behind each cell lives in the researcher's working notes or nowhere at all. When a state changes its treatment of a category, identifying which client matrices contain an affected cell requires opening them one at a time, and firms with hundreds of clients simply do not do it comprehensively. Exposure therefore accumulates silently: a determination made correctly in one year quietly becomes wrong, and the error surfaces on audit, where the firm's own work product is the thing being examined.

## Why Nobody Has Built This
Compliance software solves the downstream problem — once you know a transaction is taxable, rate engines calculate correctly and filing software files correctly. The upstream determination was left to human researchers because it requires reading statutes, regulations, letter rulings, and administrative guidance across fifty regimes and applying them to a specific client's facts. Vendors sell rate data because rates are objective, uniform in structure, and licensable; taxability determinations are interpretive, client-specific, and carry professional liability, which no rate vendor wants. Firms did not build it themselves because each one's matrix is a spreadsheet that works well enough until the moment it does not.

## What to Build
A determination store where each cell is a structured object: client, category, jurisdiction, position, the authorities relied on, the reasoning, the researcher, the date, and a confidence level. A monitoring layer tracks state legislative and administrative sources — statutes, regulations, department bulletins, letter rulings — and for each detected change traverses the store to identify every determination resting on the amended authority, across every client at once. Affected cells are flagged with the specific change attached, ranked by client exposure, and routed to the responsible researcher. Because determinations are structured rather than trapped in spreadsheet layout, the store also answers questions the practice currently cannot ask: where has the firm taken inconsistent positions on the same category across clients, which jurisdictions carry the most unreviewed determinations, and which positions rest on authority that has since been superseded.

## Target Customer
SALT practice leaders and national indirect tax directors running research teams of 15-100, and the specialist SALT firms whose entire product is determination work.

## Impact If Built
Converts the practice's largest liability into a managed asset. Rule changes propagate to affected clients in hours rather than being caught at audit, which is the difference between advisory revenue and a professional liability claim. Proactive notification is itself sellable — the client learns of an exposure from their advisor rather than from a state notice, which is the single most retention-positive event in the relationship.
