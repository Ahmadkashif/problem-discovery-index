# Permit Correction Letters, One Jurisdiction at a Time

**Industry:** [[architecture-firms|Architecture Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Code search and permit portals are mature, but nothing tells an architect what this building department's plan examiners actually object to, so every correction cycle is answered from scratch.
**Tags:** #large-language-models #bert #transformers #k-nearest-neighbors #compliance #workflow-orchestration #automation

## The Problem
A permit set goes in; four to twelve weeks later (estimate) a correction letter comes back with twenty to eighty numbered comments. Some are code: an exit access travel distance over the limit, a missing fire-resistance rating at a shaft, plumbing fixture counts that don't match the occupant load. Some are local amendments the national code doesn't contain. Some are the examiner's habits: a demand for a specific code-analysis sheet format, an energy compliance form, a structural special inspection statement worded a particular way. The project architect sorts the comments, routes the structural and MEP ones to consultants, revises sheets, writes a response letter keyed to each comment and resubmits — and each further round costs the owner weeks of carrying cost on a building that cannot start.

Firms working repeatedly in the same jurisdictions learn the patterns, but the learning lives in a project architect's memory and old response letters on a shared drive. A firm entering a new city starts at zero, and the same comments are drawn out of it on project after project.

## What Already Exists
ICC Digital Codes and UpCodes make model codes and many local amendments searchable, and UpCodes adds an assistant that answers code questions. Jurisdictions run electronic plan review through ProjectDox, Accela, Tyler EnerGov or Bluebeam Studio Sessions, which deliver the comments. AI pre-check tools such as Archistar and CivCheck sell to building departments to screen submittals before an examiner sees them. Drawing checkers such as Helonic and InspectMind scan sets for code errors against the model code.

## The Customisation Gap
What none of them hold is the architect's side of the history: the comments this jurisdiction issued on this building type, how the firm answered them, and which answers cleared on the next round. The architect-specific layer needs: parsing correction letters into structured comments by code section, discipline and sheet; matching them to the firm's past comments and accepted responses across projects; flagging local amendments and recurring examiner requests during design development rather than after submission; drafting response letters keyed to the comment numbering with links to revised sheet clouds; and tracking which consultant owns each open item. The code itself is the generic part. The jurisdictional memory is the gap.

## Impact If Solved
Removing even one correction round on a typical commercial permit gives the owner back four to twelve weeks (estimate) and the project architect several days of response work per round, and lets a firm enter a new jurisdiction with the institutional memory it would otherwise take three or four projects to build.
