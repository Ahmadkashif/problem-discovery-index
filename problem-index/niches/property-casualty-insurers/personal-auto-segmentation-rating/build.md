# Adverse Selection Radar After Every Rate Change

**Niche:** [[niches/property-casualty-insurers/personal-auto-segmentation-rating/profile|Personal Auto Segmentation & Telematics Rating]]
**Industry:** [[industries/property-casualty-insurers|Property & Casualty Insurers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A carrier takes a rate change and watches its retention number, but cannot see until a year of losses arrives whether the drivers who stayed are the ones it wanted.
**Tags:** #causal-inference #survival-analysis #gradient-boosting #hypothesis-testing #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rank drivers by expected loss more finely than the carrier quoting next to them and get that segmentation through state rate review, and whoever keeps its best risks after a rate change without a regulator disapproval takes the account.

## The Problem
After a rate change, retention and new-business counts move. The question that matters is which risks moved. If the drivers whose predicted loss fell after the change are leaving for a competitor's sharper price while the ones it underprices stay, the loss ratio deteriorates. The carrier finds out months later, after the claims come in. Competitive rate data shows where the carrier sits on price; it does not show what happened to the book.

## Why Nobody Has Built This
Pricing teams own the model, distribution teams own retention, and actuarial owns emerging losses. The comparison requires joining competitive rate positions, renewal outcomes and model-predicted loss at policy level, and estimating what retention would have been without the change.

## What to Build
A post-change monitor that compares, by predicted-loss decile, retention and new-business conversion before and after each rate change against a counterfactual from unchanged states and competitor rate movements. It estimates the expected-loss mix of the business gained and lost within weeks. It warns when the carrier is retaining a worse book than its rate change assumed, and quantifies the loss-ratio effect before claims arrive.

## Target Customer
Personal auto pricing and product leaders at carriers selling through comparative raters and direct channels.

## Impact If Built
Adverse selection is caught in weeks rather than a year, and the next rate change corrects the segments that are leaking.
