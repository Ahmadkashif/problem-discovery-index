# Lease Obligations Kept in a Spreadsheet

**Industry:** [[oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Contract-management software already tracks renewal dates and obligations for every other kind of contract; an oil and gas lease's obligations depend on production, unit designations, shut-in status and depth clauses that no generic tool understands, so lease analysts track them in spreadsheets.
**Tags:** #large-language-models #transformers #survival-analysis #feature-engineering #compliance #workflow-orchestration #automation

## The Problem
An operator's acreage is a patchwork of leases signed over decades on different forms. Each has a primary term, after which it survives only if there is production or operations "in paying quantities" on the lease or on lands pooled with it. Many add clauses that bite: a continuous-development clause that requires the next well within 120 or 180 days of the last (typical terms, estimate), a Pugh clause that releases acreage outside a unit, depth severance that releases rights below the deepest producing formation, shut-in royalty payments due on a set date when a gas well is shut in, and delay rentals on older forms. Federal and state leases add their own rules.

The lease analyst tracks this in a land system and a spreadsheet of expirations. Whether a lease is "held by production" depends on wells, units, production months and shut-in periods that live in other systems. A missed shut-in payment or a lapsed continuous-development deadline can terminate a lease the company paid to acquire, and the first notice may be a top lease taken by a competitor or a demand for a release.

## What Already Exists
Land modules from Quorum, W Energy, PakEnergy and Pandell store leases, tracts and obligation dates, and Enverus offers lease and ownership data. Generic contract-lifecycle tools (Ironclad, Icertis, DocuSign CLM) extract clauses and remind people of renewal dates. GIS tools map acreage and units.

## The Customisation Gap
Lease survival is not a date; it is a rule applied to production and operations data. The industry-specific layer must extract the clauses from scanned leases on dozens of forms and their amendments; link each tract to the wells and units that hold it; read monthly production and shut-in status from the production system; compute held-by-production status and the next deadline under each clause; and warn the land and drilling teams when the drilling schedule no longer meets an obligation. Generic CLM extracts a renewal date. It cannot tell an analyst that a Pugh clause will release 640 acres if the unit's only well stays shut in for 91 days.

## Impact If Solved
An operator with ~5,000 active leases (estimate) could put every obligation on one dashboard driven by production data rather than a spreadsheet, and avoid losing even one or two leases a year. At Permian acreage values of thousands of dollars per net acre (estimate), one lost 160-acre lease can cost more than the software.
