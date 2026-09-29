# Consent Handled as a Configuration Setting

**Niche:** [[niches/crm-platforms/conversation-intelligence/profile|Conversation Intelligence]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Recording a call with a customer is a legal question that differs by jurisdiction and a trust question everywhere, and it is typically managed by an announcement at the start of the call and a checkbox in an administration screen.
**Tags:** #compliance #descriptive-statistics #evaluation-metrics #workflow-orchestration #automation #confidence-intervals #quick-win #worker-facing
**Contested on:** Every serious competitor in conversation intelligence is fighting to turn a recorded sales call into coaching a manager acts on and deal signal a forecast can use — and whoever converts recordings into acted-upon change takes the account.

## The Problem
A representative dials into a call with participants in four states and two countries. Some of those jurisdictions require all parties to consent to recording; some require only one. The product plays an announcement, which may or may not constitute consent depending on where each participant is, and the representative — who has no idea where anyone is sitting — proceeds. The recording is retained indefinitely, is searchable by anyone in the organisation with access, and may be used in training material shown to people the customer has never met. None of that was explained to the customer beyond an announcement they heard while joining.

## Why It's Still Broken
Consent was treated as a compliance checkbox at purchase, satisfied by an announcement and an administrative setting, and the legal review happened once at procurement rather than continuously at call time. Determining each participant's jurisdiction is genuinely awkward and is the reason the industry settled on a blanket announcement. Retention was never a design decision — recordings accumulate because storage is cheap and nobody specified a policy. And the customer, who is the person with the strongest interest, has no voice in any of it.

## What a Fix Looks Like
Make consent a workflow rather than a setting. Determine the applicable rule from what is knowable — participant location where available, account address, dial-in country — and default to the strictest applicable standard rather than the permissive one, which is both safer and the correct posture. Capture affirmative consent rather than assumed consent where the jurisdiction requires it, which is a prompt rather than an announcement and is entirely feasible in a scheduled call. Give the customer a plain statement of what is recorded, how long it is kept and what it is used for, including internal training use, which most customers have never been told. Set retention deliberately with an expiry, and delete on request. Record the consent basis with the recording, so a later question about a specific call has an answer. And give representatives a clear indication of the recording status and a way to stop it, since they are the ones in the room and are currently the least empowered participant in the decision.

## Who Feels the Pain
Customers recorded and retained under terms they were never told; representatives responsible for a legal determination they cannot make; and the organisation, carrying an exposure that scales with every call it stores.

## Impact If Fixed
Defaulting to the strictest applicable standard and setting a retention policy are both configuration-level changes with immediate risk reduction. The customer-facing disclosure is the part most likely to be resisted and is the one that would most improve the category's standing with the people whose conversations it records.
