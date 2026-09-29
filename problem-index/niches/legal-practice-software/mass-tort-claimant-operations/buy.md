# Document Extraction Adapted to Proof of Use and Injury

**Niche:** [[niches/legal-practice-software/mass-tort-claimant-operations/profile|Mass Tort — Claimant Operations at Scale]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document extraction from medical records is a commodity capability sold into a dozen industries, and mass tort firms still have contract reviewers reading pharmacy printouts to answer two binary questions, with no measurement of whether the reviewers agree with each other.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #hypothesis-testing #automation #compliance
**Contested on:** Every serious competitor in mass tort software is fighting to move forty thousand claimants through record retrieval, proof of exposure and lien resolution without an operation that collapses under its own headcount — and whoever holds throughput per claimant lowest takes the account.

## The Problem
Two questions decide whether a claimant is real: did they use the product, and do they have the injury. The evidence is a pile of medical records, pharmacy histories and purchase documentation, often hundreds of pages, frequently scanned, sometimes handwritten. A contract reviewer reads them and answers. Thousands of reviewers answer millions of times across an inventory. Nobody measures whether two reviewers looking at the same file reach the same answer, which means the qualification standard the firm is actually applying is unknown to the firm — and is the thing the defendant will attack when it challenges unsupported claims.

## What Already Exists
Layout-aware document parsing, medical record abstraction and long-context extraction are mature, with multiple vendors selling into healthcare, insurance and legal. eDiscovery platforms provide review workflow, sampling and quality control machinery that has been standard in document review for fifteen years — including the statistical apparatus for measuring reviewer agreement, which the eDiscovery world treats as basic and the mass tort world does not use.

## The Customization Gap
The adaptation is narrow and specific to the two determinations. It requires: (1) extraction targeted at product use — drug or device identification across brand, generic and misspelled names, with dates of use and prescriber — and at the specific injury definition the litigation's qualification criteria set, which changes per litigation and must be configurable rather than coded; (2) evidence citation for every extracted fact, to the page and passage, because the output has to survive a challenge; (3) confidence thresholds with human review below them and, critically, sampled human review above them, so automation quality is continuously measured rather than assumed; (4) inter-reviewer agreement measurement as a standing metric on the human side, borrowed directly from eDiscovery practice, so the firm knows what standard it is applying; and (5) a defensible record of the whole process, since qualification methodology is itself discoverable and contested in these litigations.

## Target Customer
Mass tort firms and the litigation support vendors performing record review at inventory scale, and the claims administrators who apply qualification criteria post-settlement.

## Impact If Solved
Automated first-pass extraction with sampled verification typically removes the majority of routine review labour at a measured accuracy the firm can state — which is both a cost reduction and a defensibility improvement. Agreement measurement on the human side usually comes as an unwelcome surprise the first time it is run, and that surprise is precisely the exposure the firm did not know it had.
