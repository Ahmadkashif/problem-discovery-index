# Scheduling Against Availability That Is Actually True

**Niche:** [[niches/restaurant-tech-platforms/labor-scheduling-availability/profile|Labour Scheduling & Availability]]
**Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Auto-scheduling fails because it is built on stated availability, and stated availability is a form an employee filled in once — the real thing is visible in months of accepted, declined, swapped and no-showed shifts.
**Tags:** #logistic-regression #gradient-boosting #optimization-fundamentals #combinatorics-and-counting #confidence-intervals #evaluation-metrics #worker-facing #automation
**Contested on:** Every serious competitor in restaurant scheduling is fighting to produce a schedule that respects who can genuinely work, so the manager stops spending the week on the phone finding cover — and whoever gets the share of shifts that survive the week highest takes the account.

## The Problem
An employee's availability form says weekday evenings. In practice they have declined every Monday for two months because of a class, they will pick up a Saturday lunch if asked directly, and they have never once worked past ten on a weeknight without swapping out. The manager knows all of this. The auto-scheduler knows the form. So the generated schedule assigns Monday evening, the employee cannot work it, and the manager spends Tuesday on the phone. After two such weeks the manager stops using auto-scheduling and goes back to the afternoon with a spreadsheet, which is exactly what has happened across the category.

## Why Nobody Has Built This
Vendors treat stated availability as an input to be trusted because it is what the employee provided and because inferring otherwise feels presumptuous — and the products have never framed inferred availability as what it is, a way to stop asking people to work shifts they cannot work. There is also a genuine care requirement: inferences about when someone can work can shade into inferences about their life, and a system that quietly learns an employee is unavailable Thursdays and stops offering Thursdays has affected their income without telling them. That is a design problem with a good answer — show the employee what the system believes and let them correct it — and it has been used as a reason not to try.

## What to Build
An availability model learned from behaviour and made visible to the person it describes. Accepted, declined, swapped, traded and no-showed shifts over months yield a probability that this employee works a given shift, by day, by time, by notice given. That probability replaces the form as the scheduling input, with the form as a hard constraint where the employee has set one. The schedule is then a constrained optimisation against the demand forecast: coverage by skill and station, labour cost target, overtime and minor restrictions, predictive scheduling compliance, and the soft preferences that make a schedule liveable. Crucially, every employee sees their own inferred availability and can correct it directly, which both fixes errors and keeps the system honest — a worker should never discover their hours dropped because a model inferred something about them silently.

## Target Customer
Restaurant scheduling vendors, multi-unit operators where manager scheduling time is a measurable cost, and independents whose general manager loses a shift a week to the puzzle.

## Impact If Built
A manager's week contains an afternoon of scheduling and several hours of phone calls, and a schedule that survives removes most of both. For employees, being offered shifts they can actually work is a direct improvement in a job where scheduling friction is a leading source of dissatisfaction — and transparency about the inference is what separates that from surveillance.
