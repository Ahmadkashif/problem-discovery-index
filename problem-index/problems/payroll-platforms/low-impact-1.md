# Time to Gross Pay Rule Configuration

**Industry:** [[payroll-platforms|Payroll Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every platform can express overtime, differentials and premiums as configurable rules, and employers configure them wrong because the regular rate of pay is genuinely hard and nobody checks the configuration against the law.
**Tags:** #large-language-models #bert #hypothesis-testing #descriptive-statistics #confidence-intervals #evaluation-metrics #compliance #automation

## The Problem
Turning recorded hours into gross pay looks arithmetic and is not. Overtime is owed on hours over forty in a week federally, over eight in a day in some states, and on the seventh consecutive day in others. Double time exists in some jurisdictions. Meal and rest break premiums are owed when a break is missed or late, at a rate that itself depends on the regular rate. Shift differentials, non-discretionary bonuses and commissions must be folded into the regular rate before overtime is computed — a calculation that is frequently done wrong and is the basis for a large share of wage and hour litigation.

The platforms can represent all of this. The configuration is done by an employer's payroll administrator, from a settings page, based on their understanding of rules that vary by state and change.

The result is systematic, invisible error. An employer excluding a non-discretionary bonus from the regular rate underpays overtime on every affected cheque, for years, until a lawsuit or an audit. Nobody checks, because checking requires comparing the configuration against the law rather than against itself.

## What Already Exists
Time and attendance platforms and payroll systems ship configurable earnings and overtime rules. Wage and hour compliance guidance is published by the Department of Labor and by state agencies. Employment law publishers track developments. Some platforms offer state-level rule presets. Litigation support experts perform these calculations forensically after the fact.

## The Customisation Gap
Presets exist at state level and the errors are in the interaction between rules and the employer's own pay practices — which earnings are non-discretionary, how a bonus is allocated across the period it was earned, whether a differential is included in the regular rate. Those are the questions no preset answers and every employer resolves by guessing.

Configuration verification is entirely absent. Whether the configured rule produces the legally required result is testable: generate scenarios across schedule patterns and earnings combinations, compute pay under both the configuration and the statutory rule, and report divergence. That is straightforward, would catch the errors that currently surface in litigation, and no vendor does it.

Population anomaly detection is the cheaper complement. Employers whose overtime as a share of hours diverges sharply from comparable employers, or whose break premium rate is implausibly low for their industry and state, are visible in the provider's cross-employer data and are not looked at.

## Impact If Solved
Wage and hour exposure is one of the largest employment liabilities employers carry and it originates in a settings page filled in by someone doing their best. Verifying configuration against the statutory calculation protects workers from underpayment they cannot detect and employers from claims they cannot currently see coming.
