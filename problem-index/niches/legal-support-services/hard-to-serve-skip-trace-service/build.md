# Serve Probability for a Located Subject

**Niche:** [[niches/legal-support-services/hard-to-serve-skip-trace-service/profile|Hard-to-Serve & Skip-Trace Service]]
**Industry:** [[industries/legal-support-services|Legal Support Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Skip-trace tools say where someone probably lives; nothing says when and how that person can actually be handed papers before the deadline, which is the judgement the best hard-serve specialists sell.
**Tags:** #tacit-knowledge-ml #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to locate and serve the defendant who does not want to be found inside the service window, and whoever converts the most dead-address and evasive files into valid service before the court's deadline takes the litigator's account.

## The Problem
After a skip trace returns three candidate addresses, the specialist decides which to try first, at what times, whether to stake out, whether the subject's workplace is a better bet, and when the diligence is enough to ask for alternative service. Juniors burn days on low-probability addresses.

## Why Nobody Has Built This
Hard serves are a small share of volume and recorded inconsistently; the specialists who are good at them are one-person businesses whose method is their brand. Skip-trace vendors sell location, not service, and have no outcome data on what happened at the door.

## What to Build
A model trained on hard-serve histories — candidate addresses and their sources, attempt sequences, stakeout logs, workplace attempts and outcomes — that ranks candidate addresses by serve probability, recommends the next tactic and window, and estimates time-to-service against the remaining days in the window, so the attorney knows early whether to file for an extension or substituted service.

## Target Customer
Hard-serve specialists and the litigation firms that hire them; national networks that route rush and evasive work to their best servers.

## Impact If Built
Fewer cases slipping past the service window, earlier motions for alternative service where they are warranted, and a junior server who plans like a veteran.
