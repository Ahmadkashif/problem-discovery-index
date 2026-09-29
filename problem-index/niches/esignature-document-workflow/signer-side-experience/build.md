# The Person Who Has to Sign and Cannot Ask

**Niche:** [[niches/esignature-document-workflow/signer-side-experience/profile|The Signer Side]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The signer is the single point of failure for every agreement in the category and is the only participant with no account, no context, no support route and no product.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #worker-facing #revenue-impact #automation
**Contested on:** Every serious competitor that takes the counterparty seriously is fighting to make the person receiving an agreement able to understand it, trust it and ask about it without leaving the envelope — and whoever does that raises completion, which is the only number the sender buys on.

## The Problem
A contractor receives an eleven-page master services agreement from a company they have not worked with, on a Thursday evening, on a phone. They have one question: whether the indemnity clause means what they think it means. There is no way to ask it inside the envelope. Their options are to email the sender's operations address and wait, to sign without knowing, or to do nothing — and doing nothing is the least effortful, so a meaningful share of people choose it. The envelope sits open-and-unsigned for eleven days and is chased by three identical reminders, none of which addresses the actual obstacle.

## Why Nobody Has Built This
The signer does not pay, so no product manager's metric moves when the signer's experience improves — except completion, which everybody reports and nobody attributes to this. Building for the signer means building for someone with no account and no prior relationship, which is uncomfortable for a product organisation used to authenticated users. And answering questions about an agreement edges toward advice, which makes legal departments nervous — a real concern that argues for careful scoping rather than for silence, since the current state is that the signer proceeds uninformed.

## What to Build
A signer-side layer inside the envelope. A plain-language summary of what the agreement actually commits the signer to — obligations, duration, termination, payment, liability, renewal — generated from the document, shown alongside it rather than in place of it, with every statement linked to the clause it came from so the signer can check it. A question route that works: questions asked in the envelope, routed to the sender, with common ones answered from the sender's own prepared material and the rest escalated, which turns an eleven-day silence into a same-day exchange. Explicit paths for the two things signers most often need and cannot do — "I am not the right person, here is who is" and "I cannot agree to clause nine" — both of which give the sender exactly the information that would resolve the stall. Deliberate handling of unusual terms: a clause that is materially unusual for this document type should be flagged to the signer, because a summary that presents an unusual auto-renewal identically to a standard one is a summary that serves the sender rather than the signer. And a durable record for the signer of what they signed, with whom and when, which nobody currently provides across senders.

## Target Customer
Signature platform vendors, for whom completion rate is the differentiator in a commoditising category; and senders with high-volume counterparty agreements — contractor onboarding, supplier terms, patient and client paperwork — where completion is a genuine operational cost.

## Impact If Built
The signer causes most of the non-completion the category loses revenue to, and the causes are ordinary and addressable. Building for the party who does not pay is uncomfortable and is where the remaining differentiation is, since the sender-side product is finished.
