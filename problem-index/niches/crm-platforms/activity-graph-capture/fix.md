# Reading the Mailbox Without a Designed Privacy Position

**Niche:** [[niches/crm-platforms/activity-graph-capture/profile|Activity Graph Capture]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Activity capture connects to an employee's mailbox and calendar continuously, and what it reads, what it stores and what it excludes is governed by a permission scope nobody outside the administration team has examined.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #automation #confidence-intervals #worker-facing #quick-win
**Contested on:** Every serious competitor in activity capture is fighting to reconstruct a complete, correctly attributed engagement graph from email and calendar without asking a representative to do anything — and whoever holds coverage and attribution accuracy highest takes the account.

## The Problem
A representative's mailbox is connected to the capture platform with a broad permission scope. The platform reads everything and filters afterwards, which means personal correspondence, internal discussions, medical appointments in the calendar and messages from a recruiter all pass through the system before being discarded — or, depending on the implementation, are stored and marked as excluded. The representative was told the company uses an activity capture tool. They were not told that the mechanism reads the whole mailbox, and in most organisations nobody could tell them precisely what is retained, because the answer lives in a configuration and a vendor's data handling document.

## Why It's Still Broken
Broad scopes are simpler to implement than narrow ones and the mail platforms' permission models do not always offer fine-grained alternatives. Filtering after ingestion is easier than filtering before. And the people affected — representatives — were not consulted, because the product was procured by revenue operations for leadership. The absence of a designed position is not usually a decision to be invasive; it is the absence of anyone asking the question.

## What a Fix Looks Like
Design the boundary and publish it. Capture only external correspondence and calendar entries with external participants, filtered at the point of access rather than after storage wherever the platform's permission model allows it. Exclude entirely the categories that are obviously outside scope — personal domains not associated with any account, internal-only threads, entries marked private — and state the exclusion rules plainly rather than in a data processing addendum. Give the representative a view of what has been captured from their mailbox and a mechanism to exclude a thread or a contact, which costs almost nothing and transforms the relationship. Publish retention: what is kept, for how long, and what happens when the representative leaves. Where the mail platform's scopes are too coarse, say so rather than relying on post-hoc filtering to make it acceptable, and press the platform for a narrower scope — this is a case where the vendors have collective leverage and have not used it.

## Who Feels the Pain
Representatives whose entire mailbox passes through a system they did not choose; administrators who cannot answer a simple question about what is stored; and the organisation, carrying an exposure that becomes visible only when an employee asks.

## Impact If Fixed
Filtering at access rather than after ingestion is a technical change with a real reduction in what is held, and a representative-facing view of their own captured data is cheap and directly addresses the category's most reasonable objection. Both are achievable without reducing the coverage the product is measured on, which is the point worth making to a vendor: the privacy position and the product quality are not in tension here.
