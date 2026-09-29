# Terminology and Translation Memory Leverage

**Industry:** [[localization-services|Localization Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every account has a translation memory and a glossary, both of which degrade quietly until linguists stop trusting them and work around them.
**Tags:** #bert #word-embeddings #contrastive-learning #transformers #k-nearest-neighbors #evaluation-metrics #data-integration #feature-engineering

## The Problem
Translation memory stores previously approved translations and offers them as matches for new segments, and terminology databases hold the approved rendering of key terms. Both are core infrastructure and both decay.

Memories accumulate inconsistency. The same source segment appears with several approved translations from different projects, eras and vendors, and the system offers all of them without saying which is current or which context each belongs to. Fuzzy matches near the threshold require as much work to check as to retranslate. Segments approved years ago under a different style guide sit alongside recent ones with equal authority.

Glossaries drift from usage. Terms are added during onboarding and rarely revisited; product names change; the marketing team adopts new language that never reaches the terminology database; and a linguist who follows the glossary produces text that contradicts the client's own current website.

The result is that experienced linguists develop private heuristics about when to trust the memory, which is a sign that the infrastructure is not doing its job, and quality inconsistency is blamed on linguists when it originates in the assets.

## What Already Exists
Every translation management system provides memory and terminology management with fuzzy matching, concordance search and term recognition — Phrase, Smartling, XTM, memoQ and Trados all do this competently. Automatic term extraction exists. Quality estimation can score MT output and some systems use it to route segments. Memory cleaning and deduplication tooling exists and is typically run as an occasional maintenance project.

## The Customisation Gap
Matching is string-based and the problem is semantic and contextual. Whether a stored translation applies depends on the context the segment appears in — a button label, a legal notice, marketing copy — and on whether it reflects current approved usage. Embedding-based retrieval that accounts for context and recency, and that surfaces disagreement between stored variants rather than listing them, is what a linguist actually needs.

Memory health is the second gap. Contradictory entries, stale segments, entries inconsistent with current terminology, and matches that are routinely rejected by linguists are all detectable, and reporting them as a maintained quality metric turns an occasional cleanup project into continuous hygiene.

Terminology needs to be validated against reality. A glossary term that contradicts the client's own live content, or that no one in the market uses, is a defect, and detecting it requires comparing the termbase against the client's published content and against market language — which nothing does.

And the per-client customisation is register and domain: what counts as a good match differs completely between a medical device manual and a consumer app, and a single fuzzy threshold applied across an account is wrong for both.

## Impact If Solved
Memory and terminology determine both the cost and the consistency of every word translated, and they degrade invisibly until linguists route around them — at which point the leverage the client is paying for has evaporated. Context-aware retrieval, continuous memory health monitoring and terminology validated against live content and market usage restore the leverage and remove a recurring source of quality disputes that are currently attributed to the wrong party.
