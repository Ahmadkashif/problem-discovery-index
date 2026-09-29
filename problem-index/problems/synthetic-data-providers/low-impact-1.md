# Relational and Constraint Preservation

**Industry:** [[synthetic-data-providers|Synthetic Data Providers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Single-table synthesis is a solved and competitive product, and real enterprise data is forty tables with foreign keys, temporal ordering and business rules that generic generators break silently.
**Tags:** #gans #diffusion-models #variational-inference #graph-neural-networks #hypothesis-testing #evaluation-metrics #feature-engineering #data-integration

## The Problem
A customer's data is not a table. It is a schema: customers, accounts, transactions, addresses, claims, events, with foreign keys binding them, cardinalities that reflect reality, temporal orderings that must hold, and business rules that were never written down but are enforced by the application that produced the data.

A synthetic version must preserve all of it. A transaction must reference an account that exists. An account opened after a transaction on it is nonsense. A claim date before a policy effective date will crash the customer's test suite. A patient with a prostate diagnosis and a female gender marker will be spotted immediately by any clinician reviewing the output.

Generic tabular generators handle each table independently and then attempt to stitch. The stitching is where it fails, and the failures are frequently silent — the data looks plausible in aggregate and violates a rule that matters only in the specific workflow the customer bought it for.

So the customer's engineer discovers the problem when their application rejects the data, and the vendor's solutions engineer spends the proof of concept adding constraints by hand.

## What Already Exists
The Synthetic Data Vault library explicitly supports multi-table synthesis with parent-child relationships and is the reference implementation. Commercial platforms from Gretel, MOSTLY AI, Tonic and Hazy all offer relational modes. Referential integrity enforcement is standard. Data profiling tools can infer schemas and basic constraints. Test data management platforms handle subsetting and masking for non-synthetic use cases.

## The Customisation Gap
Referential integrity is the easy constraint and the only one handled well. The constraints that break customers are semantic: an ordering between dates across tables, a sum that must reconcile, a status transition that cannot skip a state, a code that is only valid with certain other codes.

Nobody discovers these automatically. They are present in the real data as invariants that hold across every row, and inferring them — candidate constraint generation followed by statistical validation against the real dataset — is a well-shaped problem that the profiling tools do not attempt beyond simple range and uniqueness checks.

Long-tail cardinality is the second gap. Most customers have a handful of accounts with thousands of transactions and a majority with two, and generators trained to match the mean produce a distribution that looks right in aggregate and wrong in the tail — which is exactly where the interesting test cases and the privacy risk both live.

Constraint-aware generation is the third. Once constraints are known, generating data that satisfies them by construction is different from generating freely and rejecting violations, and rejection sampling degrades badly as constraint count rises.

## Impact If Solved
Relational fidelity is the reason most enterprise proofs of concept stall, and it is currently repaired by hand in every engagement. Automatic constraint discovery and constraint-aware generation converts a bespoke solutions-engineering exercise into a property of the product.
