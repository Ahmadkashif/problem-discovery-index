# Door-Through-Door Service Level Scheduling

**Niche:** [[niches/non-emergency-medical-transport/elderly-homebound-populations/profile|Elderly Homebound Populations]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No NEMT scheduling system distinguishes between curb-to-curb and door-through-door service, causing routes built for 2-minute pickups to fail on 15-minute elderly patient assistance stops.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #worker-facing

## The Problem
NEMT routing assumes a pickup takes 2-5 minutes: the driver arrives, the patient walks to the vehicle, and they depart. For elderly homebound patients, the actual process is: the driver parks, walks to the door, rings the bell, waits for the patient to get to the door (2-5 minutes for mobility-limited elderly), assists the patient with a walker down steps or through a building hallway, helps them into the vehicle, secures mobility equipment, and departs — a 12-20 minute process. Routes built with standard dwell time assumptions systematically run late for every subsequent patient after an elderly door-through-door pickup. Experienced dispatchers know which patients need extended time and manually pad their routes, but this knowledge is personal and disappears with dispatcher turnover.

## Why Nobody Has Built This
The door-through-door service level is not a standard Medicaid billing category in most states — it falls between "ambulatory" and "wheelchair" in the service taxonomy, with no separate reimbursement code. NEMT software reflects the billing categories, not the operational reality. Building a door-through-door scheduling layer requires creating a new service classification, learning patient-specific dwell times from historical data, and integrating this into route optimization — all for a service level that does not have a distinct revenue code.

## What to Build
A scheduling module that classifies patients on a granular mobility/assistance scale (not just ambulatory/wheelchair) and predicts per-patient pickup and dropoff dwell times based on: mobility level, home layout (floor level, stairs, building type), required assistance (walker, oxygen, cognitive prompting), weather conditions, and historical trip durations for that specific patient. Routes are built using patient-specific dwell time predictions rather than category-wide defaults. Dispatchers see a route timeline that accurately reflects the 15-minute elderly pickups alongside the 3-minute ambulatory pickups, preventing the cascading delays that make every subsequent patient late.

## Target Customer
NEMT providers where 30%+ of trip volume serves elderly homebound patients, and dispatchers who build routes knowing they will run late because the scheduling system does not account for door-through-door time.

## Impact If Built
Improves on-time performance for elderly patient routes from 65-70% to 90%+ by accurately scheduling the time required for door-through-door assistance. Reduces cascading delays that affect 3-5 subsequent patients per route, and provides data to support advocacy for a door-through-door Medicaid reimbursement rate that covers the actual cost of service.
