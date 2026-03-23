# Payment Method Friction and Collection Cost

**Niche:** [[niches/auto-dealers-independent/buy-here-pay-here/profile|Buy Here Pay Here (BHPH) Dealers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** BHPH customers make weekly or bi-weekly payments, but most dealers still collect via in-person cash or phone-based card transactions because digital payment infrastructure doesn't serve the subprime demographic.
**Tags:** #automation #workflow-orchestration #worker-facing #revenue-impact

## The Problem
BHPH customers typically pay in person (cash or debit card at the dealership) or by phone (calling in a card number to a collections clerk). Both methods are labor-intensive: processing 200 payments per week requires 2-3 staff members spending 15-20 hours/week on payment collection alone. Customer-initiated digital payment options (ACH autopay, mobile payment apps) have adoption rates under 20% because the subprime demographic has unstable banking relationships, often uses prepaid debit cards, and distrusts autopay arrangements that might overdraft their accounts.

## Why It's Still Broken
Standard payment processors (Stripe, Square) work for one-time transactions but don't handle the recurring payment management that BHPH requires (tracking schedules, applying payments to principal vs. interest, managing partial payments, handling deferrals). BHPH-specific DMS tools handle the accounting side but offer limited self-service payment options. Payix and similar BHPH payment platforms exist but have limited mobile experience and don't address the core adoption barrier: customers who don't trust or don't have stable bank accounts for ACH.

## What a Fix Looks Like
A mobile-first payment platform designed for subprime demographics: text-based payment reminders with a one-tap payment link, support for prepaid debit cards and cash-loading at retail locations (similar to Cash App's cash deposit network), flexible partial payment processing with automated application to the loan, transparent balance and payment history accessible without creating an account, and real-time payment confirmation to both customer and dealer. The key design principle: remove every possible friction point for a customer who may not have a stable bank account or smartphone data plan.

## Who Feels the Pain
Collections clerks who spend 15-20 hours/week processing payments by phone and in person, and dealer owners who lose accounts to delinquency because the payment process itself is an obstacle for customers who want to pay but find it inconvenient.

## Impact If Fixed
Shifting 40-50% of payments to self-service digital channels recovers 8-12 hours/week of staff time (worth $15K-25K/year in labor). On-time payment rates typically improve 5-10% when friction is reduced, recovering $15K-30K/year on a 500-account portfolio. Reduces the need for starter-interrupt interventions, which damage customer relationships and accelerate voluntary repossession.
