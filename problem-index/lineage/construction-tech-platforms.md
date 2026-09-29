# Lineage: Construction Tech Platforms

**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** PlanGrid — an iPad app that held a project's drawing set as individual sheets keyed by sheet number, replaced each sheet with its newest version from the cloud, and hyperlinked every detail callout to the sheet it points at
**Builder:** PlanGrid
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A building is described by its drawing set, and the drawing set never stops changing.

A commercial job's plans run to hundreds or thousands of sheets. Every addendum, bulletin and answered RFI reissues some of them. On paper, each reissue meant printing the changed sheets, trucking them to site, and having someone slip them into every copy of the set in the trailer and in every foreman's truck — then pulling the superseded ones out.

**The expensive failure was not the printing. It was the sheet nobody pulled.** A crew that frames, pours or runs conduit off a superseded sheet builds something that has to be torn out. Nothing on a paper set tells the reader it is stale; currency depended entirely on a person's diligence in a plan room.

## What Got Built

A drawing viewer whose unit is the **sheet**, not the file.

PlanGrid ingested a set, read each sheet's number from its title block by OCR, and stored the set as a collection of numbered sheets. Uploading a new version set replaced each sheet with the same number, so the field tablet showed only the current one — the plan room's slip-in, done by software.

The second mechanism mattered as much. Construction drawings are a hypertext written on paper: a bubble reading "5/A-501" means *detail 5 on sheet A-501*. PlanGrid read those callouts and turned them into links, so a foreman tapped rather than flipped. Its own help pages warn that when OCR misreads a sheet number, the callouts pointing at it fail to link — a small admission of how much rests on that one field.

Markups, photos and issues were pinned to sheets and carried forward across versions.

## Who Built It, And Why Them

PlanGrid was founded in 2011 by **Tracy Young**, a Sacramento State construction-management graduate (2008) who had been a project engineer at the general contractor Rudolph and Sletten, with Ryan Sutton-Gee, also from construction, and engineers Ralph Gootee and Antoine Hersen. It went through Y Combinator's Winter 2012 batch.

**Why them:** the founders were the people inside the plan room. Young has described the specific pain as "3,000-page blueprints" turning over several times a project, and named the core issue plainly: *"Version control of construction data is a huge problem, and there was no software to help manage it."* The iPad, released in 2010, was the enabling hardware — a screen large enough to read a sheet, light enough for a site walk.

The incumbents had no reason to build it. Autodesk sold authoring tools to designers; the paper set was the architect's deliverable and the contractor's problem. **The pain sat with the builder's project engineer, and a project engineer founded the company.** That is why the product is shaped around sheets and sheet numbers — the contractor's unit of reference — rather than around the CAD model the designers work in.

Autodesk bought PlanGrid for $875 million, completing the deal on 20 December 2018, and later retired the brand into Autodesk Construction Cloud.

## What It Cost

**It digitised the sheet and kept the sheet.** PlanGrid made the paper set current, not smarter. Version control happens at page level: a sheet is either the new one or the old one. What changed *on* the sheet, and whether it matters to the electrician rather than the drywaller, is left to the human eye or a generic overlay.

The plan room became a vendor's server.

## What You Still Touch

Every superintendent opening a drawing on a tablet uses PlanGrid's grammar — sheets keyed by number, callouts as links, the newest version by default, markups floating above versions. The unsolved remainder is exactly the part the sheet model skipped: trade-relevant change between versions.

- [[problems/construction-tech-platforms/low-impact-2|🟡 Trade-Specific Drawing Comparison]] — the sheet-level version control that stops at "which sheet is current"
- [[problems/construction-tech-platforms/worker-life-2|🟢 Project Engineer RFI Chase]] — the founder's own job, still chasing answers that reissue sheets
- [[niches/construction-tech-platforms/submittal-rfi-routing/profile|Submittal & RFI Routing Content]]
- [[niches/construction-tech-platforms/small-sub-field-tools/profile|Small Subcontractor Field Tools]]

**Sources:** Wikipedia, *PlanGrid* (2011 founding; seed investors including Y Combinator; $1.1M seed May 2012; iPhone release September 2012; Autodesk acquisition announced 20 November 2018, completed 20 December 2018, $875M); Y Combinator blog, *Founder Stories: Tracy Young of PlanGrid (YC W12)* (founders' backgrounds, the version-control quotation); Sacramento State, *Tracy Young brings the construction industry into the mobile era* (2008 degree, Rudolph and Sletten, "3,000-page blueprints"); PlanGrid Help Center articles on sheet numbering, OCR and automatic callout hyperlinking, and on sheet slip-ins between version sets (read via search snippets; the version-control FAQ returned HTTP 403). ⚠️ **Not established:** the date the first iPad version shipped and the exact feature set at launch — whether OCR sheet numbering and callout hyperlinking were present in the first release or added later could not be confirmed; the mechanism is described here as the product came to work. Early pricing (per project, per sheet or per user) not established.
