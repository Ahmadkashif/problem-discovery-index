# Multi-Ministry Facility Scheduling

**Industry:** [[faith-organizations|Faith Organizations]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Church buildings serve 15+ ministries across 7 days — generic calendar tools can't handle room setup requirements, AV needs, or volunteer staffing dependencies.
**Tags:** #gradient-boosting #decision-trees #linear-regression #feature-engineering #evaluation-metrics #cross-validation #probability-distributions #workflow-orchestration

## The Problem
A typical mid-size church facility hosts Sunday worship (multiple services), Wednesday evening programs, youth group, children's ministry, recovery groups (AA, Celebrate Recovery), women's and men's Bible studies, community meals, food pantry operations, music rehearsals, staff meetings, and external rentals — all competing for the same fellowship hall, sanctuary, kitchen, classrooms, and parking lot. Scheduling collisions are constant: the youth group sets up the gym for dodgeball at the same time the women's ministry expected it for a banquet. Setup and teardown times aren't tracked, so back-to-back bookings leave no transition window. AV equipment gets double-committed because it lives in a separate sign-out sheet.

## What Already Exists
Google Calendar, Microsoft Bookings, and tools like Skedda handle basic room reservation. Planning Center has a "Rooms" feature. But none of these understand the compound dependencies of church scheduling: booking the sanctuary for a concert also requires the sound booth, three AV volunteers, 200 chairs in concert configuration (not Sunday morning rows), and a 90-minute teardown window before the next event. Generic tools treat rooms as independent resources rather than interconnected systems.

## The Customisation Gap
The scheduling system needs to model rooms as configurable spaces with named layouts (sanctuary: "rows," "concert," "round tables," "empty"), attach resource dependencies (AV cart, projector, kitchen access, nursery staffing) to events rather than rooms, enforce setup/teardown buffers calculated from layout-change complexity, and predict demand patterns to recommend optimal time slots for new recurring events. A regression model trained on historical booking data can estimate realistic setup times based on event type and configuration change, replacing the current guesswork that causes cascading delays every weekend.

## Impact If Solved
Eliminates the 3-5 scheduling conflicts per month that currently require last-minute room swaps, volunteer scrambles, and strained inter-ministry relationships. Facility managers save 4-6 hours weekly on coordination calls and emails.
