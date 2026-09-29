# Propensity Modelling Applied to Attendance

**Niche:** [[niches/scheduling-booking-platforms/no-show-and-attendance/profile|No-Show & Attendance]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Propensity and uplift modelling are standard in marketing and credit, with mature libraries and a large literature, and appointment attendance is a textbook instance nobody has modelled.
**Tags:** #gradient-boosting #logistic-regression #causal-inference #cross-validation #evaluation-metrics #confidence-intervals #hypothesis-testing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict which bookings will not be honoured and intervene on the ones worth intervening on — and whoever raises attendance takes the account, because the slot cannot be sold twice and the operator counts the loss every week.

## The Problem
Predicting a binary behaviour from historical features and then deciding whom to target with a costly intervention is the canonical propensity-plus-uplift problem, solved repeatedly in direct marketing, collections and credit. Appointment attendance has clean labels, abundant volume, stable features and an intervention with a measurable cost. The healthcare literature has even modelled it specifically. The scheduling category uses none of it.

## What Already Exists
Gradient boosting and regularised regression for propensity, with excellent free implementations; uplift and treatment-effect modelling libraries; calibration methods; experiment design and sequential testing frameworks; and a published healthcare no-show prediction literature with known feature sets and reported performance. Every platform holds years of labelled outcomes.

## The Customization Gap
The adaptation is to a small-business, multi-tenant, cross-sector setting. It requires: (1) pooled modelling with per-tenant adaptation, since a single salon has too few appointments to fit anything and the vendor has millions across thousands of them, which makes hierarchical or transfer-based approaches the right shape and is the central adaptation; (2) uplift rather than propensity as the deployment target, because the useful question is who changes behaviour when contacted and not who is likely to miss — a customer certain to attend and one certain to miss both waste the intervention; (3) an economic objective, weighting each booking by the slot's value and the intervention's cost and friction, since a deposit request has a real cost in abandoned bookings that a pure accuracy metric ignores; (4) fairness scrutiny, because features correlated with income, neighbourhood or first-time status can produce systematically harsher treatment of some customers, and a deposit requirement is a real access barrier — this needs measuring and bounding rather than assuming; and (5) continuous experimentation built in, since the intervention changes the behaviour being modelled and a system with no holdout will drift into confident nonsense.

## Target Customer
Scheduling and booking platform vendors, vertical platforms with booking modules, and the payment providers who supply the deposit mechanism.

## Impact If Solved
Every technique required is mature and the data is unusually clean, which makes this one of the best-posed problems in this part of the vault. Pooled-with-adaptation modelling is what makes it work for small operators, and the fairness bound is the constraint that keeps the intervention defensible.
