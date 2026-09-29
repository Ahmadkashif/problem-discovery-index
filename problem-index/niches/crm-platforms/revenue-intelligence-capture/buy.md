# Experimentation Infrastructure for Sales Coaching

**Niche:** [[niches/crm-platforms/revenue-intelligence-capture/profile|Revenue Intelligence & Capture]]
**Industry:** [[industries/crm-platforms|CRM Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Online experimentation platforms are mature commodity infrastructure that product organisations run hundreds of tests a year on, and the sales organisation in the same building rolls out coaching programmes to everyone and measures adoption.
**Tags:** #hypothesis-testing #causal-inference #confidence-intervals #evaluation-metrics #cross-validation #descriptive-statistics #workflow-orchestration #revenue-impact
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A sales organisation rolls out a new discovery framework to all two hundred representatives. Six months later win rate is up two points, or down one, and nobody can attribute either to the framework because the market moved, the product changed, three competitors repriced and forty representatives turned over. The same company's product team would never ship a change of comparable cost without a controlled test, and has the infrastructure to run one sitting in the building.

## What Already Exists
Experimentation platforms — both commercial and open — provide assignment, exposure tracking, sequential testing, variance reduction and analysis as standard. The methodology for cluster-randomised and stepped-wedge designs, which is what a sales organisation needs, is well developed in clinical and education research. Power analysis tooling is free. Everything required to test a coaching intervention properly exists and is used daily two floors away.

## The Customization Gap
The adaptation is to an organisation where the unit of randomisation is a person with a quota. It requires: (1) cluster randomisation at the team or territory level rather than the individual, since representatives on a team talk to each other and individual assignment contaminates immediately; (2) power analysis stated up front, because most sales organisations are too small to detect the effect sizes being claimed and saying so honestly is more useful than an underpowered result presented as evidence; (3) stepped-wedge designs as the practical default, where every team eventually receives the intervention and the order is randomised — which removes most of the fairness objection to withholding coaching from a group whose pay depends on performance; (4) outcome measures that account for the long sales cycle, since a coaching change tested against quarterly bookings measures very little when deals take nine months, and leading indicators have to be chosen carefully; and (5) explicit handling of the compensation dimension, because a representative who believes an experiment cost them commission is a serious problem and the design should make that impossible rather than unlikely.

## Target Customer
Large sales organisations with enough teams to randomise, enablement functions whose programmes are evaluated by attendance, and the revenue intelligence vendors whose coaching claims are currently untested.

## Impact If Solved
Enablement spend is substantial and is allocated on belief, and the infrastructure to allocate it on evidence is already licensed by the same company. Stepped-wedge design is the specific adaptation that makes this politically feasible in an organisation where withholding a supposed advantage from a quota-carrying team is otherwise unacceptable.
