# Translation With Verification Instead of Two Languages

**Niche:** [[niches/customer-support-platforms/customers-who-cannot-self-serve/profile|Customers Who Cannot Self-Serve]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Machine translation is cheap, good and built into every support platform, and most companies support two languages — because nobody will send an answer in a language they cannot read and check.
**Tags:** #seq2seq #transformers #attention-mechanisms #evaluation-metrics #confidence-intervals #compliance #automation #worker-facing
**Contested on:** Every serious competitor that takes this seriously is fighting to get a customer who cannot use the self-service path to a person quickly and in their own language — and whoever stops routing them in circles takes a population the category has optimised against.

## The Problem
A support organisation could answer in thirty languages tomorrow at negligible cost. It answers in two. The obstacle is not the translation and not the price; it is that a support leader cannot verify that a translated answer is correct, appropriate and free of the specific error that turns a helpful reply into a harmful one — and being confidently wrong in a language nobody on the team reads is a risk they reasonably decline. The result is that a large population of customers is served in a language they did not choose or is not served at all, because a quality assurance problem has been treated as a translation problem.

## What Already Exists
Neural machine translation is mature across the languages that matter, with strong quality in the high-resource pairs covering most of any consumer base. Quality estimation — predicting the reliability of a translation without a reference — is a developed research area with usable implementations. Back-translation checking is elementary. Terminology management and translation memory are established localisation practice. Human review services are available on demand. Every component of a verification layer exists.

## The Customization Gap
The adaptation is to make quality checkable at the moment of sending. It requires: (1) quality estimation on every outbound translation, with low-confidence output routed to human review rather than sent, which converts an unbounded risk into a managed one and is the specific change that unlocks the whole thing; (2) a reviewed terminology base per language for the terms that carry consequence — product names, legal and financial terms, safety instructions — since these are where generic translation errs and where the errors matter; (3) severity-aware gating, so a translated answer about a payment, a safety matter or a contractual right is reviewed at a much lower confidence threshold than one about an opening time; (4) back-translation shown to the agent, which lets a monolingual agent sanity-check what they are sending and is a small feature with a large effect on willingness to use it; and (5) the customer told plainly that the reply was machine translated with a route to a human speaker, which is honest and is what a customer would want to know.

## Target Customer
Support platform vendors, consumer organisations with linguistically diverse customer bases, and the public sector and regulated bodies with obligations to communicate accessibly.

## Impact If Solved
Quality estimation with human review gating turns an unbounded risk into a bounded cost and is what makes multilingual support deployable rather than merely possible. The population served is large and is currently told, in effect, that their language is not supported — which is a choice the organisation is making for a reason that has a solution.
