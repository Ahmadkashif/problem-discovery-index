# The Specialty Evidence Ledger

**Niche:** [[niches/healthcare-practice-software/specialty-ehr-platforms/profile|Specialty EHR Platforms]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** In every specialty the physical evidence that justifies the visit — the image, the slide, the measurement — enters the chart as an attachment and leaves the chart as an attachment, so it can never be joined to the code it was supposed to support.
**Tags:** #object-detection #semantic-segmentation #large-language-models #feature-engineering #evaluation-metrics #data-integration #compliance #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the specialty-specific form of this contest.

## The Problem
Specialty medicine is evidence-dense. An ophthalmologist bills on what an OCT scan shows; a dermatologist bills on what a pathology report says about a specific lesion; an orthopaedist bills on a range-of-motion figure and an implant identifier. In almost every specialty EHR, that evidence arrives as a file. It is viewable, printable and attachable to a claim if a payer asks, and it is not data. The consequence is that the specialty's central fact and the specialty's billing structure live in different layers of the product, joined by a human who retypes one into the other and occasionally gets it wrong in a way that becomes a denial, an amended claim, or in the worst case a laterality error in a chart.

## Why Nobody Has Built This
The vendors are competing on interface *count*, which is a number a buyer can compare in a demo, and structuring an inbound artefact is invisible in a demo. Structuring is also genuinely hard in a specialty-specific way: the artefact formats are proprietary or semi-standard, the device manufacturers have no commercial reason to help, and extracting a measurement from a vendor-specific report requires per-device work that does not amortise across specialties. And the incumbents' template libraries are their moat, so the roadmap conversation always resolves toward more templates. The decomposition below exists because a single generic "evidence ledger" is the same mistake at the product level — the work only pays when it is done to the depth of one specialty's chain.

## What to Build
An evidence ledger that treats each inbound artefact as a first-class clinical object: parsed to the measurement or finding level, bound to the anatomical site and laterality it concerns, timestamped against the encounter, and linked forward to the codes it supports and backward to the order that produced it. It exposes the state of every open loop — what was ordered, what has returned, what has been acted on — and it drives the claim rather than sitting beside it. Built properly, the coding follows the evidence automatically and the chart becomes queryable across the practice's history for the first time.

## Target Customer
Specialty EHR vendors defending a physician-owner base against horizontal platforms, and the larger specialty groups and management-services organisations that have the volume to demand it.

## Impact If Built
Eliminating the retype step removes an error class that produces both denials and clinical risk, and converting attachments to data makes the practice's own history searchable — which is the precondition for every downstream analytic the vendor has promised and not shipped. The competitive effect is larger than the operational one: evidence structuring is the first capability in this niche that a competitor cannot match by adding another interface to a list.
