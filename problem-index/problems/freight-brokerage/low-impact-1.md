# Carrier Reliability Scoring and Double-Broker Fraud Detection

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic carrier vetting tools check FMCSA authority status and safety rating, but don't score carriers on the behavioral signals that predict service failure and double-brokering fraud — patterns in their load acceptance, communication behavior, and tracking compliance that experienced dispatchers recognize from prior incidents.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #bias-variance-tradeoff

## The Problem

Double-brokering fraud — where a carrier books a load and then re-brokers it to another carrier without the shipper's knowledge — is the most serious service risk in freight brokerage. A double-brokered load often results in cargo theft, delivery failure, or billing confusion. The freight industry loses hundreds of millions of dollars annually to double-brokering and carrier fraud. Experienced dispatchers recognize warning patterns: carriers who negotiate unusually aggressively on rate, who ask unusual questions about the freight value or pickup location, or who have check-calls going unanswered after booking.

Generic carrier vetting platforms (MyCarrierPortal, Carrier411) check regulatory compliance but don't model behavioral fraud signals or predict reliability from transaction pattern data.

## What Already Exists

FMCSA SAFER database provides safety ratings and authority status. MyCarrierPortal and Carrier411 provide insurance and compliance verification. No platform scores carriers on behavioral reliability signals from transaction history.

## The Customisation Gap

A carrier reliability tool needs: (1) the broker's own transaction history with each carrier (on-time delivery rate, check-call compliance, load acceptance vs. abandonment rate, rate negotiation pattern); (2) industry-wide behavioral signals from DAT and FMCSA safety event data; (3) anomaly detection for fraud indicators (unusual rate behavior, sudden MC authority age mismatch with equipment profile, location-tracking abnormalities). The broker's own transaction history with each carrier is the differentiating signal — no external platform has this data.

## Impact If Solved

A single double-brokered load with cargo theft costs $50,000-$500,000 in cargo value plus liability exposure. For a brokerage doing 15,000 loads per year, reducing service failure rate by 0.1% saves $75,000-$750,000 annually in cargo claims and customer relationship costs.
