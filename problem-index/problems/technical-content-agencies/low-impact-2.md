# Information Architecture and Findability

**Industry:** [[technical-content-agencies|Technical Content Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The answer exists and the reader cannot find it, which is the most common documentation failure and the one nobody measures because the page has a pageview either way.
**Tags:** #bert #word-embeddings #contrastive-learning #graph-neural-networks #k-means-clustering #evaluation-metrics #dimensionality-reduction #data-integration

## The Problem
A substantial share of documentation failures are findability rather than content. The page exists, it is accurate, and the reader searched a term the page does not use, or navigated a hierarchy that files the answer somewhere they did not think to look, or found a page that looks right and is about a different version.

The evidence is unambiguous when anyone looks: support tickets whose answer is a link to an existing page, community answers that consist of a documentation URL, and search queries that return the right page ranked below three wrong ones. Each of those is a findability failure and each is recorded.

The vocabulary mismatch is the core mechanism. Documentation is written by people who know the system, using the system's own terms; readers search with the words for the problem they have. Someone whose deployment is failing searches for the error message or the symptom, not for the subsystem name the documentation is organised around.

Version confusion compounds it. A reader arrives from a general search on a page for an old version and follows instructions that no longer apply, which produces an accuracy failure that was actually a navigation failure.

## What Already Exists
Documentation search is typically Algolia DocSearch or a hosted platform equivalent, with faceting and version filtering. Information architecture is designed by content strategists using card sorting and tree testing. Some platforms offer related-content suggestions and breadcrumb navigation. Redirects and canonical tags handle version routing where someone maintains them. Diátaxis and similar frameworks give teams a principled structure for organising documentation by purpose.

## The Customisation Gap
Search is the primary navigation for technical documentation and is tuned as an afterthought. Synonym and vocabulary mapping between reader language and system language is the highest-value intervention available and is derivable from the site's own zero-result and rephrasing queries — which are logged and not analysed. A search that understands that a particular error message corresponds to a particular configuration topic solves a large share of failures with no new content.

The architecture itself should be evaluated against observed navigation rather than designed and left. Where readers actually look for things, which sections they never reach, and which pages are only ever found by search rather than by browsing, are all measurable, and they identify structural problems that a card sort with eight participants cannot.

Cross-corpus fragmentation is the third gap. Answers live across reference documentation, guides, blog posts, community threads and release notes, and readers search one surface. Unified retrieval across everything the organisation has published, with source and currency shown, is closer to what a reader needs than a well-organised documentation site alone.

And version routing needs to be handled at arrival, not by a banner. Detecting that a reader arrived from an external search on a version that does not match their apparent context, and offering the right one, addresses a failure mode that currently produces accuracy complaints.

## Impact If Solved
Findability failures are the most common documentation problem and the cheapest to fix, because the content already exists. Vocabulary mapping derived from the site's own failed queries typically resolves a large fraction immediately; architecture evaluated against observed navigation replaces design intuition with evidence; and unified cross-corpus retrieval matches how readers actually look for answers rather than how organisations file them.
