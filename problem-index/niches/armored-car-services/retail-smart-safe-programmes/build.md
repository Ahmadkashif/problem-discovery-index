# Pickups Set by Cash at Risk, Not by Calendar

**Niche:** [[niches/armored-car-services/retail-smart-safe-programmes/profile|Retail Cash Pickup & Smart-Safe Programmes]]
**Industry:** [[industries/armored-car-services|Armored Car Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Once credit no longer depends on the truck, the only reasons to collect a safe are cash at risk, cassette capacity and float cost, yet pickups are still booked on fixed weekdays.
**Tags:** #time-series-forecasting #optimization-fundamentals #gradient-boosting #monte-carlo-methods #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to put a store's cash into its bank account the day it is taken without a daily truck stop, and whoever gets next-day provisional credit posted at the most of the retailer's banks with the fewest pickups takes the account.

## The Problem
A chain on smart safes still has a pickup calendar: Tuesday and Friday for big stores, weekly for small ones. Some stores fill their cassettes before pickup and start making manual drops; others sit on cash the carrier guarantees and the bank is charging float on. The carrier's routes carry stops that are not needed and miss ones that are.

## Why Nobody Has Built This
Pickup schedules are written into contracts and priced per stop, so neither side has had a reason to make them dynamic. Carriers' route systems plan fixed recurring stops. Safe data reaches the carrier's systems but is used for credit, not for planning.

## What to Build
A forecast of each safe's accumulation by day, from its validated drop history, store sales patterns and calendar, combined with the cassette capacity, the guarantee limit per safe, the bank's float charge and the carrier's route days. An optimiser schedules each pickup when cash at risk, capacity or float cost crosses a threshold, and packs those pickups into the carrier's routes. The retailer sees the expected float and pickup count per store; the carrier sees stops it can drop.

## Target Customer
Directors of smart-safe and digital retail programmes at carriers; treasury teams at chains with several hundred stores on safes.

## Impact If Built
Dropping unnecessary pickups and adding needed ones cuts truck-hours for the carrier and float plus manual drops for the retailer — the number on which both decide whether the programme is worth renewing.
