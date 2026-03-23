# Childcare-Aware Dynamic Shift Scheduling

**Niche:** [[niches/childcare-centers/ratio-scheduling-ops/profile|Staff Scheduling & Ratio Compliance Operations]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic workforce scheduling platforms optimize for labor cost and employee preferences but have no concept of room-level ratio constraints, age-group-specific staff requirements, or credential-based room eligibility.
**Tags:** #reinforcement-learning #regression #tabular-ml #automation #compliance

## The Problem
Center directors build weekly staff schedules that must simultaneously satisfy: state-mandated staff-to-child ratios by age group (e.g., 1:4 infants, 1:7 toddlers, 1:10 preschool), teacher credential requirements by room (lead teacher must hold CDA or higher), staff availability and PTO, legally mandated break windows, and staggered shift coverage for 10-12 hour operating days. A center with 15 staff across 6 rooms generates thousands of valid schedule combinations — directors currently spend 2-4 hours weekly building schedules in spreadsheets or on paper, then spend another 1-2 hours daily adjusting when reality diverges from the plan.

## What Already Exists
Workforce scheduling platforms like When I Work, Deputy, Homebase, and 7shifts handle shift creation, employee availability, PTO tracking, time clock integration, and labor cost optimization. They are mature, well-designed, and widely adopted in restaurants, retail, and healthcare. Some offer "compliance" features for break laws and overtime rules. Procare and brightwheel include basic scheduling views but without optimization — they show the schedule, they don't generate one.

## The Customization Gap
No generic scheduling platform understands that Room 2 requires exactly 2 adults when 8 toddlers are present, that only staff with an Infant/Toddler CDA can be assigned to the infant room, that a teacher's 30-minute break must be covered by a floater who is simultaneously eligible for that room's age group, or that the lunch hour transition from 11:30-12:30 requires temporary double-staffing in the preschool room because 10 children return from outdoor play while 10 others are still eating. The customization layer is a constraint engine that sits on top of generic shift scheduling and ensures every generated schedule satisfies ratio, credential, and transition-overlap requirements — rejecting any schedule that would create a compliance gap.

## Target Customer
Center Directors and Assistant Directors at centers with 10+ staff, where manual schedule-building complexity exceeds what intuition and spreadsheets can reliably handle — roughly 40,000-50,000 centers in the US.

## Impact If Solved
Reduces weekly schedule-building time from 2-4 hours to under 30 minutes. Eliminates the "I forgot that Ms. Rodriguez can't be in the infant room" errors that currently create ratio violations discoverable only when the schedule is already in effect. Generates schedules that minimize labor cost while guaranteeing 100% ratio compliance — something no director can reliably do manually across 6+ rooms.
