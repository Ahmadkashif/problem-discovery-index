# Cross-Program Client Dashboard

**Niche:** [[niches/nonprofits-social-services/rural-community-action-agencies/profile|Rural Community Action Agencies]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Case management platforms like Apricot and ETO track individual programs but cannot provide a unified client view across LIHEAP, Head Start, weatherization, housing, and employment programs within a single CAA.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
A rural CAA family may simultaneously receive LIHEAP energy assistance, Head Start for their preschooler, weatherization services for their home, and employment services for a parent. Each program tracks the family in a separate system — ChildPlus for Head Start, a state LIHEAP database, Apricot for CSBG-funded services. No case manager can see the full picture of services a family receives, leading to duplicated intake interviews, missed referral opportunities, and inability to track whole-family outcomes. When the family's circumstances change (job loss, move, new baby), the information must be updated in 4 separate systems.

## What Already Exists
Apricot (Social Solutions), ETO (Bonterra), and Penelope provide general nonprofit case management. ChildPlus handles Head Start. State systems handle LIHEAP and TANF. Power BI and Tableau can aggregate data for reporting. However, none of these tools can serve as a single-pane-of-glass across the heterogeneous program-specific systems a CAA operates.

## The Customization Gap
The missing layer is a lightweight integration dashboard that reads from multiple program databases (via API or nightly data extract), presents a unified family profile showing all active services, flags when a life change in one program should trigger a referral or update in another, and provides the case manager with a single place to view the family's journey across all programs without replacing any existing system.

## Target Customer
Program managers at CAAs operating 5+ simultaneous federal and state programs who cannot see cross-program client engagement.

## Impact If Solved
Eliminates 40% of redundant intake interviews (families tell their story once, not five times), increases cross-program referrals by 35%, and enables whole-family outcome tracking that funders increasingly require.
