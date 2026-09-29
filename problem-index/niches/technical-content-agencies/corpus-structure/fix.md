# The Sentence That Needs the Page Around It

**Niche:** [[niches/technical-content-agencies/corpus-structure/profile|Corpus Structure & Disambiguation]]
**Industry:** [[industries/technical-content-agencies|Technical Content Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** The paragraph says "in this version" and nothing in the paragraph says which version that is.
**Tags:** #quick-win #compliance #evaluation-metrics #automation #descriptive-statistics #data-integration #word-embeddings #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to write statements that stay true when extracted from their surroundings — and whoever establishes that craft takes the account.

## The Problem
Documentation is full of deictic references: this version, the previous step, as described above, the default behaviour, the recommended approach. Each depends entirely on where the reader is. Extracted — by an assistant, by a search snippet, by a reader who arrived deep-linked from elsewhere — they are ambiguous or wrong. They are also easy to find, because they use a small set of recognisable phrases.

## Why It's Still Broken
The phrases read naturally — a reference that is perfectly clear to someone reading the page in order is invisible as a defect to the author writing it, and no check flags it. Style guides address tone rather than context dependence. Deep-linked and extracted reading was rare. And nobody has named the problem.

## What a Fix Looks Like
Lint for the phrases and fix the pages that are extracted most. Add a lint rule for deictic and context-dependent phrases, which is the fix and catches most of them mechanically. Fix the highest-traffic and most-referenced pages first rather than the whole corpus. State the version explicitly wherever behaviour is version-specific, which is the single most valuable substitution. Replace references to position with references to the thing itself, which reads better anyway. Add a version and applicability line to pages that lack one. Check that code examples run standalone rather than depending on setup elsewhere on the page. Make the rule part of the style guide so new content complies by default. Review pages that appear in assistant answers with particular care, since those are the ones being extracted. Apply the rule to release notes and deprecation notices especially, as those are where an inverted meaning does the most damage. And record the fixed pages so the improvement is attributable.

## Who Feels the Pain
Readers who arrive deep-linked and are told something false; developers receiving an extracted statement without its version; support teams handling the consequences; and writers whose careful prose becomes wrong when quoted.

## Impact If Fixed
A reference perfectly clear to someone reading in order is invisible as a defect to the author writing it, and no check flags it. A lint rule for deictic phrases catches most of them mechanically.
