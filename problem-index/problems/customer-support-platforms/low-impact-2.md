# Multilingual Support Coverage

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Machine translation is cheap, good and built into every support platform, and most companies still support two languages — because translation quality is unverifiable at the moment it matters and nobody will risk being wrong in a language they cannot read.
**Tags:** #transformers #large-language-models #bert #word-embeddings #transfer-learning #evaluation-metrics #confidence-intervals #compliance

## The Problem
A company with customers in twenty countries typically supports one or two languages well and offers the rest a delayed, partial, or English-only experience. Customers in unsupported languages get worse outcomes on every metric.

The obvious answer has been available for years. Machine translation is inexpensive and generally good, and every major support platform offers it for both agent replies and knowledge base content.

Adoption is far lower than the quality would justify, and the reason is verification rather than quality. A support manager cannot read the Japanese translation of their refund policy. If it is subtly wrong — a negation dropped, an obligation reversed, a legal term rendered loosely — nobody in the company will notice, and the company has made a commitment in writing to a customer it cannot review. Support text is disproportionately full of exactly the constructs translation handles worst: conditionals, obligations, negations and product-specific terminology.

So companies translate marketing content, where errors are embarrassing, and hesitate on support content, where errors are contractual.

## What Already Exists
Machine translation is a mature commodity from several providers and is embedded in the support platforms. Translation memory and terminology management tools are established. Localisation vendors provide human review at scale. Knowledge base localisation workflows exist in the major platforms. Multilingual routing to native-speaking agents is standard where such agents exist.

## The Customisation Gap
Quality estimation at the segment level is the missing piece. The company does not need every translation reviewed; it needs to know which ones are risky. Estimating translation confidence per segment, and flagging the ones containing negations, conditionals, obligations or unglossed product terminology, would let a small review budget cover the parts that matter.

Terminology enforcement is the second gap. Product names, plan tiers, feature names and legal terms must render consistently and correctly, and generic translation does not know which strings are terms of art. A maintained glossary applied and verified per segment resolves most of the genuine risk.

Round-trip verification is the practical trick nobody productises: translating back and comparing meaning catches the reversed negations and dropped conditions that constitute the dangerous errors, and it can run automatically on every outbound message.

Regulated content is the third gap and deserves an explicit boundary — refund terms, privacy statements and anything with legal effect should route to human review by policy rather than by confidence score.

## Impact If Solved
Language is one of the largest remaining inequities in customer support, and the barrier is not translation quality but the absence of any way to know when a translation is wrong. Segment-level confidence with terminology enforcement makes broad language coverage a manageable risk rather than an unbounded one.
