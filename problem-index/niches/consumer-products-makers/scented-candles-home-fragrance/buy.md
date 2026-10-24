# Formulation PLM Fitted to Wax, Wick and Vessel

**Niche:** [[niches/consumer-products-makers/scented-candles-home-fragrance/profile|Scented Candles & Home Fragrance]]
**Industry:** [[industries/consumer-products-makers|Consumer Products Makers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process-manufacturing PLM already manages formulas, specs and approvals for food and cosmetics; nobody has configured it for a candle recipe and its burn test.
**Tags:** #large-language-models #feature-engineering #compliance #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to turn each season's fragrance brief into candles that pass burn testing before the retailer's holiday set ships, and whoever puts the most passing new scents on the holiday shelf takes the account.

## The Problem
A candle recipe is a formula (wax blend, fragrance at a load, dye), a component list (vessel, wick, lid, label, carton) and a test history. Mid-sized makers keep all three in separate spreadsheets and folders. When a fragrance house reformulates an oil to meet a new IFRA amendment, or a vessel supplier changes its glass, nobody can list which SKUs use it, so the lab either re-tests the whole range or none of it. Product managers then re-key specifications into each retailer's item-setup forms for every programme.

## What Already Exists
Formulation and product-lifecycle systems built for food, cosmetics and chemicals (Centric PLM, Selerant, Trace One and the formulation modules of process ERPs) manage formulas, specifications, supplier documents, change requests and approvals, with where-used queries and audit trails.

## The Customization Gap
Candle-specific objects and rules: wick series and size as a formula attribute tied to vessel diameter; fragrance load limits read from the fragrance house's IFRA certificate for candles (category 12); vessel and glass specifications against ASTM F2179; burn-test results stored as structured records against ASTM F2417 criteria; ASTM F2058 caution-label text as a controlled field; and a change trigger that opens re-testing for every SKU a supplier change touches.

## Target Customer
Product development and quality leads at candle makers with ~200+ active SKUs (estimate) and several seasonal programmes a year.

## Impact If Solved
A supplier change re-tests only the ~10–30 SKUs it touches instead of a whole range (estimate), and retailer item-setup re-keying drops by ~2–3 hours per new SKU, roughly 100–150 hours a year at a maker launching ~50 SKUs (estimate).
