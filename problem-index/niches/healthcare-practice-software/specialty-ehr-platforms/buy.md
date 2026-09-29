# Horizontal EHR Verticalised Without a Template Library

**Niche:** [[niches/healthcare-practice-software/specialty-ehr-platforms/profile|Specialty EHR Platforms]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Horizontal ambulatory platforms already have the claims engine, the scheduler and the patient portal a specialty practice needs, and lose the account anyway over a documentation experience that a configuration layer could supply.
**Tags:** #large-language-models #transformers #feature-engineering #evaluation-metrics #workflow-orchestration #data-integration #automation #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the specialty-specific form of this contest.

## The Problem
A dermatology practice evaluating athenahealth against ModMed is not comparing claims engines; the horizontal platform's is probably better. It is comparing what the first six weeks feel like. On the specialty platform, the lesion map, the cryotherapy template and the path-result workflow are already there. On the horizontal platform, someone has to build them, and that someone is a practice manager with no time. The account goes to the specialty vendor, and the horizontal vendor concludes it needs a specialty template library — a multi-year content investment that is stale the year it ships.

## What Already Exists
Every major horizontal platform ships a template builder, a form designer and a configuration layer, and all of them are used by a minority of customers because building a good template requires knowing both the specialty and the tool. Third-party template marketplaces exist and are thin. Ambient documentation vendors — Abridge, Nuance DAX, Suki — have taken a large share of the note-writing problem out of the template layer entirely, which is the development that makes this adaptation newly viable, and which the incumbents have mostly answered by reselling rather than by rethinking what a template is for.

## The Customization Gap
The adaptation is to stop shipping templates and start generating the structure from the practice's own record. It requires: (1) ingesting a candidate practice's historical notes, orders and claims during evaluation, and inferring the discrete fields that practice actually populates — which is a far smaller set than any published specialty template; (2) generating the capture surface from that inference and letting the physician correct it in use rather than in a configuration screen; (3) mapping the inferred structure to the specialty's coding requirements so that the fields which drive reimbursement are never the optional ones; (4) treating ambient capture as the default input and the structured field as the derived artefact, which inverts the current relationship; and (5) measuring success on time-to-document rather than on template count, because that is the number the physician-owner is actually deciding on.

## Target Customer
Horizontal ambulatory vendors losing specialty accounts they should win on platform strength, and specialty groups on a horizontal platform who have given up on configuration and are documenting in free text.

## Impact If Solved
A horizontal vendor that can stand a specialty practice up in days rather than months competes on its actual strengths — claims, scale, integration breadth — instead of on a content library it will always lose. For the practice, inferring structure from its own history rather than adopting a published template typically cuts the field set by half while raising the share of encounters documented discretely, which is the combination that makes structured capture survive contact with clinic.
