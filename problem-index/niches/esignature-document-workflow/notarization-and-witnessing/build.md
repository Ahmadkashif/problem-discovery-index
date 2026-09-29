# An Act That Will Be Accepted Where It Is Going

**Niche:** [[niches/esignature-document-workflow/notarization-and-witnessing/profile|Notarization & Witnessing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A remote notarization is performed correctly under the notary's state law and is then rejected by the county, registry or counterparty it was destined for, which nobody could check beforehand.
**Tags:** #logistic-regression #graph-theory #bert #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in remote notarization is fighting to produce an act that will be accepted — by the recipient county, registry, court or counterparty — in every jurisdiction the customer transacts in, and whoever has the widest accepted footprint takes the volume.

## The Problem
A document is notarized remotely by a properly commissioned notary following that state's procedure exactly. It is then submitted to a county that does not accept remote acts, or to a registry that requires a specific certificate format, or to a counterparty's counsel who will not accept it on general principle. The act has to be redone in person, sometimes after the transaction has moved on. The signer, the notary and the platform all did everything correctly and the outcome still failed, because acceptance is determined at the destination and nothing told anyone what the destination requires.

## Why Nobody Has Built This
Platforms are built around performing the act and their compliance work stops at the notary's own commissioning state, which is where their legal exposure sits. Acceptance at the destination is the customer's problem by contract. The destination universe is large and heterogeneous — thousands of recording jurisdictions, registries, courts and institutional counterparties — and publishes its requirements inconsistently. And rejections are handled as one-off operational problems rather than as data, so the industry regenerates the same knowledge continuously and never accumulates it.

## What to Build
Destination-aware notarization. Before the act, determine where the document is going and what that destination requires: permissible act types, certificate and seal format, identity-proofing standard, session-recording retention, and any signer-presence condition. Determine whether the combination of signer location, notary commission and document type is permissible at all under the governing state's rules, which is deterministic given maintained rule content. Where the requirements are unknown, say so explicitly and offer the conservative path, rather than proceeding and discovering later — an explicit unknown is a usable answer and a silent assumption is not. Then capture every rejection with its stated reason as structured data, which turns each failure into a permanent improvement and is the mechanism that makes the destination knowledge accumulate rather than evaporate. For witnessing, the same logic applies to a different rule set — witness count, eligibility, presence requirements by instrument type — and it is the more restrictive of the two for estate documents.

## Target Customer
Remote notarization platforms, title and escrow operations, estate planning and legal operations functions, and the lending and corporate secretarial teams whose instruments must be accepted somewhere specific.

## Impact If Built
Acceptance uncertainty is the reason a legally available capability is used in a minority of eligible transactions. Making the destination requirement knowable before the act converts a post-hoc failure into a pre-flight check, and the rejection feedback loop is what makes the knowledge base viable where private spreadsheets have failed.
