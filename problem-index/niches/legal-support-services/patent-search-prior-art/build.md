# A Beaten-Search Register

**Niche:** [[niches/legal-support-services/patent-search-prior-art/profile|Patent Search & Prior-Art Analysis]]
**Industry:** [[industries/legal-support-services|Legal Support Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every search a house delivers is eventually tested — by the examiner's citations, by a competitor's IPR petition, by a court — and no house publishes a systematic record of when its search was beaten by art someone else found.
**Tags:** #tacit-knowledge-ml #transformers #contrastive-learning #evaluation-metrics #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find the closest prior art — including non-patent and foreign-language literature — before the examiner, the PTAB petitioner or the opposing expert does, and whoever's searches are least often beaten by art someone else finds later takes the account.

## The Problem
A patentability search reports the five closest references; eighteen months later the examiner cites a sixth that is closer. An invalidity search finds nothing strong; a co-defendant's IPR petition, filed with a different searcher, relies on a Japanese utility model nobody charted. These are the most informative events a search house can observe about its own quality, and they arrive as public documents that nobody joins back to the search.

## Why Nobody Has Built This
Searches are delivered as Word reports, not data. Some houses measure search process — Evalueserve markets a Search Quality Index with precision and recall targets — but not later outcomes. The downstream documents (office actions, PCT search reports, PTAB petitions and decisions) are public but scattered, and the link from a delivered search to the later application or litigation must be made per client. Houses compete on turnaround and price, so measuring misses has looked like a cost.

## What to Build
A register, run inside each client relationship or with the client's consent because delivered searches are client work product, that ingests each delivered search as structured data (target claims, references, ratings, classes searched) and monitors the public record for the same family or patent: examiner citations, search report categories, petitions and decisions. Each later reference is compared with the delivered set; misses are classified by why (unsearched class, language, non-patent literature, analyst rated it low) and rolled up by analyst, technology and source.

## Target Customer
Heads of search operations at search houses; in-house search groups at large filers.

## Impact If Built
A house can prove its recall to clients with evidence, train analysts on their own misses, and target the sources and classes where it is weakest.
