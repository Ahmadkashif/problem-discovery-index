# Exchange Policy as Versioned Code

**Niche:** [[niches/financial-data-vendors/entitlements-exchange-reporting/profile|Entitlements & Exchange Reporting]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each exchange's data policy is prose that changes every year, and its translation into declaration logic lives in one specialist's spreadsheet.
**Tags:** #large-language-models #bert #evaluation-metrics #compliance #workflow-orchestration #automation
**Contested on:** Every serious competitor in this niche is fighting to prove, per user and per use, exactly what each client was entitled to and declared — and whoever makes the exchange audit an uneventful lookup keeps both the exchanges and the clients' market data managers on side.

## The Problem
Dozens of exchanges, each with its own definitions and fee categories, revised annually; declarations computed by hand against the current version.

## Why Nobody Has Built This
Volume per exchange is small, the expertise is rare, and nobody has owned a cross-exchange rules model.

## What to Build
Extract each policy into structured, effective-dated rules with links back to the clause; join them to entitlement events; compute declarations with provenance; diff each policy revision and estimate its fee impact before it takes effect.

## Target Customer
Exchange relations and market data compliance at vendors and redistributors.

## Impact If Built
Removes single-person dependency and turns audits into reproducible computations.
