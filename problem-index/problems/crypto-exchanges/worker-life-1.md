# The Transaction Monitoring Analyst Tracing Hops

**Industry:** [[crypto-exchanges|Crypto Exchanges]]
**Type:** Worker Life Changing
**One-liner:** Analysts trace funds backwards through a public ledger in a vendor's graph interface, one hop at a time, writing narratives about people they will never hear from again.
**Tags:** #graph-neural-networks #graph-theory #large-language-models #bert #k-nearest-neighbors #evaluation-metrics #worker-facing #compliance

## The Problem
An alert fires on a deposit. The analyst opens the vendor's graph tool and works backwards: this address received from that one, which received from a cluster labelled as an exchange, which received from something unlabelled, which touched a mixer four hops back.

The tracing is manual and visual. Click, expand, read the labels, decide which branch matters, expand again. Chains fan out quickly and the analyst is making continuous judgements about which paths are worth following, on a graph that can branch without limit.

Then the narrative. A suspicious activity report requires a written account of what was observed and why it is suspicious, with the on-chain evidence described in prose that a reader without blockchain expertise can follow. Analysts write several of these a week. They are highly formulaic and entirely hand-written.

Alongside it runs sanctions screening, which is stricter and less forgiving — an address on the SDN list is a hard stop, and the tracing question becomes whether funds passed through one, which has the same fan-out problem with a bright line at the end.

And the cases repeat. A few dozen typologies account for nearly everything: a mixer withdrawal, a peel chain, a chain-hop through a bridge, a gambling service, a known scam consolidation pattern. Each is recognised from experience and traced from scratch.

## Why It Matters to the Worker
The work is investigative and is performed under a queue metric. Tracing a peel chain properly takes as long as it takes; the queue does not know that, and the pressure is to stop when the story is good enough rather than when it is complete.

Writing is a large fraction of the job and is not what analysts are hired for. A skilled blockchain investigator spends hours a week composing formulaic prose, and the quality of that prose determines whether the report is useful to a regulator who may never read it.

Outcome feedback is close to zero. Reports go out and almost nothing comes back. Analysts spend careers filing narratives about suspected criminality without learning whether they were right, which is unusual even in financial crime and is corrosive over time. Some cope by treating filing as the objective, which is precisely the defensive posture the whole regime is criticised for.

And the tooling belongs to the vendor. The analyst's skill is substantially skill in one company's interface, and the exchange's own history of what its analysts found is not accumulated into anything reusable.

## What a Solution Looks Like
Automated path finding with the judgement surfaced. The question an analyst answers hop by hop — which branch carries the material flow — is a graph search with a value function, and computing candidate paths to known entities, ranked, turns hours of clicking into a review. Preserve the ability to explore manually; replace the mechanical part.

Typology classification. The recurring patterns — peel chains, mixer withdrawal structures, chain-hop laundering through bridges, scam consolidation — are recognisable graph motifs, and naming the typology at alert time tells the analyst what they are looking at before they start.

Narrative drafting from the traced evidence. The facts are structured by the time the tracing is done; the report is a rendering of them into a required form. This is the single largest time saving available in the role and the least controversial.

An internal case corpus. Every investigation an exchange has done is evidence about addresses, entities and patterns, and it currently lives in closed cases. Retrieval over it — has anyone here seen this counterparty, this pattern, this customer archetype — makes the institution's own experience available.

Feedback wherever it can be obtained. Law enforcement responses, subpoena correlations and confirmed outcomes are scarce and should be routed back to the analysts who filed, because scarce feedback that is delivered is worth far more than abundant feedback that is not.

## Impact If Solved
This role carries genuine investigative skill and spends most of its hours on graph clicking and formulaic writing, with no outcome signal at all. Automating path discovery, naming typologies and drafting narratives returns analysts to the judgement they are employed for, and an internal case corpus stops the institution from losing everything its investigators have learned.
