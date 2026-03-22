# Hidden Condition Documentation & Change Order Generator

**Niche:** [[niches/general-contractors/residential-remodeling/profile|Residential Remodeling Contractors]]
**Industry:** [[industries/general-contractors|General Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a remodeler opens a wall and discovers galvanized plumbing that needs replacing, the tool captures photos, generates a scope description, estimates the cost, and produces a client-ready change order — all from the jobsite in under 5 minutes.
**Tags:** #cnns #object-detection #large-language-models #tacit-knowledge-ml #automation #revenue-impact

## The Problem
Remodeling projects routinely encounter hidden conditions during demolition: corroded plumbing behind walls, knob-and-tube wiring requiring replacement, water-damaged subfloor beneath tile, structural deficiencies masked by drywall, asbestos in older homes. When a crew member discovers a hidden condition, the contractor must: (1) document it with photos and description, (2) determine the additional scope of work required, (3) estimate the cost of the additional work, (4) present it to the homeowner for approval before proceeding, and (5) get a signed change order. Currently, step 1 is a phone photo texted to the homeowner with a verbal explanation. Steps 2-5 happen hours or days later when the contractor gets back to the office and writes it up — during which time the project is either stalled (waiting for approval) or the contractor proceeds at risk (doing the work before getting the signed change order).

## Why Nobody Has Built This
Generating a change order from a hidden condition requires combining visual recognition (what am I looking at — corroded pipe, damaged subfloor, outdated wiring), scope definition (what work is needed to remediate), cost estimation (labor hours, materials, subcontractor costs), and document generation (professional change order with photos, description, and pricing). This spans computer vision, domain-specific knowledge, and document generation — a combination that wasn't practical until recent advances in multimodal AI. The remodeling segment is also highly fragmented (thousands of small operators) with low willingness to pay for software, making it commercially unattractive for traditional SaaS companies.

## What to Build
A mobile-first tool where the contractor photographs a hidden condition, speaks a brief description ("Found corroded galvanized supply lines behind the kitchen wall, needs to be replaced with PEX from the main to the fixtures"), and the system generates a complete change order: annotated photos, written scope description, estimated cost based on local labor rates and material prices, and a client-facing approval interface. The cost estimate uses a combination of the contractor's historical pricing data (if available) and regional cost databases (RSMeans, local supplier pricing). The homeowner receives the change order via text/email and can approve with a digital signature. The system maintains a log of all hidden conditions and change orders for the project, creating an audit trail that protects both parties.

## Target Customer
Remodeling contractors (5-20 employees) doing kitchen, bath, basement, and whole-home renovations who currently lose 15-30% of change order revenue because they don't document and bill for hidden condition work in a timely manner.

## Impact If Built
Recovers 10-20% of currently unbilled change order revenue (on a $60K average remodel, that's $6-12K per project in work the contractor does but doesn't charge for). Reduces hidden-condition-related project delays from days (waiting for office write-up) to minutes (generated on-site). Creates a documented audit trail that reduces homeowner disputes about change order pricing and necessity.
