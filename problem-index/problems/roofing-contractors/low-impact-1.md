# Insurance Supplement Writing and Xactimate Line-Item Generation

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic document generation tools exist but don't understand Xactimate's line-item taxonomy, insurance adjuster argumentation patterns, or the specific language required to justify storm damage line items that adjusters routinely contest.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #loss-functions #evaluation-metrics #automation #revenue-impact

## The Problem

Insurance claim supplements — additional line items submitted after the initial adjuster estimate — are the primary revenue lever in insurance restoration roofing. A skilled supplement writer knows: which line items adjusters commonly omit (O&P markup, dumpster, permit fee, ice-and-water shield, drip edge, starter strip), how to write the scope narrative to support each contested item, and what code references to cite when the adjuster denies a line item as non-code-required. This supplement writing skill is learned over years of claim negotiation and is not documented in any accessible format.

Generic AI writing tools can draft professional text but don't know Xactimate's specific line-item codes, don't know which line items are commonly contested in which insurance carriers, and don't know the code citations that support each disputed item.

## What Already Exists

Xactimate's own platform has some template functionality. Several roofing-specific supplement services exist (contractors outsource supplement writing to specialists). No AI tool exists that generates Xactimate-ready supplement packages from inspection report inputs.

## The Customisation Gap

A roofing-specific supplement AI needs: (1) a structured knowledge base of Xactimate line-item codes relevant to roofing (300-400 line items); (2) a database of commonly contested line items by carrier; (3) code citation library (IRC, NRCA guidelines) supporting disputed line items; (4) an LLM layer that takes the inspection damage summary as input and generates the supplement document with proper line items, scope narrative, and code citations. The carrier-specific knowledge and Xactimate line-item taxonomy are not in any general-purpose AI tool.

## Impact If Solved

Enables any estimator to write supplement packages that previously required 5+ years of claim negotiation experience. Average supplement value per insurance job is $1,500–$4,000. A firm completing 100 insurance jobs per year recovers $150,000–$400,000 in additional approved claim value.
