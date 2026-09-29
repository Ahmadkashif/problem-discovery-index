# Where Did This Code Come From

**Niche:** [[niches/developer-tools-vendors/enterprise-assistant-governance/profile|Enterprise Assistant Governance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An enterprise cannot say which of its code was generated, by which model, from what context, which makes every licence, audit and incident question unanswerable after the fact.
**Tags:** #graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #compliance #data-integration #automation
**Contested on:** Every serious competitor here is fighting to make an assistant approvable by a security and legal function — provenance, licence exposure, data boundaries and audit — and whoever does that takes the enterprise, because a blocked tool has no adoption to win.

## The Problem
A customer's security review asks how a particular component was developed and whether any third-party code was incorporated. The engineering team knows that assistants were in use across the period. They cannot say which parts of the component were generated, what context was sent, which model version produced it, or whether the filter that was supposed to catch public code matches was enabled for that repository at that time. The honest answer is that nobody knows, which in a regulated industry is a finding rather than an inconvenience — and it is the reason deployments stall.

## Why Nobody Has Built This
Assistants were built as productivity features and provenance is an afterthought that becomes expensive to add retrospectively. Recording which code was generated requires marking at acceptance and carrying the mark through edits, which is real engineering nobody prioritised because no developer asked for it. Vendors also have a mild disincentive: a complete provenance record makes the licence exposure question answerable, and answerable is not always favourable. And the enterprise buyers who need it have expressed the requirement as contractual assurance rather than as a product capability, which lets vendors satisfy it with language.

## What to Build
Provenance as a durable property of the code. Mark generated regions at acceptance, with the model, its version, the prompt context summary and the policy state in force, and carry the marking through subsequent edits with decay as the human rewrites it — so the record degrades honestly rather than claiming certainty it does not have. Retain the record with the repository rather than in vendor telemetry, since an audit answer that depends on a vendor's logs is not an answer the enterprise controls. Check generated output against public code corpora at generation time and record the result, which turns a filter into evidence. Attach the policy state, so the organisation can show which controls were active for which repository at which time. Make the whole thing queryable: what proportion of this component is generated, from which models, with what public-match findings — which is the question that arrives in security reviews and currently has no answer. And support retrospective reconstruction where the marking was not in place, using stylometric and structural signals with honest confidence, since every organisation has a period before this existed.

## Target Customer
Chief information security officers and legal functions in regulated industries, platform engineering teams deploying assistants at scale, and the assistant vendors whose enterprise deals stall on exactly this.

## Impact If Built
Provenance is the question that blocks enterprise deployment and it is answered today with contractual language rather than evidence. Marking at acceptance is cheap and impossible to retrofit, which makes every quarter of delay permanently lossy for the code written in it.
