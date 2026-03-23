# Change Order Ripple Effect

**Niche:** [[niches/event-planning/vendor-coordination/profile|Vendor Coordination Automation]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Fix (Pain Point)
**One-liner:** When the client changes the head count from 200 to 250, the planner must manually identify every affected vendor and communicate the change — missing one means a disaster.
**Tags:** #automation #workflow-orchestration #data-integration

## The Problem
Event details change constantly: head count adjusts, timeline shifts, venue layout changes, dietary restrictions update, entertainment is added or dropped. Each change ripples through multiple vendors — but the planner must manually trace the impact. Head count change: affects caterer (meal count), venue (room setup), rentals (tables, chairs, linens), bar service (alcohol quantities), valet (parking capacity), and potentially florist (additional centerpieces). The planner must identify each affected vendor, calculate the specific impact, and communicate the change with updated details. Missing one vendor creates a visible failure on event day.

## Why It's Still Broken
There's no dependency map between event details and vendor contracts. The planner carries this map in their head — they know the caterer cares about head count but not about the DJ's set list. When changes overlap or arrive in rapid succession (3 changes in 2 days), the mental model breaks down. The planner sends the head count update to the caterer and rentals but forgets the bar service. No tool models these dependencies because they're event-specific and vendor-specific.

## What a Fix Looks Like
A change impact mapping system: for each event, the planner defines which vendors are affected by which detail categories (head count → caterer, venue, rentals, bar; timeline → all vendors; entertainment → AV, lighting, venue). When a change is logged (head count from 200 to 250), the system identifies all affected vendors, generates change notifications with vendor-specific impact descriptions, and tracks acknowledgment. The planner reviews and sends with one action. Nothing is missed because the dependency map is explicit, not mental.

## Who Feels the Pain
Event planners managing events with 15+ vendors where 3-5 detail changes occur in the final month, each requiring 4-8 vendor notifications that are currently manual and error-prone.

## Impact If Fixed
Eliminates vendor miscommunication from missed change notifications (which cause event-day failures in 10-15% of events), reduces change management time from 2-3 hours per change to 15 minutes, and removes the cognitive burden of carrying vendor dependency maps in the planner's head.
