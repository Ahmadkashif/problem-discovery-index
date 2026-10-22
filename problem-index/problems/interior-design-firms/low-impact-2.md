# Commercial FF&E Specification and Code Compliance

**Industry:** [[interior-design-firms|Interior Design Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Commercial specification software is organised around building construction divisions, so the furniture, fabrics and finishes that interior designers specify for hotels, offices and care homes are still written as spreadsheets and checked against codes by hand.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #workflow-orchestration #automation

## The Problem
A hotel renovation's FF&E package can run to several hundred line items: guestroom case goods, lounge seating, lighting, drapery, carpet, wallcovering, artwork and accessories, each with a specification sheet giving dimensions, materials, finishes, performance ratings, quantities, a basis-of-design product and acceptable alternates. The package must meet the brand's design standards, the property's PIP scope, and fire and performance requirements that depend on where the item goes: upholstered seating to the applicable flammability standard, wallcovering to a flame-spread class under ASTM E84, contract fabrics to an abrasion rating measured in double rubs, and accessible routes and fixtures to ADA. Healthcare and senior living add cleanability, bleach resistance and bariatric load ratings.

Designers assemble this in Excel, copy product data from manufacturer PDFs and websites, and check compliance by reading each spec sheet against a checklist. When a manufacturer discontinues a fabric, or a purchasing agent proposes a cheaper alternate, the check is repeated by hand, and the alternate that passes on price but fails the double-rub or flammability requirement is caught late or not at all.

## What Already Exists
Architectural specification tools such as Deltek Specpoint, MasterSpec and BSD SpecLink produce construction specifications organised by CSI MasterFormat divisions. Studio-management tools such as Studio Designer, Programa and DesignManager produce FF&E schedules and tearsheets for residential work. Product data comes from manufacturer websites, PDF spec sheets and Material Bank.

## The Customisation Gap
Construction specification tools treat FF&E as a thin division at the end of the book; residential studio tools have no concept of performance codes, brand standards or alternates. The commercial interiors layer needs: a product record that carries code-relevant attributes (flammability test, flame-spread class, double rubs, cleanability, weight rating) extracted from spec sheets and test reports rather than typed in; rules by occupancy type and location within the building that evaluate each line against those attributes; a brand-standards library that checks a hotel package against the franchisor's requirements and the PIP; and an alternates workflow that compares a proposed substitute against the basis-of-design product attribute by attribute before anyone approves it. The data extraction is now a solved class of problem; the domain rules are the customisation.

## Impact If Solved
A hospitality or healthcare interiors team stops re-checking hundreds of spec sheets by hand for every revision and alternate, cuts days from each bid package, and closes the most common route to a failed inspection or a costly post-install replacement: an alternate that matched on look and price but not on the code.
