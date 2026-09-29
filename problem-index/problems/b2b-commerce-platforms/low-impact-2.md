# Industrial Catalogue Data Quality

**Industry:** [[b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Product information management is a mature category and industrial catalogues remain incomplete, because attributes arrive as manufacturer PDFs and nobody has the staff to key hundreds of thousands of parts.
**Tags:** #large-language-models #bert #word-embeddings #cnns #k-nearest-neighbors #evaluation-metrics #data-integration #transfer-learning

## The Problem
An industrial distributor's catalogue runs to hundreds of thousands or millions of items. Each has technical attributes that determine whether it is the right part: dimensions, materials, tolerances, ratings, thread specifications, voltage, compatibility.

Those attributes arrive from manufacturers as PDF datasheets, spreadsheets in idiosyncratic formats, and sometimes as printed catalogues. Structuring them is manual, and no distributor has the staff to do it for the whole catalogue, so it gets done for the top-selling items and the long tail remains a part number, a short description and a price.

The consequences are direct. A customer cannot filter to the specification they need, so they cannot find the part, so they call inside sales — which is the cost the storefront exists to remove. Or they order the wrong part, which produces a return, a reship and a delay on a job site.

Cross-referencing compounds it. Customers search by a competitor's part number or by an OEM number, and the crosswalk between equivalent parts across manufacturers is commercially valuable and largely absent outside a few categories.

## What Already Exists
Product information management platforms handle attribute storage, governance and syndication well once data exists. Industry classification standards (UNSPSC, ETIM, eCl@ss) provide attribute schemas by category. Manufacturers increasingly publish structured data, inconsistently. Document extraction from PDFs is mature. Some categories have established cross-reference databases. Search platforms support faceted filtering when attributes are populated.

## The Customisation Gap
PIM systems store attributes and do not create them, and creation is the entire problem. Extracting structured attributes from manufacturer datasheets is a well-shaped document task on a document class that is highly variable in layout and highly consistent in content, and it is performed by data entry staff.

Category schema mapping is the second gap. Industry standards define attribute sets per category and mapping a manufacturer's own terminology onto them is manual, so distributors either adopt a standard partially or invent their own.

Cross-reference generation is where the commercial value concentrates. Determining that this manufacturer's part is functionally equivalent to that one requires comparing specifications, which requires the specifications to be structured — so it is gated on the same extraction problem and is worth more than the attributes themselves.

Completeness measurement is absent. Which attributes matter for findability in each category, and how complete the catalogue is against them, is answerable from search and support-call data and would direct the data effort at the items where it pays.

## Impact If Solved
Catalogue completeness determines whether a customer can find a part without calling, which is the entire self-service proposition in industrial distribution. Extracting attributes from datasheets at scale, and generating cross-references from the resulting specifications, converts a permanently backlogged data entry function into a solved layer.
