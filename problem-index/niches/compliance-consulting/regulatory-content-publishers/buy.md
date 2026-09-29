# Change Monitoring Adapted to Sub-Regulatory Guidance

**Niche:** [[niches/compliance-consulting/regulatory-content-publishers/profile|Regulatory Intelligence Publishers]]
**Industry:** [[industries/compliance-consulting|Compliance Consulting]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Regulatory tracking tools cover formal rulemaking well and miss the speech, the FAQ update, and the enforcement action — which is where the real change in supervisory expectation actually happens.
**Tags:** #bert #transformers #large-language-models #transfer-learning #change-point-detection #word-embeddings #evaluation-metrics #automation #compliance #data-integration

## The Problem
Formal rulemaking is the visible tip of regulatory change and the smaller part of what compliance teams have to respond to. Supervisory expectation shifts through examination manual updates, FAQ revisions, no-action positions, enforcement actions whose theory is novel, and speeches by officials that signal a change in posture. Those arrive irregularly, in unstructured form, sometimes with no notification at all — an agency quietly updating a page. The publisher's analysts monitor them by watching sources manually, which forces prioritization by agency prominence, so coverage of the largest regulators is strong and coverage of the specialist and state-level bodies is thin. Those are exactly where a subscriber gets caught out.

## What Already Exists
Regulatory change management is a real product category. Thomson Reuters, Wolters Kluwer's own tooling, Compliance.ai, and Ascent all monitor federal registers and major agency feeds, classify by topic, and route to owners. Legislative tracking covers state bills well. Document change detection is commodity infrastructure.

## The Customization Gap
Those products are built around structured, well-published sources with notification mechanisms, and their coverage reflects it — formal rulemaking is tracked comprehensively, sub-regulatory material patchily, and web-published changes with no notice barely at all. Classification is also generic: a change tagged "consumer protection" is useless when the editorially relevant question is which specific obligation it modifies. The adaptation is coverage engineered for unstructured and unannounced sources — monitoring pages, manuals, FAQs, and enforcement dockets as first-class inputs with change detection tuned to substantive rather than cosmetic edits — combined with classification against the publisher's own obligation taxonomy rather than a topic tree. Enforcement actions need particular treatment, since the interpretively important content is the theory of liability rather than the facts, and extracting it requires reading the action the way an analyst does. Because these sources are unreliable, coverage completeness must be estimated and reported rather than assumed: the system should say which sources and jurisdictions it is confident it is catching, which is a question no current tool asks.

## Target Customer
Directors of regulatory content and coverage leads at intelligence publishers, and the analysts who currently choose which agencies to watch closely because they cannot watch all of them.

## Impact If Solved
Extends reliable coverage into the sub-regulatory space where supervisory expectation actually moves and where every competitor is equally thin. Measured completeness also converts an implicit promise into a stated one, which is the claim a compliance officer most wants before relying on a monitoring service.
