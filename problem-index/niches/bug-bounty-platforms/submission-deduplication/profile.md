# Submission Deduplication & Filtering

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the mechanical share of triage — duplicates, scanner output, out-of-scope targets — is removed before a human reads, or absorbed by analysts one submission at a time.

## Profile

**Market Size:** ~$75M
**Share of Parent Industry:** ~5%
**Digital Adoption:** Moderate — partial automation, keyword-based
**Target Buyer:** Platform engineering, triage operations
**Automation Potential:** Very high — it is matching and classification

## What Makes This a Distinct Niche

Underneath the judgement work of triage is a mechanical layer: determining whether this submission describes something already submitted, whether it is machine-generated output pasted into a form, and whether the target was ever in scope. None of those requires security expertise. All of them currently consume it.

Duplicate detection is the largest piece and is done by keyword search over prior submissions. It works when the second researcher used similar vocabulary and fails otherwise, which means the same finding described in different words reaches a human twice. Scanner output detection is shallow, mostly pattern-matching on tool names. Scope checking is a person reading a policy page.

This is a distinct market from triage proper because the buyer is platform engineering rather than triage leadership, the work is classification rather than judgement, and success is measured in submissions removed from the human queue rather than in decision quality. It sits alongside [[niches/bug-bounty-platforms/payments-and-operations/profile|⚡ Payments & Programme Operations]] as the mechanical pair in a business whose margin is analyst time.

## Current Tools & Gaps

Manual keyword search across prior submissions within a programme. Some tool-name and output-format pattern matching for scanner detection. Reputation-based queue ordering as a proxy for quality. Canned responses for common invalid categories. Scope tables consulted by hand.

The gaps are conspicuous given how tractable the problem is. Duplicate matching is lexical, so paraphrase defeats it entirely, and embedding-based semantic matching — a commodity technique — is not deployed. Cross-programme duplicate signals are unused, so a researcher submitting the same finding to twenty programmes is detected twenty times independently. Scanner output classification is brittle and easily defeated by trivial editing. Scope checking has nothing structured to check against. And nothing measures the filter's own error rate, so nobody knows how often a real finding is caught by an automated screen.

## Problems

- [[niches/bug-bounty-platforms/submission-deduplication/build|🔨 Build: Semantic Matching Before the Human]]
- [[niches/bug-bounty-platforms/submission-deduplication/buy|🛒 Buy: Near-Duplicate Detection From Everywhere Else]]
- [[niches/bug-bounty-platforms/submission-deduplication/fix|🔧 Fix: Keyword Search Finds the Duplicates That Rhyme]]
