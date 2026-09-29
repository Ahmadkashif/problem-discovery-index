# Fix: The Password Was Never Changed

**Niche:** [[niches/virtual-assistant-services/access-and-security/profile|Access, Credentials & Data Security]]
**Industry:** [[industries/virtual-assistant-services|Virtual Assistant Services]]
**Type:** Fix (Pain Point)
**One-liner:** A placement ends, the assistant is asked to stop using the accounts, and nobody revokes anything.
**Tags:** #compliance #descriptive-statistics #workflow-orchestration #evaluation-metrics #confidence-intervals #quick-win #automation #data-integration
**Contested on:** Whether ending a placement will trigger an actual revocation rather than a request.

## The Problem

A placement ends — a replacement, a resignation, a client cancelling. The account manager thanks the assistant, the assistant stops working, and the accounts remain as they were.

The executive's password is known to a former contractor, indefinitely. The shared vault entry is still active. The guest account, where one exists, is still enabled. The travel site login, the expense tool, the CRM, the scheduling tool — all still work. Changing the executive's password disrupts the executive, so it is deferred and then forgotten.

Nobody has malicious intent and that is not the point. Credentials to an executive's mailbox and calendar remain live with a former contractor in another jurisdiction, and neither the client's security function nor the agency has a record of what was granted or any confirmation that it was removed.

## Why It's Still Broken

Offboarding depends on someone remembering, at a moment when the relationship is ending and often ending awkwardly. There is no list of what was granted, because nothing recorded the grants — they happened one at a time, in messages, over months.

Changing the executive's own password has a real cost to the executive, which is enough friction to defer it indefinitely.

And responsibility is genuinely unclear. The agency does not own the client's systems. The client's IT does not know about the arrangement. The executive assumes the agency handles it. The assistant has no standing to insist their own access be removed, though many would prefer it.

## What a Fix Looks Like

Keep a list, and make the list the offboarding checklist.

Record every access grant at the moment it is made: system, level, how it was granted, by whom, on what date. Ten seconds per grant, maintained by the assistant or the account manager, and it is the single artefact that makes offboarding possible. Without it, revocation is guesswork.

Review it at intervals. A quarterly look at the list catches the grants that accumulated for a one-off task and were never removed, which is most of the surplus.

Trigger revocation from the placement lifecycle. Ending a placement in the agency's system produces the checklist with every item to be revoked, assigned, with a confirmation required per item and a completion record. This is workflow and it is the whole fix.

Prefer delegated access precisely because it revokes cleanly. Where the assistant has their own identity with delegated rights, offboarding is one action and is verifiable. Where they have the executive's password, it requires a password change and there is no way to confirm the credential is not retained. Migrating the highest-risk systems to delegation is worth doing for this reason alone.

Confirm to the client. A short completion record — these accesses existed, these were revoked, on this date — closes the loop, is the kind of thing a client's security function asks for, and takes a minute to produce from the checklist.

And do it for every placement end, including the friendly ones. The awkward departures are handled carefully; the amicable ones are where access quietly persists.

## Who Feels the Pain

Clients, carrying live credentials to executive systems held by former contractors they no longer have a relationship with, usually without knowing. Executives, who will be the ones asked about it if anything happens. Assistants, who retain access they do not want and have no way to be sure it has been removed. And agencies, who will own the consequences of an incident on an access path they never documented.

## Impact If Fixed

Access ends when the placement does, verifiably. The client gets a record of what existed and what was removed. And the most serious risk this industry carries — which is real, ongoing and mostly invisible to the people who would care about it — gets closed with a checklist and a workflow trigger.
