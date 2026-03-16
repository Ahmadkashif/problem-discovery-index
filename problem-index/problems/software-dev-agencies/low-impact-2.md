# Code Quality & Tech Debt Assessment for Handoff

**Industry:** [[software-dev-agencies|Software Development Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Static analysis tools exist but none produce a client-readable tech debt report that maps code health to business risk and maintenance cost.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml

## The Problem
Every agency project ends with a handoff — either to the client's internal team, a maintenance contractor, or back to the agency on a retainer. The codebase at handoff carries accumulated tech debt from deadline pressure, mid-project pivots, and the gap between "works" and "works well." Neither the agency nor the client has a clear, quantified picture of what that debt will cost to service. The agency risks reputation damage when the client's team inherits a fragile codebase; the client risks budget surprises when "small changes" take weeks because of hidden coupling.

## What Already Exists
SonarQube, CodeClimate, and similar static analysis tools generate code quality metrics — cyclomatic complexity, duplication, test coverage, vulnerability counts. GitHub Copilot and AI code review tools flag issues at the PR level. But these tools produce developer-oriented reports full of metrics that mean nothing to a client CTO or product owner. They also lack context about the project's constraints — a high-complexity module might be intentional (complex domain logic) or accidental (rushed implementation).

## The Customisation Gap
Agency handoff requires: (1) aggregating static analysis metrics with project context (timeline pressure, requirement changes, team composition) to distinguish intentional complexity from debt, (2) classifying each debt item by business impact severity — "this will break under 2x load" vs. "this makes new feature development 30% slower," (3) generating a client-facing report with estimated remediation costs in hours/dollars, not code metrics, and (4) producing a prioritized remediation roadmap that a non-technical stakeholder can approve. The classification model needs training on agency-specific patterns where shortcuts are taken under delivery pressure.

## Impact If Solved
Agencies differentiate on transparency, improving client retention for maintenance contracts (worth 20-40% of initial project value). Clients avoid the "second agency rebuild" pattern where they hire a new agency to redo what the first agency built, costing the industry billions in redundant work.
