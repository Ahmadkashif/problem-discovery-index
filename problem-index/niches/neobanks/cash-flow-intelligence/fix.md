# The Alert That Fires Too Late

**Niche:** [[niches/neobanks/cash-flow-intelligence/profile|Cash-Flow Intelligence]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The low balance alert arrives when the balance is already low, which is after the rent went out and before the pay arrives, when there is nothing left to do about it.
**Tags:** #time-series-forecasting #change-point-detection #evaluation-metrics #confidence-intervals #quick-win #revenue-impact #automation #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to turn a complete view of a customer's financial life into something that helps them rather than into a balance screen — and whoever does that earns the primacy the whole model depends on.

## The Problem
The alert triggers on a balance threshold. By the time the balance is below it, the rent has gone out, the direct debits have processed, and the customer has four days until payday with no options. The institution could have seen this coming a week earlier — the rent amount and date are entirely predictable, the income timing is known, the discretionary pattern is consistent — and the alert is triggered by the state rather than by the forecast. It tells the customer something they already know at the moment it has stopped being useful.

## Why It's Still Broken
A threshold alert is trivial to implement and a forecast alert is not, so the easy version shipped and the useful one did not — the implementation cost determined the product, and the threshold looks like the same feature from the outside. A wrong forecast alert is embarrassing, which raises the perceived bar. Nobody measures whether the alert changed anything. And in some models the institution earns when the customer runs short.

## What a Fix Looks Like
Alert on the forecast, not the balance. Predict the shortfall from the customer's own known commitments and income timing and warn while there is still time to act, which is the fix and is the difference between an alert that helps and one that narrates. Give notice proportional to what could be done about it, since a week's warning permits action and a day's does not. Say what is causing it, because a customer told they will be short on Thursday because rent and a subscription both fall before payday can actually respond. Offer the specific options — move a payment, pause a subscription, an advance where the product supports it — rather than delivering a warning and stopping. Handle the irregular-income case, where the forecast is uncertain and the honest alert is conditional rather than absent. Suppress the alerts that do not need acting on, since alert fatigue destroys the channel and a customer who routinely runs close to zero and always recovers does not need warning weekly. Measure whether the alert changed behaviour, which is the only meaningful evaluation and which nobody runs. Report forecast accuracy, because a customer who has been wrongly warned twice will ignore the third. Handle the conflict honestly where fee income depends on the shortfall, since building this properly may reduce revenue and should be decided deliberately rather than by leaving the feature unbuilt. And measure overdrafts and fees avoided, because that number is both the customer benefit and, in most models, the commercial case for primacy.

## Who Feels the Pain
Customers warned at the moment nothing can be done; institutions whose most useful possible feature is a threshold; and the financially precarious, for whom a week's notice is the difference between a plan and a fee.

## Impact If Fixed
The implementation cost determined the product and the threshold alert looks identical from the outside while being useless. Forecasting the shortfall from known commitments and income timing gives notice proportional to what can be done about it.
