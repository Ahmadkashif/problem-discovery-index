# Curtailments, Free-Flooring Ends and Payoffs Unit by Unit

**Industry:** [[powersports-and-boat-dealers|Powersports & Boat Dealers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The office manager tracks every floored unit's free-interest end date, curtailment schedule and payoff deadline across two to four lenders in a spreadsheet, and accounting software built for receivables and payables doesn't model any of it.
**Tags:** #time-series-forecasting #survival-analysis #data-integration #workflow-orchestration #automation #revenue-impact

## The Problem
Every new unit on the lot is financed unit by unit. A boat dealer may floor Brunswick product through Brunswick Acceptance, another hull line and its outboards through a second lender, and used inventory through a bank line. A powersports dealer floors Polaris through Polaris Acceptance, Harley through HDFS and the rest through Northpoint or a bank. Each unit carries its own terms: an OEM-paid interest period (MasterCraft reimburses dealer floorplan interest "generally ranging up to nine months"), then interest at the dealer's cost, then curtailment payments of principal as the unit ages. OneWater's 10-K says curtailments "reduce the allowable advance rate as our inventory ages". When a unit sells, the payoff is due within a short window, and a unit sold but not paid off is "sold out of trust", the finding every lender audit looks for.

The controller or office manager keeps this in a spreadsheet updated from lender statements and portals. They decide what to pay, when to request a curtailment extension, and which units to flag to the general manager before the free period ends. A missed curtailment draws a fee or a default notice; a late payoff draws an audit finding.

## What Already Exists
DMS accounting modules record floorplan notes payable and payoffs; lender portals (Wells Fargo CDF's, Northpoint's, Huntington's) show each lender's own units and statements; field audit firms count units for the lenders, profiled under [[franchised-car-dealers|Franchised Car Dealers]]. Car dealers' floorplan reconciliation tools assume one or two captive lenders and a monthly-interest model.

## The Customisation Gap
The recreational version needs: unit-level terms from several lenders in one ledger, including OEM interest-reimbursement periods that end on different dates by model year and programme; curtailment schedules by lender and age band; seasonal projections of cash needed for curtailments in the off-season, when units sell slowly; payoff tracking from DMS sale to lender payment with alerts before the payoff window closes; and an aged-unit list ranked by the cost of carrying each unit one more month against the OEM retail programme available to move it. The rules are contractual and stable once captured; the work is ingesting statements from several lenders in different formats.

## Impact If Solved
A dealer with 300 floored units across three lenders (estimate) that never misses a payoff window and plans its winter curtailments avoids audit findings and fees and frees a few days of office time a month; on aged boats, acting 30 days earlier on a $60,000 unit saves several hundred dollars of interest each (estimate).
