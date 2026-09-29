# Lineage: Freelance Marketplaces

**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the oDesk Work Diary — a desktop time-tracker that logs billable hours in ten-minute segments, each backed by a screenshot taken at a random moment and an activity count, as the evidence for a guaranteed hourly payment
**Builder:** oDesk
**Builder in vault:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Verification:** partial — see Sources

## The Problem That Came First

An hour of remote work could not be proved.

A freelance project priced as a whole — a logo, a translation — can be judged on delivery. Open-ended work cannot. Software maintenance, research and ongoing support are naturally bought by the hour, and an hour is only worth paying for if someone can see it was worked. In an office a manager sees it. Across an ocean, between two parties who have never met, nobody does.

That left both sides exposed. A client paying hourly had no evidence the hours happened. A contractor billing hourly had no protection if the client simply refused to pay. Elance, founded in Jersey City in 1998, was characterised by oDesk's later CEO as a fixed-price market — bids for defined projects, where the deliverable carries the proof. Hourly remote work had no equivalent.

## What Got Built

**The Work Diary**, fed by oDesk's desktop "Team" application.

The contractor runs the application while working. It records time in ten-minute blocks. In each block it takes a screenshot at a random moment and counts keystrokes and mouse clicks to produce an "activity level"; the contractor adds a memo saying what they were doing. Optional webcam captures were also supported. The blocks are uploaded to a diary the client can inspect, and the week's logged time is billed to the client automatically.

The payment rule is the point. oDesk's contractor manual tied its **Payment Guarantee** to auto-tracked time: hourly contract, time logged through the application with memos, and a client with a verified payment method. Time entered manually billed the same way but was not guaranteed. Upwork later stated the principle directly: "the primary reason this technology exists is because it is the underpinning of our Payment Protection."

So the screenshot is not only surveillance for the client. It is the evidence on which the platform agrees to underwrite the contractor's pay.

## Who Built It, And Why Them

**oDesk**, founded by Odysseas Tsatalos and Stratis Karamanlakis, two friends who grew up together in Greece and worked together remotely — one in the United States, one in Greece.

The origin is a refusal. By the founders' own account, Tsatalos's employer did not want to hire Karamanlakis because he lived too far away to communicate with, collaborate with and monitor as effectively as someone in the office. They worked together remotely anyway, and Tsatalos framed the company's question as how to bring "the trust, visibility and control" of a shared office to a remote relationship.

That explains why oDesk built monitoring rather than, say, better project scoping. The founders' own problem was an employer's objection to an unseen worker. The answer they built reproduced what the employer could see in an office — presence, hours, a view of the screen — and turned it into a record. Early oDesk ran as a staffing firm, according to its later CEO Gary Swart, before becoming a self-serve marketplace; the hourly model with tracking was what Swart contrasted with Elance's fixed-price model.

## What It Cost

The worker gave up privacy to be guaranteed payment. Screens are captured whatever is open on them, and a deleted screenshot deletes its ten minutes of billable time. Coverage in 2018 recorded freelancers describing the tool as invasive.

It also set a measure of work as activity: keystrokes and clicks per ten minutes stand in for output. And it established that the platform, not the two parties, holds the authoritative record of what was done — the same position from which it later ranks, rates and decides disputes.

## What You Still Touch

Every hourly contract on Upwork still runs through the descendant of this diary, and the platform's standing as judge of who worked and who gets paid began with it.

- [[problems/freelance-marketplaces/low-impact-2|🟡 Dispute Resolution and Escrow Adjudication]] — the diary as evidence
- [[problems/freelance-marketplaces/high-impact|🔴 The Ranking Sets the Income and Nobody Will Explain It]] — the platform's record, turned into a score
- [[problems/freelance-marketplaces/worker-life-2|🟢 The Trust and Safety Agent Deciding Who Keeps Their Account]]
- [[niches/freelance-marketplaces/payments-and-escrow/profile|Payments, Escrow & Cross-Border]]
- [[niches/freelance-marketplaces/dispute-resolution/profile|Dispute Resolution]]

**Sources:** Wikipedia, *Upwork* (oDesk founded 2003 by Tsatalos and Karamanlakis, collaborating remotely between the US and Greece; originally a staffing firm; Elance founded 1998 in Jersey City; 2013 merger, 2015 rebrand); this vault's `history/freelance-marketplaces.md` (same founding facts, from the same Wikipedia articles — vault material, not independent corroboration); oDesk Freelancer Manual (SlideShare copy; random screenshots within ten-minute intervals; Payment Guarantee conditions; manual time billed but not guaranteed); Caroline O'Donovan, BuzzFeed News, 7 August 2018 (screenshots, keystroke and click counts, occasional webcam photos; Upwork's "underpinning of our Payment Protection" quote); search-result summaries of Upwork's 2013 blog "What Does 'oDesk' Mean Anyway?" and Tsatalos's Medium essay (the employer's objection; "trust, visibility and control" quote) — both pages returned 403 and were not read directly; Mixergy interview with Gary Swart (staffing-firm origin; hourly tracking contrasted with Elance's fixed-price model). ⚠️ **Not established:** the date the Work Diary or its screenshot feature first shipped. An oDesk press release announcing general availability of "oDesk Team" exists but returned 403; a 2006 PC Magazine review is mentioned only in a search summary. Mixergy's introduction dates the founders' collaboration to 2005, conflicting with Wikipedia's 2003 founding; not resolved.
