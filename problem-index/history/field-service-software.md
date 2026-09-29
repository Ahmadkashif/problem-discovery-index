# History: Field Service Software

**Industry:** [[industries/field-service-software|Field Service Software]]
**Primary Wave:** [[series/eras/wave-08-mobile-gps|8 — Mobile & GPS]]
**Secondary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Origin Parent:** *(none)* — see below
**Episode Tier:** 1
**Transferable Pattern:** A tool built to solve the dispatcher's problem — matching a job to a person — creates, as an unavoidable by-product, a continuous record of where the technician was and how long each task took. Nobody had to intend the surveillance for it to arrive.

> **Origin Parent — omitted.** No industry in `origins/` bequeathed this one anything specific. Field service platforms descend from the general logic of scheduling and dispatch software, which this vault's earlier waves cover generically (departmental systems, client-server ERP), but no single origin industry names field service as a child in its `legacy.md`. This is a category built directly by three vendors within the span this vault covers, not inherited from an earlier one.

> **Template note.** This is the industry the brief for this batch predicted would have **no contest and no corpse**, and the prediction holds. There is no fight to narrate and nothing has died. The absence is the finding, not a gap in the research.

## Before

A field service business — HVAC, plumbing, electrical, garage-door, pest control — ran its dispatch on a literal board: index cards or magnets on a whiteboard, one per job, moved by hand as a dispatcher matched a customer's call to a technician's remaining day. Price books lived in binders, one per trade, updated by hand when a supplier's cost changed. A completed job was a paper work order, filled in by the technician and turned in at the end of the day or the end of the week, and equipment history — what was serviced last time, and what was found — existed only if someone had thought to write it down and someone else later found the right piece of paper.

## The Origin Event — Three Companies, No Single Date

There is no founding moment to point to, and manufacturing one would misrepresent how this category actually formed. **ServiceTitan was founded in 2007** by Ara Mahdessian and Vahe Kuzoyan, but its cloud platform did not launch until **2012** — a five-year gap between the company existing and the product existing, which is itself worth noting rather than smoothing over. Jobber and Housecall Pro entered the same category later in the decade, aimed at smaller operators than ServiceTitan's enterprise-leaning residential trades focus; this session could not verify precise founding dates for either and does not assert any.

What all of them did, arriving at different times with different target customers, was the same conversion: take the whiteboard and the binder and put them in a browser, with a phone app for the technician standing in for the paper work order. **The mechanism is Wave 6 — cloud economics making a small business a viable SaaS customer.** What makes this a Wave 8 story as well is what the phone app could do that the paper form could not: report the technician's location continuously, timestamp arrival and departure automatically, and attach a photograph to the record without anyone transcribing anything.

## What Became Cheap

Running a multi-technician trades business without a whiteboard, a filing cabinet and someone's memory as the system of record. Scheduling, dispatch, invoicing and payment collection all moved into one searchable system, and — as a direct consequence of the technician carrying a phone rather than a clipboard — the business gained continuous knowledge of where its own workforce was and how long each job actually took, at no additional hardware cost.

## Why There Is No Contest and No Corpse

Dentistry is this project's control case for an industry with no competitive fight; this one is a milder version of the same finding. ServiceTitan, Jobber, Housecall Pro, FieldEdge, ServiceMax and Salesforce Field Service coexist because they serve different segments — enterprise and large residential trades, small and mid-sized operators, and OEM or commercial equipment service, respectively — rather than fighting for the same account. A contractor choosing between them is choosing by business size and trade, not watching one vendor take share from another in a duel. **Nobody's business model here depends on a competitor's failure**, and none of these companies has gone under. There is nothing to narrate as a contest because the market segmented instead of fighting, and there is no graveyard because segmentation does not produce corpses the way a price war does.

## The Trade-Off

The interesting trade in this industry is not commercial, it is structural, and the brief for this batch names it precisely: **this software solved the dispatcher's problem and created a surveillance surface for the technician as a side effect.** But the shape of that surface is different from a gig platform's, and the difference is worth being exact about. A technician here is typically a **W-2 employee of the contracting business**, not an independent contractor of the software vendor. The platform vendor — ServiceTitan or Jobber — sells continuous location, time-on-job and photo-verification data to the **contractor who employs the technician**, not to itself. The asymmetric hold Wave 8 describes elsewhere runs platform-to-worker with no employer in between; here it runs **vendor-to-employer-to-worker**, a three-party chain rather than two, and the employer sits in the middle holding both the legal responsibilities of an employer and a new continuous instrument for supervising the person those responsibilities cover.

That is a materially different situation from a gig platform's deactivation-with-no-appeal problem — a W-2 technician has wage-and-hour law, workers' compensation and, in some trades, union protection that a contractor does not have. But the underlying mechanism — the app that helps a dispatcher plan the day also produces the record a manager uses to evaluate the person who did it — is the same one-directional instrumentation the entire wave is named for, arriving through a business relationship the vault's other Wave 8 industries do not have.

## What's Still Open

- [[problems/field-service-software/high-impact|🔴 First-Time Fix and the Dispatch Match]]
- [[problems/field-service-software/worker-life-1|🟢 Dispatcher Continuous Re-Planning]]
- [[problems/field-service-software/worker-life-2|🟢 Technician Administration at the Truck]]
- [[niches/field-service-software/field-technician-tools/profile|Field Technician Tools]]
- [[niches/field-service-software/equipment-asset-history/profile|Equipment Asset History]]
- [[niches/field-service-software/flat-rate-price-book-content/profile|Flat-Rate Price Book Content]]
- [[niches/field-service-software/residential-trades-platforms/profile|Residential Trades Platforms]]

## The Transferable Pattern

> **Before assuming a monitoring problem is a platform's deliberate choice, check whether an employer sits between the platform and the worker. The instrumentation can be identical and the accountable party can still be completely different — and an FDE who conflates the two will propose a fix aimed at the wrong company.**

Field service software also carries a second, more mundane lesson worth keeping: this vault's own hub note observes that dispatch — "which technician, with which parts, at which time, for this specific job" — remains a person moving cards on a board, digitally, even after every vendor here has offered routing and scheduling optimisation. The tool for encoding a dispatcher's judgement has existed for over a decade and adoption is still described as low, because the judgement being replaced is tacit and the dispatcher does not trust an algorithm with it yet. Availability of a capability and adoption of it are not the same milestone, and the gap between them can be a decade wide even without a regulatory or legal obstacle in the way.

**Sources:** Wikipedia, *ServiceTitan* (founded 2007, platform launched 2012, December 2024 IPO); this vault's `industries/field-service-software.md` and `niches/field-service-software/_overview.md`. Founding dates for Jobber and Housecall Pro were not independently verified this session and are not asserted.
