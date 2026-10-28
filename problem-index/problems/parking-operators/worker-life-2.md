# The Remote Agent Behind Three Hundred Gate Intercoms

**Industry:** [[parking-operators|Parking Operators]]
**Type:** Worker Life Changing
**One-liner:** When an unstaffed garage's gate will not open, a remote agent answers the intercom, works out the problem from a camera and four systems, and decides whether to raise the arm, all while the next driver is honking.
**Tags:** #large-language-models #transformers #bert #worker-facing #automation #workflow-orchestration #quick-win

## The Problem
As operators take cashiers out of booths, the help button at the exit lane rings a remote agent instead. One agent covers hundreds of lanes across many garages, often overnight. Each call is a driver who cannot get out. Their card was declined, the ticket is lost, a validation from the restaurant did not scan, a monthly card has lapsed, the plate camera misread a dirty plate, the app shows a reservation the PARCS does not, or the gate is broken. The agent has a few seconds of video, the PARCS transaction screen, the reservation portals and the monthly-account list. They have to decide whether to charge a lost-ticket fee, take a card number by voice, or raise the arm and log it. Each garage has its own owner rules on fees and overrides. At a busy exit after an event, calls stack faster than they can be answered and cars back up into the street.

## Why It Matters to the Worker
The calls are tense. Drivers are angry, sometimes abusive, and many assume a person is choosing not to let them out. The agent is judged on two things that pull against each other: answer and clear calls fast, and do not give away revenue with free gate raises. Every raise is a mark against them on the revenue-control report, yet refusing one on a broken lane creates a complaint and a queue. They switch between several logins, re-type plate numbers, and keep the override rules for each garage in their head or in a binder. Overnight shifts are long and lonely, and the job has the turnover of any call centre.

## What a Solution Looks Like
A voice assistant answers first and handles the routine cases itself. It reads the plate and finds the session, checks the reservation and the monthly account, takes payment, and applies the garage's lost-ticket rule. It passes the agent only the calls that need judgement, with a one-line summary: what the driver says, what the systems show, which rule applies and what it recommends. For a gate raise, it logs the reason and the evidence automatically, so the revenue-control report shows why the arm went up. The agent spends their attention on the genuinely stuck driver and the broken lane.

## Impact If Solved
If an assistant clears ~50–60% of intercom calls without a person (estimate), an agent covering 300 lanes handles about half as many calls a shift. Each gate raise then carries a recorded reason instead of an unexplained override, and in a call centre where most of the job is repeat cases, the agent is left with the work that needs a person.
