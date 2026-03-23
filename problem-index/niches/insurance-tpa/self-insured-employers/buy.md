# Stop-Loss Placement Optimization Tool

**Niche:** [[niches/insurance-tpa/self-insured-employers/profile|Self-Insured Employer Programs]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Insurance placement platforms exist for commercial P&C but none are built for the specific dynamics of stop-loss purchasing — individual and aggregate attachment points, laser determinations, and run-in/run-out provisions.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
Self-insured employers purchase stop-loss insurance to cap their exposure on individual high-cost claims (specific stop-loss) and total annual claims (aggregate stop-loss). Choosing the right attachment points is a complex optimization problem: lower attachments cost more in premium but reduce volatility; higher attachments save premium but increase risk. Currently, brokers set attachment points using rules of thumb and carrier quotes, not modeling based on the employer's actual claims distribution.

## What Already Exists
Insurance placement platforms like Zywave, Applied Epic, and Indio handle commercial P&C submissions. Actuarial tools like Milliman's MedInsight provide sophisticated modeling but require actuarial expertise and six-figure engagements. Neither is accessible to the mid-market broker advising a 500-employee self-insured group.

## The Customization Gap
The gap is a broker-facing tool that takes an employer's historical claims data, models the probability distribution of future claims, and simulates total cost (claims + premium) at various specific and aggregate attachment points. It should account for known large claimants (lasers), trend factors, and plan design changes — outputting a recommendation the broker can present to the CFO alongside carrier quotes.

## Target Customer
Benefits brokers advising mid-market self-insured employers, and CFOs who want to understand the risk-cost tradeoff of different stop-loss structures.

## Impact If Solved
Optimized stop-loss placement saves employers 8-15% on stop-loss premium (typically $500K-$2M for a mid-market group) while maintaining equivalent risk protection. Brokers differentiate on analytics rather than carrier relationships alone.
