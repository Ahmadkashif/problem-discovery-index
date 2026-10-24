# Retail Assortment Planning for a Boat Lot

**Niche:** [[niches/powersports-and-boat-dealers/model-year-stocking-floorplan/profile|Model-Year Stocking & Floorplan Curtailment]]
**Industry:** [[industries/powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Apparel and sporting-goods retailers have planned seasonal assortments by size and colour for decades; a boat dealer plans the same kind of buy with a spreadsheet.
**Tags:** #time-series-forecasting #survival-analysis #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to set a dealer's model-year stocking order and aged-unit plan so that inventory sells before the floorplan's free period ends, and whoever leaves the fewest units past their first curtailment at model-year end takes the account.

## The Problem
A seasonal buy committed months ahead, financed by a lender with a clock, sold through a short peak and marked down at season's end: that is apparel retail's problem, and assortment and markdown planning tools exist for it. Boat and powersports dealers face the same structure with units worth $15,000–150,000 each (estimate) and no planning tool.

## What Already Exists
Merchandise and assortment planning software from the large retail planning vendors forecasts demand by attribute, plans the pre-season buy and optimises markdowns against inventory carrying cost.

## The Customization Gap
The adaptation needs: units described by configuration (hull length, engine horsepower, package, colour) instead of SKU sizes; floorplan terms per unit (OEM interest periods by programme, lender curtailment schedules) as the carrying-cost model; OEM retail programmes as the markdown lever, because the dealer rarely funds the whole discount; dealer trades as a transfer option; and a demand signal from registrations by segment and county rather than point-of-sale history. Volumes are hundreds of units, not millions of SKUs, so the planner must work with thin data.

## Target Customer
Inventory managers and general managers at dealer groups with 10 or more stores.

## Impact If Solved
Moving a group's pre-season buy from intuition to a planned assortment that cuts aged units by 10% (estimate) frees several million dollars of floorplan capacity for a 50-store group.
