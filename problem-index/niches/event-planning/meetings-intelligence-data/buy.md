# Entity Resolution Adapted to Organization Naming Chaos

**Niche:** [[niches/event-planning/meetings-intelligence-data/profile|Meetings & Events Intelligence Data]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The record says a meeting was held by "NW Regional Sales — Acme," and the entire value of the product depends on knowing that this is the same buying organization as "Acme Corporation Meetings" three cities over.
**Tags:** #contrastive-learning #bert #transformers #word-embeddings #graph-neural-networks #random-forests #evaluation-metrics #confidence-intervals #data-integration #automation

## The Problem
Meeting records are captured as whatever a reader board or a source said — a division name, an abbreviation, an association's chapter, an acronym, a booking agency acting for someone else. Resolving those into the account a salesperson can actually pursue is the product, and it is done by researchers using judgment. Errors run both ways and both are damaging: fragmenting one account into six makes it look small and gets it deprioritized, while merging two unrelated organizations sends a salesperson into a call with the wrong history. Consistency between researchers is unmeasured, and account-level history — the thing subscribers pay for — is only as good as the resolution beneath it.

## What Already Exists
Entity resolution is mature and well served. Senzing, Zingg, the enterprise MDM platforms, and firmographic providers like Dun & Bradstreet all handle organization matching with hierarchy awareness, alias handling, and review queues, and integrate with commercial company registries.

## The Customization Gap
Those tools resolve organization names against reference data, which works when the name approximates the legal entity. Here the captured string is frequently a division, a programme name, a chapter, or an intermediary, and the target is not the legal entity but the buying centre — the group that decides where to meet, which may be a division in one company and headquarters in another. No general resolver has a concept of a buying centre. The adaptation is resolution against a meetings-specific organizational model, using signals the general tools do not have: geographic pattern of prior meetings, event type and size consistency, seasonal recurrence, and the intermediary relationships where an agency books repeatedly for the same client. Confidence must be explicit per link, so a salesperson sees where history is firmly attributed and where it is inferred. And association and chapter structures need their own handling, since a national body and its regional chapters are related but are not one account.

## Target Customer
Heads of data operations and research at meetings intelligence providers, and the hotel sales teams whose account histories are only as reliable as the resolution behind them.

## Impact If Solved
Fixes the layer everything else sits on, and makes account history trustworthy in both directions — no phantom small accounts, no wrongly merged ones. Explicit link confidence also lets a salesperson calibrate how hard to lean on a record, which is what they currently do by instinct.
