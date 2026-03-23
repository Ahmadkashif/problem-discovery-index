# Account Assignment Imbalance Across Sales Reps

**Niche:** [[niches/restaurant-suppliers/sales-territory-optimization/profile|Sales Territory Optimization]]
**Industry:** [[industries/restaurant-suppliers|Restaurant Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** Sales managers assign territories once and never rebalance — after 2-3 years of account growth, closures, and rep turnover, one rep manages $4M in accounts while another manages $1.5M, creating compensation inequity, burnout, and under-served accounts that churn.
**Tags:** #regression #tabular-ml #revenue-impact #worker-facing

## The Problem
At a typical independent restaurant supplier with 8 sales reps, the highest-producing rep manages $4M-$5M in account revenue while the lowest manages $1M-$1.5M. This imbalance develops organically: the senior rep accumulated large accounts over years, new restaurant openings in their territory added to their book, and when other reps left, their accounts were distributed by geographic convenience rather than workload balance. The consequence: the over-loaded rep cannot visit all accounts at appropriate frequency (visiting 150 accounts weekly vs. the recommended 80-100), leading to under-served accounts that begin to churn. The under-loaded rep has spare capacity but no authority to pick up accounts in another rep's territory. The sales manager knows the imbalance exists but dreads the political process of rebalancing — moving an account from one rep to another means the losing rep's commissions decrease and the chef-rep relationship is disrupted.

## Why It's Still Broken
Three barriers prevent rebalancing: (1) data — the sales manager does not have a clear picture of each rep's total account revenue, visit frequency, and workload because this data lives in the ERP (order data), the rep's calendar (visit data), and the rep's head (relationship data) with no unified view, (2) politics — reps view their accounts as personal property and resist reassignment, (3) risk — reassigning a $200K account from its current rep to a new rep risks losing the account entirely if the chef does not bond with the new rep. The result: managers avoid rebalancing until a crisis (rep burnout, major account loss, rep departure) forces a reactive reshuffling that is worse than a planned rebalancing would have been.

## What a Fix Looks Like
A territory health dashboard that: (1) visualizes rep-level workload (total accounts, total revenue, visits per account per month, drive time per visit) with imbalance indicators ("Rep A is at 140% of optimal workload, Rep C is at 60%"), (2) models the impact of rebalancing scenarios ("move 15 accounts from Rep A to Rep C — Rep A's workload drops to 110%, Rep C's rises to 85%, total at-risk revenue from relationship disruption: $120K"), (3) recommends which accounts to move based on lowest relationship switching cost (newer accounts, accounts with delivery relationship more than rep relationship, accounts where the current rep is under-visiting anyway), and (4) tracks rebalancing outcomes (did moved accounts retain, grow, or churn?) to improve future recommendations.

## Who Feels the Pain
Over-loaded reps who burn out trying to serve 150 accounts at the quality level required to retain them. Under-loaded reps who have capacity but lack opportunity. Sales managers who know the imbalance exists but cannot justify the disruption of rebalancing without data. The accounts themselves — under-visited accounts receive worse service and eventually leave for a competitor who gives them more attention.

## Impact If Fixed
Account visits per rep normalized to 80-100 accounts, improving visit quality and frequency for under-served accounts. Customer retention improves 10-15% in previously under-visited accounts. Rep turnover decreases — burnout from overload is the #2 reason reps leave (after compensation). Revenue per rep normalizes, enabling fair commission structures. Long-term: an annual territory rebalancing process (rather than crisis-driven) becomes a manageable operational cadence.
