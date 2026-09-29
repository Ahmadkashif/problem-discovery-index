# Conversational Intake Instead of a Category Picker

**Niche:** [[niches/proptech-platforms/work-order-triage-dispatch/profile|Work Order Triage & Vendor Dispatch]]
**Industry:** [[industries/proptech-platforms|Proptech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Conversational interfaces and media capture are commodity, and maintenance intake still asks a resident to choose a category from a list they cannot possibly choose correctly.
**Tags:** #large-language-models #transformers #cnns #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in maintenance triage is fighting to turn a resident's free-text complaint into the right trade, the right urgency and the right vendor without a site manager reading it — and whoever triages most accurately takes the account.

## The Problem
A resident hears a noise in the wall. The portal asks them to pick a category: Plumbing, Electrical, HVAC, Appliance, General. They pick one, probably wrong, and type a short description. Nobody asks the two questions that would resolve it — is it constant or intermittent, is it near a bathroom — because a static form cannot ask a follow-up. The resident could have taken a five-second video and did not, because nothing asked them to. The information that would have made triage easy was available at intake and was not collected.

## What Already Exists
Conversational interfaces built on language models are cheap and reliable for structured elicitation. Multilingual support is commodity, which matters because rental populations are linguistically diverse and current intake forms are typically English-only. Photo and video capture in a web portal is trivial. Image classification for common household conditions — water staining, mould, appliance models, visible damage — works well with modest adaptation. Every component is purchasable.

## The Customization Gap
The adaptation is a short, adaptive elicitation designed around what actually resolves ambiguity. It requires: (1) follow-up questions chosen for information gain against the triage model rather than from a script, so the resident answers two questions instead of eight and the two are the ones that matter; (2) media requested specifically and contextually — "can you take a short video of the noise" — since an unprompted request for photos is ignored and a specific one is usually met; (3) genuine multilingual intake in the languages of the resident population, which is a fairness issue as much as an accuracy one, since residents who describe a problem in a second language are currently triaged worse; (4) immediate safety guidance in the flow, because the same conversation that detects a possible gas smell or an active leak should tell the resident what to do in the next sixty seconds; and (5) a hard stop on friction — a resident who wants to type one sentence and submit must always be able to, since an intake that interrogates will be abandoned and abandonment is worse than an ambiguous request.

## Target Customer
Property operators with resident portals, platform vendors whose intake is a category picker, and vendor marketplaces receiving badly specified work.

## Impact If Solved
Better intake is the cheapest route to better triage, because it improves the input rather than modelling around a bad one, and the components are all off the shelf. Multilingual intake and in-flow safety guidance are the elements with the clearest benefit to residents rather than only to the operator, and both are currently absent almost everywhere.
