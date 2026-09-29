# Linking Only What Should Be Linked

**Niche:** [[niches/developer-relations-agencies/identity-and-privacy/profile|Identity Linking & Privacy Design]]
**Industry:** [[industries/developer-relations-agencies|Developer Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The link is technically achievable and the question of whether it should be made has never been answered.
**Tags:** #compliance #data-integration #k-nearest-neighbors #evaluation-metrics #confidence-intervals #graph-theory #descriptive-statistics #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to connect the same pseudonymous developer across a conference, a community, a piece of content and a signup — and whoever does that acceptably takes the account.

## The Problem
A developer's advocacy exposure and their eventual adoption are recorded in different systems under different identities. Linking them would settle the field's measurement problem. It would also mean connecting a conference badge to a community handle to a product account for people who chose different identities in each, in a profession that is unusually attentive to being tracked. The technical problem is tractable and the legitimacy problem is the real one.

## Why Nobody Has Built This
The field's instinct — that this should be approached carefully — is correct, and has resulted in it not being approached at all rather than being approached properly. No consent mechanism exists for it. Nobody has defined what linking would be acceptable. And a firm that gets it wrong damages the community relationship the whole function rests on.

## What to Build
Design the consent and minimisation first, and link only what that permits. Establish what linking is acceptable and obtain consent for it explicitly, which is the core — a linking capability built before that question is answered is the wrong artefact regardless of how well it works. Prefer self-declared connections — a developer choosing to associate their community handle with their account — over inference, since consent obtained is worth more than accuracy inferred. Minimise: link only the fields needed for the measurement and discard the rest, which limits both the risk and the temptation. Aggregate as early as possible so individual-level data does not persist, which is the design that makes the whole thing defensible. Be transparent with the community about what is linked and why, since discovering it later is the failure mode that matters. Offer a clear opt-out that is honoured and visible. Handle the pseudonymity deliberately, because a developer who uses different identities in different places has usually done so on purpose. Keep the linked data inside a narrow boundary with access controls and retention limits. Publish the position, which is what would let the field have the conversation. And be willing to conclude that some links should not be made, which is a legitimate outcome and one a measurement product will resist.

## Target Customer
Developer relations and data leadership, privacy and legal functions, developer platform vendors, and privacy engineering providers.

## Impact If Built
The link is technically achievable and nobody has answered whether it should be made, so the field does neither properly. Consent and minimisation designed first is what makes any of it legitimate.
