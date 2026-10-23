# Rekey or Retrofit, Decided Unit by Unit

**Niche:** [[niches/locksmiths/rental-turnover-rekeying/profile|Rental-Turnover Rekeying & Smart-Lock Retrofit]]
**Industry:** [[industries/locksmiths|Locksmiths]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A property manager with 3,000 scattered rental homes pays for a rekey truck roll at every turn and can't tell which homes would be cheaper with a smart lock, because turn frequency, travel and lock condition are never put side by side.
**Tags:** #gradient-boosting #survival-analysis #optimization-fundamentals #data-integration #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to reset access at every unit turn before the next resident moves in, and whoever can prove every door was reset before move-in, by rekey or smart-lock code change, at the lowest cost per turn takes the account.

## The Problem
Rekey cost per turn depends on the property: distance from the locksmith, number of exterior doors, lock condition and how often residents turn over. A smart-lock retrofit costs more up front but removes most future rekey visits, enables self-guided showings and logs access. Managers decide by policy ("all new acquisitions get smart locks") rather than by unit economics, and locksmiths quote whatever is asked.

## Why Nobody Has Built This
The inputs sit in different systems. Turn history is in the property-management software, rekey invoices in accounts payable, lock hardware in nobody's records, and smart-lock costs in a vendor proposal. Locksmiths don't see the portfolio, and managers don't see the lock.

## What to Build
A planner that joins turn history and lease data, past rekey invoices and travel times, and a door and lock inventory captured at the next visit. It forecasts each unit's turns over the hardware life with survival models and computes rekey-versus-retrofit cost per unit, including showing and access-logging benefits where the manager values them. It produces a retrofit schedule that bundles nearby units into efficient routes, and a turn-day plan for the rest.

## Target Customer
Single-family rental operators and multifamily managers with large portfolios; the locksmith firms that hold their access contracts.

## Impact If Built
Retrofit spend goes where it pays back, rekey truck rolls fall, and the locksmith moves from per-turn vendor to the portfolio's access partner.
