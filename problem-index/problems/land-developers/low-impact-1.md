# Lot Option and Takedown Contract Tracking

**Industry:** [[land-developers|Land Developers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every developer selling lots to production builders administers the same option and takedown terms (phase delivery dates, takedown quotas, deposits, price escalators, walk-away rights) from a spreadsheet rebuilt for each contract.
**Tags:** #large-language-models #transformers #seq2seq #evaluation-metrics #workflow-orchestration #automation #revenue-impact

## The Problem
A developer that sells finished lots to builders signs a lot purchase or option agreement per builder per phase. Each one sets how many lots the builder must take down and when (often a quarterly quota after a phase is delivered), the earnest money or option deposit (~10–20% of lot price, estimate) and how it is credited at each takedown, a base price with an escalator (a fixed percentage per quarter, or a share of the builder's home price), the developer's delivery obligations (paved streets, utilities stubbed, plat recorded) and remedies on both sides. Land bankers and option platforms add a second layer: the builder pays an option fee on the platform's capital, and the developer delivers into the platform. Forestar alone held $193.3M of builder earnest money at the end of fiscal 2025 and sold 927 lots through lot bankers.

Administration is mechanical and unforgiving. The finance team calculates each takedown's price with the right escalator, credits the right slice of deposit, checks the builder took its quota, bills the closing, and tracks which lots are delivered, reserved, under contract or released. When a builder slows down, a missed quota triggers notice rights. Whether the developer can reprice, resell or keep the deposit depends on clauses that someone has to find. Errors leak margin quietly: an escalator applied from the wrong date, a deposit credited twice, a quota miss nobody noticed until the cure period ran out.

## What Already Exists
Contract lifecycle management tools (Ironclad, DocuSign CLM, Agiloft) store and search contracts and track key dates. Construction and real estate accounting systems (Sage Intacct, Yardi, MRI, Sage 300 CRE) bill and post closings. Homebuilders run their side in their own ERPs and land systems. [[title-and-settlement-offices|Title & Settlement Offices]] close each takedown. Most developers still keep the takedown schedule in Excel.

## The Customisation Gap
Generic CLM extracts dates and parties; it does not understand a takedown. The land-specific logic is a lot-level ledger: each lot's status from raw through platted, delivered, taken down and closed; the quota per period and its cure rules; escalator formulas (fixed, indexed or home-price share) with their start dates; deposit crediting per lot; delivery conditions tied to the developer's own milestones (plat recording, municipal acceptance, dry utilities energised); and the option-platform layer where a land banker owns the lots and the builder pays a fee. It also needs a phase-level forecast linking builder sales pace to the next quarter's takedown, so the developer sees a quota miss coming. None of the generic tools has a lot as a data object.

## Impact If Solved
A takedown ledger built from the contracts themselves, with escalators and deposits computed per lot, removes the reconciliation work at every closing and catches the missed quota or wrong escalator while the cure period is still open. For a developer closing ~3,000 lots a year (estimate), errors on 1% of closings at ~$5,000 each come to ~$150K a year (estimate). Catching one missed quota inside its cure period protects a phase's deposit, ~$1.1M on 100 lots at 10% of a $108,400 lot (estimate).
