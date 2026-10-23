# The On-Call Schedule Keyed by Hand

**Industry:** [[answering-services|Telephone Answering Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Who is on call tonight is decided in a hospital scheduling tool, a group text or a practice manager's spreadsheet, and the answering service learns it by fax or email and re-keys it, so a common cause of a failed escalation is a schedule that was right yesterday.
**Tags:** #large-language-models #transformers #data-integration #automation #workflow-orchestration #compliance

## The Problem
An answering service's on-call module holds, for each client, who covers which hours, in what order to escalate, and how to reach them. A twelve-physician group might send next month's rotation as a PDF export from Amion or QGenda; a contractor texts the owner's name for the weekend; a property manager emails a spreadsheet of maintenance technicians by building. Setup staff key it in, usually in advance, and then the swaps start: a physician trades a Saturday, a technician calls in sick, a backup changes mid-shift. Swaps reach the service by phone call to the operator, by an email nobody reads until morning, or not at all.

When the schedule is wrong, the operator pages the off-duty physician, who ignores it or calls back annoyed, while the patient waits. This failure mode is behind the negligence cases: a New York court in 2017 found a service negligent over messages sent to an outdated pager. Night supervisors spend part of every shift resolving "who's actually on" by calling around.

## What Already Exists
Physician scheduling products (Amion, QGenda) and hospital on-call systems manage rotations well and can publish schedules; calendar sync is generic; the TAS platforms have on-call modules with escalation chains and some import capability; secure-messaging apps (Amtelco Secure Messages and its competitors) let clinicians set their own availability status.

## The Customisation Gap
The answering service needs one source of truth per client, kept current without keying. That means connectors to the scheduling tools its clients actually use, and parsing of the PDFs, spreadsheets and emails sent by those that do not. It needs effective-dated rules (this rotation, this swap, this backup chain, these call types to this person), reconciliation that flags conflicts before the shift starts ("two physicians claim Saturday; nobody has Sunday 7 p.m.-midnight"), and a confirmation loop asking the on-call person to acknowledge the shift. The audit trail must show exactly which schedule governed any page. Language models handle the unstructured inputs; the hard part is the effective-dating and the reconciliation logic, which no general calendar tool models.

## Impact If Solved
Removing re-keying saves ~3-6 hours a week of setup-staff keying per 100 medical accounts (estimate) and could cut misdirected pages by ~30-50% (estimate), along with the supervisor time spent chasing coverage at night. Each client gets a pre-shift coverage check it can see, which turns a hidden failure into a visible, fixable one before the first call arrives.
