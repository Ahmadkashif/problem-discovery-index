# Cross-Customer Learning Over Public Components

**Niche:** [[niches/software-supply-chain-security/dependency-corpus-intelligence/profile|Dependency Corpus Intelligence]]
**Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The components are the same public software in every customer, which makes cross-customer learning unusually easy here, and the category has not attempted it.
**Tags:** #transfer-learning #gradient-boosting #graph-theory #k-means-clustering #evaluation-metrics #confidence-intervals #cross-validation #compliance
**Contested on:** Every serious competitor that gets here is fighting to use a fleet-wide record of dependency graphs, dismissals, fixes and upgrade outcomes — and whoever does that can estimate real exploitability, real upgrade risk and real remediation effort, which are the three questions every finding raises.

## The Problem
Most cross-customer learning problems are hard because each customer's data is idiosyncratic. This one is not: the vulnerable components are literally identical public packages in every customer's estate, the vulnerabilities are the same public advisories, and the determinations are about the same code. An assessment made at one organisation is directly informative about the same component at another, and the category treats each customer's findings as an isolated universe.

## What Already Exists
Transfer and multi-task learning; federated approaches for customers who will not permit pooling; the public package and advisory ecosystems, which supply the shared identity layer; the exploitability exchange formats, designed precisely to share these determinations; and the empirical vulnerability research community's methods for estimating exploitation.

## The Customization Gap
The adaptation is to sharing determinations about public components without sharing anything about customers. It requires: (1) a representation containing only public identities and outcomes — this component, this version, this vulnerability, this assessment — with nothing about the customer's code or configuration, which is sufficient for most of the learning and is what makes this governable where other corpus opportunities are not; (2) usage-pattern abstraction for the cases where applicability depends on how the component is used, expressed as a pattern rather than as code, which is the piece requiring care; (3) adoption of the exchange formats, since they exist for exactly this and a vendor-proprietary representation reproduces the isolation; (4) honest treatment of assessment quality, because dismissals include both expert determinations and people clearing a queue, and pooling them uncritically will learn that everything is inapplicable — which is the obvious failure mode and requires weighting by assessor and by evidence; and (5) a federated option for customers who will not contribute, since regulated organisations are a meaningful segment and excluding them shrinks the corpus.

## Target Customer
Supply chain security vendors, the exchange format communities, and the security functions who would both contribute and benefit.

## Impact If Solved
The shared public component identity makes this the easiest cross-customer learning problem in the vault and it has not been attempted. Assessment quality weighting is the necessary safeguard, since pooling dismissals uncritically learns the wrong lesson.
