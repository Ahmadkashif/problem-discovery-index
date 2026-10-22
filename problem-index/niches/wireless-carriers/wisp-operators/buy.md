# Subscription Billing Built for Towers and Sectors

**Niche:** [[niches/wireless-carriers/wisp-operators/profile|Fixed Wireless ISPs (WISPs)]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic subscription billing handles invoices and payments but has no idea which tower and sector a customer hangs off, which is the first question in every outage and every upgrade decision.
**Tags:** #feature-engineering #data-integration #workflow-orchestration #automation #quick-win
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to deliver advertised speeds to rural homes over fixed wireless, but the contest splits in two. Before the sale it is qualifying a specific roofline correctly; after the sale it is keeping evening-peak experience inside the plan on shared and often unlicensed spectrum. The data, people, clocks and vendors differ, so the niche is decomposed into contested sub-niches below.

## The Problem
When a sector fails, the WISP needs to know who is affected, notify them, credit them if needed, and log it for FCC and state reporting. When a sector is full, it needs to know which customers to move or upgrade. Generic billing knows plans and payment status only.

## What Already Exists
General subscription billing (Chargebee, Stripe Billing, QuickBooks) and WISP-specific billing such as Sonar, Splynx and Visp, which add some network awareness.

## The Customization Gap
The adaptation needs the network topology as a first-class object (tower, sector, access point, customer radio), outage-to-customer mapping with automatic notices and credits, plan-to-sector capacity accounting, and exports in the location formats the FCC's Broadband Data Collection requires.

## Target Customer
Smaller WISPs still on generic billing, and WISP billing vendors adding network intelligence.

## Impact If Solved
Outages are communicated in minutes, credits follow policy, and capacity decisions are made per sector rather than by hunch.
