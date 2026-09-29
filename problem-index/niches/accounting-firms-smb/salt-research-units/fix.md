# Determination Reasoning Is Never Recorded With the Determination
**Niche:** [[niches/accounting-firms-smb/salt-research-units/profile|State & Local Tax Research Units]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher spends three hours establishing that a service is not taxable in Ohio, records the word "exempt" in a spreadsheet cell, and the three hours of reasoning are gone.
**Tags:** #bert #transformers #large-language-models #workflow-orchestration #data-integration #worker-facing #tacit-knowledge-ml #compliance

## The Problem
The output of SALT research is compressed to almost nothing at the moment of recording. A researcher reads statute, regulation, and a letter ruling, weighs an ambiguity, reaches a position, and writes a single word into a cell. Everything that made the determination defensible — the authorities, the interpretation, the client facts it depended on, the confidence the researcher actually had — is discarded. When the position is questioned on audit two years later, the firm must reconstruct the research from scratch, often with a different person, sometimes reaching a different answer. When a similar question arrives for another client, no one knows the firm has already researched it, so it is researched again. Practices repeat the same determinations across clients continuously without any awareness that they are doing so.

## Why It's Still Broken
The recording medium is the problem, and it persists because it is convenient. A spreadsheet cell holds one value; capturing reasoning means writing it somewhere else and maintaining the link by hand, which nobody sustains under deadline. Research platforms hold the authorities but have no notion of the firm's client-specific conclusions. Document management holds memos but is not connected to the matrix that drives compliance. The friction is entirely at the point of capture: the researcher has the reasoning in mind at exactly the moment the workflow gives them no place to put it, and thirty seconds later the opportunity is gone.

## What a Fix Looks Like
Move capture into the research act itself. The researcher works in an environment where authorities consulted are recorded as they are opened, and the determination is entered as a short structured rationale — position, authorities relied on, client facts assumed, confidence — rather than as a bare value. The cost has to be seconds, not minutes, or it will not survive contact with deadline pressure; drafting the rationale from the authorities the researcher actually consulted is what makes that possible, leaving them to correct rather than compose. Once determinations carry their reasoning, two capabilities follow immediately. The firm can search its own prior determinations before starting new research, which eliminates the silent duplication across clients. And audit defense begins from a complete contemporaneous record instead of a reconstruction.

## Who Feels the Pain
Researchers who redo work the firm has already done and cannot prove their own prior reasoning; practice leaders carrying professional liability on positions whose basis is undocumented; and the client, who pays twice for the same research.

## Impact If Fixed
Eliminates duplicated research across a client base — the largest recoverable inefficiency in a SALT practice. Converts audit defense from reconstruction into retrieval. Builds, as a byproduct of normal work, a proprietary determination corpus that is the practice's most defensible asset and the foundation for everything else automatable in the niche.
