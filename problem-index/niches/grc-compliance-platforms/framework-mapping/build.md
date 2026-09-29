# Build: One Control Set, Many Frameworks

**Niche:** Framework Mapping & Crosswalks
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A canonical control set with maintained, granular mappings to every framework, so an organisation implements once and demonstrates many times — including through framework revisions.
**Tags:** #bert #large-language-models #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Whether an organisation pursuing several frameworks implements one control set once, or implements substantially the same things repeatedly.

## The Problem

Frameworks overlap heavily and express themselves differently. One asks that logical access be restricted to authorised users. Another requires role-based access control with documented approval. A third specifies least privilege with periodic review. These are, operationally, largely the same control with different emphasis, and an organisation satisfying any of them well has substantially satisfied the others.

The apparatus does not reflect that. The organisation implements for its first framework, then works through the second framework's checklist finding that most items are nearly satisfied and each needs some adjustment, different evidence framing or an additional artefact. The reconciliation lives in a spreadsheet mapping one framework's control identifiers to another's, obtained from a consultant or a standards body, accurate on the day it was made.

Then a framework revises. Controls are renumbered, merged, split and reworded. The spreadsheet is now wrong in ways nobody can enumerate without reading both versions side by side, and the work of determining what actually changed for this organisation falls on one compliance manager with a document comparison.

The frameworks are public, stable texts. The mapping between them is a semantic problem over a fixed corpus, which is exactly the kind of problem that has become tractable and that nobody has properly attacked.

## Why Nobody Has Built This

**Mappings are a moat.** Platforms maintain mapping tables as proprietary assets and multi-framework support is a selling point. A shared, open, high-quality mapping would commoditise something several vendors charge for.

**The relationships are genuinely messy.** Requirements map partially, conditionally and many-to-many. A control may satisfy one framework's requirement fully and another's only under certain conditions. Representing that properly is harder than a lookup table, and lookup tables are what exist because they are what fits a spreadsheet.

**Evidence sufficiency differs even where requirements match.** Two frameworks can ask for the same control and expect different evidence — one accepts a configuration screenshot, another wants a documented review with approvals. Mapping requirements without mapping evidence expectations leaves the work in place.

**Auditor judgement is the final arbiter.** Whether evidence satisfies a requirement is an auditor's call, varying by firm and individual. A mapping that says the requirement is satisfied cannot bind the auditor, so the organisation hedges by doing the extra work anyway.

**Revision cadences are unsynchronised.** Frameworks revise independently, which means maintenance is continuous rather than periodic, and continuous maintenance of a semantic artefact is expensive and unglamorous.

**Nobody owns the canonical set.** The common control frameworks that exist are maintained by small organisations or consortia with limited resources relative to the scope, and none has become the default.

## What to Build

**A canonical control set defined by operational intent.** Not by any framework's numbering — by what is actually being done: this configuration enforced, this review performed at this cadence, this record retained. Frameworks then map onto it rather than the reverse, which is the structural inversion that makes the whole thing work.

**Granular, typed mappings.** Full satisfaction, partial satisfaction with a stated remainder, conditional satisfaction with the condition named. A requirement satisfied only if the control is implemented in a particular way should say so. This is the detail that makes a mapping usable rather than indicative.

**Map evidence expectations, not just requirements.** Per framework and per requirement, what evidence is actually expected and in what form. Where two frameworks accept the same artefact, say so; where they do not, name the difference. This is where the duplicated work actually lives.

**Maintain through revisions semi-automatically.** When a framework publishes a revision, compute the diff against the prior version, propose mapping updates from the changed text, and route them for expert review. The proposal is automatable over a stable public corpus; the review is not, and the combination is what makes continuous maintenance affordable.

**Report the delta per organisation.** At revision, tell each organisation which of its existing controls are affected and what specifically changed for them. Today this is a compliance manager reading two documents.

**Price the next framework.** Given the current control set, what adding a new framework would genuinely require — the controls already satisfied, the partial ones, and the genuinely new. Organisations make this decision commercially, with no basis, all the time.

**Open the canonical set.** Its value is in adoption and in auditors recognising it. A proprietary mapping that auditors do not accept saves nobody any work, which argues for an open standard with commercial products built on top.

## Target Customer

The compliance platforms, for whom a genuinely unified control model is a real differentiator over parallel checklists — though the open-mapping argument cuts against their current position.

Organisations pursuing four or more frameworks, where the duplication is largest and the compliance function is smallest relative to the work.

Standards bodies and the existing common-framework maintainers, who have the legitimacy and lack the resources, and for whom automated revision diffing would multiply their capacity.

## Impact If Built

The consolidation the category has promised for a decade would actually happen. Implement once, demonstrate many times, is achievable and currently is not.

Evidence expectation mapping addresses where the duplicated effort really sits — organisations mostly do not re-implement controls, they re-evidence them.

And automated revision diffing would remove the recurring shock that currently accompanies every framework update, where a small team reads two long documents to work out what changed for them.
