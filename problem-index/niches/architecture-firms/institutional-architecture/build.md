# Owner Design Standards as Checkable Rules

**Niche:** [[niches/architecture-firms/institutional-architecture/profile|Institutional Architecture]]
**Industry:** [[industries/architecture-firms|Architecture Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Universities, health systems and state agencies each hand architects a design standards manual of hundreds of pages, and conformance is checked by someone reading it.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #automation #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to win qualifications-based selections from institutional owners on the strength of past delivery — but health systems select on clinical planning and a record of passing state health-facility review, while school districts and civic owners select on delivering bond-funded programmes on budget, and the winners differ. Decomposed into contested sub-niches below.

## The Problem
Large institutional owners publish design and construction standards: the university's manual specifying approved door hardware, mechanical room clearances, classroom technology rough-ins, room numbering and Division 01 language; the health system's standards for patient rooms and infection-control details; the state agency's minimum building standards. Architects must comply, and the owner's facilities staff review each submission against the manual. Both sides do it by reading. Non-conformances are found at 95% CDs or in construction, when changing them is expensive.

## Why Nobody Has Built This
Each owner's manual is different, written in prose, updated irregularly and rarely versioned. Model-checking tools such as Solibri check generic BIM rules, and code-checking tools check codes; neither is configured for one owner's standards because no single owner is a large enough market, and the architects who must comply see each manual as a one-off.

## What to Build
A service that converts an owner's standards manual into a structured, versioned rule set — measurable requirements as model checks, product requirements as specification checks, and the rest as a review checklist — then checks the architect's model, specification and sheets at each phase and produces a conformance report both sides can use. The owner licenses it once and every design team uses it.

## Target Customer
Facilities planning and design directors at universities, health systems and state agencies running capital programmes, and the institutional practices that work for them repeatedly.

## Impact If Built
Non-conformances found at schematic design instead of construction, owner review hours cut on every submission, and a standards manual that finally tells the owner which requirements are routinely missed or waived.
