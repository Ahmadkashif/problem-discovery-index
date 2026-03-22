# Fiber Route Optimization and Construction Sequencing

**Niche:** [[niches/utility-contractors/telecom-fiber/profile|Telecom & Fiber]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An optimization engine that takes a fiber deployment area, pole/conduit infrastructure, make-ready status, permitting timelines, and customer demand density as inputs and produces an optimized construction sequence that maximizes homes-passed per month while respecting make-ready dependencies — replacing the manual sequencing that project managers currently perform with spreadsheets and wall maps.
**Tags:** #reinforcement-learning #gradient-boosting #workflow-orchestration #automation #revenue-impact

## The Problem
A fiber-to-the-home (FTTH) deployment covering 50,000 homes takes 2-4 years and involves building 200-500 miles of fiber in a specific sequence. The sequence depends on: make-ready completion (can't build aerial fiber until poles are ready), permitting status (can't build until permits are issued for each segment), customer demand (high-demand areas generate revenue sooner), construction crew availability, material delivery schedules, and seasonal constraints (frozen ground limits underground construction in northern markets). The project manager optimizes this sequence manually, typically achieving 50-70% of theoretically optimal homes-passed-per-month rates because manual planning can't evaluate the combinatorial explosion of sequencing options across 500+ construction segments with 10+ constraint dimensions.

## Why Nobody Has Built This
The constraint space is unique to fiber construction: make-ready completion is uncertain (pole owners provide estimated timelines but miss them regularly), permitting timelines vary by municipality (some process in days, others in months), and construction productivity varies by method (aerial is 2-3x faster than underground) and terrain. The optimization must re-run weekly as make-ready completions, permit approvals, and crew availability change. Generic project scheduling tools (MS Project, Primavera) model task dependencies but not the probabilistic constraints (make-ready might be ready next week, or might not) that define fiber construction sequencing.

## What to Build
A fiber construction sequencing optimizer that: (1) ingests the fiber network design (segments, poles, conduit routes, homes per segment) from the OSP design tool; (2) tracks make-ready status per pole/segment from the make-ready tracking system; (3) models permitting timelines per municipality based on historical processing times; (4) optimizes the construction sequence to maximize homes-passed per month (revenue acceleration) subject to make-ready completion, permitting, crew availability, and material delivery constraints; (5) re-optimizes weekly as constraints update — a make-ready that completes early opens a new high-priority segment; (6) produces a rolling 4-week construction schedule with daily segment assignments per crew, material delivery requirements, and traffic control needs.

## Target Customer
Fiber internet service providers (ISPs) deploying FTTH networks — Lumen (Quantum Fiber), Frontier, Consolidated Communications, and hundreds of independent ISPs. Fiber construction contractors (MasTec, Dycom, Quanta) managing FTTH builds for ISPs.

## Impact If Built
Increases homes-passed-per-month by 20-35% through optimized construction sequencing, accelerating revenue realization by 6-12 months on a multi-year deployment. Reduces construction crew idle time (waiting for make-ready or permits) by 15-25%, saving $500K-2M per year for a major FTTH deployment. Provides ISP executives with realistic deployment timelines based on actual constraint data rather than optimistic manual projections.
