# Client Review & Approval Workflow for Video Production

**Industry:** [[video-production-smb|SMB Video Production]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Frame-accurate client feedback stops getting lost in email threads and vague Slack messages, cutting revision cycle time in half.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #word-embeddings #entropy-cross-entropy-kl-divergence #workflow-orchestration

## The Problem
Clients watch a rough cut and send feedback via email, Slack, text, or phone call. Their comments are rarely frame-accurate — "the transition around 1:20 feels off" or "can you make the intro more dynamic?" Editors must translate these into specific timeline edits, often requiring a follow-up call to clarify intent. A single round of revisions that should take 2 hours consumes 6 hours when you include the back-and-forth interpretation cycle. Multiple stakeholders on the client side compound the problem — the marketing director, the VP, and legal each send separate, sometimes contradictory notes through different channels.

## What Already Exists
Frame.io provides frame-accurate commenting directly on video timelines and is the industry standard for review workflows. Vimeo Review has similar capabilities. Both tools solve the technical problem of pinpointing feedback to specific frames.

## The Customisation Gap
Frame.io assumes reviewers will use the platform's commenting interface, but most SMB clients refuse to create accounts or learn new tools — they reply to the Vimeo link via email. The gap is an NLP layer that ingests feedback from any channel (email, Slack, SMS, voice transcription), extracts actionable revision requests, maps vague temporal references ("around the middle," "near the end of the interview section") to specific timecodes using the project's edit decision list, and consolidates conflicting notes from multiple stakeholders into a single prioritized revision list the editor can execute sequentially. Production-specific terminology ("J-cut," "lower third," "b-roll coverage") must be understood natively, not treated as generic text.

## Impact If Solved
Editors reclaim 3-5 hours per project in interpretation overhead. Revision turnaround drops from 3-5 business days to 1-2, compressing project timelines and improving client satisfaction scores.
