# Vending and Bin Replenishment on Generic Min/Max

**Industry:** [[industrial-distributors|Industrial Distributors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Inventory planning tools forecast a warehouse's demand well; they don't forecast what one vending machine on second shift at one customer's plant will dispense next week.
**Tags:** #time-series-forecasting #exponential-smoothing #gradient-boosting #bayesian-inference #feature-engineering #automation #data-integration

## The Problem
Distributors increasingly hold stock inside the customer's plant: bins on the line, cribs in the maintenance shop and vending machines that dispense gloves, cutting tools, abrasives, batteries and safety glasses against an employee badge. Fastenal ran 44.7% of its 2025 sales through managed inventory and vending, with 136,638 weighted bin and vending installations; Grainger KeepStock and dozens of regional distributors run the same model. Someone has to keep every slot stocked. In most programmes that means a replenishment rep walking the plant on a schedule, counting or scanning bins, and keying a refill order, with min/max levels set once at installation and rarely revisited.

The result is two failures at once. Slow movers sit for months, often on consignment that the distributor owns and pays to carry. Fast movers run out between visits, and a stockout of a cutting insert or a safety item stops work — exactly what the programme was sold to prevent. Usage is lumpy: it follows the customer's production schedule, shift patterns, new jobs and the occasional employee who takes a box of gloves home.

## What Already Exists
ERP min/max and reorder-point logic in Prophet 21, Infor CSD and similar systems; supply chain planning tools that forecast at warehouse level; vending and crib software (AutoCrib, CribMaster, Apex and the distributors' own platforms) that logs every dispense by employee, job and time; and weight or RFID bins that report levels automatically.

## The Customisation Gap
Generic planning forecasts a few thousand SKUs at a few locations with long histories. Point-of-use replenishment is the opposite: tens of thousands of slot-level series, most with intermittent demand, each tied to one customer's production calendar. The missing logic is slot-level intermittent-demand forecasting that uses the customer's shift and job data; min/max levels re-optimised continuously against the cost of a stockout at that slot, which differs between a safety item and a spare drill bit; consignment carrying cost charged against the account; and visit routing that sends the rep only to the plants and aisles that need it. Dispense logs exist; they are used for billing and usage reports, not for planning.

## Impact If Solved
Cutting consigned inventory by ~15–25% while holding or reducing stockouts (estimate) frees working capital on every programme, and replacing fixed walk-around visits with signal-driven ones gives a replenishment rep back ~1–2 days a week across a territory. It also turns usage data into the savings evidence national accounts ask for at re-bid.
