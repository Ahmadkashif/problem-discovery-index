# Build: Scoped, Attributed, Revocable Assistant Access

**Niche:** [[niches/virtual-assistant-services/access-and-security/profile|Access, Credentials & Data Security]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Give the assistant their own identity with delegated, scoped access to what the work needs, logged as theirs and revocable in one action.
**Tags:** #compliance #data-integration #workflow-orchestration #evaluation-metrics #graph-theory #confidence-intervals #automation #worker-facing
**Contested on:** Whether a personal arrangement can be moved onto proper identity infrastructure without making the work harder.

## The Problem

Assistant access is arranged between an executive and an assistant, personally, in a chat message containing a password. It bypasses the client's IT function entirely, which is why it persists — nobody with a security remit is involved in the decision.

The resulting posture has three defects. Access is total rather than scoped, because sharing a credential shares everything behind it. Actions are unattributable, because the log shows the executive. And revocation is a promise, because a password shared once is known permanently and changing it disrupts the executive too.

Add a contractor in another jurisdiction, engaged through an agency, working on a personal device that may be shared, and the arrangement is one most security functions would refuse if asked. They are not asked.

## Why Nobody Has Built This

Because the correct tooling exists and nobody has packaged it for this context. Delegated mailbox and calendar access, guest identities, scoped OAuth grants and password managers with shared vaults are all available and all require someone to set them up, which means someone has to care enough to spend an afternoon on it.

The executive does not, because the shared password works today. The assistant cannot, because they have no standing to demand better. The agency has not, because it is the client's environment. And IT does not know the arrangement exists.

The agency is the party with both the relationship and the recurring interest — this happens with every placement — and the one best positioned to make it standard.

## What to Build

An access provisioning and offboarding capability that an agency can run as part of every placement.

**Give the assistant their own identity.** A guest or contractor account in the client's environment where one exists, with delegated access to the executive's mailbox and calendar rather than the executive's credentials. This is a supported feature of every major platform and it solves attribution and revocation at once.

**Scope by what the work needs.** A checklist mapping task types to the systems and permission levels they require, so access is granted deliberately rather than wholesale. Most assistants need calendar write, delegated mail send, travel booking and expenses — not the whole inbox and not the banking portal.

**Manage credentials where delegation is not possible.** Third-party systems with no delegation support need a shared vault with per-user access, logging and revocation, rather than a password in a chat message. Password managers do this well and cost very little.

**Provision and deprovision as a process.** A placement start triggers a defined provisioning sequence; a placement end triggers a defined revocation sequence with confirmation. Offboarding is where this fails most often and it is pure workflow.

**Log and report.** What the assistant has access to, when it was granted, when it was last used and when it will be reviewed. An access review at each placement anniversary catches the accumulated grants nobody removed.

**Make it the agency's standard.** An agency that provisions properly for every client is doing something no competitor does, it is the easiest thing in this industry to explain to a client's security function, and it is increasingly what a mid-sized client's procurement will ask about.

## Target Customer

Agencies, for whom this is a differentiator with larger clients and a genuine reduction in their own exposure. Also client IT and security functions once they discover the arrangement exists, which usually happens during an audit or an incident.

## Impact If Built

The assistant's actions become attributable, which is the precondition for any audit or incident response. Access becomes scoped rather than total. Offboarding actually removes access. And an arrangement that most security functions would refuse becomes one they can approve — which is what lets agencies serve larger clients at all.
