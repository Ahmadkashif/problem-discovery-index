# Obligation-Level Impact Routing Across Jurisdictions

**Niche:** [[niches/compliance-consulting/regulatory-content-publishers/profile|Regulatory Intelligence Publishers]]
**Industry:** [[industries/compliance-consulting|Compliance Consulting]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A single rule change lands on subscribers who each need to know which of their own controls it touches, and the publisher answers by sending everyone the same alert.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #transfer-learning #evaluation-metrics #compliance #data-integration #revenue-impact

## The Problem
The publisher's corpus is organized around regulations and its subscribers are organized around controls. A change to a rule matters to a given subscriber only if it touches an obligation they are actually subject to, implemented by a control they actually run, in a jurisdiction they actually operate in. The publisher knows the first part and not the rest, so alerting is broadcast: everyone subscribed to a topic receives everything, and each subscriber's compliance team performs the triage that determines whether it matters to them. That triage is the expensive part of the subscriber's job and the reason they bought the subscription in the first place. Meanwhile the same triage is being performed independently by thousands of organizations against the same corpus.

## Why Nobody Has Built This
The content was built as a regulatory library and indexed by source — agency, citation, topic — which is the natural structure for publishing and the wrong one for routing. Restructuring it around obligations means decomposing decades of interpretive content into discrete requirements with applicability conditions attached, which is substantial editorial work with no immediate revenue attached. Cross-jurisdiction obligation equivalence is harder still: two states requiring materially the same thing in different language is a judgment the corpus records nowhere. And routing to a subscriber's own control set requires knowing that control set, which means an integration the publisher has historically avoided because it moves them closer to being a system of record.

## What to Build
An obligation layer over the corpus. Each interpretive statement is decomposed into discrete obligations carrying applicability conditions — entity type, size threshold, activity, jurisdiction — and linked to equivalent obligations elsewhere, so the corpus knows when three states are requiring the same thing. Rulemakings and guidance resolve against obligations rather than against topics, which is what makes impact routing possible at all. Subscribers map their own control set to the obligation layer once, either directly or through the mapping their GRC platform already holds, and from then on receive changes scoped to what they are actually subject to, with the affected controls named. The queue at both ends sorts by consequence rather than by arrival. For the publisher, the obligation graph is also the thing that turns a library into a system subscribers cannot easily leave, because the mapping they build is retained value.

## Target Customer
Heads of regulatory intelligence and VPs of content at publishers running 200-1,000 analysts, and the compliance leaders at subscriber organizations whose teams currently triage broadcast alerts by hand.

## Impact If Built
Moves the product from a library to a routing engine, which is a different and considerably more defensible category — a subscriber who has mapped their controls has switching costs a content subscription never generates. It also removes the duplicated triage that thousands of subscribers perform independently, which is precisely the labour the subscription was supposed to eliminate and currently does not.
