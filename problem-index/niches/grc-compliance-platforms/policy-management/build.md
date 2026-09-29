# Build: Policies Bound to Controls

**Niche:** Policy & Document Management
**Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Link every policy statement to the control that implements it, so divergence between what the document says and what the systems do is detected rather than discovered at audit.
**Tags:** #bert #large-language-models #word-embeddings #evaluation-metrics #change-point-detection #compliance #automation #data-integration
**Contested on:** Whether the policy set describes how the organisation actually operates, or is a document library maintained because an auditor will ask for it.

## The Problem

An access control policy states that privileged access is reviewed quarterly, that multi-factor authentication is required for all administrative accounts, and that access is revoked within one business day of departure.

The organisation's actual state is observable. The compliance platform knows whether reviews are happening and at what cadence, what proportion of administrative accounts have multi-factor authentication, and how long revocations actually take. It monitors all of it continuously.

Nothing compares the two. The policy is a document in a library; the control state is a dashboard. They can diverge for years without detection, and they do — the policy says one business day because the template said one business day, and revocation actually takes four.

This matters more than it appears. A policy is a statement of what the organisation does, produced to auditors, customers and regulators. A policy the organisation does not follow is worse than no policy: it is documentary evidence of a known and unmet commitment, and in an incident investigation that is precisely the document that gets quoted.

The link between the two layers is the missing piece, and both layers already exist in the same product.

## Why Nobody Has Built This

**Policy is treated as a document problem.** Policy management was built as a document library with workflow, borrowing from HR and legal document practice. Nothing in that lineage suggests connecting a paragraph to a system state.

**The link is semantic and per-statement.** A policy paragraph does not map to a control cleanly. Extracting the checkable assertions from prose and binding each to a control is real work and is more than a document reference.

**Detecting divergence produces findings customers do not want.** A platform reporting that a customer's policy claims something their systems do not do has generated an uncomfortable finding about a document the customer already signed off.

**Templates are the business model.** Platforms supply policy templates to accelerate certification, and templates by construction describe a generic organisation rather than the specific one. Binding them to actual state would reveal how much of the template does not apply.

**Nobody is measured on policy accuracy.** Auditors check that a policy exists, is approved, is current and is acknowledged. Whether it describes reality is largely outside the assessment.

**The fix implies editing policies more often.** Binding policy to state means updating documents when practice changes, which means more frequent approval cycles, which nobody wants.

## What to Build

**Extract checkable assertions from policy text.** Statements containing a commitment with a measurable parameter — a cadence, a threshold, a coverage claim, a time limit. Not every sentence is checkable and a useful fraction is.

**Bind each assertion to a control and its observed state.** The policy says quarterly; the control data says the last three reviews were at five-month intervals. Surface the comparison as part of the policy's status rather than as a separate report.

**Flag divergence continuously.** A policy assertion no longer matched by observed state is a finding — either the practice should change or the policy should. Presenting the choice explicitly is the product, and today neither happens because nobody notices.

**Suggest policy text from actual state.** Where the organisation's real practice is well characterised, propose wording that describes it accurately. A policy generated from observed configuration is far more defensible than one adapted from a template.

**Trigger review from change, not only from the calendar.** When a control's state changes materially, review the policy statements bound to it. Annual review is the wrong cadence for a document that is supposed to describe a changing organisation.

**Tie attestation to the parts that concern the reader.** Rather than acknowledging a fifty-page document, staff confirm the specific obligations that apply to their role. This makes attestation mean something and is a better artefact for the auditor too.

**Identify the unbound remainder.** Policy statements with no corresponding control are either aspirations, manual processes, or things nobody does. Listing them is uncomfortable and is the most honest output the system could produce.

## Target Customer

The compliance platforms, where both layers already exist inside one product and are not connected — this is an integration of their own components rather than a new capability.

Compliance and legal leadership, for whom a policy set that demonstrably matches practice is a materially stronger position in an incident, a regulatory enquiry or a customer dispute.

## Impact If Built

The policy layer stops being decorative. A document set that is continuously checked against system state is a genuine description of the organisation rather than a library maintained for inspection.

Divergence detection converts the most dangerous document in a compliance programme — a written commitment nobody is meeting — from a latent liability into a routine finding.

And generating policy text from observed state would replace template-derived documents describing a generic company with ones describing the actual one, which is both more useful and considerably more defensible.
