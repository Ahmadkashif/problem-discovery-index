# Fix: The Policy Describes a Company That Does Not Exist

**Niche:** Policy & Document Management
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Policies generated from templates describe practices the organisation never adopted, everyone signs them, and they become the standard the organisation will be held to.
**Tags:** #evaluation-metrics #compliance #confidence-intervals #worker-facing #data-integration #workflow-orchestration
**Contested on:** Whether the policy set describes how the organisation actually operates, or is a document library maintained because an auditor will ask for it.

## The Problem

A company pursuing its first certification uses the platform's policy templates. Fifteen documents are generated, lightly edited to insert the company name and a few specifics, approved by someone senior, and distributed for acknowledgement.

The templates describe a well-run organisation of a certain size. They specify a change advisory board, quarterly access reviews with documented approval, annual disaster recovery testing, a formal risk register reviewed by a committee, and incident response with defined severity tiers and communication trees.

The company has forty people. It does some of this informally and some of it not at all. Nobody reads the documents carefully enough to notice, because reading fifteen policies carefully is a day's work and the purpose of the exercise was to have them.

Now the organisation has documented commitments it does not meet. In an audit this is a finding if anyone checks. In an incident it is worse: a written statement that the organisation would do something it did not do, produced during investigation, read by a regulator or a plaintiff. The document intended to demonstrate diligence becomes evidence of a known unmet obligation.

## Why It's Still Broken

**Templates are how certification gets accelerated.** The platforms supply them because writing fifteen policies from scratch is a real barrier, and they genuinely help. The cost is that they describe a generic organisation.

**Nobody reads them closely.** The approver is senior and busy, the staff acknowledging them are scrolling, and the auditor checks existence, approval and currency rather than accuracy.

**Editing them down looks like weakening them.** Removing a commitment the company does not meet feels like lowering standards, when it is actually making the document honest. Nobody wants to be the person who removed the disaster recovery testing requirement.

**Auditors rarely test policy against practice.** An audit samples control evidence and checks that policies exist and are current. Whether the policy's specific claims hold is not usually tested directly, so the divergence survives.

**The liability is deferred and abstract.** The risk materialises only in an incident or a dispute, which is exactly the kind of deferred cost organisations discount heavily.

**Nothing compares document to reality.** The platform holds both the policies and the control state and does not check one against the other, so the divergence is undetectable by design.

## What a Fix Looks Like

**Read the templates once, properly, and cut what is not true.** A day of work at the start, removing or adjusting every commitment the organisation does not actually meet. This is the whole fix and it is available to any organisation immediately.

**Write what you do, not what a template says.** A shorter policy accurately describing a forty-person company's actual practice is a better document than a long one describing a company that does not exist — better for the auditor, better for staff, and vastly better in an incident.

**Check the specific claims against control state.** Where the policy says quarterly and the data says five-monthly, fix one of them. The comparison is available inside the platform and nobody performs it.

**Review when practice changes, not only annually.** A policy that describes a process the team stopped following six months ago is the common case, and change-triggered review is the only cadence that catches it.

**Make approval mean reading.** The approver should be confirming that the document describes the organisation, which requires them to have read it. Approval as a signature on an unread template is the moment the problem is created.

**Retire policies that describe nothing.** The policy set grows monotonically because removing a document requires justification. An annual cull of documents that describe no actual practice would shrink the set to something people might read.

**Ask the auditor to test accuracy.** An organisation that invites its auditor to check policy against practice gets a real finding early, when it is cheap, rather than a discovery during an incident.

## Who Feels the Pain

The organisation, holding documented commitments it does not meet, which is a worse position than having no policy at all and is created by the act of trying to be compliant.

Staff, acknowledging documents that describe procedures nobody follows, which teaches them that the compliance apparatus is not to be taken literally — an attitude that then applies to the parts that matter.

The compliance manager, who often knows the policies overstate reality and lacks the standing to propose cutting commitments a leader approved.

And the organisation again, in an incident, when the policy is read back to them by someone with an interest in the gap.

## Impact If Fixed

Reading the templates once and cutting what is untrue costs a day and removes a real, deferred liability that most organisations do not know they have taken on.

A shorter, accurate policy set is better on every dimension that matters — more likely to be read, easier to maintain, more defensible under scrutiny, and a truer description of the organisation.

And checking policy claims against control state is a comparison the platform can already make between two things it already holds, which makes its absence a product gap rather than a hard problem.
