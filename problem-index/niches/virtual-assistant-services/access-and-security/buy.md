# Buy: Identity and Access Tooling Adapted to a Personal Arrangement

**Niche:** [[niches/virtual-assistant-services/access-and-security/profile|Access, Credentials & Data Security]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Identity and access management is mature and is bought by IT departments; this access is arranged by an executive who will not involve IT.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #confidence-intervals #automation #descriptive-statistics #worker-facing
**Contested on:** Whether enterprise identity tooling can reach an arrangement made privately between two people.

## The Problem

Identity and access management is one of the better-served areas in enterprise software. Directory services, single sign-on, conditional access, privileged access management, guest identities, password managers and access review tooling are all mature and widely deployed.

None of it reaches this arrangement, because the arrangement is made outside the organisation's process. An executive hires an assistant through an agency, shares a password, and IT learns about it during an audit if at all. The tooling is not inadequate; it is unapplied, and the reason is organisational rather than technical.

## What Already Exists

Microsoft Entra and Google Workspace identity, with delegated mailbox and calendar access. Guest and external identity support. Okta and the SSO layer. 1Password, Bitwarden and the business password managers with shared vaults. Privileged access management products. Access review and certification tooling. Device management platforms.

## The Customization Gap

**The buyer is an executive, not IT, and they will not read a configuration guide.** Whatever is deployed must be arranged by the agency on the executive's behalf, in minutes, with the executive approving rather than configuring. The distribution problem is the whole problem and no IAM product addresses it.

**The identity is cross-organisation and cross-agency.** The assistant needs an identity in the client's environment, provided by an agency, potentially for several clients at once. Guest identity handles the first part; managing an assistant's identities across multiple clients from the agency's side has no product.

**Third-party systems without delegation are the majority of the problem.** Travel sites, expense tools, subscription services and small SaaS products mostly have no delegated access model, so a shared vault is the only answer. Mapping which of a client's systems support delegation and which need vaulting is per-client work nobody packages.

**Offboarding must be a single reliable action.** Access review and deprovisioning tooling exists and assumes an HR-triggered joiner-mover-leaver process. Here the trigger is a placement ending, often abruptly, and the process is an account manager remembering. Wiring placement lifecycle to deprovisioning is the integration that matters most.

**The device is personal and often shared.** The assistant works from their own machine, in a household, in another jurisdiction. Device management is either unavailable or disproportionate, and the practical answer is browser-isolated access and vaulted credentials rather than endpoint agents — a posture the MDM-centric products do not offer.

## Target Customer

Agencies wanting a standard access practice they can run for every client, which is both a security improvement and a sales asset with larger buyers. Also the password manager and identity vendors, for whom placed contractors with cross-organisation access are a segment their enterprise model does not reach.

## Impact If Solved

The delegation, vaulting, guest identity and review machinery gets bought, and the executive-friendly provisioning, cross-client identity management, third-party system mapping, placement-triggered offboarding and personal-device posture get built. Concretely: an access arrangement a security function would approve, set up in the same ten minutes that currently produces a password in a chat window.
