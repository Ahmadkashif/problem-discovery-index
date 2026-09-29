# Broker Cost Basis Reporting

**Niche:** [[niches/crypto-exchanges/tax-basis-and-reporting/profile|Tax Basis & Reporting]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Securities brokers solved cost basis reporting with transfer statements, lot selection and a standardised regime, all of which assume a broker on the other side.
**Tags:** #compliance #data-integration #evaluation-metrics #automation #workflow-orchestration #confidence-intervals #descriptive-statistics #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to establish a defensible cost basis for assets that arrived from somewhere else with nothing attached — and whoever reconstructs basis most accurately files the fewest wrong forms under a regime that now makes it a legal obligation.

## The Problem
Cost basis reporting was solved for securities: brokers track basis per lot, pass transfer statements when positions move between them, support lot selection methods, handle corporate actions and wash sales, and file standardised forms. The infrastructure took years and works. Crypto exchanges face the same obligation with a critical difference — the counterparty is frequently a self-custodied wallet with no broker attached and no statement to send.

## What Already Exists
Lot-level basis tracking; broker-to-broker transfer statement infrastructure; lot selection methods and their reporting; corporate action and wash sale handling; and the standardised filing regime.

## The Customization Gap
The adaptation is to transfers with no counterparty broker. It requires: (1) basis inference from a public ledger where no statement exists, which has no securities analogue and is the substantive adaptation; (2) self-custody as a routine intermediate step, so a position may leave and return with no institutional record in between; (3) assets acquired by mining, staking, airdrop and fork, whose basis rules have no securities equivalent; (4) twenty-four-hour markets with no settlement date convention, complicating the acquisition timestamp; and (5) confidence-scored basis as a reportable concept, since some figures are inferred and the regime has no field for that.

## Target Customer
Exchange tax operations, tax authorities designing the regime's practical requirements, crypto tax vendors, and securities tax platform vendors entering the asset class.

## Impact If Solved
The securities regime works because a broker sits on both ends. Inferring basis across a self-custody gap is the missing capability, and the ledger makes it possible in a way securities never could.
