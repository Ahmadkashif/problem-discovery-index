# Schema Mapping That Learns Across Migrations

**Niche:** [[niches/healthcare-practice-software/ehr-data-migration-services/profile|EHR Data Migration & Conversion]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A vendor that has migrated fifty practices off the same legacy system starts the fifty-first from a blank spreadsheet, because no product treats a completed mapping as reusable knowledge.
**Tags:** #bert #word-embeddings #large-language-models #k-nearest-neighbors #transfer-learning #evaluation-metrics #confidence-intervals #tacit-knowledge-ml
**Contested on:** Every serious competitor in EHR migration is fighting to map an unfamiliar legacy database to a target schema with clinical fidelity and without a consultant hand-reading tables — and whoever maps fastest with the fewest post-go-live surprises takes the account.

## The Problem
An implementation consultant receives a database backup with 800 tables. She finds the one holding medications by querying candidates and reading values, works out that a status column uses integers whose meaning she infers from the data, discovers that allergies were recorded in a free-text field until 2016 and in a coded field after, and writes the mapping. Four months later, another consultant at the same company receives a backup of the same legacy product from a different practice, and does all of it again. The knowledge exists in the first consultant's head and in a spreadsheet on a shared drive with a name nobody can search.

## Why Nobody Has Built This
Migration is priced as services, so the labour is revenue rather than cost, and the incentive to automate it is weaker than it looks from outside. The work also resists naive automation: column names are uninformative, the same legacy product is configured differently at every practice, and a mapping that is 95% right produces a chart that is subtly wrong, which is worse than one that is obviously wrong. And the training data — completed mappings — is scattered across spreadsheets and consultants' inboxes rather than held in any system, so even a vendor that wanted to learn from its own history would have to assemble the corpus first.

## What to Build
A mapping workbench whose unit of knowledge is a validated source-to-target correspondence, accumulated across every migration the vendor performs. For a new source database it proposes mappings from three signals together: name and structural similarity to previously mapped sources, value-distribution fingerprints of the column contents, and the semantics of the target field. Each proposal carries a confidence and the prior migrations supporting it, so the consultant reviews rather than discovers. Coded-value dictionaries — the integer-to-status lookups, the local code sets — are captured once per legacy product and reused. Anything below threshold is escalated with the evidence gathered rather than left blank. The consultant's corrections feed straight back, which is what makes the fiftieth migration genuinely cheaper than the first.

## Target Customer
Ambulatory EHR vendors running migration at volume, the conversion specialist firms they subcontract, and the private-equity-backed practice groups consolidating onto a single platform across dozens of acquired practices.

## Impact If Built
Cutting mapping time by half to two-thirds on a repeat legacy source is the realistic range once a corpus exists, which compresses the implementation timeline that practices complain about most and removes the largest block of consultant evening work in the function. It also converts an individual's tacit knowledge into an asset the vendor keeps when they leave, which in a role with this turnover is the more durable benefit.
