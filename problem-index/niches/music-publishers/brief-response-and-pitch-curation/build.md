# A Pitch Ledger That Learns What Each Supervisor Licenses

**Niche:** [[niches/music-publishers/brief-response-and-pitch-curation/profile|Brief Response & Pitch Curation]]
**Industry:** [[industries/music-publishers|Music Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The brief, the pitch and the outcome sit in three systems, so the rep's judgement about what each supervisor buys is never recorded or learned from.
**Tags:** #tacit-knowledge-ml #transformers #contrastive-learning #word-embeddings #large-language-models #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put the song the supervisor will actually license among the first few they hear, inside the brief's 24–48 hour window, and whoever does that most often becomes the supervisor's first call.

## The Problem
A sync team answers hundreds of briefs a year (estimate). Each produces a playlist, occasionally a quote request, rarely a licence. The publisher keeps the licence and loses the rest: what was asked, what else was sent and what was shortlisted. That history is exactly what separates a senior rep from a junior one.

## Why Nobody Has Built This
Pitch tools store playlists, rights systems store licences and briefs live in email, so nobody owns the join. Outcome labels are noisy, since silence after a pitch is not a no. And reps will not fill in forms under a deadline.

## What to Build
A ledger that parses briefs from email, links them automatically to the playlist sent and to any quote, licence or lapse, and grades each pitched song. Over the ledger sits a ranker that encodes briefs (text and reference tracks) and songs (audio, lyrics, metadata, licence history). It is trained on pitched, shortlisted and licensed outcomes and conditioned on the recipient, and it returns a short list with reasons and clearance status in minutes.

## Target Customer
Heads of sync at publishers with catalogues of tens of thousands of songs or more.

## Impact If Built
Higher shortlist and licence rates per brief without adding reps. A rep's pattern recognition is kept when they leave, and a junior can answer a brief like a senior.
