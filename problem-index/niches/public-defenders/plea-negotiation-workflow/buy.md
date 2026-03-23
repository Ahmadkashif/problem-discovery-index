# Sentencing Data Adapted for Defense-Side Plea Evaluation

**Niche:** [[niches/public-defenders/plea-negotiation-workflow/profile|Plea Negotiation Workflow]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Sentencing databases exist for judges and prosecutors (USSC, state sentencing commissions) but aren't structured for the defense question: "Is this plea offer better or worse than what my client would likely get at trial?"
**Tags:** #gradient-boosting #regression #tabular-ml #quick-win

## The Problem
When evaluating a plea offer, defenders need to answer a comparative question: what would this defendant likely receive if convicted at trial versus what the plea offers? Sentencing data exists — the U.S. Sentencing Commission publishes federal data, and most state sentencing commissions maintain disposition databases. But this data is organized for policy analysis, not case-level defense decision-making. The defender can't easily query: "For defendants with similar profiles charged with [X] in this jurisdiction, what was the median sentence after trial versus after plea?"

## What Already Exists
The U.S. Sentencing Commission's USSC database (federal cases), state sentencing commission databases (varies by state), court administrative records accessible through Odyssey/Tyler Technologies, and academic datasets (NCSC's State Court Processing Statistics). Some jurisdictions publish sentencing dashboards for judges. Measures for Justice provides county-level criminal justice metrics.

## The Customization Gap
Defense-side plea evaluation requires: filtering by defendant characteristics (criminal history score, demographics, employment, housing), comparing plea outcomes to trial outcomes for similarly-situated defendants, adjusting for judge-specific sentencing patterns, and presenting results as a decision-support tool (not a research database). The interface must answer the defender's question in under 2 minutes — "given this offer, what's my client's expected value of going to trial?" — with confidence intervals that account for judicial discretion.

## Target Customer
Public defender offices, state indigent defense commissions, and legal aid organizations that support indigent defense.

## Impact If Solved
Gives every public defender access to sentencing benchmarks that currently exist only in aggregate statistics. Enables evidence-based plea advice to clients, improving informed consent. Estimated 5-10 minutes saved per case on sentencing research, and measurable improvement in client satisfaction with the defense process.
