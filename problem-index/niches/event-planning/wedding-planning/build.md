# Day-Of Timeline Orchestration Engine

**Niche:** [[niches/event-planning/wedding-planning/profile|Wedding Planning]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool dynamically manages the wedding day timeline in real time — adjusting all downstream events when the ceremony starts 20 minutes late, and notifying each affected vendor automatically.
**Tags:** #automation #workflow-orchestration #ai-agent

## The Problem
A wedding day timeline has 40-80 time-specific events involving different vendors: photographer arrives at 10am for getting-ready photos, florist delivers at noon, caterer begins setup at 1pm, ceremony at 4pm, cocktail hour at 4:30pm, dinner service at 6pm, cake cutting at 7:30pm, DJ starts dance music at 8pm. When anything runs late (and something always does), every downstream event must shift. The planner manually calculates the cascade, then texts or calls each affected vendor: "ceremony delayed 20 minutes, push cocktail to 4:50, dinner to 6:20." With 15+ vendors to notify, this takes 15-20 minutes of the planner's time during the most stressful moment of the day.

## Why Nobody Has Built This
Wedding timelines are created in spreadsheets or planning apps as static documents. Dynamic rescheduling requires modeling dependencies (can't start dinner until cocktail hour ends, can't do cake cutting until dinner concludes), vendor-specific constraints (caterer needs 30 minutes notice for service timing changes, band must end by 10pm regardless), and notification preferences (text the DJ, call the caterer, email the venue). No planning tool models these dependencies or integrates with real-time communication.

## What to Build
A dynamic timeline engine where the planner inputs the day's schedule with dependencies and vendor assignments. When a delay occurs, the planner marks the actual time and the system cascades adjustments through all dependent events, respecting hard constraints (venue curfew, band contract end time). Automated notifications go to each affected vendor via their preferred channel with their updated timeline. The planner sees a real-time dashboard showing which vendors have acknowledged the changes.

## Target Customer
Wedding planners managing 20+ weddings per year who spend the most stressful moments of wedding days on a phone making timeline adjustment calls instead of managing the event.

## Impact If Built
Saves 15-30 minutes of critical time during every wedding, reduces vendor miscommunication (the florist who doesn't know cocktail hour moved and delivers centerpieces to an empty room), and allows the planner to focus on the couple and guests rather than logistics coordination during the event.
