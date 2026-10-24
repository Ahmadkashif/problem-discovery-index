# The Ingredient Change That Restarts Qualification

**Niche:** [[niches/defense-systems-manufacturers/solid-rocket-motor-supply/profile|Solid Rocket Motor & Propellant Ingredient Supply]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Fix (Pain Point)
**One-liner:** When an ingredient supplier closes, a motor maker may have to redo formulation, motor and missile qualification, and nobody knows in advance which ingredients carry that risk.
**Tags:** #graph-neural-networks #survival-analysis #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to put qualified motors on missile lines at the contracted rate, and whoever delivers the most flight-qualified motors per month takes the account.

## The Problem
In 2025 Nammo learned that a propellant-ingredient supplier was closing with no alternative, and Breaking Defense reported that requalifying a propellant can mean redoing formulation, motor and missile qualification. Some key ingredients have a single US source. The single points of failure sit several tiers down, where motor makers have the least visibility.

## Why It's Still Broken
Ingredient supply is tracked as purchase orders, not as qualification risk. The link between an ingredient, the formulations that use it, the motors qualified on those formulations and the missiles that carry them is held in engineers' heads and in qualification reports, not in a queryable structure.

## What a Fix Looks Like
A dependency map from every ingredient and its sources to formulations, motors and end items, annotated with qualification status and the cost and time to requalify, refreshed from purchasing data and supplier health signals. Each quarter it ranks the ingredients whose loss would stop the most motor deliveries, so second sources are qualified before they are needed.

## Who Feels the Pain
Propulsion engineers forced into emergency requalification, programme managers facing a stopped motor line, and buyers with no alternative supplier to call.

## Impact If Fixed
Starting a second-source qualification a year before a supplier fails instead of after turns a potential line stoppage into a planned change.
