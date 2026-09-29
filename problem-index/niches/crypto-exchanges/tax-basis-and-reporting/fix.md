# Zero Basis by Default

**Niche:** [[niches/crypto-exchanges/tax-basis-and-reporting/profile|Tax Basis & Reporting]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Fix (Pain Point)
**One-liner:** When basis is unknown the form reports zero, which taxes the customer on the full proceeds of an asset they may have bought at a loss.
**Tags:** #compliance #quick-win #automation #evaluation-metrics #worker-facing #descriptive-statistics #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to establish a defensible cost basis for assets that arrived from somewhere else with nothing attached — and whoever reconstructs basis most accurately files the fewest wrong forms under a regime that now makes it a legal obligation.

## The Problem
A customer moves coins in from their own hardware wallet, sells, and receives a form stating a gain equal to the entire sale proceeds. They bought at a higher price. Correcting it means reconstructing their own records, which they may not have, and filing an adjustment. The exchange knows the deposit came from an address, knows the date, and defaulted to zero because that was the simplest field to populate. The support queue fills every filing season with people disputing a number the exchange generated without looking.

## Why It's Still Broken
Zero was the default the form-generation code needed for a missing value, so a placeholder became a policy — and nobody revisited it because the error lands on the customer. Collecting basis from customers was optional and therefore largely uncollected. The chain evidence sits in a different team's tooling. And the volume of disputes is treated as a seasonal support problem rather than as a data problem.

## What a Fix Looks Like
Stop defaulting and start asking. Prompt for basis at the moment of deposit rather than at filing season, which is the fix and is when the customer actually knows the answer. Flag zero-basis positions to the customer before the form is generated, since a correction before filing costs nothing and a correction after costs everyone. Report how many positions are on zero basis, which is a one-query diagnostic and will be a larger number than anyone expects. Use the deposit date's market price as a stated estimate where nothing better exists, because an estimate with a label is better than a zero that is definitely wrong. Match transfers from the exchange's own customers automatically, as those have exact basis and are being defaulted alongside the rest. Accept structured basis submission rather than support tickets, so the correction path is not a person reading emails. Prioritise outreach by position size, since the harm is concentrated. Keep the basis once supplied, because customers currently re-supply it every year. Explain on the form what the zero means, as customers reasonably read it as the exchange's assertion. And track dispute volume as the metric, which is the direct measure of whether the default is being fixed.

## Who Feels the Pain
Customers taxed on proceeds rather than on gain; support teams handling a seasonal dispute flood; tax preparers reconstructing records from nothing; and exchanges filing forms they know to be wrong.

## Impact If Fixed
A placeholder for a missing field became a policy because the error lands on the customer. Prompting at deposit, matching internal transfers and labelling estimates removes most zero-basis filings before the form is generated.
