# AI-Powered Pre-Move Condition Documentation

**Niche:** [[niches/moving-companies/damage-claims-documentation/profile|Damage Claims Documentation & Resolution]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool exists that systematically captures and catalogs the pre-move condition of every item with sufficient detail to definitively resolve damage disputes.
**Tags:** #cnn #object-detection #computer-vision #multiclass-classification #automation

## The Problem
When a customer claims an item was damaged during the move, the mover's only defense is pre-move photos — if they exist. Currently, crew leads snap photos on their personal phones during the walk-through, with no standardization on what to photograph, how many angles to capture, or how to catalog which photo belongs to which item. Photos end up in a camera roll mixed with personal pictures, are rarely uploaded to any system, and when a claim arrives 30 days later, the crew lead may have already left the company. The mover pays the claim not because they caused the damage, but because they can't prove they didn't.

## Why Nobody Has Built This
Building this requires combining item detection (identifying furniture types from photos), condition assessment (detecting pre-existing scratches, dents, stains), and a structured documentation workflow that crews will actually follow under time pressure. The computer vision challenge is non-trivial: distinguishing a pre-existing scratch from a lighting artifact on a dark wood surface requires training data that doesn't exist in public datasets. Moving companies haven't demanded this because they've accepted claim payouts as a cost of business rather than a solvable documentation problem.

## What to Build
A mobile app that guides crew leads through a structured pre-move photo capture workflow. The app uses object detection to identify each major item (sofa, dresser, TV, etc.), prompts for multiple angles, automatically flags surfaces where pre-existing damage is detected (scratches, dents, water marks, fabric tears), and generates a timestamped, geotagged condition report linked to the move order. When a claim arrives, the system retrieves the relevant pre-move photos and condition assessment for that specific item, enabling instant comparison.

## Target Customer
Moving company owners and operations managers who pay $2,000-10,000/month in damage claims and currently have no systematic pre-move documentation process.

## Impact If Built
Reduces claim payout rates by 30-50% by providing documented evidence of pre-existing damage. On a company doing 200 moves/month with a 20% claim rate and $300 average claim, this saves $3,600-6,000/month. Eliminates fraudulent claims (estimated at 15-25% of total claims) entirely.
