# Document Assembly Adapted to Evidence Sufficiency

**Niche:** [[niches/legal-practice-software/immigration-practice-platforms/profile|Immigration Practice Platforms]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document assembly has been solved technology for twenty years and immigration practice uses it to fill forms, which was never the hard part — the hard part is knowing whether the evidence package attached to those forms is sufficient.
**Tags:** #large-language-models #bert #logistic-regression #evaluation-metrics #confidence-intervals #compliance #automation #tacit-knowledge-ml
**Contested on:** Every serious competitor in immigration case management is fighting to keep an open case's forms, evidence set and procedural posture correct when the policy underneath it changes mid-case — and whoever propagates a policy change across an active caseload fastest takes the account.

## The Problem
Filling an I-130 or an I-485 correctly from a client questionnaire is a solved problem that every vendor does adequately. The filing still fails, or generates a request for evidence, because the supporting package was thin: the marriage evidence did not cover the right period, the employment letter did not address the specific criteria, the country conditions documentation was generic where this adjudicator expects specificity. The lawyer's judgment about sufficiency is the whole value of the lawyer, and it is applied from memory of what has worked, case by case, with no record of what actually did.

## What Already Exists
HotDocs, Documate, Afterpattern-descendant tooling and every immigration vendor's native assembly engine handle conditional form generation well. Evidence checklists ship with every product, derived from the published requirements, and are static per case type. USCIS publishes the policy manual and evidentiary standards. Language models capable of assessing whether a document addresses a stated criterion are ordinary now. The generation half is bought; the evaluation half does not exist.

## The Customization Gap
The adaptation is to evaluate the package rather than to generate it. It requires: (1) deriving the evidence requirement from the case's specific facts and current policy rather than from its type, since two marriage-based cases with different histories need materially different packages; (2) assessing each submitted document against the criterion it is meant to satisfy, and reporting what is thin rather than merely what is absent — a checklist marks a box when a file is attached, which is the wrong test; (3) learning from the firm's own outcome history which evidence patterns drew requests for evidence and which did not, per benefit type and, where the data supports it, per service center; (4) surfacing the assessment to the lawyer as a pre-filing review with reasoning, never as a score, since the judgment stays with the lawyer and the consequences fall on the client; and (5) versioning the assessment against the policy in force, so a package reviewed in March is not re-judged in June by a standard that did not exist.

## Target Customer
Immigration firms and nonprofit providers filing at volume, and the case management vendors whose assembly engines already hold the forms and the questionnaire data.

## Impact If Solved
Reducing requests for evidence is the single most valuable outcome in this practice area: each one costs months of a client's life and unbillable firm time on a flat-fee matter. Pre-filing sufficiency review against the firm's own RFE history is achievable with data the firm already generates and currently discards, and it converts a senior lawyer's tacit standard into something a junior can apply.
