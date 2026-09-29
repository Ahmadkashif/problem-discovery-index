# Duplicate Detection and Question Answering

**Niche:** [[niches/open-source-commercial-vendors/issue-and-contribution-triage/profile|Issue & Contribution Triage]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Semantic duplicate detection and retrieval-based question answering are mature and are deployed in every commercial support organisation, and open-source projects use a search box.
**Tags:** #bert #word-embeddings #large-language-models #k-nearest-neighbors #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to reduce the queue rather than to organise it — and whoever does that takes the maintainer teams, because templates, labels and bots have been standard for a decade and the arithmetic is unchanged.

## The Problem
Recognising that a new report describes the same problem as an existing one, and answering a question from a corpus of documentation and prior answers, are both standard capabilities with mature implementations and are deployed in every commercial support organisation of any size. Open-source projects, which have far larger question volumes and far smaller teams, have a full-text search box and a request in the contribution guide to search before posting.

## What Already Exists
Sentence and passage embedding models; semantic duplicate and near-duplicate detection; retrieval-augmented question answering; issue classification models with published work on this exact corpus; and the support deflection product category. All mature, most free, and much of it demonstrated on open-source issue data in the research literature.

## The Customization Gap
The adaptation is to a volunteer-maintained project with a public, adversarially-read interface. It requires: (1) tone and failure behaviour appropriate to a volunteer community, since an automated response that is wrong or dismissive in public damages the project's relationship with its contributors in a way a commercial support deflection does not — this is the constraint that determines whether it is accepted; (2) high precision on duplicate detection, because wrongly closing a distinct issue as a duplicate is a specific and visible harm and the correct behaviour is to suggest rather than to close; (3) version awareness, since a large share of reports concern a version that has been superseded and the answer is frequently an upgrade, which requires knowing which version the reporter is on and what changed since; (4) operation across the fragmented corpus of issues, discussions, chat and forum content, which is where the answers actually are and is scattered by construction; and (5) maintainer control throughout, since a project's maintainers must be able to see, adjust and switch off anything acting in their name.

## Target Customer
Code hosting platforms, maintainer tooling projects, foundations, and the vendors employing maintainers.

## Impact If Solved
The capabilities are mature and are deployed where the volume is lower and the staffing higher, which is an inversion. Suggesting rather than closing duplicates and getting the tone right are what determine whether a volunteer community accepts any of it.
