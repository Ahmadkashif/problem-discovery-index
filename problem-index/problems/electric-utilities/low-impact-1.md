# Rate Case Discovery Run as a Document Hunt

**Industry:** [[electric-utilities|Electric Distribution Utilities]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every contested rate case brings hundreds to thousands of intervenor data requests with response deadlines of about ten days, and the utility answers them by emailing witnesses and searching shared drives for workpapers it has answered before.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
Once a utility files a rate case, the commission staff, the state consumer advocate, industrial customer groups and environmental intervenors serve data requests: "Provide the workpapers supporting the 2025 vegetation management adjustment," "Explain the variance in Account 593 between the test year and 2023," "Provide all studies relied on for the proposed customer charge." A contested case can bring hundreds to thousands of requests (estimate). Each has a response deadline set in the procedural schedule, often around ten days (estimate). Each must be routed to the right witness, answered consistently with the testimony, checked by counsel, marked confidential where needed and served.

The regulatory affairs team runs this as a tracking spreadsheet and an email chase. Many requests repeat questions asked in the last case or in another jurisdiction of the same holding company, but finding the prior answer means searching shared drives and the commission's e-filing system by hand. Inconsistent answers between witnesses, or between this case and the last, become cross-examination material.

## What Already Exists
Generic legal technology covers parts of the workflow. E-discovery platforms such as Relativity and Everlaw handle litigation document review, contract and matter management tools track deadlines, and enterprise search (SharePoint, Microsoft Copilot over Microsoft 365) finds documents. A few regulatory filing tools manage docket calendars. None of them is built around a data request as the unit of work.

## The Customisation Gap
Rate case discovery has its own structure. Requests reference FERC Uniform System of Accounts numbers, test-year adjustments, schedule and workpaper identifiers from the minimum filing requirements, and the witness who sponsored each exhibit. Responses must stay consistent with pre-filed testimony and with answers already served in the same case. They must respect protective-order confidentiality tiers, and they are public once filed, so a careless answer becomes a precedent in every other jurisdiction. The missing layer classifies each request by topic, account and witness, retrieves prior answers and the supporting workpaper, drafts a response for the witness to edit, and checks the draft against testimony and earlier answers before it is served.

## Impact If Solved
A regulatory team that answers repeat questions from a searchable archive could cut response drafting time by perhaps a third to a half (estimate), meet procedural deadlines without weekend surges, and catch inconsistencies before intervenors do, which protects the revenue requirement the case is about.
