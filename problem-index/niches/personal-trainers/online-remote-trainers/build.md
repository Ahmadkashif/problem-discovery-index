# Client Priority Queue with Auto-Generated Adjustment Recommendations

**Niche:** [[niches/personal-trainers/online-remote-trainers/profile|Online Remote Trainers]]
**Industry:** [[industries/personal-trainers|Personal Trainers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform analyzes an online trainer's 50+ client check-ins and ranks which clients need immediate attention, which are on track, and which need program adjustments — forcing trainers to review every client identically regardless of urgency.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #ai-agent #workflow-orchestration

## The Problem
An online trainer with 50 clients receives 50 weekly check-ins, each containing weight, measurements, training logs, nutrition logs, and sometimes progress photos. Reviewing each check-in takes 10-20 minutes — 8-16 hours per week on review alone. Experienced trainers develop pattern recognition for which clients need intervention: a client whose weight spiked while training adherence was high likely has a water retention issue, not a diet problem; a client whose strength plateaued but measurements are still improving is fine. This tacit knowledge about what matters in check-in data determines which clients get thoughtful adjustments and which get "keep going." But the trainer reviews them linearly — alphabetically or by submission order — wasting time on clients who are progressing normally while potentially missing urgent cases buried later in the queue.

## Why Nobody Has Built This
Trainerize and TrueCoach display check-in data but don't analyze it — they're data collection tools, not intelligence tools. Building a priority queue requires understanding what "needs attention" means in context: a 2-pound weight gain means different things for a client in a caloric surplus trying to build muscle vs. a client in a deficit trying to lose fat. The adjustment logic is goal-dependent, phase-dependent (cutting vs. bulking vs. maintaining), and individually calibrated (some clients' weight fluctuates 3-5 pounds daily from water retention). Encoding this coaching judgment into software requires deep fitness domain expertise combined with ML capability.

## What to Build
A coaching intelligence layer that: (1) ingests check-in data from Trainerize/TrueCoach via API or from a native check-in system, (2) scores each client on urgency based on goal-relative progress trends (not absolute numbers), (3) ranks the weekly review queue so the trainer addresses the most urgent clients first, (4) auto-generates adjustment recommendations for straightforward cases (e.g., "Client progressing normally — suggest increasing squat by 5 lbs, maintain current calories"), and (5) flags anomalies that require human judgment (sudden weight swings, reported pain, missed training sessions). The trainer focuses creative energy on complex cases and approves AI recommendations for routine ones.

## Target Customer
Online personal trainers managing 30-100+ remote clients who spend 8-16 hours per week on check-in review and program adjustment.

## Impact If Built
Reduces weekly client review time by 40-60% (saving 4-8 hours per week), improves client outcomes by ensuring high-priority clients get attention first, and enables trainers to scale from 40-50 clients to 80-100 without quality degradation — doubling revenue capacity from $8K-10K/month to $15K-20K/month.
