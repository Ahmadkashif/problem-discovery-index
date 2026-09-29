# A Provable Configuration

**Niche:** [[niches/payroll-platforms/regular-rate-premium-calculation/profile|Regular Rate & Premium Calculation]]
**Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An employer cannot currently demonstrate that its overtime configuration matches the law in the states where its employees work, which is the exact thing it will be asked to demonstrate if it is ever challenged.
**Tags:** #bert #large-language-models #hypothesis-testing #evaluation-metrics #confidence-intervals #compliance #automation #combinatorics-and-counting
**Contested on:** Every serious competitor in wage calculation is fighting to compute the regular rate and every premium correctly for every jurisdiction an employer operates in — and whoever can prove a configuration matches the law takes the account.

## The Problem
An employer with hourly staff in eleven states is asked, in a wage and hour matter, to demonstrate that its overtime calculations were correct. It produces its payroll configuration, its earnings codes and its pay registers. What it cannot produce is a demonstration that the configuration implements the applicable law in each of those states — because nobody has ever performed that comparison, in either direction. The employer may be entirely correct and cannot show it, or may be wrong in one state for three years and not know.

## Why Nobody Has Built This
Wage and hour rules are published in statute, regulation and guidance rather than in any executable form, and turning them into checkable rules is content work that no provider has undertaken for the same liability reasons that recur throughout this vault. The configuration side is equally unrepresented: earnings codes and inclusion flags are a configuration in a database rather than a stated rule set, so even with executable law there is nothing to compare against without first extracting the configuration's meaning. Both halves are tractable and neither exists.

## What to Build
Executable wage and hour content and a comparison against the extracted meaning of an employer's configuration. The content encodes, per jurisdiction and with effective dates, the overtime thresholds and bases, the earnings types that must be included in the regular rate, the premium obligations and their own regular-rate treatment, and the interaction rules. The employer's configuration is decompiled into the same representation — which earnings codes are included, which thresholds apply, which premiums are configured — so the comparison is rule against rule rather than document against database. Divergence is reported per jurisdiction with the affected population and the estimated exposure. Test cases are generated from the content and run against the live engine, so the assertion is not merely that the configuration looks right but that the engine actually produces the right number for a representative population of scenarios. The output is a dated compliance statement, which is what the employer needs and cannot obtain today.

## Target Customer
Payroll providers, employers with multi-state hourly workforces, professional employer organisations, and the employment counsel who currently answer this question with an opinion.

## Impact If Built
A provable configuration converts the most litigated area of wage and hour from an unexamined risk into a dated statement. For the employers who are correct it is a defence they cannot currently mount; for those who are not, it is a correction that stops the accumulation and identifies who is owed what — which is the outcome that matters for the employees involved.
