# Submittal & RFI Routing Logic

**Industry:** [[construction-tech-platforms|Construction Tech Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Submittal and RFI workflow engines are mature and universally deployed; deciding who a given item should actually go to, and by when, is still read out of the specification by a project engineer.
**Tags:** #large-language-models #bert #transformers #word-embeddings #transfer-learning #workflow-orchestration #automation

## The Problem
Every construction management platform handles submittals and RFIs: create, route, review, respond, log, close. The workflow is solved.

Populating it is not. A project's submittal register is derived from the specification — hundreds of pages defining what must be submitted for each section, in what form, to whom, with what review period. A project engineer reads the spec and builds the register by hand, typically over days, at the start of every project. Routing rules follow: this section goes to the structural engineer, that one to the architect, this one to the owner's representative, with review durations that the spec states and the contract sometimes contradicts.

RFIs are worse, because they arrive unplanned. Somebody in the field asks a question; a project engineer decides which spec section it touches, who can answer it, and what it affects downstream. That judgement is experience, and it is the difference between an RFI answered in four days and one that sits for three weeks with the wrong reviewer.

## What Already Exists
Procore, Autodesk Construction Cloud and their peers ship complete submittal and RFI modules with configurable approval chains, due date tracking and escalation. Specification management tools exist. Document AI extracts structure from spec PDFs with reasonable accuracy. Template registers are sold and shared between contractors.

## The Customisation Gap
Templates transfer poorly because specifications are project-specific documents assembled by a design team from master guide specs with edits, and the edits are exactly where the risk lives. A register built from a template misses the section the architect modified, which is the one that generates the dispute.

Generating the register from the actual specification is the gap — reading the submitted spec, extracting each required submittal with its section reference, form, quantity and review period, and proposing the register for engineer confirmation. That is a well-shaped extraction problem on documents the platform already stores and does not read.

Routing is the second half and is where the vendor's cross-project data would matter. Across hundreds of thousands of projects the platform has observed which reviewer types answer which kinds of item quickly and which do not, and it can predict both the correct routing and the realistic review duration — as opposed to the contractual one, which is frequently fiction.

## Impact If Solved
Register creation is a multi-day manual task at the start of every project, and mis-routing is one of the most common causes of the RFI latency that drives schedule slip. Both are addressable from documents already in the system, which makes this the cheapest real improvement available in the category.
