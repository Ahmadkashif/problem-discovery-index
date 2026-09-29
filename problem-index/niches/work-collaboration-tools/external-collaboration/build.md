# A Shared Space With Two Organisations' Rules

**Niche:** [[niches/work-collaboration-tools/external-collaboration/profile|External Collaboration]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Collaboration tools model one organisation with one set of rules, and cross-organisational work needs a space where both parties' retention, access and confidentiality obligations apply at once — which is why it happens over email instead.
**Tags:** #graph-theory #compliance #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in external collaboration is fighting to let someone outside the organisation participate properly without a licence, an account provisioning process or a loss of control — and whoever makes the outside party a first-class participant takes the work that currently happens over email.

## The Problem
An agency and a client want to work together on a campaign. The client's tool requires guest accounts, which their security function restricts; the agency's tool is not approved by the client; a shared drive raises questions about whose retention policy applies and who owns the content when the engagement ends. So they use email. Files are attached, versions diverge, decisions are made in threads that only some people are on, and six months later nobody can reconstruct why something was approved. Every tool involved is capable of hosting the work and none of them is capable of hosting a relationship between two organisations that each have obligations.

## Why Nobody Has Built This
The permission and identity models in these products were designed around a single directory and a single administrator, which is the right model for internal work and is structurally incapable of representing two organisations with independent policies. Guest access was bolted on and inherits the host's rules entirely, which is why the guest's organisation frequently will not permit it. And the commercial model works against it: every vendor wants the other organisation to become a customer rather than to participate as an equal, so the incentive is to make external participation just uncomfortable enough.

## What to Build
A shared workspace as a first-class object with two owners. Both organisations' policies apply to content within it, with the more restrictive governing where they conflict — which is the rule professional practice already uses and which no product implements. Membership is federated from each side's own directory, so each organisation manages its own people and neither provisions accounts for the other. Content ownership and disposition on termination is established at creation rather than negotiated at the end, including what each party retains, which is a live and frequently contentious question in professional services. Retention and legal hold apply from both sides independently, which means a document may be held by one party's obligation and aged out by the other's, and the space must represent that rather than pick one. And the record survives the relationship: when an engagement ends, each party retains what they are entitled to in a form they can use, which is the specific need that currently drives everything back to email and attachments.

## Target Customer
Agencies, professional services firms, and any organisation with substantial cross-boundary work; collaboration platform vendors; and the regulated organisations for whom external collaboration is currently blocked entirely.

## Impact If Built
Cross-organisational work is a very large share of professional activity and is conducted with the worst available tooling, for structural reasons that are about permission models rather than about capability. A genuinely two-party workspace would move that work into a managed environment, which benefits both parties' compliance positions as well as their productivity — and the termination provision is the specific thing that makes professional firms willing to try.
