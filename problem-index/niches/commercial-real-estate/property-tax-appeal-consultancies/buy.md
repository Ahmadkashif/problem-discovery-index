# Assessment Data Ingestion Adapted to Jurisdictional Chaos

**Niche:** [[niches/commercial-real-estate/property-tax-appeal-consultancies/profile|Property Tax Appeal Consultancies]]
**Industry:** [[industries/commercial-real-estate|Commercial Real Estate]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Web scraping and document extraction are solved; the problem is that three thousand jurisdictions publish assessments in three thousand formats, change them without notice, and use the same words to mean different things.
**Tags:** #bert #transformers #large-language-models #transfer-learning #word-embeddings #change-point-detection #evaluation-metrics #automation #data-integration #workflow-orchestration

## The Problem
Everything starts with knowing what a parcel was assessed at, on what basis, and by when it can be appealed. That information sits in county and municipal systems ranging from modern APIs to scanned notices mailed on paper, with terminology that varies fundamentally — assessed value, market value, taxable value, and equalized value mean different things in different states and are sometimes used interchangeably within one. Firms maintain armies of scrapers and manual collection processes, and the failure mode is silent: a jurisdiction changes its portal or its terminology, collection breaks or subtly misinterprets, and nobody notices until a deadline is missed or an analysis is built on the wrong figure.

## What Already Exists
Web data collection and document extraction are commodity capabilities. Commercial scraping platforms handle rendering, rotation, and change detection; document AI services extract fields from scanned notices at high accuracy; several vendors sell public records collection as a service. Workflow orchestration for thousands of scheduled jobs is a solved engineering problem.

## The Customization Gap
Every one of those returns fields; none of them understands what the fields mean. The hard part is semantic normalization across jurisdictions whose value concepts genuinely differ — mapping a state's assessed value to a comparable basis requires knowing that state's assessment ratio, its equalization mechanism, and its exemption structure, and those are legal facts rather than data fields. The adaptation is a jurisdiction model that carries the assessment framework as structured knowledge — value concepts, ratios, appeal procedures and deadlines, notice conventions — with collection normalized against it rather than into a flat schema. Change detection has to be semantic rather than structural: a portal redesign that changes layout matters less than a jurisdiction quietly redefining a value concept, and only the second corrupts the analysis. And collection health must be measured per jurisdiction with explicit coverage reporting, because in a business where a missed deadline is a lost year, silent failure is the risk that matters.

## Target Customer
Heads of data operations and national practice leaders at property tax firms, and the analysts who currently rebuild broken collection and reconcile terminology by hand.

## Impact If Solved
Removes the silent failure mode that costs whole appeal years, and frees a large manual collection effort. A properly modelled jurisdiction layer is also the foundation for the outcome model and the deadline system — neither can work reliably on data whose meaning varies by county and is normalized ad hoc.
