# Binding Estimate Accuracy on Heavy Household Goods

**Niche:** [[niches/moving-companies/long-distance-interstate/profile|Long-Distance Interstate Movers]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** When a binding estimate says 8,000 lbs and the scale reads 10,500 lbs, the mover eats $1,200 in cost — and this happens on 20-30% of interstate moves.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A binding estimate is a legal commitment: the mover must honor the quoted price regardless of actual weight. When the estimate is accurate, everyone wins. When it's low (which happens on 20-30% of moves), the mover absorbs the cost difference — a 2,500-lb underestimate at $0.50/lb costs $1,250 in direct margin loss plus additional fuel, labor, and truck space. When the estimate is high, the customer shops around and books with a competitor. The estimation accuracy problem costs the industry an estimated 8-12% of gross revenue annually, split between margin erosion on underestimates and lost bookings on overestimates.

## Why It's Still Broken
Weight estimation is the deepest tacit knowledge problem in moving: an experienced estimator looks at a living room and knows the solid oak bookshelf with hardcover books weighs 400 lbs, not the 150 lbs that a typical inventory calculator assigns to "bookshelf." They mentally add 30% for the garage full of tools the homeowner forgot to mention. They factor in the 3 years of accumulated "stuff" in closets that no survey captures. This judgment takes 3-5 years to develop, and during the ramp-up period, junior estimators consistently underestimate by 15-25% — costing the company $50,000-$150,000/year in absorbed overages.

## What a Fix Looks Like
A weight estimation model trained on historical move data: inventory items (from survey) + home characteristics (square footage, bedrooms, garage, basement, years lived) + historical actual-vs-estimated weight for similar homes. The model produces a weight estimate with confidence interval and flags risk factors: "Homes with garages and 10+ years of occupancy average 22% more weight than inventory suggests — your estimate may be low by 1,500-2,000 lbs." The estimator reviews the model's output alongside their own judgment, catching the systematic biases that cost margin.

## Who Feels the Pain
The junior estimator who quoted 8,000 lbs on a binding estimate, watched the scale read 10,500 lbs, and now has to explain to the owner why this move just lost $1,250 — and the owner who absorbs these losses 15-20 times per month across their estimating team.

## Impact If Fixed
Improving binding estimate accuracy from +/-18% to +/-8% recovers 4-6% of gross revenue on interstate moves — worth $30,000-$100,000/year for a mover doing $1M-$3M in long-distance revenue.
