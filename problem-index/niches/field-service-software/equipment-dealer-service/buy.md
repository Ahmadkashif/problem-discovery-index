# Shop Scheduling From Automotive Dealer Practice

**Niche:** [[niches/field-service-software/equipment-dealer-service/profile|Equipment Dealer Service Departments]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automotive dealerships solved service shop scheduling, technician productivity measurement and customer communication a generation ago with mature commercial products, and equipment dealers next door run a whiteboard.
**Tags:** #optimization-fundamentals #dynamic-programming #time-series-forecasting #evaluation-metrics #confidence-intervals #workflow-orchestration #automation #worker-facing
**Contested on:** Every serious competitor in dealer service software is fighting to get a machine back into the field inside the window the customer's season allows — and whoever cuts downtime during the narrow weeks that matter takes the dealership.

## The Problem
A service manager assigns jobs to technicians and bays on a whiteboard each morning. Jobs waiting on parts sit in a corner of the yard. Technician specialisation — who is good on a particular drivetrain or a particular electronic system — is in the manager's head. A machine can wait days for a specific technician to become free while others are underutilised, and nobody can see it because there is no schedule, only an assignment.

## What Already Exists
Automotive dealer service scheduling is a mature commercial category, with products handling appointment scheduling against technician capacity, flat-rate time allowances, bay allocation, parts hold status, technician efficiency measurement and automated customer status communication. The methods and the workflows transfer almost directly. Equipment manufacturers publish repair time allowances in the same way automotive manufacturers do. Nothing about the problem is novel.

## The Customization Gap
The adaptation is to a shop whose jobs are larger, less predictable and frequently held on parts. It requires: (1) repair time estimation from the dealer's own realised times rather than from the manufacturer's warranty allowance, since the allowance is a reimbursement rate and using it for planning is the root cause of most promise failures; (2) parts hold modelled as a first-class state with an expected release date, because a substantial share of shop occupancy is machines waiting rather than machines being worked on, and a scheduler that ignores it is scheduling fiction; (3) technician capability at a finer grain than a certification list, learned from realised times and rework by machine system, which is what the service manager is actually doing mentally; (4) field service and shop scheduled together, since the same technicians do both and the current practice of managing them separately is why field calls destroy shop plans; and (5) seasonal surge handling, including how overflow work and outside contractors are brought in, which automotive practice does not need and this segment does every year.

## Target Customer
Equipment dealers and dealer groups, and the dealer management system vendors who have historically invested in sales and finance rather than in the service bay.

## Impact If Solved
Realised-time estimation and explicit parts-hold state together produce something the department has never had — a schedule that means something — which is the precondition for every promise it makes to a customer. The transfer from automotive practice is direct enough that the development is an adaptation rather than an invention, which is why the absence is a matter of attention rather than difficulty.
