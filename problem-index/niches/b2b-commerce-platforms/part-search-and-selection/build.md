# A Ranked List for a Question With One Answer

**Niche:** [[niches/b2b-commerce-platforms/part-search-and-selection/profile|Part Search & Selection]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Industrial buyers need to be told which single part is correct, and the storefront returns a ranked list of plausible matches, which is the wrong shape of answer to a question where the wrong part stops a machine.
**Tags:** #k-nearest-neighbors #word-embeddings #evaluation-metrics #graph-theory #confidence-intervals #object-detection #large-language-models #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to identify the one correct item in three hundred thousand from whatever the buyer happens to have — and whoever does that takes the account, because the alternative is calling a specialist and the wrong part stops a machine.

## The Problem
A technician sends a maintenance buyer a part number from a competitor's label and a photograph. The buyer searches the number and gets nothing. They search the description and get four hundred results ranked by relevance, none of which they can distinguish because the specification attributes that would separate them are blank. They cannot risk ordering the wrong one, because fitting it means a return, a delay and a machine standing idle. They call the distributor's technical desk, where a specialist identifies it in two minutes from knowledge and a cross-reference book. The storefront's answer to a single-answer question was a ranked list it could not even populate.

## Why Nobody Has Built This
Search came from consumer commerce where a ranked list is the correct output and precision matters less than recall. Cross-reference and specification data is the hardest part of a technical catalogue and is chronically incomplete, which makes any specification-driven experience unreliable. The specialist resolves it, so the failure converts into a call. And nobody has treated identification as a different problem from search.

## What to Build
Identify rather than rank. Build cross-reference lookup as a first-class capability across competitor, manufacturer and legacy numbers, which is the single most common entry point in technical distribution and is patchy everywhere — this is where most of the calls come from and where the data can be assembled. Support specification-driven narrowing: the buyer states the dimensions, materials, ratings and thread they know, and the system eliminates rather than ranks, asking for the next discriminating attribute — which is how a specialist actually works and is a completely different interaction from a search box. Return an identification with a confidence and the reasoning, so the buyer can verify it, since an unexplained recommendation is not actionable when the wrong part is expensive. Support photograph-based identification, which is how a technician communicates and is now feasible. Model compatibility and fitment explicitly — what this part fits, what supersedes it, what it replaces — since those relationships are how technical catalogues are actually navigated. Say when the catalogue cannot answer and route to a specialist with the context gathered, which is a better outcome than a bad ranked list and preserves the relationship. Feed the specialists' identifications back as data, since their resolutions are the labelled examples this capability needs. And measure identification accuracy rather than search relevance, because the buyer's question has a right answer.

## Target Customer
Technical distributors and manufacturers, maintenance and engineering buyers, and the technical desks answering the calls.

## Impact If Built
A ranked list is the wrong shape of answer to a question with one right answer and an expensive wrong one. Specification-driven elimination is how a specialist works and is a different interaction from a search box, and the specialists' own resolutions are the labelled data the capability needs.
