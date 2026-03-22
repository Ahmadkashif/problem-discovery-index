# Material Lead Time Tracking for Specialty Metals

**Niche:** [[niches/roofing-contractors/metal-roofing-specialty/profile|Metal Roofing Specialty]]
**Industry:** [[industries/roofing-contractors|Roofing Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Metal roofing panels have 2-12 week lead times that vary by manufacturer, color, gauge, and current demand — but contractors commit to installation dates before confirming material availability, creating project delays that cascade through the schedule and damage customer relationships.
**Tags:** #time-series-forecasting #gradient-boosting #feature-engineering #data-integration #workflow-orchestration #worker-facing

## The Problem
Unlike shingle roofing where material is available same-day from any ABC Supply or SRS Distribution branch, metal roofing panels are manufactured to order. Standard Galvalume colors in common gauges (24ga or 26ga) from high-volume manufacturers (ATAS, Drexel, McElroy) may ship in 2-3 weeks. Custom colors add 4-6 weeks. Specialty materials (copper, zinc, Cor-Ten weathering steel) run 8-12 weeks. Stone-coated metal tiles (DECRA, Boral) have variable lead times based on production schedules. A metal roofing contractor signs a $25,000 job, promises a 3-week installation start, and then discovers the customer's chosen color in the specified panel profile has an 8-week lead time because the manufacturer is running a different color batch. The contractor either delays the project (losing credibility and potentially the contract), substitutes a different color (disappointing the customer), or pays a 20-40% premium for rush production. This problem compounds when multiple manufacturers are involved — trim from one supplier and panels from another, each with different lead time schedules.

## Why It's Still Broken
Manufacturer lead times are communicated via phone calls to sales reps — there is no real-time API or dashboard showing current production schedules, color batch timing, or inventory levels for any major metal panel manufacturer. Lead times shift weekly based on order backlog, raw material availability (steel coil pricing and supply), and seasonal demand patterns (spring and summer have longer lead times). Contractors learn about lead time changes only when they place an order and receive an acknowledgment with a ship date 2-4 weeks later than expected. No aggregation exists across manufacturers — a contractor comparing ATAS vs. Drexel vs. McElroy for a specific color and profile cannot see comparative lead times without calling all three.

## What a Fix Looks Like
A lead time aggregation and forecasting platform that tracks actual ship dates versus quoted lead times across metal panel manufacturers, building a historical database that predicts real lead times by manufacturer, panel profile, color, gauge, and time of year. The system would crowdsource data from participating contractors: when a contractor places an order and receives shipment, they log the actual lead time, building a real-time picture of each manufacturer's current performance. A time-series forecasting model trained on historical patterns predicts lead times 4-8 weeks forward, accounting for seasonal demand, known raw material constraints, and manufacturer capacity. When a contractor is quoting a job, the system shows: "Standing seam 24ga Burnished Slate — ATAS: 3 weeks (high confidence), Drexel: 5 weeks (medium confidence), McElroy: 2 weeks (high confidence)." The system alerts contractors when lead times for their open orders are trending longer than quoted.

## Who Feels the Pain
Metal roofing estimators who commit to installation dates without accurate lead time information, then manage customer frustration when projects delay. Project managers juggling 10-20 active metal roofing projects where material arrival dates shift weekly. Customers who chose metal roofing for its longevity and aesthetics but experience a frustrating 2-3 month process that their neighbor's shingle reroof completed in a week.

## Impact If Fixed
Eliminates project delays caused by lead time surprises on 15-25% of metal roofing jobs, protecting $3,000-8,000 per job in customer concessions and rush-order premiums. Enables contractors to steer customers toward colors and profiles with shorter lead times at the quoting stage, improving close rates by setting realistic expectations upfront.
