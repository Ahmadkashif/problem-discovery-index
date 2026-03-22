# Automated Pipe Sizing and DWV Layout from Architectural Plans

**Niche:** [[niches/plumbing-contractors/commercial-new-construction/profile|Commercial New Construction Plumbing]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Extract fixture counts from architectural plans, calculate pipe sizing per IPC/UPC fixture unit tables, and generate DWV isometric drawings — replacing 40-120 hours of manual drafting and spreadsheet calculations per project with automated output.
**Tags:** #cnns #object-detection #large-language-models #optimization-fundamentals #feature-engineering #automation #revenue-impact

## The Problem
When a commercial plumbing contractor receives architectural plans for a new building, a drafter or project manager must: (1) count every plumbing fixture on every floor (toilets, sinks, floor drains, mop basins, drinking fountains — often 200-2,000 fixtures per project), (2) assign fixture unit values per IPC/UPC code tables, (3) calculate cumulative drainage fixture units for each branch, stack, and building drain, (4) size every pipe segment based on fixture unit loads and slope requirements, (5) size vent stacks and relief vents, and (6) produce isometric shop drawings showing pipe sizes, materials, fittings, and routing. This process takes 40-120 hours per project for a trained drafter and is entirely rule-based — the code tables are deterministic, the fixture unit assignments are standardized, and the pipe sizing follows published flow charts. Yet no tool automates the full pipeline from plan reading to sized isometric output for plumbing contractors.

## Why Nobody Has Built This
The first step — extracting fixture counts and locations from architectural plans — requires computer vision (fixture symbols vary by architect, and plans arrive as PDFs, not structured BIM models). MEP engineering software (Trimble, Autodesk Fabrication) handles pipe sizing but assumes the engineer manually identifies fixtures and routes pipes. Bridging the gap between plan reading and pipe sizing requires a CNN-based fixture detection model trained on thousands of architectural plans with varied symbol conventions, plus a rule engine that maps detected fixtures to IPC/UPC fixture unit values and runs the sizing cascade. The plumbing code varies by jurisdiction (IPC in most states, UPC in California and a few others), adding a configuration layer. Commercial plumbing contractors are not software-forward buyers — the tool must produce output that a foreman can hand to a journeyman, not a parametric model that requires CAD expertise.

## What to Build
A web application that accepts architectural plan PDFs or Revit models, uses a CNN-based object detection model to identify and count plumbing fixtures by type and location, maps them to IPC or UPC fixture unit values (configurable by jurisdiction), runs the DWV pipe sizing cascade (branch → stack → building drain → building sewer), and outputs sized isometric drawings in PDF and DWF format. The fixture detection model is trained on a labeled dataset of architectural plans with fixture symbols annotated. Post-detection, a deterministic rule engine handles all pipe sizing — no ML needed for the calculation itself. The system reduces a 40-120 hour drafting process to a 2-4 hour review-and-adjust workflow. Pricing at $200-500 per project or $500-1,500/month subscription positions it below a drafter's salary but above commodity software.

## Target Customer
Commercial plumbing contractors bidding 5-20 projects per year, currently employing a full-time drafter ($60-90K/year) or outsourcing shop drawings to engineering firms ($2,000-8,000 per project), who want faster bid turnaround and lower overhead on plan takeoff.

## Impact If Built
Reduces shop drawing production time by 70-85%, enabling a contractor to bid more projects with the same staff. A contractor currently spending $80K/year on drafting labor or outsourcing could cut that to $20-30K while bidding 30-50% more projects. Faster bid turnaround also improves win rate — GCs award to contractors who submit complete, accurate bids on time.
