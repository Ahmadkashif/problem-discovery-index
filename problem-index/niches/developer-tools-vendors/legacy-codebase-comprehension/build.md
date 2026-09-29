# The System Nobody Can Specify

**Niche:** [[niches/developer-tools-vendors/legacy-codebase-comprehension/profile|Legacy Codebase Comprehension]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that has run a business for thirty years encodes thousands of decisions nobody has written down, and every attempt to modernise it begins by discovering that nobody can say what it does.
**Tags:** #large-language-models #graph-theory #transformers #bert #evaluation-metrics #confidence-intervals #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor here is fighting to let an engineer understand and safely change a system written decades ago by people who have left — and whoever does that takes the enterprise, because these estates run the business and nobody dares touch them.

## The Problem
An insurer wants to change how a particular premium adjustment works. The logic lives in a program written in 1994, modified perhaps two hundred times since, containing conditional branches whose purpose is a regulation from 2003, a special case for a book of business acquired in 2008, and a workaround for a data problem that was fixed a decade ago. No documentation describes any of this. The two people who understood it have retired. A change is estimated at nine months, most of which is establishing what the current behaviour is, and the estimate is honest.

## Why Nobody Has Built This
The tooling ecosystem follows developer population and public code, and these languages have neither — they have a large installed base and a small, ageing and largely non-public corpus. Vendors of the underlying platforms have had a captive market with limited incentive to invest in comprehension. Consultancies sell modernisation projects, for which incomplete understanding is not obviously against their interest. And until recently the analysis genuinely was hard: reconstructing intent from code requires reading it the way an experienced maintainer does, which is now far more feasible than it was.

## What to Build
Comprehension as the product, ahead of any modernisation. Build the structural map first: program and job dependencies, data flow through files and databases, entry points and callers, which is mechanical static analysis and is the foundation everything else needs. Extract the decisions the system makes — the conditional logic that constitutes business rules — and present them as an enumerable catalogue rather than as code, since "what does this system decide" is the question every stakeholder asks and no artefact answers. Reconstruct intent where it can be inferred, using the code alongside whatever contextual evidence survives: change history, ticket references in comments, variable naming, the surrounding structure — with the inference marked as inference, because a confident wrong explanation of a thirty-year-old system is dangerous. Identify what is live and what is dead, using runtime evidence where it exists, since these estates carry a large dead fraction nobody can safely remove without proof. Attach each rule to the change that introduced it where history survives, which frequently recovers the reason. And make the whole thing incremental, because a comprehension exercise scoped as a project will be cut exactly as the CLM back-catalogue migration is.

## Target Customer
Banks, insurers, utilities, governments and industrial firms maintaining decades-old systems, the modernisation consultancies serving them, and the platform vendors whose installed base this is.

## Impact If Built
Modernisation programmes fail at a well-documented rate largely because they begin without a specification of what is being replaced, and comprehension is the missing prerequisite rather than a nice-to-have. The decision catalogue is the artefact every stakeholder asks for and nothing currently produces.
