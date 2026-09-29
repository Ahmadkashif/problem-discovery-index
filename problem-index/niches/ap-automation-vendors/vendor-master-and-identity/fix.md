# Four Records, One Supplier

**Niche:** [[niches/ap-automation-vendors/vendor-master-and-identity/profile|Vendor Master & Identity]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The same supplier exists four times in the master file and nobody knows which one to use.
**Tags:** #quick-win #data-integration #graph-theory #evaluation-metrics #automation #descriptive-statistics #worker-facing #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to know who a vendor actually is and whether their payment details are real — and the contest splits cleanly enough that it is not terminal.

## The Problem
The supplier was onboarded in 2016 under their trading name, again in 2019 under their legal entity after an acquisition, again in 2021 by a different department who did not find the existing records, and once more with a typo. Purchase orders point at one, invoices arrive matching another, payments go to a third, and spend reporting splits across all four. Everybody in AP knows about it and nobody has authority or time to merge them.

## Why It's Still Broken
Duplicate checking runs on exact matches at creation, so anything with a different spelling passes — and the check was designed to prevent obvious accidents rather than to resolve identity. Merging records has consequences in the ERP that nobody wants to own. The duplicates accumulate slowly. And no report counts them.

## What a Fix Looks Like
Find them and make merging safe. Run fuzzy matching across the master file and report likely duplicate groups, which is the fix and is a well-understood computation nobody runs. Use tax identifiers, bank details, addresses and invoice history as matching evidence rather than names alone, since names are the least reliable field. Rank by spend so the consequential duplicates are addressed first, as a long tail of dormant records does not matter. Show what would be affected by a merge, because the fear of breaking history is what prevents action. Support a link without a merge, which captures most of the reporting and matching benefit at a fraction of the risk. Prevent new duplicates at creation with fuzzy checking, since the file will otherwise refill. Report spend consolidated across the group, which frequently reveals that a supplier is far more significant than anyone realised and changes procurement conversations. Flag records with conflicting bank details in the same group, as those are both an operational and a fraud concern. Use cross-customer evidence to confirm which entity is which, because other buyers have the same supplier resolved. And report duplicate rate as a data quality metric, since customers currently have no idea.

## Who Feels the Pain
Clerks guessing which record to use; procurement with fragmented spend visibility; payments going to stale accounts; and finance reporting understating supplier concentration.

## Impact If Fixed
The duplicate check runs on exact matches at creation because it was built to prevent obvious accidents rather than to resolve identity. Fuzzy matching ranked by spend, with link-without-merge as the safe action, addresses the consequential duplicates without touching ERP history.
