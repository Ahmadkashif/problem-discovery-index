# The Matter Record in Two Languages

**Niche:** [[niches/legal-practice-software/limited-english-client-practices/profile|Limited-English-Client Practices]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No legal platform keeps the client-language version of a communication as part of the record, so a firm that explains a settlement in Spanish has documented an English summary of a conversation that happened in another language.
**Tags:** #seq2seq #transformers #large-language-models #attention-mechanisms #evaluation-metrics #confidence-intervals #compliance #worker-facing
**Contested on:** Every serious competitor selling to firms whose clients do not speak English is fighting to make the entire client-facing path — intake, documents, status, signature, court communication — work in the client's language without a bilingual staff member in the middle, and whoever covers that path end to end takes the account.

## The Problem
A paralegal explains a settlement offer to a client in Spanish over the phone, answers questions, and logs a note in English saying the offer was explained and the client understood. What the client was actually told exists nowhere. If a dispute arises about informed consent to a settlement — which in personal injury and immigration practice is a real and recurring category of complaint — the firm's evidence is an English note about a Spanish conversation, written by the person whose conduct is in question. The same pattern applies to retainers, document requests, and every status update, and it is universal in this segment.

## Why Nobody Has Built This
The category never modelled the client as a language-distinct participant. Products have a notes field and a portal; making the client's language a property of the matter that propagates through every outbound artefact is a change that touches templates, portal, document generation, e-signature and the record model at once, for a segment vendors do not track as a segment. There is also an unexamined assumption that bilingual staff solve it, which they do operationally and not evidentially — the firm gets the communication and loses the record.

## What to Build
A matter record in which every client-facing artefact exists in both languages, linked, versioned and stored. Outbound communications are generated in English and rendered in the client's language with the client-language version being what is sent and what is retained. Retainers, settlement explanations and any document the client signs get human review of the translation as a matter of policy, because machine translation of a binding legal document without review is not acceptable and the product should enforce that rather than leave it to discretion. Client-facing summaries — what happened, what happens next, what you need to do — are generated in the client's language at plain-language reading level, which most of this population needs regardless of language. The record then answers the question that currently cannot be answered: what did we actually tell this client, in the language they speak.

## Target Customer
Immigration, personal injury, workers' compensation, family and consumer practices whose client base is substantially limited-English-proficient, and the practice management vendors who have never segmented them.

## Impact If Built
The evidential gain is the point: a firm that can produce the client-language document it sent has a defence that currently does not exist, and a firm that cannot is exposed on every settlement. Operationally it removes the bilingual staff member from the routine communication path, which is where most of the bottleneck is, while keeping them on the conversations that genuinely need a person.
