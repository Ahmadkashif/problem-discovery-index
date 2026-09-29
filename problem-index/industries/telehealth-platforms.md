# Telehealth Platforms

## Profile
**Category:** Platform Labour & Digital Work
**Market Size:** ~$30B US in virtual care delivery, spanning general medical platforms, employer and payer-contracted services, behavioural health, and direct-to-consumer prescribing businesses
**Tech Maturity:** Strong delivery infrastructure, thin clinical measurement. Video visits, asynchronous intake, e-prescribing, scheduling across state licensure and payer integration all work at scale. What the platforms measure is visit volume, wait time, and satisfaction; what they largely do not measure is whether the patient got better.
**Workforce:** Physicians, nurse practitioners, physician assistants and therapists — many working as contractors across several platforms; care coordinators and patient support; clinical operations and quality staff; licensure and credentialing teams

## Key Pain Themes
Clinicians on these platforms work to throughput expectations. Visits are short, frequently asynchronous, and the volume targets are set against a business model with thin per-visit economics. A clinician deciding whether to prescribe, refer or reassure is doing so from a questionnaire and a short interaction, without the longitudinal record and without the physical examination, and the platform's metrics reward the visit closing rather than the problem resolving.

Prescribing is where this became a public issue. Direct-to-consumer platforms that combine a subscription, a short assessment and a prescription have faced federal scrutiny and enforcement, particularly around controlled substances, and the regulatory position on remote prescribing of controlled substances has been repeatedly extended rather than settled. Clinicians working on these platforms sit inside a commercial structure whose revenue depends on a prescription being written and a professional obligation that does not.

The third theme is fragmentation of the record. A patient may see a different clinician each visit, on a platform that does not connect to their primary care record, for a problem that has a history the clinician cannot see. Continuity is the thing virtual care is worst at and the thing most conditions require.

## Current Tech Landscape
Video and asynchronous visit infrastructure is mature. E-prescribing runs through Surescripts and equivalent networks. Scheduling systems handle multi-state licensure matching, which is a substantial constraint since a clinician can only see patients in states where they are licensed. Electronic health records at these platforms are typically purpose-built and interoperate poorly with external systems; information exchange through national networks exists and is inconsistently used. Payer integration and eligibility checking are standard for insured models. Remote monitoring device integration is growing in chronic care programmes.

## Problems
- [[problems/telehealth-platforms/high-impact|🔴 High Impact: The Visit Closes and Nobody Measures Whether the Patient Got Better]]
- [[problems/telehealth-platforms/low-impact-1|🟡 Low Impact: Licensure, Scheduling and Clinician Supply Matching]]
- [[problems/telehealth-platforms/low-impact-2|🟡 Low Impact: Intake, Documentation and Coding]]
- [[problems/telehealth-platforms/worker-life-1|🟢 Worker Life: The Clinician on a Visit Quota]]
- [[problems/telehealth-platforms/worker-life-2|🟢 Worker Life: The Care Coordinator Between Systems That Do Not Talk]]
- [[problems/telehealth-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/telehealth-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Telehealth platforms have the structural advantage of a complete digital record of every interaction and the structural disadvantage of seeing patients in episodes rather than over time. What they measure reflects the business rather than the medicine: visits completed, time to appointment, satisfaction scores. Whether the symptom resolved, whether the patient ended up in an emergency department a week later, whether the prescription was refilled or abandoned — all of that is either in the platform's own data or obtainable through claims and exchange networks, and is not systematically examined. A platform that measured resolution rather than throughput would be able to defend its clinical model in a regulatory environment that is increasingly asking, and would give its clinicians the one thing they currently lack, which is any feedback on whether their decisions were right.
