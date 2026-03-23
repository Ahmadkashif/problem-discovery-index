# Tipped-Worker Overtime Compliance

**Niche:** [[niches/independent-restaurants/tip-pooling-workforce-management/profile|Tip Pooling & Workforce Scheduling Operations]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Scheduling tools flag overtime hours but do not calculate overtime pay correctly for tipped employees — where the rate depends on the tip credit, the regular rate, and the "regular rate of pay" including tips.
**Tags:** #compliance #automation #tabular-ml #worker-facing

## The Problem
Overtime for tipped employees is calculated differently than for non-tipped workers. If an employer takes a tip credit, the overtime rate is based on the full minimum wage (not the reduced tipped wage), plus any applicable tip credit adjustments. When a tipped employee works different roles in the same week (server at $2.13/hour + tips for some shifts, hostess at $7.25/hour for others), the overtime calculation requires a weighted average "regular rate of pay." Most restaurant managers get this wrong, overpaying some employees and underpaying others — both of which create legal exposure.

## What Already Exists
7shifts, Homebase, and When I Work flag when an employee approaches 40 hours and calculate overtime at 1.5x the base rate. ADP and Gusto payroll processors handle tip reporting for tax purposes. But none of these tools correctly calculate the weighted overtime rate for dual-role tipped workers or adjust overtime calculations for tip credit jurisdictions.

## The Customization Gap
The tool must understand the employee's tip credit status, calculate the correct regular rate of pay when employees work multiple roles at different wage rates in the same week, apply the correct overtime premium based on jurisdiction-specific rules, and flag scheduling conflicts before they happen (e.g., "scheduling Maria as hostess Thursday will trigger overtime at $18.75/hour instead of her tipped rate — consider scheduling her as server instead").

## Target Customer
Restaurant managers in tip-credit states who schedule employees across multiple roles (server, bartender, host, busser) and do not know whether their overtime calculations are legally correct.

## Impact If Solved
Correct overtime calculation prevents DOL back-pay claims averaging $15K-$75K per incident, and proactive scheduling suggestions reduce unintended overtime costs by $200-$500/week.
