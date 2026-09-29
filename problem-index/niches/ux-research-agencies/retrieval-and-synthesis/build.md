# An Answer Rather Than a Result List

**Niche:** [[niches/ux-research-agencies/retrieval-and-synthesis/profile|Retrieval & Synthesis]]
**Industry:** [[industries/ux-research-agencies|UX Research Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The question is whether users understand this concept and the search returns transcripts containing the word.
**Tags:** #word-embeddings #transformers #large-language-models #k-nearest-neighbors #evaluation-metrics #data-integration #dimensionality-reduction #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to get a usable answer out of years of transcripts and tagged findings when the question is a design question rather than a keyword — and whoever answers it takes the account.

## The Problem
Somebody asks a specific design question. The repository's search matches words against transcripts and tags applied by different people over several years with no shared vocabulary. It returns either nothing or hundreds of fragments, none of which is an answer. The person asking wanted a synthesis — what have we found about this, how strongly, when — and got a list they have no time to read.

## Why Nobody Has Built This
Repository tooling treats findings as documents to be stored rather than as claims to be synthesised. Tag inconsistency is assumed to require re-tagging the corpus. Synthesis across studies with different methods and samples is genuinely delicate. And nobody has measured how often search fails, so the failure is folklore rather than a metric.

## What to Build
Retrieve on meaning and synthesise with the evidence attached. Build semantic retrieval over transcripts, findings and reports so a design question matches material that does not share its vocabulary, which is the core and is the failure everyone experiences. Synthesise the retrieved material into a claim with its supporting evidence rather than returning fragments, since that is what the question asked for. Weight by study quality, sample size and recency, which is what makes a synthesis trustworthy rather than an average of everything. Surface contradictions between studies explicitly, as those are the most useful result and are currently invisible. Normalise inconsistent tagging automatically rather than requiring a re-tagging project. Ground every claim in retrievable quotes and clips, because a researcher will not accept a summary they cannot verify. State when the corpus does not support an answer rather than producing a weak one. Handle the age and product context of each finding, since a result about a product that has since changed can mislead badly. Support follow-up questions, as the first query is rarely the real one. And make it work on the corpus as it stands, which is the whole point of separating this from curation.

## Target Customer
UX research agencies and in-house teams, research operations, repository vendors, and enterprise search providers.

## Impact If Built
The search matches words against tags applied by different people over years with no shared vocabulary, and returns a list nobody reads. Semantic retrieval with weighted synthesis turns the corpus into an answer.
