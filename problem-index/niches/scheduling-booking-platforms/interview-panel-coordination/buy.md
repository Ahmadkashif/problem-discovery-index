# Timetabling Research Applied to Hiring

**Niche:** [[niches/scheduling-booking-platforms/interview-panel-coordination/profile|Interview Panel Coordination]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** University examination timetabling is a decades-old research field that places thousands of constrained events across people and rooms, and interview panels are the same problem at a hundredth of the scale.
**Tags:** #convex-optimization #dynamic-programming #graph-theory #optimization-fundamentals #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to place a multi-person interview panel across busy calendars in one pass, with the sequence and eligibility constraints satisfied — and whoever does that takes the talent acquisition account, because panel scheduling is the coordinator's entire week.

## The Problem
Timetabling — placing constrained events involving overlapping sets of people and resources, with precedence, capacity and preference constraints — has an international research community, standard benchmark problems, published algorithms and open solvers. Instances with thousands of events are solved routinely. A five-person interview panel is a trivially small instance of the same problem and is solved by a person with a messaging application.

## What Already Exists
Constraint programming and mixed-integer solvers, free and fast; the timetabling literature with benchmark datasets and competition results; graph colouring formulations for conflict avoidance; employee rostering research for the load-balancing half; and calendar APIs supplying free-busy. Everything needed is published, tested and available at no cost.

## The Customization Gap
The adaptation is to human interviewers whose availability is soft and whose consent matters. It requires: (1) treating declared availability as a prior rather than as truth, since interviewers hold provisional time, accept things they will move and protect undeclared focus time — which means proposing rather than assigning, and re-solving when reality disagrees; (2) an objective centred on candidate experience and elapsed time, because the candidate is the party who leaves, and most scheduling tooling optimises the opposite way; (3) fatigue and equity constraints on interviewers, so the willing are not exhausted — a load-balancing objective with hard caps, which is where rostering research applies directly; (4) explicability, since a coordinator will override a solution they do not understand and their override is usually informed by something the model does not know; and (5) minimal-change repair as the primary mode rather than the exception, because reschedules outnumber initial placements and a repair that moves everything is worse than useless.

## Target Customer
Applicant tracking and interview coordination vendors, scheduling platform vendors moving into hiring, and large talent acquisition functions with dedicated coordination teams.

## Impact If Solved
A mature research field addresses a far smaller instance of the same problem and has never been applied here. Soft availability and minimal-change repair are the two adaptations, and the candidate-centred objective is the design choice that separates a useful product from a scheduling display.
