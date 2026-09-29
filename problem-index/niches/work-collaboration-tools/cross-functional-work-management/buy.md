# Critical Path and Dependency Analysis Off the Shelf

**Niche:** [[niches/work-collaboration-tools/cross-functional-work-management/profile|Cross-Functional Work Management]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Critical path analysis and schedule risk simulation are textbook techniques implemented in construction and engineering project software for decades, and cross-functional work management shows a Gantt chart with no critical path at all.
**Tags:** #graph-theory #dynamic-programming #monte-carlo-methods #confidence-intervals #evaluation-metrics #optimization-fundamentals #time-series-forecasting #hypothesis-testing
**Contested on:** Every serious competitor in cross-functional work management is fighting to assemble the real state of a programme spanning functions that each work in a different tool — and whoever produces that view without asking anyone takes the account.

## The Problem
A programme has two hundred items with dependencies across six functions. Which of them actually determines the completion date, how much slack each of the others has, and what a two-week delay in any given one would do to the finish are all standard outputs of critical path analysis, which construction software has produced since the 1960s. The cross-functional tool shows a timeline with bars and dependency arrows and computes none of it, so the programme manager's attention is allocated by whoever is loudest rather than by what is on the path.

## What Already Exists
Critical path method, resource levelling and schedule risk analysis through Monte Carlo simulation are mature, documented and implemented in project management software across construction, engineering and defence. Graph algorithms for longest path are elementary. Probabilistic duration modelling is standard. Everything required is textbook and free, and the construction tech niche elsewhere in this vault describes the same techniques being underused in the industry that invented them.

## The Customization Gap
The adaptation is to a programme whose durations are uncertain and whose dependencies cross tools. It requires: (1) durations as distributions from the organisation's own history of comparable work rather than as single estimates, since a deterministic critical path on estimated durations is precisely wrong in a domain where the estimates are poor; (2) handoffs included as path elements with their own durations, which is the build note's subject and without which the computed path omits the part that actually delays things; (3) dependencies that span tools, resolved through federation rather than requiring everything to be modelled in one product — which is what makes it usable in a real estate of nine tools; (4) sensitivity analysis as the primary output, since the useful question is which few items most affect the finish date rather than what the finish date is, and that ranking is what should direct a programme manager's week; and (5) presentation without the vocabulary, because cross-functional programme leaders are not schedulers and a product that requires them to understand float will not be used.

## Target Customer
Cross-functional work management vendors, programme management offices, and the transformation functions running large multi-function initiatives.

## Impact If Solved
Sensitivity analysis tells a programme manager which handful of items to spend their attention on, which is the decision they make every week with no evidence. The techniques are decades old and free; the adaptation is probabilistic durations, handoffs on the path, and presentation to someone who has never heard of float.
