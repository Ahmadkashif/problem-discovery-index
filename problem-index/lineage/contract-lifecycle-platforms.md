# Lineage: Contract Lifecycle Platforms

**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** CUAD — the Contract Understanding Atticus Dataset: 510 commercial contracts from SEC EDGAR, hand-labelled by lawyers against 41 clause categories, with 13,000+ annotations
**Builder:** The Atticus Project
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A company's promises live in prose. Notice periods, most-favoured-nation terms, change-of-control triggers, liability caps: each is a sentence somewhere in an executed agreement, and the only instrument that could find it was a lawyer reading.

That instrument is expensive. The CUAD paper opens with the economics: many law firms spend roughly half their time reviewing contracts, and large-firm billing rates run about $500–$900 an hour, so a single transaction can cost hundreds of thousands of dollars in review alone. Most of each contract is irrelevant. CUAD's own count is that labelled clauses make up about 10% of a contract, and any one category about 0.25%. **The job was finding needles, and it was billed by the hour.**

Machine help had an unusual blocker. Contracts are confidential, so there was no large public corpus of them, and labelling one needs legal training. Without labels there is nothing to train on or score against.

## What Got Built

A labelled dataset and the taxonomy inside it.

CUAD fixes **41 label categories** — the clauses "lawyers pay particular attention to" — grouped into general information (parties, dates, governing law, renewal terms), restrictive covenants (non-compete, exclusivity, no-solicit, most favoured nation), and revenue risks (uncapped liability, minimum commitment, liquidated damages, audit rights). Each is a span-extraction task: for every contract and category, highlight the exact text a reviewing lawyer should read.

The contracts came from EDGAR, because public companies must file material agreements with the SEC and those filings are free. That is the only reason a corpus of real, heavily negotiated contracts could be published at all. The set spans 25 contract types and is released under CC BY 4.0.

## Who Built It, And Why Them

The Atticus Project, a nonprofit working on AI in law, supplied the legal side; Dan Hendrycks and Collin Burns of UC Berkeley supplied the machine-learning benchmark. The paper was posted in March 2021 and accepted to the NeurIPS 2021 Datasets and Benchmarks track.

**Why a nonprofit and not a vendor.** Every CLM company building extraction had the same need and a reason not to meet it in public: a vendor's labelled corpus is its moat. The labour is the barrier. Law-student annotators took 70–100 hours of contract-review training before labelling, each page was reviewed at least four times, and the authors put a conservative value of over $2 million on the result. A party with no product to protect could pay that and give it away; the benchmark exists because the people building it were not selling the extractor.

The Berkeley side supplied the reason to care: CUAD was pitched as a test of whether deep learning reaches domains where expert labels are scarce. The Atticus Project's founding date and founders were not established.

## What It Cost

**The taxonomy is a choice, and it travels.** Forty-one categories drawn from what M&A reviewers flag became the default schema for "what is in a contract". Obligations outside the list — data-protection commitments, service levels, bespoke operational promises — are exactly what an enterprise back catalogue is full of and exactly what the benchmark does not score.

The corpus is also skewed: EDGAR contracts are material agreements of public companies, more negotiated than an ordinary company's NDAs and order forms. And the task is extraction, not interpretation. Finding the cap on liability is not knowing whether it is acceptable.

## What You Still Touch

When a CLM product ingests a folder of legacy PDFs and returns a grid of renewal dates, governing law and assignment clauses, the columns look much like CUAD's categories because the field benchmarked itself on them. The part that never made the list is still read by hand.

- [[problems/contract-lifecycle-platforms/high-impact|🔴 The Unstructured Back Catalogue]] — the backlog CUAD-style extraction was built to open
- [[problems/contract-lifecycle-platforms/low-impact-1|🟡 Clause Library and Playbook Curation]] — a taxonomy, but the company's own, and it drifts
- [[niches/contract-lifecycle-platforms/back-catalogue-obligations/profile|Back Catalogue Obligations]]
- [[niches/contract-lifecycle-platforms/third-party-paper-review/profile|Third-Party Paper Review]]

**Sources:** Hendrycks, Burns, Chen & Ball, *CUAD: An Expert-Annotated NLP Dataset for Legal Contract Review*, arXiv:2103.06268 (submitted 10 March 2021; revised 8 November 2021) — source of the 50%-of-time figure (itself citing CEB 2017), the $500–$900 rates, the 10% and 0.25% shares, the three label groups, EDGAR sourcing, 25 contract types, 70–100 hours of annotator training and the $2 million valuation; atticusprojectai.org/cuad (510 contracts, 13,000+ labels, 41 categories, CC BY 4.0, NeurIPS 2021 Datasets and Benchmarks); category list read from `category_descriptions.csv` in github.com/TheAtticusProject/cuad. ⚠️ **Not established:** the Atticus Project's founding date and founders — neither its CUAD page nor the GitHub repository states them. WebSearch was unavailable this session (session cap reached); research ran on WebFetch against known URLs. An earlier candidate artefact for this note — the legal redline comparison program (CompareRite, DeltaView) — was dropped because no source reachable this session established who built either or when; Wikipedia's *Workshare* and *Litera* entries do not cover them.
