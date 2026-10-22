# Electric Outage Management Adapted to Cable Plant

**Niche:** [[niches/wired-broadband-providers/hfc-plant-maintenance/profile|HFC Plant Maintenance & Proactive Network Maintenance]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Electric utilities have long inferred the failed device upstream of a cluster of customer calls and smart-meter alarms; cable operators face the same tree-shaped inference problem with richer data and weaker tooling.
**Tags:** #graph-theory #bayesian-inference #feature-engineering #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to locate an outside-plant impairment from modem telemetry before customers call, and whoever sends the right crew to the right span first, without a premises visit, takes the account.

## The Problem
HFC plant is a tree: node, amplifiers, taps, drops. When a set of modems degrades together, the fault is almost always at the deepest element they share. Cable operators reason about this by eye, on PNM screens and paper strand maps.

## What Already Exists
Electric distribution utilities run outage management systems (Oracle Utilities Network Management, GE and Schneider ADMS products) that take customer calls and AMI meter "last gasp" messages, trace them up the connectivity model and predict the protective device that operated, then dispatch crews and track restoration.

## The Customization Gap
The adaptation needs: a connectivity model built from cable strand maps (node, amplifier cascade, tap ports) with span lengths; inputs that are graded degradations rather than binary outages (pre-equalization echo, spectrum notches, codeword errors), so inference is probabilistic rather than "which fuse blew"; integration with PNM echo-distance estimates to choose between candidate elements; and maintenance work orders rather than restoration crews as the output.

## Target Customer
Network operations leaders at cable operators and telcos, particularly those whose parent companies or partners already run an electric OMS (co-op and municipal broadband providers).

## Impact If Solved
A proven inference pattern from a neighbouring utility gives cable operators upstream fault prediction without a greenfield build, and electric co-ops entering broadband can extend a system their staff already know.
