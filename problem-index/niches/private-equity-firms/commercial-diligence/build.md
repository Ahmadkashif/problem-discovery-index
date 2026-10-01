# Fifty Interviews Synthesised by the Most Junior Person in the Room

**Niche:** [[niches/private-equity-firms/commercial-diligence/profile|Commercial Diligence]]
**Industry:** [[industries/private-equity-firms|Private Equity Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A CDD study runs dozens of customer and expert interviews in three weeks, and the synthesis that becomes the investment thesis is done by hand the night before the readout.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to say, from evidence gathered in four weeks, whether the target's revenue will still be there and growing in five years — because that judgement is the exit multiple.

## The Problem
Customer interviews are the heart of commercial diligence: why do you buy from this company, what would make you switch, how is your spend changing. A study runs thirty to eighty of them, plus expert and competitor calls. Notes are typed by the interviewer, coded into themes on a spreadsheet, and turned into slides with representative quotes. The senior consultant's skill — hearing the hesitation that means a customer is about to churn — is not captured in the notes.

## Why Nobody Has Built This
Interviews are confidential to the engagement, recordings are often not permitted, and providers treat synthesis as craft. Generic transcript tools summarise but do not code against a CDD framework (switching cost, share of wallet, price sensitivity, competitive set).

## What to Build
A synthesis engine trained on the CDD question set: transcripts or notes coded automatically to the standard framework with quotes linked; a running tally of themes that updates as interviews arrive so the team can redirect remaining calls; sentiment and hedging detection tuned to what experienced interviewers flag as risk; and contradictions surfaced between what customers say and what management claims in the CIM.

## Target Customer
CDD practice heads at strategy firms and boutiques; sponsors running in-house commercial diligence.

## Impact If Built
Synthesis compresses from days to hours and the experienced interviewer's ear becomes a team asset, with the remaining calls redirected to the questions the first twenty raised.
