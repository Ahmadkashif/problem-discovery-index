# A Live Map of What Each Court Will Show

**Niche:** [[niches/investigation-and-screening-firms/county-court-record-retrieval/profile|County Court Record Retrieval]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a county search can be matched to a candidate depends on which identifiers that court displays this month, and that knowledge lives in individual researchers' heads.
**Tags:** #tacit-knowledge-ml #change-point-detection #feature-engineering #evaluation-metrics #data-integration #compliance
**Contested on:** Every serious competitor in this niche is fighting to return a county criminal search with the full disposition and the identifiers needed to match it inside the screener's turnaround window, from courts that restrict or refuse online access, and whoever covers the most slow and restricted counties without a re-pull takes the account.

## The Problem
Each court decides what its index and terminals show: full date of birth, year only, nothing; address; case number formats; whether dispositions are entered within days or months. These rules change after court rulings, new privacy policies or system upgrades, usually without notice. A retriever finds out when its runners start returning results that cannot be matched, and a screener finds out when its possible-match queue for that county grows.

## Why Nobody Has Built This
Every retriever and screener tracks this privately, and the knowledge is a competitive asset. Courts publish access policies inconsistently, and the effective rule — what the clerk will actually let a runner see — is only learned at the counter.

## What to Build
A per-court access profile maintained from every search the retriever runs: which identifiers were visible, disposition lag measured from case filing dates, turnaround, rejections and re-pulls, with change detection that flags a court whose pattern shifts. Runners confirm changes with one tap. Screeners subscribe to the profiles for their order routing and to tell candidates in advance when extra identifiers will be needed.

## Target Customer
Owners of court-runner networks and researcher firms, and fulfilment heads at screening firms buying from them.

## Impact If Built
Re-pulls and unmatchable results fall, access changes are known within days rather than weeks, and the senior researcher's knowledge of each court becomes a product the firm keeps.
