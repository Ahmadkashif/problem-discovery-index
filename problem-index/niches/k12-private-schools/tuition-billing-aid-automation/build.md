# Financial Aid Award Optimization Engine

**Niche:** [[niches/k12-private-schools/tuition-billing-aid-automation/profile|Tuition Billing & Financial Aid Optimization]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool optimizes financial aid allocation to maximize enrollment yield subject to a total aid budget — schools distribute aid based on committee judgment and static income thresholds without modeling the enrollment impact.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #data-integration

## The Problem
A school with a $3M aid budget distributes awards through committee review: each family submits an SSS (School and Student Services) application, a committee reviews the financial data, and an award is made based on calculated need, competitive considerations, and available budget. The committee does not model the relationship between award amount and enrollment probability — they award what they think is fair and hope the family enrolls. Some families receive more aid than necessary to secure enrollment (over-award), while others receive too little and choose a competitor (under-award). The gap between optimal and actual aid allocation can be $200K-$500K in lost net tuition revenue.

## Why Nobody Has Built This
Financial aid optimization requires joining SSS/FACTS financial data with historical enrollment outcomes to build a model of price sensitivity — something no school has done systematically. The optimization must respect constraints (minimum award floors, maximum percentages, board diversity targets) and handle the sensitivity of treating aid as a pricing strategy. Schools are uncomfortable with the framing of "optimizing aid" because it conflicts with their mission-driven self-image, even though the result (better allocation) serves students.

## What to Build
A constrained optimization engine that takes the pool of aid-eligible families, their financial profiles (SSS data), and the school's aid budget, and produces an award allocation that maximizes expected net tuition revenue (total tuition collected minus total aid awarded). The model predicts enrollment probability as a function of award amount for each family, trained on historical aid-to-outcome data. The committee reviews the optimized allocation and adjusts as needed — the model provides a data-informed starting point, not a replacement for committee judgment.

## Target Customer
CFOs and business office directors at independent day schools with $1M+ in annual financial aid budgets who currently allocate aid through committee judgment without quantitative modeling.

## Impact If Built
Increases net tuition revenue by 3-8% ($90K-$400K at a school with a $3M aid budget) by reducing over-awards and preventing under-awards that lose price-sensitive families. Enables the school to serve more families with the same aid budget by allocating more precisely.
