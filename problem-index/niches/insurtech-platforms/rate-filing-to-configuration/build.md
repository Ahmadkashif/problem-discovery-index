# The Filing as a Machine-Readable Artefact

**Niche:** [[niches/insurtech-platforms/rate-filing-to-configuration/profile|Rate Filing to Configuration]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A rate filing and a rating engine configuration express the same algorithm in two forms, one written for a regulator and one for a machine, and a specialist translates between them by hand for every state.
**Tags:** #large-language-models #bert #transformers #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in rating technology is fighting to turn an approved filing into working, verified configuration across fifty states without a specialist retyping it — and whoever shortens filing-to-production most takes the account.

## The Problem
An approved filing arrives: a rate manual with base rates by territory and class, a set of multiplicative and additive factors, rules governing their application, minimum premiums, rounding conventions and a dozen state-specific exceptions. A configuration specialist reads it and builds the equivalent in the rating engine over several weeks, then tests sample risks against manually computed expected premiums. The filing said something precise and the configuration is an interpretation of it, and whether the two agree is established by sampling.

## Why Nobody Has Built This
Filings are written for human regulators in prose and tables, with no machine-readable representation, because the regulatory process has never required one. The translation requires understanding rating algebra, which is a specialised skill, and the population that has it is small. There is also an institutional risk aversion that is well founded: a mistranslated rate is a regulatory exposure across every policy written under it, so a carrier faced with the choice between a slow reliable specialist and an automated translation has reasonably chosen the specialist. The answer is to make the automation verifiable rather than to avoid it.

## What to Build
An intermediate representation of a rating algorithm that both sides can be checked against. Extraction reads the filed manual into that representation — base tables, factors, application rules, ordering, rounding, minimums, state exceptions — with every element cited to the page and paragraph it came from, and with genuinely ambiguous provisions flagged rather than resolved. Configuration is then generated from the representation rather than hand-built, and — crucially — existing configuration can be decompiled into the same representation and compared, which is what turns this into a verification tool as well as a generation tool. The comparison is the product: a diff between the filed rate and the production configuration, computed continuously, is the artefact no carrier currently has and every carrier's compliance function would want. The ambiguity flagging matters as much, since a filing that can be read two ways is a real and common situation that a specialist resolves by judgement and that should be surfaced rather than silently decided.

## Target Customer
Carriers filing in multiple states, rating engine and core system vendors, and the rate filing consultancies who currently supply the specialist labour.

## Impact If Built
Filing-to-production time gates every product and pricing change a carrier makes, and it is consumed almost entirely by translation and verification. Generating configuration from an extracted representation compresses weeks into days; the continuous filed-versus-production comparison addresses a compliance exposure that is currently managed by process discipline and by the continued employment of a small number of specialists.
