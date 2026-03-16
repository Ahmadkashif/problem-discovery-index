# Damage Claims Documentation and Resolution

**Industry:** [[moving-companies|Moving Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Damage claims are already handled by insurance software, but none of it understands moving-specific liability tiers, pre-existing vs. transit damage, or the photographic evidence workflows movers actually need.
**Tags:** #cnn #object-detection #computer-vision #compliance

## The Problem
On roughly one in three long-distance moves, at least one item arrives with new damage — a scratch on a dresser, a cracked mirror, a dented appliance. The customer files a claim, the company must determine liability (full-value protection vs. released-value at $0.60/lb), document the damage with photos, assess whether the damage is pre-existing or transit-related, and either settle or dispute. This process takes 2-6 weeks, consumes 4-8 hours of administrative time per claim, and frequently ends in customer disputes that generate chargebacks or negative reviews regardless of outcome.

## What Already Exists
General claims management tools (ClaimVantage, Snapsheet) handle insurance workflows but assume an auto or property context. They don't understand FMCSA valuation tiers, the difference between full-value protection and released-value coverage, or the specific documentation requirements for interstate household goods carriers. Moving companies end up using email folders and shared drives to manage claim photos, forms, and correspondence.

## The Customisation Gap
A moving-specific claims system needs: (1) structured before/during/after photo capture integrated into the move workflow so crews document item condition at origin and destination, (2) a CNN-based comparison engine that flags items where destination photos show damage not present in origin photos, distinguishing new scratches from pre-existing wear, (3) automatic liability calculation based on the valuation tier the customer selected and the item's declared value, and (4) templated settlement offers that comply with FMCSA's 120-day acknowledgment and 120-day settlement deadlines for interstate claims. The photo comparison model needs to handle variable lighting, angles, and the fact that "before" photos are often taken hastily by crews under time pressure.

## Impact If Solved
Cuts claim resolution time from 4-6 weeks to under 10 days. Reduces administrative burden per claim from 4-8 hours to under 1 hour. Decreases disputed claims by 30-40% through objective photographic evidence that both parties can review.
