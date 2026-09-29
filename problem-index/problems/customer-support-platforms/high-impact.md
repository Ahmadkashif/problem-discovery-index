# Knowledge Decay Under Generative Deflection

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Type:** High Impact
**One-liner:** Generative answering made the knowledge base load-bearing overnight, and the knowledge base was already stale — so the industry needs to detect which articles have quietly become wrong before an agent answers a thousand customers from them.
**Tags:** #large-language-models #bert #transformers #word-embeddings #change-point-detection #hypothesis-testing #evaluation-metrics #confidence-intervals #revenue-impact

## The Problem
Deflection has always been the category's economics: every question answered without a human is a cost avoided. For twenty years the mechanism was a help centre that customers mostly did not read.

Generative answering changed the stakes completely. A model answering from the knowledge base will answer confidently whether or not the underlying article is still true, and it will do so at volume, in the company's voice, without the hedging a human would apply. The knowledge base moved from a self-service convenience to the substrate of the company's answers, and nobody upgraded it.

It was already decaying. Articles are written when a feature ships and are rarely revisited. The product changes; the screenshot is now wrong; a setting moved; a limit changed; a plan tier was renamed. Nothing connects a product change to the articles it invalidates, so the corpus drifts continuously and silently.

The failure mode this produces is specific and worse than the old one. Previously a stale article meant a customer got confused and contacted support. Now it means an automated answer asserts something false, the customer acts on it, and the company discovers the problem through a complaint — or does not discover it at all, since a confidently answered wrong question generates no ticket.

## Why It's Unsolved
Knowledge management has always been under-resourced because its value was diffuse. One knowledge manager maintains a corpus that engineering, product and marketing all change without telling them. That was survivable when the corpus was a convenience and is not now.

Staleness is genuinely hard to detect from the article alone. An article does not know the product changed. The signals that would reveal it are elsewhere — in release notes, in the product's own configuration, in support tickets that contradict the article, in customers who read it and then contacted support anyway.

That last signal is the strongest and is systematically discarded. A customer who views an article and then opens a ticket about the same topic has told you the article failed. Every platform can observe this sequence and none of them reports it as an article quality metric.

There is also a measurement vacuum around generative answers themselves. Deflection rate is reported; answer correctness is not, because verifying it requires knowing the truth. Companies are shipping automated answers at scale with no error rate.

## What a Solution Looks Like
Staleness detected from evidence rather than from age. The strongest signals are behavioural: article viewed then ticket opened on the same topic, agents contradicting the article in their replies, and generative answers on a topic followed by customer rejection or escalation. Each is observable in the platform.

Product change linkage is the second half. Release notes, changelogs and configuration changes should map to the articles they touch, so a shipped change produces a review queue rather than silent invalidation.

Answer correctness needs its own measurement, and the honest approach is sampling with human adjudication — a small, continuously reviewed sample of generated answers, scored for factual correctness rather than for tone, producing an error rate the company can actually see. Nobody wants this number and everyone needs it.

Coverage gaps close the loop: clusters of tickets with no corresponding article are the corpus's missing pieces, and they are identifiable from the ticket text.

## Impact If Solved
Generative deflection is being deployed across the category at speed on top of corpora that were never good enough to be load-bearing. Detecting decay and measuring answer correctness is what separates automation that reduces cost from automation that erodes trust — and every signal required is already flowing through the platform.
