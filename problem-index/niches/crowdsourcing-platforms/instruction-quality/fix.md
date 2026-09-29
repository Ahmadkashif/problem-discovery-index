# Fix: The Worker's Question Goes Into a Void

**Niche:** [[niches/crowdsourcing-platforms/instruction-quality/profile|Instruction & Task Design Quality]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A worker notices the instructions are ambiguous, sends a message, receives no reply, and guesses — as do the next four hundred workers.
**Tags:** #workflow-orchestration #descriptive-statistics #evaluation-metrics #large-language-models #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Whether the first worker's question will reach the requester and the answer will reach everyone else.

## The Problem

A worker starts a batch and hits an item the instructions do not cover. They do the sensible thing and ask — through the platform's contact mechanism, into the requester's email.

Most requesters do not reply. They are a researcher running one study, an ML engineer with a deadline, or a company that posted the batch from a shared address nobody monitors. The worker waits, then guesses, then completes the batch. The next worker hits the same item and asks the same question, or does not bother because they know from experience that nobody answers.

Where a requester does reply, the answer goes to one worker. The other four hundred never see it, so the batch contains one worker's correct interpretation and hundreds of guesses, and the requester's agreement statistic reflects it.

## Why It's Still Broken

The contact mechanism was built as a message to the requester, not as a clarification system. There is no shared answer surface, no expectation of response, and nothing that makes a question visible to the people who will hit the same item.

Requesters are frequently one-off and have no operational presence. They post, they collect, they leave. An architecture assuming an engaged counterparty does not fit.

And workers have learned that asking is unpaid time with a low chance of a reply, so question volume is far below actual confusion — which the platform then reads as instructions being clear.

## What a Fix Looks Like

Make the question public to the batch, answerable by anyone, and visible to everyone working it.

Add a clarifications panel to every task, visible to all workers on that batch. Questions asked once, answers visible to all. This is the single change and it converts a private message into shared knowledge.

Let other workers answer. Experienced workers frequently know the intended reading, and a peer answer with a visible count of agreement is better than silence. Where the requester later confirms or corrects, mark it.

Prompt the requester with a threshold. When three workers ask about the same item, notify the requester as an urgent batch-quality issue rather than as a support message. Requesters who ignore individual questions respond to "eleven workers have flagged item 47 as ambiguous and your data quality is at risk".

Answer from the instructions where possible. A model reading the instructions can answer a large share of questions directly, with the relevant passage quoted, and flag the ones the instructions genuinely do not cover — which are the questions that need the requester and are the defect signal.

Count the questions as a quality metric. Question volume per hundred items, by batch and by requester, with the platform median for comparison. This is the earliest and cheapest instruction-defect signal available and it currently goes into an inbox.

And require requesters to nominate a responsive contact, or accept that unanswered clarifications above a threshold pause the batch. A requester unwilling to answer questions about their own task is a quality risk to everyone.

## Who Feels the Pain

Workers, who spend unpaid time asking questions nobody answers and are then rejected for the guess they made. Requesters, receiving data full of divergent interpretations of an item one worker tried to ask them about. And the platform, whose agreement statistics are degraded by a communication channel that does not function.

## Impact If Fixed

The first worker's question becomes everyone's answer, which is the whole difference. Requesters get alerted to ambiguity by the people encountering it rather than by the statistics afterwards. And question volume becomes the instruction-quality signal it already is, instead of a support inbox.
