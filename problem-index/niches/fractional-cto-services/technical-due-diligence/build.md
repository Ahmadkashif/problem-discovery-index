# Build: Diligence Under Restricted Access

**Niche:** Technical Due Diligence
**Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An analysis layer that runs inside the seller's boundary, emits only the aggregate findings a diligence needs, and gives the practitioner real evidence without the seller ever handing over the code.
**Tags:** #gradient-boosting #graph-neural-networks #change-point-detection #confidence-intervals #evaluation-metrics #compliance #automation
**Contested on:** Whether a technical opinion formed in two weeks under restricted code access can be made defensible enough to price an eight-figure decision.

## The Problem

The central constraint of technical due diligence is that the practitioner cannot have the thing they need to examine. A seller in a competitive process will not hand a repository to an advisor working for one of several bidders, and often will not hand it over at all until exclusivity. What is offered instead is a supervised session — a screen share, a few hours, questions answered by an engineer the seller selected — plus whatever documents the seller chose to place in the data room.

So the practitioner forms a technical opinion on a system they have seen through a window. They ask good questions and get prepared answers. They read an architecture document written for this process. They look at code for three hours with someone watching. And then they write a report that an investment committee will treat as the technical basis for a price.

Everything that would settle the important questions is inside the boundary and computable. Where change concentrates, whether the coupling makes the roadmap feasible, how much of the system has a single living author, whether delivery throughput has been stable or declining, how the incident record compares to the incident narrative. None of it requires the code to leave. All of it requires an analysis to run where the code is, and for the seller to trust that only the result comes out.

## Why Nobody Has Built This

**The trust problem is the product, and it is not a technical problem.** A seller must believe that a tool running on their crown jewels emits aggregate findings and not source code. Building that belief requires auditable output, a seller-side review gate, contractual structure and, realistically, a track record — none of which a startup has at the moment it most needs it. This is the barrier, and it is why the obvious idea has not been executed.

**Two-sided adoption with an unwilling side.** The buyer of the diligence wants this. The seller has no incentive to make diligence easier — information asymmetry is worth money in a negotiation — and the seller is the party who must install it. Any viable version has to give the seller something they want, and most designs give them nothing.

**Deal timelines punish anything requiring setup.** A diligence window is two weeks and the seller's engineering team is already stretched across the process. A tool requiring a day of their time will be declined, so the whole thing has to run from a clone and an export with effectively zero configuration.

**Incumbent diligence firms sell days.** A firm billing for a senior practitioner's two weeks has a muted interest in an instrument that compresses the evidence-gathering. The buyers who would benefit most — investors — do not currently buy tools, they buy firms.

## What to Build

An analysis package that runs inside the seller's environment and emits a fixed, reviewable set of findings.

**Emission control is the core design.** The output schema is fixed and published: aggregate metrics, distributions, rankings by module path at a declared granularity, and a risk register — never source content, never identifiable individual-level data, never anything free-form. The seller sees the complete output before it is released and can withhold it. Publishing the schema and open-sourcing the emission layer is the only realistic route to the trust the product requires; the value is in the analysis and the interpretation, not in the secrecy of what it sends.

**The findings a diligence actually needs.** Effort concentration and its match against the growth plan. Temporal coupling, which is what determines whether the post-acquisition roadmap is feasible or whether every change touches everything. Knowledge concentration — components with a single living author, stated as a bus-factor register, which is the risk most often raised and least often measured. Delivery throughput and its trend, which is the honest version of "the team is executing well." Dependency and licence exposure, where the machine answer is already the accepted one. Incident and recovery history where it exists.

**Cross-checking the seller's own narrative.** The highest-value analysis in a diligence is consistency: does the architecture document describe the coupling the repository shows, does the roadmap's assumed velocity match the delivery record, does the incident narrative match the incident log, does the headcount plan match the knowledge concentration. Prepared material is rarely false and frequently inconsistent with other prepared material, and nothing currently checks one against another.

**Give the seller a reason.** A pre-diligence self-assessment, run by the seller before the process opens, showing them what a buyer's analysis will find and letting them prepare answers or fix things. Sellers pay for this willingly — it is vendor due diligence, an established and well-funded practice — and it is the wedge that gets the technology inside the boundary in the first place, with the buy-side product following the trust rather than leading it.

**Confidence and refusal.** Every finding carries its evidence window, the disruptions in that window and a stated confidence, and the package declines to answer where the history cannot support it. A diligence practitioner citing a number to an investment committee needs to know exactly how it could be wrong.

## Target Customer

Entry is sell-side: founders and their advisors preparing for a process, who want to know what a buyer will find. This is a real market today, the buyer is motivated, and it puts the analysis inside seller boundaries repeatedly.

The destination is buy-side: private equity technical operating groups and the diligence practices that serve them, who will pay per-deal rates comfortably because the alternative is a decision priced on an opinion formed through a window.

## Impact If Built

The diligence opinion acquires a factual base. An investment committee currently receives a report whose confidence is rhetorical; this would let a share of it be evidential, with the window and the caveat attached.

The asymmetry between buyer and seller narrows without the seller giving up control, which is the only form in which it can narrow at all.

And post-acquisition, the same findings become the integration plan's starting point — the coupling map, the bus-factor register and the effort concentration are exactly what the acquirer needs on day one and currently reconstructs from scratch six months later.
