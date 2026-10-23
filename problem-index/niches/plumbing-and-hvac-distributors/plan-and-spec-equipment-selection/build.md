# The Re-Selection Engine That Shows Its Margin Against the Schedule

**Niche:** [[niches/plumbing-and-hvac-distributors/plan-and-spec-equipment-selection/profile|Plan-and-Spec Equipment & Fixture Selection]]
**Industry:** [[industries/plumbing-and-hvac-distributors|Plumbing & HVAC Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The applications veteran's value is knowing which of the house's models really meets a competitor's basis-of-design at the design conditions, and what the drawings imply that the schedule doesn't say.
**Tags:** #tacit-knowledge-ml #large-language-models #transformers #k-nearest-neighbors #gradient-boosting #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn an engineer's equipment and fixture schedules into a priced package of the supply house's own lines that helps the contractor win the bid and clears submittal, and whoever posts the most awarded packages approved on the first submittal takes the account.

## The Problem
A schedule lists RTU-3 by another brand's model with 9.2 tons total and 6.9 tons sensible at 95°F, 3,600 cfm at 0.8 inches of static, 460 volts and an IEER floor. Nominal tonnage matching gets it wrong half the time; the veteran re-runs the selection at those conditions, sees the sensible shortfall, steps up a size, adds the curb adapter because it replaces an existing unit and checks the weight on the roof. Newer quoters match nominal sizes and get rejected.

## Why Nobody Has Built This
Selection software belongs to each manufacturer and works one unit at a time; blueprint AI counts equipment but doesn't re-select across brands; and nobody has recorded which re-selections engineers accepted.

## What to Build
An engine that extracts each schedule line's requirements, retrieves candidate models from the house's manufacturers' performance tables at the stated conditions, ranks them by margin against every requirement, flags implied accessories from the drawings (replacement curbs, low-ambient, hail guards, fixture carriers by wall type, lead-free trims), and logs the specialist's choice and reason. A two-week demo works on public bid sets and published performance data.

## Target Customer
Commercial applications and quotation managers at plumbing and HVAC distributors; Rebar-type vendors as a selection layer.

## Impact If Built
If ~10–20% of substitutions now fail first submittal (estimate), catching sensible-capacity and accessory misses before the bid saves the contractor weeks per resubmittal and protects ~1–3% of package margin lost to field changes (estimate).
