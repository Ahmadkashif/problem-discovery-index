# Hazard Analysis From Safety Engineering

**Niche:** [[niches/ai-red-teaming-firms/domain-harm-taxonomies/profile|Domain Harm Taxonomies]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Process and clinical safety built systematic hazard identification precisely because unaided brainstorming misses the hazards that matter, and harm enumeration here is a brainstorm.
**Tags:** #compliance #graph-theory #evaluation-metrics #hypothesis-testing #descriptive-statistics #tacit-knowledge-ml #worker-facing #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to enumerate what actually goes wrong in one regulated deployment rather than what goes wrong in general — and whoever does that takes the account, because the generic list is the part the client already has.

## The Problem
Enumerating what can go wrong in a system, systematically enough that the important cases are not missed, is the founding problem of safety engineering. It produced structured methods — guide words applied to each element of a process, failure mode and effects analysis, systems-theoretic approaches that look at unsafe control actions rather than component failures — all designed specifically because unaided expert brainstorming reliably misses hazards. Harm enumeration for AI deployments is unaided expert brainstorming.

## What Already Exists
Guide-word based hazard identification applied systematically across a process; failure mode and effects analysis with severity, occurrence and detectability scoring; systems-theoretic process analysis focused on unsafe control actions; bow-tie analysis linking causes, events and consequences; and clinical incident taxonomies built from reported harm.

## The Customization Gap
The adaptation is to a system whose failures are in what it says rather than in what it does. It requires: (1) guide words adapted to language outputs — omitted, overconfident, inappropriate register, plausible but wrong, correct but non-compliant — which is a small vocabulary exercise with a large payoff, since guide words are what make the enumeration systematic rather than imaginative; (2) the systems-theoretic frame, which fits unusually well here because the relevant question is what unsafe action the system's output could cause a human to take, and that is exactly what unsafe control action analysis addresses; (3) detectability scored explicitly, since a wrong answer a practitioner would immediately notice and one they would not are different hazards and the failure mode scoring convention already includes this dimension; (4) incident taxonomies from the sector as a starting point, since clinical and financial incident reporting already categorises real harms and nobody has mapped those onto model failures; and (5) a workshop format that a domain practitioner can participate in without security expertise, which is how safety hazard analysis is actually run and is the practical delivery mechanism.

## Target Customer
Assessment firms, regulated deployers, domain practitioners, and the safety engineering profession for whom this is a live application area.

## Impact If Solved
Safety engineering built systematic hazard identification because brainstorming misses what matters, and this field brainstorms. Guide words adapted to language outputs, and the unsafe-control-action frame, are the two transfers that make enumeration systematic.
