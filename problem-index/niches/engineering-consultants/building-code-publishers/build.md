# The Local Amendment Layer Nobody Maintains

**Niche:** [[niches/engineering-consultants/building-code-publishers/profile|Building Code Publishers]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model code is published cleanly and then amended by thousands of jurisdictions, and every engineer in the country reconstructs the amendments for their project by reading PDFs.
**Tags:** #bert #transformers #large-language-models #graph-neural-networks #word-embeddings #change-point-detection #evaluation-metrics #compliance #data-integration #revenue-impact

## The Problem
The publisher's product ends where its users' problem begins. A model code is developed rigorously and published as a coherent document; jurisdictions then adopt it with amendments — deleting sections, changing values, adding local requirements — published as ordinances in whatever form the jurisdiction uses. The Pass 1 analysis describes the consequence precisely: engineers cross-reference PDFs of local amendments against national standards by hand, on every project, in every jurisdiction. Thousands of firms perform the same reconstruction for the same jurisdictions independently, and the organization that authored the base document has no view of what its code actually says in force anywhere.

## Why Nobody Has Built This
Amendments are the jurisdictions' legal instruments, not the publisher's, and there are thousands of them published without coordination or notification. Assembling them is a research operation the publisher has never been structured for, since its process ends at publication. There is also a liability question that has to be answered rather than avoided: stating what the code says in force in a jurisdiction is a representation, and the organization has been cautious about making one. And the model has been to sell the base publication, which makes the amendment layer look like someone else's problem even though it is where the users' cost sits.

## What to Build
An amendment layer maintained as a research product: adopted edition and effective date per jurisdiction, with amendments captured at provision level rather than as documents, so the code as enforced in a given place can be assembled and compared against the model. Building it is a collection and structuring operation of the same kind the organization already runs for its own development process, and the base code it already owns is what makes provision-level mapping tractable — an amendment is defined relative to a section the publisher authored. Delivered as a jurisdiction-resolved code rather than a base document plus a pile of ordinances, it removes the reconstruction from every firm in the country. It also produces something the organization has never had about its own work: a picture of which provisions jurisdictions routinely amend or delete, which is the strongest possible evidence for the next development cycle about where the model code does not fit practice.

## Target Customer
VPs of codes and chief technical officers at code publishers, and the engineering firms, plan reviewers, and building officials who currently reconstruct the amendment picture jurisdiction by jurisdiction.

## Impact If Built
Converts a publication into a service in the layer where the users' actual cost sits, with switching costs a document sale never generates. The amendment analytics also close a loop the code development process has never had — a direct measure of which provisions the market rejects, feeding the cycle that writes the next edition.
