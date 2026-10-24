# Ninety Operators, Ninety Statement Formats

**Niche:** [[niches/oil-and-gas-producers/non-op-working-interest-investors/profile|Non-Op Working Interest Investors]]
**Industry:** [[industries/oil-and-gas-producers|Oil & Gas Producers]]
**Type:** Fix (Pain Point)
**One-liner:** Each operator sends AFEs, JIBs and revenue statements its own way, and the non-op's staff re-key them before anyone can analyse anything.
**Tags:** #large-language-models #bert #feature-engineering #data-integration #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to decide each AFE election inside the joint operating agreement's window on better information than the operator's own proposal, and whoever's elected wells return the most cash per dollar committed takes the account.

## The Problem
Some operators send electronic files, others PDFs, others portal downloads. Well names and numbers differ between AFEs, JIBs and revenue statements, and between operators and the state. Before a non-op can compare cost overruns or audit a bill, staff must normalise everything.

## Why It's Still Broken
There is no single industry format that every operator uses (COPAS has electronic standards, recalled, but adoption varies), and small non-ops lack the engineering to build parsers for each.

## What a Fix Looks Like
An intake service that reads each operator's AFEs, JIBs and revenue statements in whatever format they arrive, maps wells to state API numbers, and produces one normalised ledger per well. Anything it cannot map goes to a review queue.

## Who Feels the Pain
Non-op accountants and analysts, and the investment team waiting on data to decide elections.

## Impact If Fixed
For a non-op with ~90 operators (estimate), automated intake can free one or two full-time staff and shorten the lag from statement to analysis from weeks to days.
