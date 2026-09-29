# Build: The Engagement Shell

**Niche:** Engagement Operations
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A single runnable engagement template that carries the scope, the contract, the access package, the interview schedule, the document requests and the close-down, so the practitioner sets it up once instead of every time.
**Tags:** #workflow-orchestration #automation #data-integration #compliance #evaluation-metrics #worker-facing
**Contested on:** Whether the administrative shell around an engagement is set up once and reused or rebuilt for every client.

## The Problem

An engagement begins and the same fortnight repeats. Scope and price it, usually from a previous statement of work. Send the NDA. Send the engagement letter. Ask for repository access, which goes to someone who asks what exactly is needed, which produces a conversation about permissions, which produces a security review nobody scheduled. Ask for the tracker. Ask for read access to the cloud console, which is refused and renegotiated. Build a document request list in a spreadsheet and email it. Chase it. Identify the eight people to interview, find their calendars, propose times, reschedule three of them. Set up a shared folder. Agree an invoicing schedule.

Every item is trivial. Together they consume several days of a senior practitioner per engagement, spread across the first two weeks in interruptions, at the exact moment when the engagement's short clock is running and nothing substantive can start without them.

At the end the mirror image happens badly: access is often not revoked, client material sits in the practitioner's folders indefinitely, and the deletion obligations in the engagement letter are met from memory or not at all.

## Why Nobody Has Built This

**It is unglamorous and the market is small.** The total value here is the smallest in the industry, and it is spread across thousands of tiny buyers. No venture-scale company gets built on it, and the practitioners who could build it would rather build something about judgement.

**Everyone's process differs in small ways that feel large.** Each practice has its own contract terms, its own scope shapes and its own view of what access it needs, so a rigid product fits nobody and a configurable one is a bigger build than the market supports.

**The client side is the hard half.** Access provisioning, scheduling and document requests all require work from the client's people, who have their own jobs and no stake in the practitioner's efficiency. A tool that only organises the practitioner's side automates the easy part.

**PSA platforms already claim this space.** They are built for firms of fifty and up, priced accordingly, and configured over weeks — which is why a three-person practice runs on spreadsheets and email instead, and why nobody has noticed the gap.

**Practitioners tolerate it.** It is annoying rather than acute, it is spread thin, and most practitioners have never added up what it costs them.

## What to Build

**An engagement as a runnable template.** Pick the engagement type — assessment, diligence, ongoing fractional — and the shell instantiates: the statement of work drafted from the scope, the contract set queued for signature, the access request package, the document request list, the interview plan, the milestone and invoicing schedule, and the close-down checklist. Configured once per practice, run per client in ten minutes.

**A standard technical advisor access package.** The single highest-value component. A documented, reusable specification of what a technical advisor needs and why — read access to repositories, tracker export, read-only cloud billing, no production data — with the security justification written, in a form a client's security team can approve in one pass instead of discovering piecemeal over a week. Publishing it as an open standard would help the whole profession and would establish whoever does it.

**Client-side self-service.** A portal where the client's team sees exactly what is needed, what has been provided and what is outstanding, and can act without an email thread. Most access delay is not refusal, it is that nobody could see the whole list at once.

**Interview scheduling that actually handles the shape.** Eight people across an organisation inside a two-week window, with dependencies — the architecture interview before the roadmap discussion — and a stated purpose per interview so participants arrive prepared. This is a real scheduling problem done by hand every single time.

**Document requests with chasing built in.** The list, the status, the automatic reminders, and — importantly — absence surfaced as a finding, because in diligence what the client cannot produce is often the most informative thing about them.

**Close-down as an auditable process.** Access revoked, material archived, client data deleted per the engagement letter, and a record of it. This is a genuine compliance exposure that practitioners currently carry without realising, and it is also the moment when the engagement record should be exported into the practice's corpus.

**Priced for the buyer that exists.** Per practitioner per month at a price an independent will pay without a conversation, or per engagement. Anything requiring a sales process is the wrong product for this market.

## Target Customer

Independent fractional CTOs and practices of two to fifteen people — too small for a PSA platform, large enough that the administrative load is material. The buying trigger is usually the third or fourth concurrent client.

The same shell fits fractional CFOs, CMOs and interim executives of every function almost unchanged, which is where the market becomes big enough to be interesting.

## Impact If Built

Several senior days returned per engagement, and more importantly returned at the start, when the engagement clock is short and every day lost to access provisioning is a day not spent on the assessment.

The access package alone compresses the most frustrating week in the profession. A standard specification that a client security team can approve in one pass turns a scattered week into an afternoon.

And the close-down becomes reliable, which removes a real and unpriced liability from a profession that holds a great deal of other people's confidential material in personal folders.
