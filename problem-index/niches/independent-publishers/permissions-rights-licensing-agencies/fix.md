# Every Hard Rights Question Is Solved Once and Then Forgotten

**Niche:** [[niches/independent-publishers/permissions-rights-licensing-agencies/profile|Permissions & Rights Licensing Agencies]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst spends three days establishing who controls a right, and the system records the answer and discards the three days.
**Tags:** #tacit-knowledge-ml #large-language-models #graph-ml #worker-facing #data-integration

## The Problem
The hard determinations are genuinely hard. Tracing a chain through three corporate acquisitions to establish which entity succeeded to a 1970s grant. Working out whether an out-of-print reversion clause triggered, and when. Establishing which of an author's estates controls a territory after a division among heirs. Deciding whether a compilation's rights sit with the compiler, the contributors, or both.

An analyst does that work — reading agreements, contacting publishers, chasing correspondence — over hours or days, and reaches a conclusion. The conclusion updates a field. The chain they reconstructed, the evidence they relied on, the parties they contacted and what those parties said, and the parts they could not verify all stay in their notes and their memory.

The same publisher's acquisition history matters for hundreds of other works. The same estate controls a large catalogue. The same reversion clause appears in every contract that publisher signed in a decade. None of it is reusable, so it is re-derived, by whoever draws the next enquiry.

## Why It's Still Broken
The system stores state, not reasoning, because it was designed to answer a licensing transaction quickly. There is a field for the rights holder and no object representing how that was determined.

Throughput pressure does the rest. Licensing runs on volume, analysts are measured on requests cleared, and writing up a determination is time that clears nothing. The individual incentive is to answer and move on, and the collective cost is invisible.

And the reusable knowledge is at the wrong level. What is worth keeping is usually a fact about a *publisher*, an *estate*, or a *contract template* — not about the work the analyst happened to be looking at. There is nowhere to attach a fact about a corporate lineage, so it attaches to nothing.

## What a Fix Looks Like
Make the determination an artefact and attach the reusable parts where they belong.

**Determination records.** The question, the chain established, the documents relied on, the parties contacted and what they confirmed, the confidence, and what remains unverified. Attached to the work and, crucially, to the entities involved.

**Entity-level knowledge as first-class records.** Publisher acquisition histories, estate structures, standard contract terms by publisher and era, known reversion behaviour. These are the facts that recur across hundreds of works, and today they exist only inside individual determinations and analysts' memories.

**Retrieval at the point of work.** When an analyst opens a difficult enquiry, prior determinations involving the same publisher, author, estate, or contract vintage should already be in front of them. That is the whole payoff, and it is what makes people fill the records in.

**Contact outcomes recorded.** Which publisher rights departments respond, how fast, and who at them actually knows — the practical knowledge that determines whether a determination takes a day or a month, currently held entirely as personal relationships.

**Flag determinations that may have gone stale.** Rights revert, estates settle, publishers are acquired. A determination made six years ago may no longer hold, and nothing currently says so.

## Who Feels the Pain
Analysts, re-deriving chains colleagues established last year. New analysts, who need years to become effective because the knowledge is in people. Leadership, whose capability is a set of tenures in a function that is expected to scale. And rights holders, who lose revenue every time an answerable question is closed as unknown.

## Impact If Fixed
The determination corpus is the organization's actual asset — the chain-of-title knowledge nobody else has — and it is being generated at great expense and thrown away one field update at a time. Capturing it compresses the cost of every subsequent hard enquiry, raises the proportion of requests that resolve rather than decline, and turns a capability that walks out at retirement into something the organization owns. It is also the precondition for answering rights questions at the corpus scale that machine-training licensing now demands.
