# Work-in-Progress Capacity Dashboard

**Niche:** [[niches/alterations-tailoring/pricing-turnaround-estimation/profile|Pricing & Turnaround Estimation]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Production management dashboards exist for manufacturing but none are scaled to the alterations shop workflow — where 50-200 garments are in varying stages of completion with different complexity levels and customer-promised deadlines.
**Tags:** #workflow-orchestration #time-series-forecasting #tabular-ml #automation

## The Problem
When a customer asks "when will this be ready?", the tailor glances at the rack of garments waiting to be done, makes a mental estimate, and says "Thursday." But the rack has garments of wildly different complexity — some are 10-minute hems, others are 90-minute jacket reconstructions. The tailor's mental estimate doesn't account for how many of those garments are due before this one, or whether tomorrow's appointments will add 15 more garments to the queue. The result: overcommitment during busy periods (leading to missed deadlines) and unnecessary conservatism during slow periods (quoting 5 days when 2 is realistic, losing urgency-driven customers).

## What Already Exists
Kanban boards (Trello), production dashboards (Monday.com), and manufacturing MES systems track work-in-progress across stages. These tools handle project-based or manufacturing workflows but not the high-volume, short-cycle alterations workflow where each "project" takes 15-90 minutes and the queue changes 20-30 times per day with new intake and completions.

## The Customization Gap
The dashboard needs to show: total garments in queue (segmented by estimated work time), committed delivery dates for each garment, daily capacity (based on staffing and historical throughput), and a capacity forecast ("if you promise 3-day turnaround on this intake, you'll be at 110% capacity on Wednesday — suggest 4 days instead"). The system learns the shop's actual throughput by tracking intake-to-completion times, adjusting capacity estimates to match reality rather than aspiration.

## Target Customer
Alterations shops processing 20+ garments per day that experience periodic overcommitment (missed deadlines during busy weeks) and want data-driven turnaround promises.

## Impact If Solved
Reduces missed deadline rate from 15-20% to under 5%, prevents overcommitment during peak periods, and enables accurate turnaround promises that build customer trust and allow the shop to charge premium pricing for genuine rush service.
