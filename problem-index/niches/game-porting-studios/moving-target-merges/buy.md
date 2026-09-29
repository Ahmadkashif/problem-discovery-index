# Fork Management From Open Source Maintenance

**Niche:** [[niches/game-porting-studios/moving-target-merges/profile|Moving-Target Merge Management]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Long-lived downstream forks solved staying in sync with a moving upstream, and porting studios merge by hand every fortnight.
**Tags:** #automation #workflow-orchestration #data-integration #graph-theory #evaluation-metrics #sets-and-logic #descriptive-statistics #compliance
**Contested on:** Every serious competitor in this niche is fighting to keep a port synchronised with a codebase that ships every fortnight without redoing the platform work each time — and whoever automates that merge takes the account.

## The Problem
Maintaining a long-lived fork against a moving upstream is a well-worn problem with well-worn answers. Linux distributions, downstream vendors and enterprise forks all keep local changes as a reviewable patch series, rebase them onto each upstream release, automate conflict detection, and deliberately upstream what they can to shrink the divergence. The practices are documented and the tooling exists. A port is exactly a long-lived downstream fork.

## What Already Exists
Patch series management and rebasing; automated conflict detection on upstream import; divergence tracking and reporting; upstreaming workflows; and continuous integration against upstream head.

## The Customization Gap
The adaptation is to a fork that can never be upstreamed and a codebase full of binary assets. It requires: (1) no upstreaming path, since the client will not take platform changes for a platform they do not ship — this is the substantive difference and removes the main mechanism forks use to shrink divergence; (2) binary assets and engine data alongside source, where text-based patch tooling does not apply; (3) a fork with a defined end date rather than indefinite maintenance, changing the cost calculus; (4) changes driven by performance and memory that are diffuse rather than localised; and (5) a client who does not structure their repository with a downstream in mind.

## Target Customer
Porting studios, build and tools engineering, publishers, and version control and fork management vendors.

## Impact If Solved
Downstream fork maintenance is a solved practice with documented tooling. No upstreaming path and a codebase full of binary assets is what removes the main mechanism and forces a different structure.
