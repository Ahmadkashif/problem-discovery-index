# Cost Estimation Adapted to Association Replacement Economics

**Niche:** [[niches/hoa-management/reserve-study-firms/profile|Reserve Study Firms]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Construction cost databases price new work bid competitively, and a reserve study prices replacement work in an occupied building paid for by a committee.
**Tags:** #tabular-ml #time-series-forecasting #data-integration #evaluation-metrics #automation

## The Problem
Half of every reserve study is cost. What will it cost to replace this roof, resurface this parking area, modernize this elevator — not today, but in the year the plan says it happens, with escalation applied.

The estimates come from construction cost databases built for contractors bidding new work. They price the work. They do not price the circumstances, and in an association the circumstances routinely dominate: the building is occupied, access is constrained, the work must be phased around residents, the job is small enough that mobilization is a large fraction of the total, and the buyer is a volunteer board that will take three bids and often accept a mid-range one after a delay.

The result is a systematic underestimate that compounds across thirty years of projection, and it lands as the special assessment nobody planned for.

## What Already Exists
RSMeans and its peers are excellent, deep, and continuously maintained construction cost databases with regional factors and escalation indices. Estimating software built on them is mature and widely used.

## The Customization Gap
Every adaptation needed here is about the buyer and the setting rather than the work.

**Occupied-building premiums.** Phasing, resident protection, restricted staging, off-hours work — these are real and they scale with the community's density and layout, which the analyst has already documented in the site inspection.

**Small-job economics.** Cost databases are most accurate at commercial scale. A 40-unit association replacing a roof is a small job where mobilization, permitting, and overhead are a much larger share of the total. The correction is not linear and the databases do not make it.

**The buyer is a board.** Associations do not procure like commercial owners. Bids are solicited by volunteers, decisions take months, work gets deferred, and the winning bid is often not the lowest. That behaviour has a cost, it is consistent, and no construction database models it.

**Escalation that fits the horizon.** A thirty-year projection is dominated by the escalation assumption, and general construction indices have proven a poor guide for specific trades — roofing and elevator work have both moved very differently from the aggregate. Trade-specific, regionally fitted escalation is a materially different number.

**Calibration against what associations actually paid.** This is the part the firm can do and the database vendor cannot. Every replacement the firm later observes is a validation point for an estimate it once made, and comparing the two is the cheapest accuracy improvement available.

## Target Customer
Principal or director of technical services at a reserve study firm, especially one working across multiple states where a single national cost factor is visibly wrong in both directions.

## Impact If Solved
Cost error is the larger half of reserve underfunding and the half nobody attends to, because component life is where the professional debate happens. A firm whose estimates track what associations actually pay produces funding plans that hold up — and can demonstrate it against its own record, which is an argument no competitor bidding on price can answer.
