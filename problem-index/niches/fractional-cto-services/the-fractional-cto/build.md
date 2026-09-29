# Build: The Context Reload

**Niche:** The Fractional CTO
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A per-client working memory that assembles what changed, what was committed and what is now at risk into a five-minute brief before every session, across four strictly separated tenants.
**Tags:** #large-language-models #bert #word-embeddings #change-point-detection #evaluation-metrics #workflow-orchestration #worker-facing
**Contested on:** Whether a practitioner holding four unrelated complex situations can reload each one to real depth in minutes.

## The Problem

Tuesday morning, and the practitioner has a session with client B at ten. They last saw client B eight days ago. In between they have run a board meeting at client A, handled an incident at client C, and spent Friday on a diligence for a fourth. The model of client B that was vivid eight days ago has gone soft at the edges.

So the half hour before ten goes to reconstruction. Scroll the Slack channel. Re-read their own notes, which are good on conclusions and thin on the texture. Check whether the thing they asked for got done. Try to recall what the head of engineering said about the contractor, and whether that was a passing remark or the beginning of a resignation. Look at the repository to see if the migration branch moved.

The reconstruction is unbilled, partial and always weakest in the same place: the human and political texture that took weeks to build and has no written form. The practitioner walks in with the technical picture roughly restored and the social picture substantially degraded, and the social picture is frequently what the session actually turns on.

Meanwhile the client experiences a practitioner who asks a question they answered last time, or who has not noticed that the thing under discussion resolved itself on Thursday. Each instance is small. Cumulatively it is the difference between a trusted advisor and an expensive visitor.

## Why Nobody Has Built This

**The market looks tiny from outside.** Independent practitioners buying individually, at consumer-ish price points, with no procurement and no expansion path. Venture-scale software does not get built for them, and the practitioners themselves are engineers who will build a personal workaround before they will buy.

**Multi-tenancy under four separate NDAs is genuinely hard.** Four clients who may be competitors, four sets of confidentiality obligations, four organisations who did not agree to a shared tool. Any system touching all four must guarantee separation architecturally and be able to demonstrate it to a client security review, which is a heavy requirement for a product with a small buyer.

**The integration surface is wide and shallow.** Four Slacks, four trackers, four repository hosts, four calendars, four sets of credentials, each granted at a level a guest advisor is given — which is usually less than an integration expects. The per-client setup cost has to be near zero or the tool is worse than nothing for an engagement that lasts nine months.

**The valuable content is the unrecorded content.** Most of what the practitioner needs — the political situation, who is quietly disengaging, what the CEO actually meant — is in conversations, not in systems. Capturing it means transcription of client meetings, which requires consent, and consent conversations in a client's boardroom are their own obstacle.

**General-purpose tools are adequate-ish.** A disciplined practitioner with a good notes system copes. The gap is real but not acute enough to drive a purchase on its own, which means the product has to be dramatically better rather than incrementally so.

## What to Build

**A pre-session brief as the whole product.** Twenty minutes before the session, one page: what changed in this client's systems since the last visit, what was committed by whom and whether it happened, what was open and remains open, what the practitioner said they would do, and the three things most likely to come up. Delivered to the phone, readable in five minutes. Everything else in the product exists to make that page good.

**Change detection between visits.** Repository activity, tracker movement, deployment events, incident occurrences, and — where access exists — the shape of Slack activity rather than its content. Not a feed; a difference. The practitioner does not want to read eight days of a client's life, they want the four things that would alter their model.

**Commitment tracking across all clients.** Every "I'll look into that" and "can you have that by Friday" captured from meeting transcripts where consent allows, held per client, surfaced in the brief. Practitioners lose commitments across the client boundary constantly and it is the most visible failure to the client.

**Capture the texture, not just the conclusions.** Structured prompts immediately after each session, five minutes, aimed at exactly what the notes always miss: who seemed disengaged, what did not get said, what is the political state, what am I worried about. Voice capture in the car afterwards is the realistic form. This is the part that decays fastest and is the hardest to reconstruct.

**Architectural separation, demonstrable.** Per-client isolation as a design property, with a client-facing explanation of it, so a practitioner can answer the security question without a conversation. Local-first is a legitimate and probably correct answer here.

**Near-zero setup, graceful degradation.** A client who grants only a repository read gets a repository-only brief. The tool must be useful at the lowest access level it will actually be given, because half of clients will never grant more.

**Engagement close-out as an export.** At the end, a structured record of the engagement — which feeds both the handover deliverable and the practice's own corpus. The practitioner who used the tool all along has already produced most of the handover.

## Target Customer

Independent fractional CTOs with three or more concurrent clients, and small practices whose practitioners each hold several engagements. The buying trigger is the fourth client — the point at which the informal system visibly stops working.

Interim executives, fractional CFOs and CMOs, and portfolio non-executive directors have an almost identical working pattern, which is where the market stops being tiny.

## Impact If Built

The reload goes from thirty degraded minutes to five good ones, which is roughly a day a month returned to a practitioner who bills by the day — the product pays for itself at almost any price.

The quality ceiling rises. A practitioner who can reliably reload four contexts to depth can carry four clients well instead of three well and one badly, which is a direct increase in both income and client outcomes.

And the client experiences continuity. The single most valuable property a fractional advisor can have is that they appear to have been thinking about the company all week, and this is the only affordable way to produce it.
