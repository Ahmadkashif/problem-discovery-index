# Revit MEP Plugin for Plumbing Contractor Shop Drawing Automation

**Niche:** [[niches/plumbing-contractors/commercial-new-construction/profile|Commercial New Construction Plumbing]]
**Industry:** [[industries/plumbing-contractors|Plumbing Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Revit MEP has plumbing design capabilities but is built for mechanical engineers, not plumbing contractors — a contractor-focused plugin that automates fixture-to-pipe-size calculations per IPC/UPC and generates field-ready isometric drawings would bridge the gap.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
Autodesk Revit MEP is the dominant BIM tool for commercial plumbing design, but it's built for MEP engineering firms who design systems, not for plumbing contractors who install them. A plumbing contractor receiving a Revit model from the engineer of record must convert the design into shop drawings — fabrication-ready isometric diagrams showing pipe sizes, fitting types, hanger locations, and dimensions that a journeyman plumber can read in the field. Revit can technically generate isometrics, but the workflow requires a Revit-proficient drafter who manually configures views, annotations, and pipe sizing parameters for each project. Most plumbing contractors don't have Revit expertise in-house and outsource this step for $2,000-8,000 per project.

## What Already Exists
Revit MEP provides pipe routing, sizing, and annotation tools. Autodesk Fabrication products (CADmep, ESTmep) handle detailing and estimating for mechanical contractors. SysQue (by Trimble) is a Revit plugin for MEP detailing. However, all three are designed for HVAC-first workflows and treat plumbing as a secondary discipline. None automate the IPC/UPC fixture unit cascade that plumbing contractors need, and their isometric output requires extensive manual formatting to produce field-readable drawings.

## The Customization Gap
A plumbing-contractor-specific Revit plugin needs to: (1) auto-calculate pipe sizes from fixture unit sums per IPC or UPC (selectable by project jurisdiction) without manual spreadsheet work, (2) generate standardized isometric views with contractor-preferred annotation styles (pipe sizes, fitting callouts, hanger spacing, slope indicators) in one click, (3) produce cut lists and fitting counts for material ordering directly from the model, and (4) export field-ready PDF packages organized by floor and zone for distribution to foremen. The plugin would be sold as an annual subscription ($2,000-5,000/year) — less than one outsourced shop drawing project — and marketed through Autodesk's app store and plumbing trade associations (PHCC, UA).

## Target Customer
Commercial plumbing contractors who receive Revit models from engineers and currently outsource shop drawing production or employ a dedicated Revit drafter, spending $15,000-60,000/year on a process that could be largely automated with plumbing-specific tooling.

## Impact If Solved
Reduces shop drawing production from 40-80 hours to 8-16 hours per project by automating pipe sizing calculations and isometric generation. Eliminates outsourcing costs of $2,000-8,000 per project. Enables contractors to bring shop drawing production in-house without hiring a full-time Revit specialist.
