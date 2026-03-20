# BOM Scrubbing and AVL Cross-Reference

**Industry:** [[electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Component search and cross-reference tools like Octopart and SiliconExpert exist for general electronics sourcing, but none of them understand an ECM's facility-specific AVL (Approved Vendor List), customer-specific component restrictions, or the form-fit-function equivalence criteria that determine whether an alternative component can actually be substituted on a specific PCBA without engineering change approval.
**Tags:** #bert #transformers #word-embeddings #transfer-learning #attention-mechanisms #feature-engineering #evaluation-metrics #data-integration #automation

## The Problem
A typical PCBA BOM contains 200-2,000 line items. When a customer sends a new BOM for quotation or when components on an existing program go on allocation or become obsolete, the procurement team must "scrub" the BOM: verify each component's availability, pricing, and lead time; identify components at risk (end-of-life, single-source, long lead time); and find approved alternatives for unavailable parts. This BOM scrub involves checking each component against the ECM's AVL (which vendors are approved for which component families), the customer's approved component list (which may restrict sourcing to specific manufacturers), and distributor availability (authorized vs. broker). A 500-line BOM scrub takes a procurement specialist 4-8 hours of manual cross-referencing between component databases, AVL spreadsheets, and distributor portals.

## What Already Exists
Octopart aggregates distributor pricing and availability. SiliconExpert provides component lifecycle status, cross-references, and compliance data. IHS Markit offers component obsolescence forecasting. DigiKey and Mouser have extensive search and parametric selection tools. None of these platforms integrate with the ECM's internal AVL, understand customer-specific sourcing restrictions, or evaluate form-fit-function equivalence in the context of a specific PCBA design — they answer "is this component available?" but not "can this component be used on this board for this customer?"

## The Customisation Gap
An ECM-specific BOM intelligence tool needs: (1) integration with the facility's AVL — which component manufacturers and distributors are approved, with approval status per component family and customer; (2) customer restriction awareness — parsing customer-specific approved component lists and sourcing restrictions (some OEM customers require components from their own AVL, others prohibit specific countries of origin); (3) form-fit-function equivalence reasoning — when an alternative is suggested, evaluating whether the package, electrical specifications, and pin compatibility match the original part in the specific circuit application; (4) risk scoring per BOM line — combining lifecycle status, supply chain risk, single-source exposure, and lead time against production schedule to prioritize procurement attention.

## Impact If Solved
Reduces BOM scrub time from 4-8 hours to 30-60 minutes per BOM. Identifies supply chain risks earlier in the NPI process, reducing line-down events from component shortages. For an ECM processing 20-50 new BOMs per month (quotation + NPI), recovering 100-400 hours of procurement specialist time monthly enables the team to focus on strategic sourcing rather than manual cross-referencing.
