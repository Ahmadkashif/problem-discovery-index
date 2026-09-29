# Policy as Code, Applied to Change Control

**Niche:** [[niches/internal-developer-platforms/regulated-and-constrained-platforms/profile|Regulated & Constrained Platforms]]
**Industry:** [[industries/internal-developer-platforms|Internal Developer Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Policy engines evaluate declarative rules before an action takes effect and are standard in cloud security, and regulated change control is implemented as a human clicking approve.
**Tags:** #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #logistic-regression #compliance #automation #workflow-orchestration
**Contested on:** Every serious competitor here is fighting to give a regulated or air-gapped organisation a platform that produces the control evidence as a by-product of shipping — and whoever does that takes those estates, because the compliance burden is where their engineering time actually goes.

## The Problem
Policy-as-code engines evaluate declarative rules against a proposed action and permit or deny it, with the decision and its reasoning recorded. They are standard in cloud security and infrastructure admission control. Regulated change control implements the same idea as a workflow in which a person clicks approve — frequently a person with no ability to evaluate the change — and the evidence is the click.

## What Already Exists
Policy engines with declarative languages and mature tooling; admission control patterns; infrastructure policy scanning; the control frameworks published by regulators and standards bodies; and attestation and provenance mechanisms from the software supply chain world.

## The Customization Gap
The adaptation is to controls an auditor will test. It requires: (1) policies expressed against the control objective rather than against a technical condition, so that the rule's provenance is traceable to the obligation it satisfies — which is what makes the automated control defensible in an audit and is the translation nobody has written down; (2) evidence emission as a first-class output of every policy evaluation, since the decision and its inputs are what the audit needs and are usually discarded after the allow or deny; (3) an exception mechanism with justification and expiry, because regulated environments genuinely need break-glass and an unrecorded exception is the finding that matters most; (4) separation of duties expressed in policy, which is the control auditors test most consistently and is entirely expressible — the author and the approver being distinct identities is a rule, not a workflow; and (5) auditor-legible output, since a policy decision rendered as structured data is evidence only if the auditor can read it, and the translation into their language is part of the product.

## Target Customer
Regulated platform engineering teams, compliance automation vendors, policy engine vendors, and the service management vendors whose change modules this would displace.

## Impact If Solved
Policy engines implement exactly this pattern in an adjacent domain and regulated change control uses a click. Emitting evidence from every policy evaluation and expressing controls against the objective are what make the automated version defensible where the manual one is merely traditional.
