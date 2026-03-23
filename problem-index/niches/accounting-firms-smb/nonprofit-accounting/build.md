# Fund-to-990 Mapping and Workpaper Generation

**Niche:** [[niches/accounting-firms-smb/nonprofit-accounting/profile|Nonprofit & Fund Accounting Specialists]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool automatically maps a nonprofit's fund-level general ledger to Form 990 line items and generates the supporting workpapers that auditors and preparers need.
**Tags:** #bert #text-classification #nlp #automation #compliance

## The Problem
Form 990 is a 12-part, 100+ line return with 16 possible schedules, and its line items do not map directly to a nonprofit's chart of accounts. Revenue from a gala event needs to be split between contribution revenue (990 Part VIII Line 1) and special event revenue (Schedule G), with direct expenses netted differently than in the general ledger. Functional expense allocation (program vs. management vs. fundraising on Part IX) requires a methodology that the nonprofit may not have formalized. CPA preparers spend 4-8 hours per nonprofit manually mapping GL accounts to 990 lines, building functional expense allocations, and creating supporting workpapers — work that is repeated from scratch each year because the mapping lives in the preparer's working memory.

## Why Nobody Has Built This
The 990 mapping logic is deeply specific to the intersection of the client's chart of accounts, their fund structure, and the current-year IRS form layout. Tax software vendors provide input screens for 990 data but not the mapping engine that transforms raw GL data into those inputs. Building this requires encoding the IRS 990 instructions as a rule engine, layering on an ML-based account classifier to map free-text account names to 990 categories, and handling the edge cases (related organizations, compensation reporting thresholds, public support tests) that make each nonprofit's 990 unique.

## What to Build
A 990 preparation assistant that imports a nonprofit's trial balance from QBO, Xero, or Sage Intacct, auto-maps accounts to 990 line items using prior-year mappings and a trained text classifier, flags accounts that need manual allocation decisions (e.g., shared costs requiring functional expense methodology), generates supporting workpapers with the mapping documentation, and exports the data in the import format for UltraTax, Lacerte, or Drake. The preparer reviews and adjusts rather than building from scratch.

## Target Customer
CPA firms preparing 20-100 nonprofit 990s annually, where each return currently requires 4-8 hours of manual mapping and workpaper creation.

## Impact If Built
Reduces 990 preparation time by 50-60%, saving 2-5 hours per return. A firm preparing 50 nonprofit returns recovers 100-250 hours per year, equivalent to $15K-$40K in freed capacity at staff billing rates.
