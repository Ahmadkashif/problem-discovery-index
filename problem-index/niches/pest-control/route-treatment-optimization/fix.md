# Service Time Estimation Guesswork

**Niche:** [[niches/pest-control/route-treatment-optimization/profile|Route & Treatment Optimization]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Fix (Pain Point)
**One-liner:** Routes are built assuming every residential treatment takes 20 minutes — but actual times range from 12 to 45 minutes based on property size, service type, and pest pressure.
**Tags:** #regression #tabular-ml #automation

## The Problem
Pest control dispatchers schedule routes using flat time estimates: "residential = 20 minutes, commercial = 45 minutes." In reality, a 1,200 sq ft condo takes 12 minutes while a 4,000 sq ft home with a heavy ant infestation takes 40 minutes. This variance creates cascading scheduling problems: routes planned for 8 hours actually take 10 hours (technician runs late for last 3 appointments), or routes finish at 2pm leaving the technician idle for 2 hours. Neither outcome is acceptable — late arrivals anger customers, early finishes waste labor capacity.

## Why It's Still Broken
Accurate service time estimates require property-specific data (square footage, number of entry points, crawl space accessibility, historical service times) that isn't captured in a structured format. Even when historical service times exist in the CRM (clock-in/clock-out records), no one analyzes them to build property-specific time estimates. The data exists — it's just never been used for prediction.

## What a Fix Looks Like
A service time prediction model trained on historical clock-in/clock-out data correlated with property attributes (square footage, service type, pest pressure level, number of previous services). The model predicts expected service duration per property per service type, with confidence intervals. Route scheduling uses predicted durations instead of flat estimates. Over time, predictions converge toward actual durations as more data accumulates, and the system flags outlier properties that consistently exceed predictions (indicating a scope issue that should trigger re-pricing).

## Who Feels the Pain
Dispatchers who build routes that either run 2 hours over or finish 2 hours early, technicians who run late and get complaint calls from waiting customers, and the company owner who pays for idle time or overtime equally.

## Impact If Fixed
Improving service time estimation accuracy from +/- 50% to +/- 15% enables tighter route packing, adding 1-2 stops per technician per day and reducing both overtime and idle time. On a 10-tech operation, this recovers $100,000-$200,000 in annual capacity.
