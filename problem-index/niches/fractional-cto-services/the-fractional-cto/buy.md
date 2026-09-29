# Buy: Personal Knowledge Management Made Multi-Tenant

**Niche:** The Fractional CTO
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Personal knowledge tools and meeting transcription already capture and retrieve everything a practitioner needs, with no concept of the four separate confidentiality boundaries it must be kept behind.
**Tags:** #large-language-models #word-embeddings #bert #evaluation-metrics #data-integration #workflow-orchestration #worker-facing
**Contested on:** Whether a practitioner holding four unrelated complex situations can reload each one to real depth in minutes.

## The Problem

The components of a working memory for a fractional practitioner all exist and are good. Meeting transcription is accurate and cheap. Personal knowledge management systems handle linked notes, search and retrieval well. Assistants can summarise and answer questions over a document corpus. Integration platforms connect to Slack, Jira, GitHub and calendars.

Assembling them into something usable for this working pattern fails on one property none of them has: strict, demonstrable separation between four clients who did not agree to share a tool and may be competitors. A practitioner who puts four clients' material into one Notion workspace or one assistant's context has created a confidentiality problem they cannot describe honestly to any of the four. Most practitioners sense this and respond by keeping four disconnected systems, which removes the cross-client capability that made the tooling attractive and leaves them with four half-used notes apps.

## What Already Exists

Meeting capture: Otter, Fireflies, Granola, Fathom, and native transcription in Zoom, Teams and Meet, with speaker attribution, summaries and action extraction that is genuinely usable.

Knowledge management: Obsidian (local-first, which matters here), Notion, Roam, Logseq, Mem, Reflect — linked notes, search, and increasingly assistants over the corpus. Obsidian's local vaults are the closest existing fit for the separation requirement and are what the most systematic practitioners already use.

Assistants and retrieval: general assistants with document context, plus retrieval tooling that makes a personal corpus queryable.

Integration: Zapier and similar for connecting sources; per-tool notification and digest features that approximate change detection badly.

Professional services automation covers time and billing across clients and nothing about context.

## The Customization Gap

**Tenancy is the whole thing.** Every one of these products has one workspace for one person, or one workspace for one organisation. The fractional pattern needs one person with N isolated contexts, enforced at the storage and retrieval layer, where a query in client B's context cannot surface client A's material, and where the isolation can be explained to a client's security reviewer in a paragraph.

**Selective cross-tenant capability.** The practitioner's principal professional advantage is pattern transfer — what worked at client A informs client C. Total isolation destroys it. What is needed is an abstracted layer that can carry patterns without carrying facts, which is a real design problem no tool has attempted.

**Per-engagement lifecycle.** Engagements start and end. A client context should be creatable in minutes, archivable at close, and deletable on request with an auditable record. Personal knowledge tools have no lifecycle concept at all.

**Change detection, not feeds.** All these tools store what the practitioner puts in them. None watch the client's systems and report what changed since the last session, which is the single most valuable input to a reload.

**Consent-aware capture.** Transcription in a client's meeting requires that client's consent, and the practitioner needs per-client capture policies with an obvious indication of which are in force. No transcription tool models client-specific consent regimes.

**The brief is a missing output format.** These tools are built for retrieval on demand. The practitioner needs an unrequested, scheduled, one-page assembly before a calendar event, which is a fundamentally different interaction.

## Target Customer

Obsidian, or a plugin ecosystem developer within it, is the most natural adapter — local-first storage is the correct architecture for the separation requirement, the user base already skews technical and professional, and vaults are already per-context by default. The commercial gap is that Obsidian's economics do not favour building this centrally, which makes it a plugin or a fork rather than a roadmap item.

Granola and the newer meeting-capture products are the alternative entry: they already sit in every session, and adding per-client context with strict separation is a smaller step than adding meeting capture to a notes product.

Buyers are fractional practitioners of every function — CTO, CFO, CMO — plus portfolio non-executives and interim executives, who share the working pattern exactly.

## Impact If Solved

The practitioner gets the tooling benefit without the confidentiality exposure, which is the trade that currently prevents adoption entirely.

Pattern transfer becomes deliberate rather than accidental. A practitioner who can ask "have I seen this before, and what did we do" across their own engagements, without the facts crossing boundaries, has multiplied the value of their own history.

And a small, ignored professional population gets tooling designed for how they actually work — a group that is growing quickly as fractional arrangements spread from technology into every executive function.
