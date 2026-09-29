# Buy: Employee Self-Service Adapted to a Worker With Two Employers

**Niche:** [[niches/remote-work-infrastructure/the-eor-worker/profile|The EOR-Employed Worker]]
**Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Employee self-service portals serve a worker with one employer whose HR team they can walk to; here there are two organisations and neither answers employment questions.
**Tags:** #compliance #data-integration #workflow-orchestration #large-language-models #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Whether self-service tooling built for a single-employer relationship can serve a split one.

## The Problem

Employee self-service is standard HR functionality. Payslips, documents, leave requests, personal detail updates, benefit enrolment, policy libraries and a help centre are available in every HRIS and are reasonably good.

They assume one employer, one HR function, one policy set and one jurisdiction. Here the worker has a legal employer in their own country whose HR function is a platform they have never met, a de facto employer abroad with its own policies that are not their terms, and statutory entitlements from a third source — their own country's law — that neither organisation's policy library describes.

## What Already Exists

HRIS self-service portals. Document and payslip delivery. Leave request workflows. Policy libraries and help centres. HR case management with ticketing. Multilingual interfaces in the larger products. Benefit enrolment portals.

## The Customization Gap

**Two organisations and the responsibilities must be explicit.** The portal has to say, for every topic, which entity is responsible and how to reach them. A single help centre implies a single employer and produces exactly the confusion the arrangement creates.

**Statutory entitlement is a third source and no policy library holds it.** The worker's rights under their own law sit alongside the employer's policy and the client's practice, and the portal must present all three with the applicable one identified. Policy libraries hold documents the employer wrote.

**The content must be per-jurisdiction and per-worker, generated.** A policy library with sixty country documents is unusable. A generated summary of this worker's own position, from their jurisdiction and tenure, in their language, is what is needed — and generative assembly from the rule base makes it affordable.

**Case routing must know which entity owns the question.** A query about a payslip goes to the legal employer; one about a performance review goes to the client; one about statutory severance goes to compliance. Generic ticketing routes everything to one queue, which is where these queries currently die.

**The relationship can end for reasons unrelated to the worker.** Self-service portals have offboarding flows triggered by an employment decision. Here the client contract ending terminates the employment, and the worker needs to understand that risk in advance — a concept no HR portal models.

## Target Customer

Platforms building worker experience on HRIS self-service and finding it assumes a single employer. Also the HRIS and self-service vendors, for whom the employer-of-record pattern is a growing deployment context their products fit awkwardly.

## Impact If Solved

The portal, document delivery, leave workflow and case machinery get reused, and the two-entity responsibility model, statutory third source, generated per-worker content, entity-aware routing and client-contract fragility get built. Concretely: a worker who can find out who to ask and what the answer is.
