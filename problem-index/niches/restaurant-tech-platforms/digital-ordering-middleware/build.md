# A Menu Model That Survives Translation

**Niche:** [[niches/restaurant-tech-platforms/digital-ordering-middleware/profile|Digital Ordering & Channel Middleware]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every menu change is performed five times by hand because no vendor has built a canonical menu representation rich enough to generate each channel's version without losing the structure the kitchen depends on.
**Tags:** #graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #data-integration #automation #workflow-orchestration
**Contested on:** Every serious competitor in ordering middleware is fighting to keep one menu correct across five channels that each model a modifier differently — and whoever requires the fewest manual rebuilds takes the account.

## The Problem
A burger has a required protein temperature, an optional cheese group where one selection is free and additional ones are priced, a bun substitution that changes the price, and a side choice that opens a nested dressing selection. The point of sale models this one way. One marketplace supports two levels of nesting and not three. Another supports required groups but not conditional pricing. A third does not support nesting at all. The middleware either maps by hand or flattens, and flattening produces orders the kitchen cannot interpret. So a person builds the menu five times and maintains it five times, and it drifts.

## Why Nobody Has Built This
The problem looks like a mapping exercise and is actually a representation problem: there is no canonical model expressive enough to hold what the point of sale means and precise enough to project losslessly onto each channel's weaker model. Building one requires understanding what each channel can and cannot represent, formalising the projection, and — crucially — deciding what to do when a projection is lossy, which is the interesting case and the one that vendors have handled by manual intervention. Channel operators have no incentive to converge, and each middleware vendor's advantage is the accumulated manual knowledge of the channels, which a canonical model would commoditise.

## What to Build
A canonical menu representation that models items, modifier groups, selection rules, conditional pricing, availability windows and nesting as an explicit structure, plus a projection engine per channel that generates that channel's menu and — the important part — reports what was lost. A lossy projection is surfaced as a decision to the operator with the alternatives: collapse this nested group into two flat groups, or suppress the item on this channel. That decision is made once and remembered, which is what turns five ongoing rebuilds into one build and a set of recorded policies. Reverse translation matters equally: an order arriving from a channel must reconstruct into the point of sale's structure so the kitchen ticket is right, and the canonical model is what makes that reliable rather than heuristic.

## Target Customer
Ordering middleware vendors, point of sale vendors with their own integrations, and multi-unit operators who currently employ people to maintain menus across channels.

## Impact If Built
Onboarding a restaurant to a new channel drops from hours of menu building to a review of projection decisions, which changes the economics of channel expansion for the whole market. For operators, one maintained menu instead of five eliminates the drift that causes wrong orders, and the explicit record of what each channel cannot represent is information no operator currently has.
