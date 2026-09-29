# Test Automation From Software Delivery

**Niche:** [[niches/game-porting-studios/cross-platform-verification/profile|Cross-Platform Verification]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software made automated regression testing across target environments standard, and game porting verifies by playing.
**Tags:** #automation #workflow-orchestration #evaluation-metrics #data-integration #change-point-detection #compliance #confidence-intervals #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to verify every change on every platform when verification means people playing the game and the client keeps shipping updates — and whoever automates that takes the account.

## The Problem
Software delivery solved regression testing across environments: automated suites run on every change, across a matrix of target platforms, with results reported per environment and failures traced to the change that caused them. Test selection narrows the run to what the change affects. The infrastructure is commoditised and the practice is universal. Game porting runs the same matrix — change by platform — entirely by hand.

## What Already Exists
Automated regression suites; matrix execution across target environments; change-scoped test selection; failure attribution to commits; and continuous reporting per environment.

## The Customization Gap
The adaptation is to a real-time interactive application whose correct output is a rendered frame. It requires: (1) assertions over rendered output and frame timing rather than over return values, so the oracle problem is genuinely different and is the substantive difference; (2) input that is controller state over time, requiring deterministic playback; (3) console devkits as the execution environment, with licensing and infrastructure constraints no test farm assumes; (4) legitimate cross-platform differences that must be tolerated while real divergence is caught; and (5) a game whose own non-determinism must be controlled before any comparison is meaningful.

## Target Customer
Porting studios, publisher QA organisations, platform holders, and test automation vendors.

## Impact If Solved
Software made matrix regression testing standard and commoditised the infrastructure. Assertions over rendered frames and controller playback on devkits is the oracle problem that has to be solved before any of it transfers.
