# Buy: Developer Experience Practice for Compliance Work

**Niche:** The Engineer Supplying Evidence
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Internal developer platforms spent a decade learning how to ask engineers for things without breaking their week, and compliance still sends tickets from outside the engineering organisation.
**Tags:** #large-language-models #evaluation-metrics #workflow-orchestration #automation #worker-facing #data-integration
**Contested on:** Whether the residual evidence work reaches engineers as a specific, contextualised, one-off task or as recurring interruption.

## The Problem

Getting engineers to do necessary work that is not their primary task is a solved discipline. Platform engineering and developer experience teams have spent a decade on it: meet developers in their existing tools, make the right thing the easy thing, automate the repetitive parts entirely, provide golden paths rather than instructions, give context rather than commands, and measure the friction you are imposing.

Compliance evidence collection does none of it. Requests arrive by email or by a ticket in a tracker the compliance team uses, phrased in framework language, from a person the engineer does not know, about a deadline they did not agree to, with no explanation and no indication of what would satisfy the ask.

The same organisation that carefully designed its deployment pipeline to minimise developer friction sends compliance requests with none of that thinking applied, because compliance sits outside the engineering organisation and was never part of the developer experience conversation.

## What Already Exists

Internal developer platforms: Backstage and its commercial variants — Roadie, Cortex, OpsLevel — with service catalogues, ownership mapping, scorecards, and the ability to surface tasks against services in the developer's own environment.

Scorecard practice: OpsLevel and Cortex in particular have made service maturity scorecards a normal part of engineering life, where a service owner sees what their service is missing and works through it at their own pace.

Developer workflow integration: pull request automation, bots that open issues with full context, chat-based task assignment, and the general pattern of bringing work to where the developer already is.

Policy as code: Open Policy Agent, Conftest and the policy engines that encode requirements as automated checks in the pipeline rather than as requests after the fact.

Service catalogues and ownership: code owners files, catalogue metadata and on-call systems that resolve a service to a responsible person.

## The Customization Gap

**Scorecards are the right model and nobody has pointed them at compliance.** A service scorecard showing that this service is missing a documented access review, alongside its other maturity items, is a far better experience than a ticket from compliance — it is owned by the team, visible continuously, and worked through without a deadline crisis. This is the clearest available adaptation and it is not hard.

**Policy as code eliminates the request entirely where it applies.** A control expressed as an automated check in the pipeline produces evidence continuously and asks nobody for anything. A meaningful share of evidence requests could be converted this way and almost none have been.

**Compliance platforms do not integrate with the developer platform.** The service catalogue knows ownership, dependencies and metadata; the compliance platform maintains its own separate mapping. Joining them would fix routing immediately.

**Golden paths have no compliance equivalent.** Platform teams provide templates where the right configuration is the default. Compliance requirements are communicated as obligations to be met rather than as paths already paved, which is the difference between a control that is satisfied by construction and one that is audited after the fact.

**Friction is measured for deployment and not for compliance.** Developer experience teams measure the time and interruption cost of the workflows they own. Nobody measures what compliance imposes, so it is not managed.

**The two functions do not talk.** The platform team and the compliance team have the same problem — getting engineers to do something consistently — and there is rarely any relationship between them.

## Target Customer

Internal developer platform vendors — Cortex, OpsLevel, Roadie — for whom compliance scorecards are an adjacent capability, a new buyer inside existing accounts, and a natural extension of what they already do.

The compliance platforms, who should be integrating into the developer platform rather than maintaining a parallel ownership model and a separate request channel.

Platform engineering leadership as the internal advocate, since compliance requests are an unmanaged source of interruption in a workflow they are otherwise responsible for.

## Impact If Solved

Compliance work joins the engineering workflow rather than interrupting it, which is exactly the transformation platform engineering achieved for deployment, security scanning and observability.

Service scorecards for compliance would convert a deadline-driven external request into a continuously visible, team-owned item — the same shift that made security findings tractable for engineering teams.

And policy as code would remove a share of evidence requests entirely, which is better than making them easier to answer.
