# An Independent Cost-to-Complete

**Niche:** [[niches/construction-tech-platforms/owner-side-project-controls/profile|Owner & Developer-Side Project Controls]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An owner's forecast of what a project will finally cost is the contractor's forecast in a different font, and no product produces an estimate from evidence the owner holds independently.
**Tags:** #bayesian-inference #survival-analysis #monte-carlo-methods #gradient-boosting #confidence-intervals #evaluation-metrics #revenue-impact #causal-inference
**Contested on:** Every serious competitor selling to owners is fighting to produce a cost-to-complete and a completion date that do not originate with the contractor being measured — and whoever makes the owner's number independent takes the account.

## The Problem
Month eight of a twenty-month project. The owner asks what it will cost. The answer assembles the contract value, approved changes, pending changes at the contractor's estimate, and a cost-to-complete supplied by the contractor. Every uncertain component in that sum comes from the party whose performance it describes. The owner's own evidence — the pace at which changes have been arriving, the RFI and submittal patterns that precede changes, how similar projects in the owner's portfolio behaved at month eight — is not used, because nothing uses it.

## Why Nobody Has Built This
Owner-side platforms grew out of document control and contract administration, where the discipline is recording what the parties exchanged, and forecasting is a different posture — it means the owner's system asserting a number that disagrees with the contractor's. That is commercially awkward for a vendor selling into a market where owners and contractors sit on the same projects. It also requires data the owner has not historically kept in usable form: past projects' outcomes, change histories and final costs, held per project in closed files rather than as a portfolio dataset. The owners who build repeatedly — institutions, healthcare systems, universities, retail chains — are exactly the ones who could do this and have never assembled the corpus.

## What to Build
A forecast built from the owner's own evidence and the owner's own history. Change order arrival is modelled as a process with a rate that varies by project phase and building type, estimated from the owner's portfolio, so pending and not-yet-raised changes are forecast rather than counted. Leading indicators the owner can see — RFI volume and age, submittal turnaround, design revision activity — feed the rate. Schedule is forecast with the same approach and the two are joined, since time and cost overrun together. The output is a distribution and a contingency sufficiency statement: given where this project is, what is the probability the remaining contingency covers the remaining risk. Divergence from the contractor's forecast is surfaced as a question to raise, with the evidence, rather than as an accusation.

## Target Customer
Institutional owners with recurring capital programmes — healthcare systems, universities, retail and hospitality chains, public agencies — developers with a portfolio, and the owner's representative firms who are paid precisely for independent judgment.

## Impact If Built
An owner who can see a divergence between its own forecast and the contractor's at month eight instead of month sixteen has time to act, which is the entire value of a forecast. For owners with recurring programmes, converting closed project files into a portfolio corpus is a one-time effort that improves every subsequent budget, contingency and schedule they set.
