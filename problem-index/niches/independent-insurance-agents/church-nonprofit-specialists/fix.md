# Abuse/Molestation Liability Coverage Gap Detection

**Niche:** [[niches/independent-insurance-agents/church-nonprofit-specialists/profile|Church & Nonprofit Specialists]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Fix (Pain Point)
**One-liner:** Many churches carry GL policies that exclude or severely sublimit abuse/molestation liability — the single most catastrophic exposure for any organization with youth programs — and neither the agent nor the church knows it until a claim occurs.
**Tags:** #binary-classification #tabular-ml #compliance #tacit-knowledge-ml

## The Problem
Standard commercial GL policies either exclude abuse/molestation liability entirely or include it with sublimits as low as $100K — far below the $1M-$5M verdicts common in these cases. Churches that purchase insurance through generalist agents often end up with standard commercial policies that do not include the specialty endorsements required for youth-serving organizations. The coverage gap is invisible: the church believes it is insured, the agent may not have flagged the exposure, and the sublimit is buried in policy endorsements that nobody reads until a claim is filed.

## Why It's Still Broken
Generalist agents who write a few church accounts per year lack the specialty knowledge to identify abuse/molestation as a coverage priority. AMS systems do not flag this exposure when a "church" or "youth organization" classification is entered. Policy review tools check for obvious gaps (liability limits, property valuations) but do not analyze endorsement-level sublimits against organization-specific risk profiles. The mismatch between the church's activities and its coverage is only visible to agents who specialize in this niche.

## What a Fix Looks Like
An automated policy analysis tool that ingests a church's GL policy (dec page + endorsements) and compares the coverage against the organization's activity profile. If the church has youth programs, counseling services, or overnight events, the tool flags abuse/molestation liability sublimits below recommended thresholds and recommends specific endorsements or carrier changes. The agent receives a coverage gap report they can present to the church board.

## Who Feels the Pain
Church administrators who discover after an incident that their $100K abuse/molestation sublimit is exhausted by defense costs alone, and agents who face E&O claims for failing to identify and communicate the coverage gap.

## Impact If Fixed
Prevents catastrophic uninsured losses for churches (average abuse/molestation claim: $1.5M-$3M) and protects agents from E&O exposure that can cost $50K-$500K per incident. Estimated 15-20% of church GL policies have material abuse/molestation coverage gaps that this tool would catch.
