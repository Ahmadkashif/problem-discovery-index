# Nobody Knows What the Company Has Promised

**Niche:** [[niches/contract-lifecycle-platforms/back-catalogue-obligations/profile|Back Catalogue Obligations]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The obligations a company carries are in thousands of executed agreements nobody has read since signature, and every CLM implementation begins by declaring that estate out of scope.
**Tags:** #large-language-models #transformers #bert #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to make the executed back catalogue answerable — what have we promised, to whom, and where — and whoever does that takes the account, because it is the question the category was bought to answer and the one every implementation declares out of scope.

## The Problem
A company plans a pricing change. Counsel is asked whether any customer contract prevents it. The honest answer is that there are four thousand executed agreements, that some of them contain price protection or most-favoured-nation terms, that nobody knows which, and that establishing it would take a team several weeks. The company proceeds on an estimate. Two years later a customer produces a 2019 agreement with a clause that makes the change a breach, and the cost of that single instance exceeds what structuring the whole estate would have cost.

## Why Nobody Has Built This
Migration was always scoped as a one-off project with a fixed budget, and it is the line item that gets cut when the implementation runs long — which it always does. Extraction was not reliable enough to trust unsupervised until recently, so the alternative was human review at a cost proportional to the estate, which made the business case impossible above a certain size. The value is also insurance-shaped: it prevents losses that are invisible when prevented, which is the hardest kind of investment to fund. And the vendors sell forward-looking workflow, where the demonstration is compelling and the implementation is tractable.

## What to Build
Continuous structuring of the legacy estate, prioritised by exposure. Extract the terms that carry consequence — parties, term and renewal, price protection, exclusivity, most-favoured-nation, service levels, liability caps, indemnities, data and security commitments, audit rights, assignment and change-of-control — with a confidence per field and an explicit escalation path for anything uncertain. Prioritise rather than processing alphabetically: contracts with live counterparties, large values, unusual length or non-standard paper first, since a company that can afford to structure a fraction of its estate should structure the exposed fraction, and nobody offers this ordering. Resolve amendment chains into operative terms, which is where most structured repositories are quietly wrong. Present the result as answerable questions rather than as a database — which customers have price protection, where are we exposed on data residency, which agreements survive a change of control — because that is how the question arrives. Treat it as continuous rather than as a migration, so the estate is progressively structured and the coverage is always visible. And report coverage honestly: this proportion of the estate, weighted by value, is structured to this confidence, which is the number that lets a general counsel say what they do and do not know.

## Target Customer
General counsel and legal operations at companies with a decade of executed agreements, enterprise risk functions, and the CLM vendors whose implementation reputation depends on this being solved.

## Impact If Built
This is the question the category exists to answer and systematically does not, and extraction has now crossed the threshold where it is economically viable at scale. Exposure-weighted prioritisation is what makes partial coverage useful, and honest coverage reporting is what makes the result trustworthy.
