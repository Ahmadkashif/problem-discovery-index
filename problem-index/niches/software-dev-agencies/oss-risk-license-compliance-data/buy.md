# Advisories That Do Not Say Which Versions They Break

**Niche:** [[niches/software-dev-agencies/oss-risk-license-compliance-data/profile|Open Source Risk & License Compliance Data]]
**Industry:** [[industries/software-dev-agencies|Software Development Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The public vulnerability record is prose about affected versions, the product needs a precise range per ecosystem, and analysts read advisories to bridge the gap.
**Tags:** #transformers #large-language-models #transfer-learning #graph-neural-networks #data-integration

## The Problem
The moat is curation. A public advisory typically says something like "versions before 2.4.1 are affected", in prose, sometimes wrongly, often without saying which package in which ecosystem, frequently without distinguishing the fix commit from the release that contained it, and regularly amended after publication.

The product needs something far more precise: for each affected package in each ecosystem, an exact version range, resolved against that ecosystem's versioning rules, with the introducing and fixing commits identified, cross-referenced to every fork, rename, backport and vendored copy. Getting this wrong in either direction is expensive — too broad and customers drown in false positives, too narrow and something real is missed.

This is done by security researchers reading advisories, commits, issue threads, patches and release notes. It is skilled, slow work, and its volume grows with disclosure volume, which grows every year. Each ecosystem has its own versioning semantics, its own naming conventions, and its own habits about backporting.

The same problem exists on the licence side. A package's licence is asserted in metadata that is frequently wrong, contradicted by headers in the files themselves, or absent, and resolving it means reading.

## What Already Exists
Language models handle technical text well, including commit messages and patches. Public vulnerability databases and ecosystem-specific advisory feeds exist and are improving. Package registries expose dependency metadata. Open tooling for version range parsing exists per ecosystem.

None of it produces the curated artefact. Public databases are the input to this work, not a substitute for it — their imprecision about affected versions is exactly the gap the vendor's customers pay to have closed. Generic information extraction returns entities and relations; the requirement is a validated version range with a confidence and a citable basis.

## The Customization Gap
**Version semantics are per-ecosystem and non-negotiable.** A range that is correct in one packaging ecosystem's ordering is wrong in another's. Any extraction must emit ranges in the target ecosystem's own semantics, and must handle pre-releases, epochs and distribution-specific backports.

**Commits are the ground truth, not the advisory.** The reliable signal is which commit introduced the flaw and which fixed it, then mapping those to releases. That is a code and history reasoning task over repositories, and it is what an experienced analyst actually does.

**Identity is a graph.** The same code appears under different package names across ecosystems, in forks, in vendored copies inside other projects, and in distribution rebuilds. Resolving a vulnerability to everything actually carrying the code is a graph problem, and unvendored copies are a known systematic blind spot.

**Precision is asymmetric and must be tunable per customer.** A false positive costs a developer an hour; a false negative can cost a breach. The extraction has to carry calibrated confidence so the product can set that trade-off, rather than emitting a range and hoping.

**Advisories mutate.** Published records are amended, disputed, withdrawn and re-scored. Curation must be versioned and re-runnable, so a customer can be told what changed and why their finding disappeared.

**The training data is the vendor's own history.** Years of analyst-curated advisory-to-range decisions, with corrections, is exactly the supervision this needs, and no one else has it.

## Target Customer
VP of Security Research or Head of Data at a software composition analysis vendor, running a curation team whose size scales with global disclosure volume.

## Impact If Solved
Curation headcount is the binding constraint on ecosystem coverage and on how fast a new vulnerability reaches customers, and disclosure volume rises every year regardless. Converting curation from reading advisories into reviewing proposed ranges with their evidence is what lets coverage grow without the team growing with it — and it directly reduces both the false positives customers complain about and the misses they do not know about.
