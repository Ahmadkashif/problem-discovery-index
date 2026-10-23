# Open Positions Matched to Cargo Orders From the Inbox

**Niche:** [[niches/ocean-shipping-carriers/dry-bulk-tanker-chartering/profile|Dry Bulk & Tanker Chartering]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A chartering desk receives every cargo order in the market by email and evaluates only the handful it has time to estimate.
**Tags:** #large-language-models #transformers #gradient-boosting #optimization-fundamentals #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to fix each open ship on the cargo that earns the most once port time, bunkers and laytime are counted, and whoever fixes the fleet at the highest time-charter equivalent against the Baltic route average takes the account.

## The Problem
Brokers send cargo orders and tonnage lists all day: commodity, quantity, load and discharge ranges, laycan, rate ideas. A chartering manager with eight ships opening in the next month can estimate a few voyages properly per ship. The rest are skimmed, and good fixtures are missed because the order arrived during a call or was phrased differently from usual.

## Why Nobody Has Built This
Email parsing tools now extract orders, but extraction is not a decision. Ranking orders against each ship needs the owner's own voyage economics — speed and consumption, port costs, the next likely cargo from the discharge area — and the desk's private view of the market, which owners do not share with vendors.

## What to Build
An agent that reads every order and position from the inbox, runs a full voyage estimate for each plausible ship-cargo pair using the owner's vessel data and current bunker and port costs, includes the ballast leg and the likely next fixture from the discharge region, and ranks the opportunities by expected time-charter equivalent with a confidence range. The desk sees the top five per ship each morning with the estimate attached, ready to counter.

## Target Customer
Chartering managers at mid-sized dry bulk and tanker owners and operators with ten to a hundred ships.

## Impact If Built
Lifting fleet TCE by $500 a day (estimate) across 30 ships is ~$5.5M a year (estimate). The lift comes from more fixtures evaluated per ship and is measured against the Baltic route average the commercial director reports to owners.
