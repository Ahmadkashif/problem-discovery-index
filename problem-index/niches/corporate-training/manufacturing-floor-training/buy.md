# Visual SOP Platform with Skills Matrix Integration

**Niche:** [[niches/corporate-training/manufacturing-floor-training/profile|Manufacturing Floor Skills Training]]
**Industry:** [[industries/corporate-training|Corporate Training]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Poka and SwipeGuide digitize SOPs with visual instructions, but they don't integrate with the plant's skills matrix — the training coordinator maintains a separate spreadsheet tracking which workers are qualified on which machines.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
Manufacturing plants maintain a skills matrix: a grid mapping every worker to every machine/process they are qualified to operate, with qualification levels (trainee, qualified, trainer) and expiration dates for recertification. This matrix drives daily work assignments — a production supervisor cannot assign a worker to a machine they're not qualified on. The skills matrix lives in a spreadsheet, updated manually when a supervisor signs off on a training completion. Meanwhile, SOP access platforms (Poka, SwipeGuide) track which SOPs a worker has viewed but do not update the skills matrix when training is completed.

## What Already Exists
Poka provides connected worker SOP access with interactive work instructions, knowledge sharing, and problem-solving on tablets. SwipeGuide offers visual step-by-step guides with completion tracking. Both serve the SOP access and training delivery function well. Skills matrix management is handled by spreadsheets, Competency Manager (ag5), or modules within MES/ERP systems.

## The Customization Gap
A bidirectional integration between visual SOP platforms and skills matrix systems that: (1) when a worker completes a training sequence in the SOP platform (views all required instructions, passes the knowledge check), the skills matrix is automatically updated with a "training complete — awaiting supervisor verification" status; (2) the supervisor receives a mobile prompt to observe and verify the skill, with a one-tap sign-off that updates the skills matrix to "qualified"; (3) recertification deadlines are calculated from the qualification date and pushed back to the SOP platform as re-training assignments; and (4) the production scheduler can query the skills matrix to determine available qualified workers per machine.

## Target Customer
Training Coordinators at manufacturing plants with 200+ floor workers who maintain skills matrices in spreadsheets and manually reconcile training completions from SOP platforms with qualification records.

## Impact If Solved
Eliminates 5-10 hours per week of manual skills matrix maintenance, ensures qualification records are always current (reducing the risk of assigning unqualified workers to machines), and creates a closed-loop training-to-qualification pipeline that currently requires 3-4 manual handoff steps.
