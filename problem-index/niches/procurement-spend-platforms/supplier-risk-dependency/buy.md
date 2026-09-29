# Network Resilience Methods From Reliability Engineering

**Niche:** [[niches/procurement-spend-platforms/supplier-risk-dependency/profile|Supplier Risk & Dependency]]
**Industry:** [[industries/procurement-spend-platforms|Procurement & Spend Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Reliability engineering has a century of method for analysing how a system fails, where its single points of failure are and how redundancy should be placed, and supply chain risk uses a heat map with three colours.
**Tags:** #graph-theory #monte-carlo-methods #probability-distributions #optimization-fundamentals #confidence-intervals #evaluation-metrics #survival-analysis #hypothesis-testing
**Contested on:** Every serious competitor in supplier risk is fighting to tell a company which single supplier failure would actually stop its operations — and whoever maps dependency rather than scoring suppliers takes the account.

## The Problem
A supply chain is a system with components, dependencies, redundancies and failure modes, and the discipline that analyses exactly that — fault tree analysis, failure mode and effects analysis, single point of failure identification, redundancy allocation, availability modelling — has been standard in engineering for decades. Supply chain risk assessment instead produces a matrix of likelihood against impact, scored qualitatively in a workshop, rendered as a heat map. The engineering department two floors away would not accept that analysis for a product and produces it for the supply base.

## What Already Exists
Reliability engineering methodology is mature and documented: fault trees, failure modes and effects analysis, reliability block diagrams, Monte Carlo availability simulation and redundancy optimisation. Graph analysis libraries are free. Network resilience analysis has a substantial literature in infrastructure and telecommunications. Supply chain network design tooling exists at the enterprise end. Every method required is established in adjacent disciplines.

## The Customization Gap
The adaptation is to a supply network whose redundancy is contractual and qualification-bound rather than physical. It requires: (1) redundancy modelled as qualified and available rather than as existing, since an alternative supplier who has not been qualified is not redundancy and counting it is the most common error in supply risk assessment; (2) recovery time rather than probability as the primary output, because the probability of a given supplier failing is genuinely hard to estimate and the time to recover from it is not, and the second is more actionable than a poorly estimated first; (3) correlated failure modelled explicitly, since suppliers in the same region, the same tier-two source or the same logistics corridor fail together and independence assumptions are exactly what has failed in real disruptions; (4) redundancy allocation as an optimisation — where should the next qualification investment go to reduce the most exposure per dollar — which is the decision the function actually makes and currently makes by judgement; and (5) outputs framed for a board, since the audience is not an engineer and revenue at risk with a recovery timeline is the language that lands.

## Target Customer
Manufacturers, supply chain risk functions, third-party risk vendors, and the business continuity and enterprise risk teams who present to boards.

## Impact If Solved
Importing reliability engineering replaces a qualitative heat map with an analysis of the same rigour the organisation applies to its own products. Modelling redundancy as qualified rather than nominal is the specific correction that matters most, because it removes the false comfort that dominates current supply risk assessments.
