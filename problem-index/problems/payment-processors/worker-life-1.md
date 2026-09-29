# The Merchant Risk Analyst

**Industry:** [[payment-processors|Payment Processors]]
**Type:** Worker Life Changing
**One-liner:** Underwriters decide a business's fate by reading its website and its processing history under an approval-time target, and never learn which of their decisions was right.
**Tags:** #large-language-models #bert #graph-neural-networks #k-nearest-neighbors #gradient-boosting #evaluation-metrics #worker-facing #compliance

## The Problem
The queue holds applications that the automated path would not approve. Each one is a business: a legal name, an EIN, a website, a stated processing volume, a beneficial owner, sometimes statements from a prior processor.

The analyst opens the website. They read what is being sold, look for a returns policy, check whether the prices are plausible, look for the signals that distinguish a real operating business from a shell — a phone number that connects, a physical address that is not a mailbox, product photography that is not lifted from a supplier catalogue. They check the name against the terminated merchant registry and against internal records. They form a view about fulfilment timelines, because a business that takes payment now and ships in eight weeks carries chargeback exposure that a restaurant does not.

Then they set limits: monthly volume cap, per-transaction cap, reserve percentage, delayed settlement. These are the levers, and they are set by policy bands and by feel.

The approval-time target is short, because merchants shop and a competitor will approve in an hour. The volume of applications is high. And the same handful of merchant archetypes recur constantly, each one re-read from scratch.

## Why It Matters to the Worker
The job is consequential in both directions and graded in only one. An approval that becomes a fraud loss is investigated and attached to the analyst's name. A decline that would have been a good merchant is invisible — the business goes to a competitor and nothing about that reaches the analyst. The feedback they receive is therefore entirely negative and entirely partial, which reliably produces underwriters who become more conservative over time regardless of whether conservatism is correct.

The second load is that the evidence is bad. They are asked to make a financial judgement about a business from a website, and websites are cheap. Experienced underwriters develop a genuinely valuable instinct for this, hold it tacitly, and lose it to the company when they leave.

The third is the pressure. Sales wants the merchant approved. Risk owns the loss. The analyst sits between them with a stopwatch running.

## What a Solution Looks Like
Website and business context read before the case opens. What the merchant sells, in a taxonomy the risk policy actually uses; fulfilment and refund terms extracted from the site's own pages; the storefront template identified and counted against every other merchant using it; the payment descriptor and hosting fingerprints matched against known entities. This is the analyst's manual first twenty minutes and it is automatable.

Entity linkage surfaced, not searched for. A new application that shares infrastructure, descriptor patterns, banking behaviour or site template with a previously terminated merchant should arrive at the top of the case with that link stated, rather than depending on an analyst thinking to check.

Comparable merchants with outcomes. Here are forty merchants we approved that look like this one, here is their chargeback rate at six months, here is what we set their reserve to. That converts a feel judgement into an empirical one and transfers the tacit skill.

Symmetric feedback. Analysts should see the realised performance of merchants they approved and, where it can be obtained, some signal about those they declined. The asymmetry in feedback is the direct cause of the drift toward conservatism.

Limits recommended from data rather than bands. Reserve and cap settings are a pricing problem with observable outcomes, and they are currently set from a policy table written years ago.

## Impact If Solved
Underwriting speed is a competitive lever and underwriting accuracy is a loss lever, and both are currently limited by how fast a person can read a website. Automating the reading, surfacing linkage and comparables, and closing the feedback loop symmetrically makes the decision faster and better at once, and keeps the instinct in the institution rather than in the individual.
