# Route-to-Booked-Job Attribution From Field-Service Records

**Niche:** [[niches/direct-mail-agencies/local-saturation-mail/profile|Local Service Businesses on Saturation Mail]]
**Industry:** [[industries/direct-mail-agencies|Direct Mail Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A plumber's field-service system holds the address of every booked job; nobody matches those addresses to the carrier routes the plumber paid to mail.
**Tags:** #causal-inference #gradient-boosting #evaluation-metrics #data-integration #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to show a plumber, roofer or pizzeria which carrier routes produced booked jobs or orders — and whoever ties route-level drops to the owner's own job records keeps the owner mailing every month.

## The Problem
A home-service owner mails 10,000 postcards a month across a dozen carrier routes. Jobs come in from mail, search, referrals and repeat customers. Without a way to see job volume by route against mailing history, the owner either keeps mailing out of habit or stops after a slow month.

## Why Nobody Has Built This
The printer or agency selling the mail has no access to the owner's job data; the field-service platform has the jobs but no record of which routes were mailed when. Each customer is too small for a bespoke analysis.

## What to Build
A connector that reads job or order addresses from field-service and POS systems, geocodes them to carrier routes, and compares new-customer job rates on mailed routes before and after each drop against similar routes left unmailed. It recommends next month's routes from housing age, home values, past job density and measured response, and reports cost per booked job by route.

## Target Customer
Owners and office managers of HVAC, plumbing, roofing, pest control and restaurant businesses mailing monthly; franchise local-marketing programmes that subsidise franchisee mail.

## Impact If Built
Owners stop mailing routes that never produce jobs and deepen the ones that do, and the agency or printer that shows this keeps the customer through the slow months.
