# Client Requirement Docs & Change Tracking

**Industry:** [[software-dev-agencies|Software Development Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Requirements already have docs tools — but none track the delta between what was agreed and what the client now wants, in agency billing terms.
**Tags:** #llm #text-generation #nlp #workflow-orchestration

## The Problem
Agencies receive requirements in wildly inconsistent formats — email threads, Figma comments, Loom videos, Google Docs with inline comments, Slack messages. When the client says "can we also add X," that change request lives in a Slack thread that nobody links back to the SOW. Three weeks later, the developer has built X, the PM forgot to log it as out-of-scope, and the agency eats the cost. The gap is not capturing requirements — it is tracking requirement drift against the contractual baseline in real time.

## What Already Exists
Confluence, Notion, and Google Docs handle document collaboration. Jira and Linear track tasks. But none of these tools understand the concept of a "contractual scope boundary." They track what needs to be done, not whether what needs to be done was part of the original agreement. Tools like PandaDoc handle the contract itself but have zero integration with the day-to-day project management layer where scope changes actually happen.

## The Customisation Gap
Agency-specific logic requires: (1) parsing the original SOW/contract to extract committed deliverables as structured scope items, (2) monitoring all client communication channels (Slack, email, Figma comments) for new requests, (3) classifying each request as in-scope, out-of-scope, or ambiguous relative to the SOW baseline, and (4) generating change order drafts with effort estimates attached. This requires understanding agency billing models (T&M vs. fixed-bid vs. retainer), contract language patterns, and the specific tech vocabulary of software projects.

## Impact If Solved
Agencies recover 10-15% of unbilled scope creep per project. A 20-person agency running 8 concurrent projects could recapture $150-300K annually in work that currently goes uninvoiced because nobody caught the scope change in time.
