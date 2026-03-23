# Client Expense Documentation Gaps

**Niche:** [[niches/tax-prep-firms/schedule-c-sole-proprietors/profile|Schedule C / Sole Proprietor Specialists]]
**Industry:** [[industries/tax-prep-firms|Tax Prep Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Sole proprietor clients claim deductions they cannot substantiate — "I spent about $3,000 on supplies" with no receipts — forcing the preparer to either accept undocumented deductions (audit risk) or reduce the deduction (client dissatisfaction).
**Tags:** #compliance #automation #worker-facing #tacit-knowledge-ml

## The Problem
Sole proprietors rarely maintain organized expense records. They arrive at the preparer's office with estimates: "I drove about 15,000 miles for work," "I spent maybe $2,000 on tools," "I had a lot of meals with clients." The preparer must decide how to handle these undocumented claims. Accepting them creates audit risk (the IRS disallows deductions without substantiation). Reducing them creates client friction ("my last preparer let me claim all of that"). Experienced preparers develop judgment about which claims are reasonable given the business type and revenue — a $5,000 tool expense is plausible for a contractor earning $150K but suspicious for a freelance writer earning $40K.

## Why It's Still Broken
The documentation problem starts in January when the client does not track expenses. By filing season, it is too late to reconstruct receipts. Preparers cannot force clients to keep better records, and the competitive pressure from lower-cost preparers who accept undocumented claims creates a race to the bottom on documentation standards. No tool helps the preparer assess the reasonableness of undocumented claims against statistical benchmarks for the client's business type and income level.

## What a Fix Looks Like
A reasonableness checking tool that compares the client's claimed deductions against aggregated benchmarks for their business type (NAICS code) and revenue level: "Your client claims $8,000 in vehicle expenses on $45K in revenue. For NAICS 484110 (trucking), the 25th-75th percentile range is $6,000-$14,000 — this claim is within normal range." The tool flags outliers and provides the preparer with data to support conversations with the client: "Your supplies claim of $12,000 is in the 98th percentile for your business type — can we document the largest purchases?"

## Who Feels the Pain
Preparers who balance audit risk against client satisfaction on every undocumented claim, spending 15-20 minutes per return on these judgment calls, and who bear E&O liability if the IRS disallows a deduction they accepted.

## Impact If Fixed
Reduces per-return time spent on documentation judgment calls by 50%. Provides audit-defensible reasoning for accepted deductions. Reduces E&O exposure by standardizing the reasonableness assessment process — the preparer's decision is supported by data, not gut feeling.
