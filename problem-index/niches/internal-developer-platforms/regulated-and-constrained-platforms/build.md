# Evidence as a By-Product Rather Than a Project

**Niche:** [[niches/internal-developer-platforms/regulated-and-constrained-platforms/profile|Regulated & Constrained Platforms]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform in a regulated organisation enforces every control the auditor asks about and records none of it in the form the auditor needs, so the evidence is assembled by hand twice a year.
**Tags:** #graph-theory #descriptive-statistics #bert #evaluation-metrics #confidence-intervals #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give a regulated or air-gapped organisation a platform that produces the control evidence as a by-product of shipping — and whoever does that takes those estates, because the compliance burden is where their engineering time actually goes.

## The Problem
A bank's platform enforces that every change is reviewed by somebody other than its author, that deployments to production require an approval from a defined group, that the artefact deployed is the one that was built from the reviewed code, and that the environment's configuration matches its declared state. All four are controls an auditor will test. None is recorded in a form the audit accepts, so twice a year a team spends several weeks extracting evidence from pipeline logs, ticket systems and repository histories, reformatting it, and reconciling the gaps. The controls were enforced perfectly and the evidence is a project.

## Why Nobody Has Built This
Platform tooling was built for organisations where the control requirements are internal preferences rather than external obligations, so evidence was never a design input. Change management systems were built by a different discipline and record approvals rather than enforcement, which means the system of record contains the paperwork and the platform contains the truth. The two are integrated by people re-entering information. And the regulated organisations have built their own glue, which works and is not a product.

## What to Build
Make the platform the system of record for the controls it enforces. Map each control objective to the platform facts that evidence it — reviewer identity distinct from author, approval by an authorised group, artefact provenance from source to deployment, environment state matching declaration — which is the translation layer and is the reusable asset, since the objectives are common across organisations in a sector. Emit evidence continuously in a retained, tamper-evident form rather than assembling it at audit, which turns weeks into an export. Report control coverage and exceptions continuously, so the organisation knows which changes lacked which evidence before the auditor does — which converts findings into fixes. Handle the emergency path explicitly, since every organisation has one and pretending otherwise produces obviously incomplete evidence; recording and justifying exceptions is a stronger position than concealing them. Replace approval gates that add latency without assurance with automated enforcement plus evidence, which is the substantive improvement and requires the evidence to be credible first. Support air-gapped operation properly, with the scheduled import channel the CI niche describes. And present the evidence for an auditor rather than for an engineer, since a record they cannot read will be supplemented by a manual control.

## Target Customer
Platform engineering in banking, insurance, healthcare, government and defence; the compliance automation vendors; and the platform tooling vendors for whom these estates are unaddressed.

## Impact If Built
These organisations enforce the controls automatically and produce the evidence manually, which inverts where the effort should be. The control-to-platform-fact mapping is common within a sector and is the reusable piece, and continuous coverage reporting turns audit findings into pre-audit fixes.
