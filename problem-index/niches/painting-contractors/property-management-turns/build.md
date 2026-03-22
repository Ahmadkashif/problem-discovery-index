# Unit Turn Painting Workflow Optimizer

**Niche:** [[niches/painting-contractors/property-management-turns/profile|Property Management Turns]]
**Industry:** [[industries/painting-contractors|Painting Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A batch scheduling and dispatch system purpose-built for unit turn painting — taking the weekly list of moveouts, assessing scope per unit (touch-up vs. partial vs. full repaint), assigning painters by skill and proximity, sequencing for minimum total vacancy time, and tracking completion with photo verification.
**Tags:** #reinforcement-learning #gradient-boosting #workflow-orchestration #automation #revenue-impact

## The Problem
A turn painting contractor serving a portfolio of 2,000-5,000 apartment units processes 400-1,000 unit turns per year. Each Monday, the property manager sends a list of 10-20 units moving out this week across 3-8 properties. The painting foreman must: (1) visit each unit to assess scope (touch-up, partial repaint, full repaint — currently a judgment call), (2) assign painters based on skill level (full repaints need experienced painters, touch-ups can be handled by junior crew), (3) sequence work to minimize vacancy time (the PM wants all 20 units ready by Friday, but 3 need full repaints that take 2 days each), and (4) coordinate material staging (standard colors at each property, but some units have accent colors or different product specs). This planning process takes 3-4 hours every Monday and produces a schedule that degrades throughout the week as scope changes (a "touch-up" unit turns out to have water damage requiring drywall repair) cascade through the sequence.

## Why Nobody Has Built This
The turn painting scheduling problem combines several challenges: variable scope assessment (each unit's scope isn't known until walkthrough), multi-site logistics (painters travel between properties), skill-based assignment constraints, and real-time schedule disruption from scope changes. Generic scheduling tools model fixed-duration tasks but can't handle the scope assessment step (which determines duration) being part of the workflow itself. The market is also fragmented — turn painting contractors range from 1-person operations to 50-person regional companies, making it hard to build a one-size-fits-all tool.

## What to Build
A mobile-first workflow platform with four modules. First, unit scope assessment: the painter walks through the unit, takes standardized photos (each wall, ceiling, trim, doors), and answers 5 structured questions about surface condition — the system recommends touch-up, partial, or full repaint with estimated hours based on unit size and condition. Second, batch scheduler: takes the week's units with assessed scope, painter availability, and property locations, and produces an optimized daily schedule that minimizes total vacancy days across all units (the PM's primary metric). Third, material staging: auto-generates material orders per property based on assessed scope — gallons of standard colors, primer, rollers, tape — sent to the paint store for delivery. Fourth, completion verification: painter takes post-completion photos, system verifies coverage against the scoped areas, and sends completion notification to the PM.

## Target Customer
Turn painting contractors serving 500+ units across 3+ properties, doing 200+ turns per year. Property management companies with in-house painting teams handling turns across their portfolio.

## Impact If Built
Reduces average unit vacancy time by 1-2 days per turn through optimized scheduling, saving property owners $50-150 per unit per day in lost rent — $100K-300K annually for a 2,000-unit portfolio. Cuts the Monday morning planning process from 3-4 hours to 30-45 minutes. Reduces scope disputes between painting contractors and PMs by documenting condition with photos and standardized assessment criteria.
