# One Identity from Model Element to Installed Assembly

**Niche:** [[niches/construction-tech-platforms/mep-prefab-coordination/profile|Mechanical & Electrical — Model-to-Fabrication Chain]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An MEP assembly is identified four separate times between the coordinated model and the installed building, by four different people in four different systems, and the resulting inability to answer "where is spool 4412" is the whole friction of prefabrication.
**Tags:** #graph-theory #data-integration #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #compliance #revenue-impact
**Contested on:** Every serious competitor in MEP contractor software is fighting to carry a coordinated model through to a fabricated, delivered, installed and tracked assembly without anyone redrawing it — and whoever closes that chain with the fewest re-entries takes the account.

## The Problem
A coordinated model contains a pipe rack for level three, zone B. It is exported to the shop system, where it becomes a set of spools with shop-assigned numbers that have no recorded relationship to the model elements. The spools are fabricated, labelled, loaded and delivered. On site, a foreman looking for the rack for a specific area has a label with a shop number, a stack of spools in a laydown yard, and a model that knows nothing about either. Installed status is reported as a percentage. The model, which is the only complete description of what the building is supposed to contain, is never told what is actually in it.

## Why Nobody Has Built This
The chain crosses three software categories with different vendors, different buyers inside the contractor, and no shared identifier standard. Model authoring vendors sell to VDC, shop systems sell to fabrication managers, and field tracking is whatever the GC's platform offers — nobody owns the whole path, and each vendor's incentive is to own its own segment rather than to make the handoff clean. There is also a real modelling difficulty: a model element is not one-to-one with a fabricated assembly, since spooling decisions split and merge elements, so the identity relationship is a graph rather than a key, and building it means recording spooling decisions as data rather than as a drawing.

## What to Build
A persistent identity layer that assigns every model element a stable identifier at coordination and records, as structured relationships, every subsequent transformation — spooled into this assembly, nested onto this cut list, fabricated on this ticket, loaded on this truck, delivered to this area, installed on this date by this crew. The graph is the product. With it, the questions the trade cannot currently answer become queries: where is the assembly for this area, what proportion of this zone is fabricated but not delivered, what is installed against the model, and which elements changed in the latest coordination round after their assemblies were already cut. That last one is the expensive case — rework caused by a coordination change arriving after fabrication — and it is detectable the moment the identity graph exists.

## Target Customer
Mechanical and electrical contractors running prefabrication shops, and the VDC, fabrication and field platform vendors serving them who each own one segment of the chain.

## Impact If Built
Contractors that close the identity chain eliminate the laydown-yard search, cut the rework caused by post-fabrication coordination changes, and get installed-versus-model progress as a by-product rather than as a reported percentage. For the trade that has invested most heavily in prefabrication, this is the difference between the investment paying what it promised and paying half of it.
