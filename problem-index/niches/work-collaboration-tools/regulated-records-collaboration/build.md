# Retention at the Record Rather Than the Container

**Niche:** [[niches/work-collaboration-tools/regulated-records-collaboration/profile|Regulated & Records-Managed Collaboration]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Retention policy is applied to whole channels and sites because nothing identifies which messages are actually records, so organisations keep everything for seven years and cannot find anything in it.
**Tags:** #bert #large-language-models #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #automation #descriptive-statistics
**Contested on:** Every serious competitor in regulated collaboration is fighting to let people work in modern tools while every communication that constitutes a record is retained, retrievable and appropriately restricted — and whoever makes that true without crippling the tools takes the sector.

## The Problem
A financial services firm applies a seven-year retention policy to its entire collaboration estate because it cannot distinguish a substantive client communication from somebody arranging lunch. The consequences run in both directions: enormous volumes of trivial content are retained at cost and become discoverable in litigation, while genuine records are buried among them and cannot be located when a regulator asks — which is the failure that actually matters. Meanwhile retention that is too aggressive in the other direction destroys records that should have been kept. Both failures come from the same cause: policy is applied to containers because nothing classifies content.

## Why Nobody Has Built This
Container-level retention is what the platforms implemented, because it is simple, defensible and requires no judgement about content. Classifying what constitutes a record requires understanding both the content and the obligation, which is a domain-specific determination that varies by sector and by record type, and no vendor has wanted to assert it. And the over-retention failure is quiet — an organisation that keeps everything appears compliant until a discovery exercise reveals the cost, which happens rarely enough not to force a change.

## What to Build
Record classification applied at the message and document level, driving retention, restriction and hold. Content is classified against the organisation's own record taxonomy — client communication, advice, transaction record, decision, internal deliberation, incidental — using the content, the participants, the channel context and the attachments, with confidence and with human review for the consequential classes. Retention, supervision and restriction policies attach to the classification rather than to the container, which means the trivial content ages out and the records are preserved and findable. Legal hold is applied at the record level and spans surfaces, including the ephemeral and the third-party content that container-level hold misses. And the decisive property is retrievability: a regulator's request should be answerable by query rather than by a discovery exercise, which requires the classification to be applied at capture rather than reconstructed later. The output is both a smaller retained corpus and a findable one, which is a better compliance position than the current over-retention on every dimension including cost.

## Target Customer
Financial services, healthcare, legal, pharmaceutical and public sector organisations; collaboration platform vendors selling into them; and the information governance and archiving vendors whose products stop at the container.

## Impact If Built
Over-retention is expensive, increases litigation exposure and makes genuine records unfindable, and it exists because classification was harder than a blanket policy. Record-level classification is now achievable, and the retrievability improvement is the part that matters most: the current failure is not usually that a record was destroyed but that it could not be found.
