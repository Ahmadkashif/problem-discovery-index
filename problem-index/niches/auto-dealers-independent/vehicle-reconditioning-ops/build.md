# Independent Dealer Recon Workflow Manager

**Niche:** [[niches/auto-dealers-independent/vehicle-reconditioning-ops/profile|Vehicle Reconditioning Operations]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No reconditioning management tool is designed for independent dealers who use a mix of in-house and external vendors — franchise-focused recon tools assume a single reconditioning center that independents don't have.
**Tags:** #automation #workflow-orchestration #data-integration #revenue-impact

## The Problem
An independent dealer reconditioning 30 vehicles per month uses their on-site mechanic for basic work, sends body work to Joe's Body Shop, sends interior repairs to a mobile upholsterer, and uses two different detail shops depending on availability. Managing this requires the recon manager to: assign work via text message to each vendor, track which vehicles are at which vendor, follow up on completion status, collect and reconcile invoices, and maintain a running cost total per vehicle. With 30 vehicles in various stages across 5 vendors, things get lost — a car sits at the body shop for an extra week because nobody followed up, costing $250 in holding cost.

## Why Nobody Has Built This
Franchise-focused recon tools (Rapid Recon, ReconVelocity) model a linear workflow through a single recon center with internal staff. Independent dealers have a networked workflow across external vendors, each operating independently. Building for independents requires modeling vendor relationships, communication preferences (some vendors only respond to texts, others use email), and variable workflows (some cars need body + detail + mechanical, others need detail only). The per-dealer revenue is lower than franchise ($100-200/month vs. $500-1,000/month), and the vendor coordination problem is harder to solve than the internal-center problem.

## What to Build
A mobile-first recon management tool that lets the recon manager: create a recon plan per vehicle (checklist of needed work items from inspection), assign each work item to an internal tech or external vendor (with automated notification via text/email), track vehicle location and work status via vendor updates (vendors respond to a simple text prompt: "Car done? Reply YES/NO"), monitor cost accrual per vehicle in real time (budget vs. actual), and alert when any vehicle exceeds time or cost thresholds. Dashboard shows all vehicles in recon with current status, location, cost, and days elapsed.

## Target Customer
Independent dealers reconditioning 15+ vehicles per month across 3+ vendors, currently managing the process via whiteboard, text messages, and memory.

## Impact If Built
Reduces average recon cycle time from 10-15 days to 5-8 days, saving $175-350 per vehicle in holding costs. On 30 vehicles/month, that's $5K-10K/month in recovered margin. Prevents cost overruns by alerting when a vehicle's recon cost exceeds the budget set at acquisition — currently discovered only when the invoice arrives weeks later.
