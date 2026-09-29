# Build: The Exceptions Are the Programme

**Niche:** Programme Operations & Compliance Reporting
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Handle the populations the standard enrolment misses — contractors, shared accounts, field staff, acquired entities — and report coverage honestly rather than reporting completion among the enrolled.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration #automation
**Contested on:** Whether the administrative machinery runs itself, or consumes the awareness manager's week on enrolment, exceptions and evidence.

## The Problem

The programme reports ninety-eight per cent completion. The denominator is the enrolled population, which is everyone in the primary HR system.

Several populations are not in it. Contractors and agency staff, frequently with organisational email and system access, managed through a procurement system rather than HR. Shared and functional accounts used by teams. Field and frontline staff without individual mailboxes. An acquired subsidiary still on its own HR platform. Third-party support staff with privileged access. And people on extended leave who return without enrolment.

Some of these populations are high exposure. A contractor with administrative access is a more attractive target than most employees. A shared account used by a warehouse team is a credential nobody owns.

None of them appears in the denominator, so the completion figure is computed over the part of the workforce the enrolment integration happened to cover. Nobody reports the coverage, so the ninety-eight per cent is read as a statement about the organisation.

Each exception is also a manual case for the awareness manager, which is where a substantial share of their administrative time goes.

## Why Nobody Has Built This

**Enrolment is built around the HR system.** The integration that works covers the population that system holds, and everything else is an exception by construction.

**Contractors belong to procurement, not HR.** The data is in a different system with a different owner and frequently a different structure, and nobody has joined them.

**Coverage reporting produces a worse number.** Reporting completion over the true population rather than the enrolled one reduces the headline, which is the number the compliance obligation is satisfied by.

**Auditors ask about completion, not coverage.** The requirement is that training was delivered to employees, and the auditor checks the completion record rather than asking who is missing.

**Exceptions are individually small.** Each is a handful of people, so each is handled manually and nobody totals them.

**Shared accounts have no individual to train.** Genuinely awkward — the account is used by several people and the training model assumes an individual — and the awkwardness has meant it is ignored rather than solved.

## What to Build

**Enumerate the true population.** Everyone with organisational email or system access, from the identity provider rather than from HR. The identity system knows who can actually log in, which is the population that matters for security training and is frequently larger than the HR roster.

**Reconcile identity against HR and flag the difference.** Accounts with access and no HR record are contractors, shared accounts, service accounts or gaps — and enumerating them is the first time most organisations would see the list.

**Handle contractors as a first-class population.** Integration with the procurement or vendor management system, with assignment on engagement and removal on completion, mirroring the joiner-leaver flow.

**Solve shared accounts explicitly.** Identify the individuals who use them and train those individuals, or state clearly that the account is untrained and treat it as a risk item. The current approach of ignoring them is the one option with no merit.

**Reassign on role change.** A person moving into a high-exposure role should have their assignment updated, which requires watching role changes rather than only joiners and leavers.

**Report coverage alongside completion.** What proportion of the true population is enrolled, stated next to the completion figure. A completion rate without a coverage denominator has the same problem as every other metric in this industry.

**Maintain the audit evidence continuously.** The package the auditor wants should exist at all times rather than being assembled annually, which is a report definition rather than a project.

## Target Customer

Awareness managers and programme operations, for whom exception handling is a large and unrecognised share of administrative time.

Compliance functions, who would recognise immediately that a completion rate over an incomplete population is a weaker assurance than they have been treating it as.

Vendors, for whom identity-based enrolment rather than HR-based enrolment is a modest integration change producing a materially more complete programme.

## Impact If Built

The programme reaches the populations it currently misses, several of which — contractors with privileged access, shared operational accounts — are higher exposure than the average employee.

Enumerating identity against HR is a reconciliation most organisations have never run, and the resulting list is informative well beyond the training programme.

And reporting coverage alongside completion would replace a figure computed over the convenient population with one computed over the real one, which is the same honesty fix that applies throughout this industry.
