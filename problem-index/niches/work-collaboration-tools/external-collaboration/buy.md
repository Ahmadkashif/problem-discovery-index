# Federated Identity Instead of Guest Accounts

**Niche:** [[niches/work-collaboration-tools/external-collaboration/profile|External Collaboration]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Federated identity has been standard for two decades and lets one organisation trust another's authentication without provisioning accounts, and collaboration products still create a guest account per external person per relationship.
**Tags:** #compliance #data-integration #graph-theory #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor in external collaboration is fighting to let someone outside the organisation participate properly without a licence, an account provisioning process or a loss of control — and whoever makes the outside party a first-class participant takes the work that currently happens over email.

## The Problem
An external collaborator needs access. The host organisation creates a guest account, which means a credential the guest's own organisation does not manage, does not disable when they leave, and cannot include in its own access reviews. The guest maintains yet another login. When they change roles or leave their employer, the guest account persists — which is the orphaned access problem this vault's contingent workforce niche describes, arriving through a different door and at larger scale. Federated identity solves exactly this and is universally deployed for enterprise applications and rarely for collaboration guests.

## What Already Exists
Federation standards and identity providers are mature and universal in enterprise environments. Cross-organisational federation patterns are established, including the business-to-business models offered by the major identity platforms. Just-in-time provisioning, attribute-based access and lifecycle signalling between organisations are all documented. Every component required is standard infrastructure that most of the organisations involved already operate.

## The Customization Gap
The adaptation is to a relationship between organisations of very different sizes and technical maturity. It requires: (1) federation that a small organisation can participate in without an identity platform of its own, since an agency with fifteen people cannot complete an enterprise federation project for each of eleven clients and that is where the current arrangements break; (2) lifecycle signalling in both directions, so that a person leaving either organisation loses access without anyone remembering — which is the single largest security benefit and is the current failure; (3) attribute exchange limited to what the collaboration requires, since federation can carry far more than a host organisation should receive about the other's people; (4) revocation that is immediate and mutual, because a relationship ending should close access from both sides and currently depends on the host remembering; and (5) a clear trust establishment process that a business relationship manager can complete, rather than one requiring two security teams to meet — which is the practical barrier in almost every case.

## Target Customer
Collaboration platform vendors, identity platform vendors for whom this is an adjacent and underserved case, and the professional services firms and agencies who maintain dozens of client-side identities.

## Impact If Solved
Orphaned external access is a well-documented security exposure with an entirely administrative cause, and federation removes it structurally rather than through periodic review. Making federation achievable for a small organisation without its own identity platform is the specific adaptation, and it is what would let the pattern spread beyond enterprise-to-enterprise relationships.
