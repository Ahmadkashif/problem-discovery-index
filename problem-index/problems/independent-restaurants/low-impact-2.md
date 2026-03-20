# Third-Party Delivery Margin Optimization

**Industry:** [[independent-restaurants|Independent Restaurants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Restaurants already have delivery through DoorDash and Uber Eats — they just have no idea which orders are profitable, which are losing money, and how to price the delivery menu differently to stop the bleed.
**Tags:** #gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics #revenue-impact

## The Problem
Independent restaurants sign up for DoorDash, Uber Eats, and Grubhub because their competitors are listed and they fear losing volume. But the commission structures — 15% on pickup, 20-30% on delivery — eat directly into already-thin margins. A $25 chicken entree that yields a 68% gross margin in-house drops to 38-48% gross margin after platform commissions, and that is before factoring in the incremental packaging cost ($0.50-$1.50 per order), the kitchen disruption of managing a parallel order stream during peak hours, and the refund/chargeback exposure that platforms resolve in the customer's favor by default. Most owners treat delivery revenue as undifferentiated topline and have no per-order margin visibility, so they cannot distinguish the profitable delivery items from the ones that cost money to fulfill.

## What Already Exists
POS systems like Toast and Square report delivery sales totals and can break down revenue by platform, but they do not connect commission tier structures, packaging costs, or platform-specific refund rates to individual menu items. Third-party aggregation dashboards like Ordermark (now Nextbite) and Cuboh consolidate orders across platforms but focus on operational routing, not margin analysis. Some chains use internal BI teams to build delivery P&Ls per menu item — independents have no equivalent capability and no time to build spreadsheets manually.

## The Customisation Gap
An independent restaurant needs a tool that ingests platform commission statements (which arrive as opaque CSV/PDF exports), maps each line item to actual ingredient costs from the POS recipe database, layers in packaging costs by item type, and produces a per-item delivery margin report. The output should flag items where delivery margin falls below a configurable threshold (e.g., 15% contribution margin), recommend delivery-specific price adjustments or menu exclusions, and model the revenue impact of removing unprofitable items from delivery platforms. The tool must handle the complexity of platform-specific commission tiers (DoorDash DashPass orders have different rates than standard), promotional pricing (platforms run discounts the restaurant agreed to weeks ago and forgot about), and the reality that platform analytics intentionally obscure true per-order economics.

## Impact If Solved
Restaurants that audit and restructure their delivery menu typically recover 3-5 margin points on delivery revenue. For a restaurant doing $5,000/week in delivery ($260K/year), that is $8,000-$13,000 in annual profit recovered — meaningful when total net income is often $30,000-$60,000. More importantly, it prevents the slow-bleed scenario where a restaurant's fastest-growing revenue channel is its least profitable.
