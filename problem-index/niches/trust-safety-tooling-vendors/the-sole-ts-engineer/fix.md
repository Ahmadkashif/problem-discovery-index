# Fix: They Do Not Know What They Are Required to Do

**Niche:** The Sole Trust & Safety Engineer
**Industry:** [[industries/trust-safety-tooling-vendors|Trust & Safety Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A generalist learning every harm type at once may not know that some of them carry specific legal obligations with specific timelines, and nothing tells them.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #worker-facing #workflow-orchestration
**Contested on:** Whether one person can own every harm type at a growing platform using tools whose accuracy they cannot verify.

## The Problem

A first trust and safety hire at a growing platform is learning the domain. They are working through abuse, harassment, spam and fraud, building processes, configuring vendor tools and handling a queue.

Some of what they own is not a matter of best practice. Child safety carries specific legal obligations in several jurisdictions — reporting requirements, preservation obligations, timelines, and specific channels — that are not discretionary and whose breach has serious consequences. Regional platform regulation increasingly imposes transparency reporting, notice-and-action processes and redress obligations with deadlines. Law enforcement request handling has its own legal requirements.

Nothing tells them. Vendor materials describe products. Industry conversation covers practice. Their company may have counsel who has never been asked about this because nobody knew to ask. And the first hire, learning six domains at once, may reasonably not know that one of them has a statutory reporting obligation attached.

This is the highest-consequence gap in the role and it is a knowledge gap rather than a capability one. The person would comply immediately if they knew. Nobody has told them.

## Why It's Still Broken

**No obligation map exists for this domain.** Privacy has platforms that tell a company what applies to them. Trust and safety has nothing equivalent a generalist can consult.

**Vendors sell capability, not obligation.** A classification vendor describes detection accuracy, not the legal requirements that attach to what is detected.

**Counsel is not asked.** Legal advises on the questions brought to them, and a first hire who does not know an obligation exists does not bring the question.

**The obligations are jurisdiction-specific and changing.** Platform regulation has expanded rapidly across several jurisdictions, which makes keeping current a specialist task.

**The professional resources assume specialisation.** Guidance written for a child safety specialist assumes they already know the obligations, so a generalist reading it starts from an assumption they do not meet.

**Nobody checks.** There is no moment at which anybody asks a growing platform whether it knows what it is required to do.

## What a Fix Looks Like

**Publish an obligation map for platforms.** By jurisdiction, by platform type, by user base — what a platform is required to do about which harm types, with timelines and channels. A document, maintained, and its absence is the central problem.

**Put the obligations in the vendor product.** A classifier detecting a category with a legal reporting obligation should say so at the point of detection, with the requirement and the channel. This is the intervention that would reach the person at the moment it matters.

**Make it part of onboarding.** A first trust and safety hire should receive a legal obligations briefing in their first week, from counsel, as a standard part of the role's start.

**Ask counsel early.** A platform's legal function should be asked, proactively, what obligations attach to the platform's content and user base. Most have not been asked because nobody framed the question.

**Build it into the professional community's materials.** A new practitioner's guide covering obligations first, before practice, would reach people at the point they most need it.

**Vendors should ask their customers.** A vendor onboarding a small platform could ask whether they have a process for the legally mandated reporting, which would surface the gap immediately and is a question nobody asks.

**Provide the channel details.** Knowing an obligation exists and knowing how to discharge it are different, and the operational detail — which channel, what format, what timeline — should be available in one place.

## Who Feels the Pain

The engineer, who would comply immediately if they knew and does not, and who carries the personal exposure if it surfaces.

The platform, in breach of a legal obligation nobody in the organisation knew applied.

The people the obligation exists to protect, which in the child safety case is the most serious version of this problem in the entire vault.

And the industry, where a known, recurring and entirely addressable knowledge gap persists because no institution has produced the document that would close it.

## Impact If Fixed

An obligation map by jurisdiction and platform type is a maintained document, is the central missing artefact, and is well within the capability of a professional body or a specialist organisation to produce.

Surfacing the obligation in the vendor product at the point of detection is the intervention that reaches the person at the moment it matters, and it is a field in a product.

And a legal obligations briefing in a first hire's first week is free, takes an hour, and addresses the highest-consequence gap in a role that exists at every growing platform.
