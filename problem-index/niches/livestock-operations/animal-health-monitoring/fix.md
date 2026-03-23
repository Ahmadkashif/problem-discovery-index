# Treatment Response Tracking Across Pull-Treat-Return Cycles

**Niche:** [[niches/livestock-operations/animal-health-monitoring/profile|Animal Health Monitoring]]
**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Type:** Fix (Pain Point)
**One-liner:** When a feedlot animal is pulled, treated, and returned to the pen, the current system loses track of whether the treatment worked — the pen rider must re-identify the treated animal among 200 pen mates, remember which drug was used, and assess response without any structured follow-up protocol or data to guide the decision.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #data-integration #worker-facing

## The Problem
A feedlot hospital processes 50-150 animals per day during peak BRD season. Each animal receives a treatment following a tiered protocol: first pull gets antibiotic A (typically Draxxin or Zuprevo, $15-30/dose), second pull gets antibiotic B ($20-40/dose), third pull is evaluated for salvage or chronic pen assignment. After treatment, the animal is returned to its home pen. The critical question — "did this animal respond to treatment?" — is answered only if the pen rider re-identifies the animal on subsequent rides, which requires remembering or checking a treatment list against 200+ head in the pen. In practice, treatment response assessment happens only when the animal is sick enough to be pulled again. This means that 20-30% of animals receiving their first treatment are not responding but are not identified until they deteriorate to second-pull severity — by which time treatment cost has doubled and permanent lung damage is more extensive.

## Why It's Still Broken
Feedlot management software records the treatment event but provides no structured workflow for follow-up assessment. The pen rider receives a daily list of animals to watch but the list grows to 30-50 animals per pen during BRD season — too many to meaningfully track while also scanning the other 150+ untreated animals. Treatment response is a clinical judgment (is the animal eating more, moving better, less depressed?) that requires observing the specific animal, not just checking a box. The system design treats treatment as an event rather than a process with follow-up.

## What a Fix Looks Like
A treatment follow-up workflow integrated with the pen riding process. When an animal is treated, the system schedules a follow-up assessment at 48 and 96 hours post-treatment. The pen rider's daily route is optimized to pass by pens with pending follow-ups. A mobile app displays the treated animal's tag number, treatment administered, and key assessment questions (eating? alert? respiratory rate?). If available, IoT sensor data (activity level, rumination recovery) provides objective treatment response metrics that flag non-responders before the pen rider reaches the pen. Non-responders are automatically escalated to the next treatment tier, and the treatment protocol database captures response rates by drug, pathogen season, and cattle type to inform protocol optimization.

## Who Feels the Pain
Pen riders who must track dozens of treated animals mentally while scanning hundreds of untreated animals for new cases. Hospital crews who process the same animals multiple times because first-treatment failures were not caught early. Consulting veterinarians who cannot analyze treatment efficacy because response data is not systematically collected. The animals themselves — delayed re-treatment extends suffering and worsens outcomes.

## Impact If Fixed
First-treatment non-responders identified 24-48 hours earlier, reducing the escalation from first to third pull by 15-20%. Treatment cost per BRD case reduced by $8-15/head through earlier second-treatment intervention. Chronic pen population reduced by 10-15%, freeing pen space and reducing the $200-500/head loss on chronic animals. Treatment protocol optimization from systematic response data saves $1-3/head across all animals placed. For a 20,000-head feedlot, combined annual impact of $80K-$200K.
