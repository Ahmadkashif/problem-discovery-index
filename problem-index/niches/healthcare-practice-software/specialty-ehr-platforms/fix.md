# The Interface Count as a Substitute for Interoperability

**Niche:** [[niches/healthcare-practice-software/specialty-ehr-platforms/profile|Specialty EHR Platforms]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Fix (Pain Point)
**One-liner:** Specialty vendors compete on how many device and lab interfaces they ship, a number that says nothing about whether the data arriving through those interfaces is usable, and the practice discovers the difference after go-live.
**Tags:** #evaluation-metrics #descriptive-statistics #hypothesis-testing #data-integration #compliance #workflow-orchestration #quick-win #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the specialty-specific form of this contest.

## The Problem
"Two hundred interfaces" is on every specialty vendor's slide. In the clinic, an interface means one of three very different things: a genuine structured feed where a measurement arrives as a discrete value bound to the right patient, site and encounter; a document feed where a PDF arrives attached to a patient and nothing else; or a fax-to-chart pipeline with a person in the middle. All three count as one. Practices choose vendors on the count, go live, and find that the interfaces they cared about are the second kind. The staff response is a manual reconciliation routine that nobody planned for and nobody budgets, and it becomes permanent.

## Why It's Still Broken
The count is a good sales number and a truthful one, so no vendor has an incentive to publish the breakdown, and no buyer knows to ask for it. On the engineering side, upgrading a document feed to a structured feed requires per-device work with a manufacturer who gains nothing from it, and the work does not generalise. Inside the vendor, interface quality has no owner: integration engineers are measured on connections delivered, support absorbs the consequences, and the two teams' metrics never meet. The result is a category-wide vocabulary problem masquerading as a technical one.

## What a Fix Looks Like
Publish the breakdown and measure the thing. Classify every interface into structured, document-only, or human-in-the-loop, and state it in the contract. Then instrument what actually arrives: for each feed, what share of messages bind to the correct patient and encounter without intervention, what share of expected fields are populated, what the median latency is from source event to chart availability, and how much staff time the reconciliation consumes. That instrumentation is mechanical, requires no modelling, and produces the one artefact this niche lacks — a comparable quality figure per interface, which lets a practice negotiate, lets the vendor prioritise, and lets a device manufacturer see its own feed ranked against its competitors'.

## Who Feels the Pain
Clinical staff running an unbudgeted reconciliation routine; practice managers who bought on a count and cannot explain the gap to the physician-owner; and the vendor's implementation consultants, who know which interfaces are real and are not asked before the contract is signed.

## Impact If Fixed
Instrumenting bind rate and latency across a specialty vendor's interface estate typically shows that a minority of feeds carry the majority of the clinical value and a different minority consume the majority of the reconciliation time — a ranking that reorders an integration roadmap immediately. For practices it converts a demo number into a diligence question. Neither side needs new technology; the measurement simply has to be made and shown.
