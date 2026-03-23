# Automated Immigration Consequence Screener

**Niche:** [[niches/public-defenders/immigration-facing-defendants/profile|Immigration-Facing Defendants]]
**Industry:** [[industries/public-defenders|Public Defenders]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool automatically cross-references a defendant's criminal charges against their immigration status to produce a case-specific deportation risk assessment — defenders do this manually or not at all.
**Tags:** #bayesian-network #binary-classification #tabular-ml #compliance #automation

## The Problem
A public defender is appointed to represent a client charged with petty theft. The client is a lawful permanent resident. The defender pleads the client to the charge without consulting an immigration expert. The conviction triggers removal proceedings — the client faces deportation and permanent separation from their U.S. citizen children. This scenario repeats thousands of times per year because most public defenders don't know immigration law and have no tool to flag the risk. The Supreme Court requires this advice (Padilla v. Kentucky), but provides no resources to deliver it.

## Why Nobody Has Built This
The intersection of criminal and immigration law is extraordinarily complex. A single criminal charge can have different immigration consequences depending on the client's immigration status (LPR vs. visa holder vs. DACA vs. TPS), the state statute's elements (categorical approach analysis), the sentence imposed, and the client's prior criminal history. Building an accurate screener requires encoding both the Immigration and Nationality Act and 50 states' criminal codes, plus tracking constantly-changing BIA and circuit court precedent. This is a legal-knowledge engineering problem that most tech companies can't staff.

## What to Build
A screening tool that takes two inputs — the client's immigration status and their current criminal charges (statute number and jurisdiction) — and produces a consequence report: deportation risk (low/medium/high/certain), specific immigration provisions triggered, alternative charges or plea structures that avoid immigration consequences ("immigration-safe pleas"), and a flag indicating whether the case requires consultation with an immigration specialist. Integrated into the case management system to auto-flag at intake when a client indicates noncitizen status.

## Target Customer
Chief Public Defenders and state indigent defense commissions. Offices in jurisdictions with significant immigrant populations (California, Texas, New York, Florida, Illinois, New Jersey) — estimated 60-70% of the market.

## Impact If Built
Brings Padilla compliance from an estimated 30-40% of noncitizen cases to near-universal screening. Prevents wrongful deportations caused by uninformed plea advice. Each prevented deportation avoids catastrophic harm to the client and their family, and saves the immigration system the cost of removal proceedings ($10K-30K per case).
