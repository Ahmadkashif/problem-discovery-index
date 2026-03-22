# ServiceTitan Tracks Agreements but Can't Predict Renewal Risk or Optimize Upsell Timing

**Niche:** [[niches/hvac-contractors/maintenance-agreement-management/profile|Maintenance Agreement Management]]
**Industry:** [[industries/hvac-contractors|HVAC Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** ServiceTitan's Membership module schedules tune-ups and sends renewal reminders on a fixed calendar — but it treats every agreement customer the same, with no insight into which customers are about to cancel, which are ready to upgrade, or which agreements are actually losing money.
**Tags:** #gradient-boosting #automation #data-integration #revenue-impact #logistic-regression

## The Problem
ServiceTitan's Membership module is the industry standard for maintenance agreement management. It tracks agreement customers, schedules seasonal tune-ups, sends automated renewal reminders (typically 30 days before expiration), and reports total agreement revenue. What it doesn't do: analyze individual agreement economics, predict renewal likelihood, or recommend targeted actions. The 30-day renewal reminder goes to all customers — the customer who attended both tune-ups and had 3 repair visits (high engagement, high renewal probability, upsell candidate) receives the same generic email as the customer who skipped both tune-ups and hasn't interacted in 11 months (low engagement, high cancellation risk, needs a retention intervention). The service manager has no visibility into which of their 800 agreements are at risk and which are growth opportunities until after the cancellation happens.

## What Already Exists
ServiceTitan Membership: agreement tracking, seasonal scheduling, renewal reminders, revenue reporting. FieldEdge Service Agreements: similar functionality with QuickBooks integration. Housecall Pro Plans: basic agreement tracking for smaller shops. All three handle the operational logistics of maintenance agreements — scheduling, reminding, billing — but none provide the analytical layer: renewal risk scoring, per-agreement profitability, upsell readiness, or retention campaign management. The data needed for analysis exists in ServiceTitan (service history, agreement tenure, customer communications) but is locked in operational tables that the reporting module doesn't analyze at the individual agreement level.

## The Customization Gap
Three analytical layers are missing from ServiceTitan's Membership module. First, renewal risk scoring: using ServiceTitan's own data (tune-up attendance, repair call frequency, email engagement, payment history) to predict which agreements will likely cancel, displayed as a sortable risk score in the Membership dashboard so the service manager can see "47 agreements expiring this month: 12 high-risk, 28 normal, 7 low-risk" and allocate retention effort accordingly. Second, per-agreement profitability: calculate revenue (agreement fee + repair revenue at discounted rate) minus cost (tune-up labor + travel + discounted repair parts/labor + priority scheduling value) for each agreement, identifying the 10-15% of agreements that cost more to service than they generate — these need repricing, tier changes, or intentional non-renewal. Third, upsell timing: flag agreement customers whose equipment is approaching replacement age (12+ years) or whose repair frequency suggests they'd benefit from a premium agreement with parts coverage, with recommended upsell timing based on the customer's next scheduled interaction.

## Target Customer
HVAC companies with 200-3,000 maintenance agreements on ServiceTitan, spending $5K-15K/year on the platform, who want more value from their agreement data than ServiceTitan's built-in reporting provides.

## Impact If Solved
Improves renewal rate by 10-15 percentage points through targeted retention interventions, worth $25K-100K in preserved recurring revenue per company. Identifies unprofitable agreements for repricing or restructuring, eliminating $10K-50K in annual losses from agreements that cost more to service than they generate. Accelerates upsell from basic to premium agreements, adding $15K-75K in incremental agreement revenue through targeted, well-timed upgrade offers.
