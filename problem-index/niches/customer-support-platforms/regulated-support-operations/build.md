# The Answer With Evidence Attached

**Niche:** [[niches/customer-support-platforms/regulated-support-operations/profile|Regulated Support Operations]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Regulated organisations cannot deploy automated answering because they cannot demonstrate an answer was accurate and appropriate, which is a verifiability problem rather than a capability one.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor in regulated support is fighting to let an organisation answer with verified accuracy in a domain where being wrong is a compliance event — and whoever makes an automated answer defensible takes the account.

## The Problem
A health insurer's support function receives large volumes of questions about coverage, eligibility and claims status, most of which are deterministic given the member's plan and record. Automating them would improve service and reduce cost substantially. The compliance function declines, correctly, because a wrong answer about coverage affects a member's medical decisions and the organisation cannot demonstrate — before deployment or after an incident — that the system's answers are accurate, consistent with the plan documents and appropriate to the member's situation. The technology is capable. The evidence is absent, and the evidence is what the decision turns on.

## Why Nobody Has Built This
The category's product direction has been resolution volume and cost reduction, measured by non-escalation, which is precisely the wrong proposition for a compliance function. Vendors have sold into regulated buyers on the same terms as everyone else and been refused. Building the verification layer requires treating accuracy as a measured property rather than as an implied one — which is what this industry's first niche argues for generally and which is a requirement rather than an improvement here.

## What to Build
Answering with a verification and evidence layer designed for supervision. Every automated answer is grounded in identified authoritative sources — the plan document, the policy, the tariff, the regulation — with the specific provision cited and retained, so the basis of an answer is a record rather than a reconstruction. Answers are constrained to question classes where the organisation has established, through evaluation against expert-verified references, that accuracy meets a stated threshold — and the threshold is per class, so deterministic eligibility questions may be automated while anything involving judgement or advice is routed to a person by design rather than by chance. Required disclosures are attached by rule and their delivery evidenced. Continuous production evaluation runs against a maintained reference set with results available to the compliance function. And the supervisory evidence pack is a standing artefact: what was asked, what was answered, on what basis, under which version of the model and the content, with what oversight — produced continuously rather than assembled when requested.

## Target Customer
Support platforms selling into regulated sectors, health insurers, financial services and utility support functions, and the compliance and risk functions who currently hold the veto.

## Impact If Built
The regulated sectors have large volumes of deterministic support questions and the lowest automation adoption in the category, entirely because of an evidence gap that is closable. Building verification into the product rather than around it converts a refusal into a controlled deployment, and the per-class accuracy threshold is the mechanism that makes the boundary defensible rather than arbitrary.
