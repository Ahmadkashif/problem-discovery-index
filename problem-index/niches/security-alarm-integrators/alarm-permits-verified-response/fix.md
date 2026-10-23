# The Fine That Reaches the Customer Before the Dealer

**Niche:** [[niches/security-alarm-integrators/alarm-permits-verified-response/profile|Alarm Permits, False-Alarm Fines & Verified-Response Compliance]]
**Industry:** [[industries/security-alarm-integrators|Security Alarm Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** The city's billing vendor mails the customer a false-alarm fine, the customer blames the alarm company, and the cancellation call is the dealer's first notice.
**Tags:** #descriptive-statistics #feature-engineering #quick-win #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep each customer's alarm eligible for police response under its own city's ordinance (permitted, under the false-alarm limit and verified to the local standard), and whoever keeps the most accounts dispatchable with the fewest fines takes the account.

## The Problem
After a few false alarms, a city's programme sends the alarm user an invoice. The customer feels they're paying twice, once for monitoring that didn't stop the false alarms and again to the city. They call to cancel. The dealer had the dispatch history all along but never connected it to the city's allowance.

## Why It's Still Broken
Fine notices go to the customer, not the dealer. The station's dispatch log and the city's count use different definitions of a false alarm. Nobody at the dealer owns watching counts against allowances.

## What a Fix Looks Like
For accounts in fining jurisdictions, count dispatch requests against the local allowance. After the first false dispatch, send the customer an explanation and offer a service check before the next one becomes a fine. Track fines reported by customers or vendors, and offer to help with a waiver where a repair fixed the cause.

## Who Feels the Pain
Customers paying fines they don't understand; retention teams fielding cancellations they could have prevented; and dealers whose reputation absorbs the city's policy.

## Impact If Fixed
A known trigger of attrition becomes a service opportunity, using dispatch records the station already keeps.
