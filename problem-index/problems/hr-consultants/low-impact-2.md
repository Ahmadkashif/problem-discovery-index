# Benefits Benchmarking for SMB Clients

**Industry:** [[hr-consultants|HR Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic salary surveys tell you what "a marketing manager" earns nationally — not what a 35-person HVAC company in suburban Phoenix should offer to stop losing technicians to competitors.
**Tags:** #gradient-boosting #regression #tabular-ml #data-integration

## The Problem
HR consultants advise SMB clients on competitive compensation and benefits packages during annual reviews, new hire offers, and retention crises. The consultant needs to answer: "Is this client's health plan competitive for their industry, geography, and size? Should they add dental? Is their PTO policy driving attrition?" Answering these questions currently requires manual synthesis from BLS data (lagging 12-18 months), Glassdoor and Payscale (self-reported, skewed toward tech), benefits broker quotes (one carrier at a time), and the consultant's own pattern recognition across their client base.

## What Already Exists
BLS Occupational Employment and Wage Statistics provide broad compensation data. Payscale, Salary.com, and Glassdoor offer salary benchmarking tools. Benefits brokers provide plan comparison spreadsheets. Mercer and Radford publish annual survey reports targeting enterprise HR.

## The Customisation Gap
None of these sources provide the intersection of industry vertical + company size + specific geography + benefits package composition that an HR consultant needs for an SMB recommendation. A 40-person plumbing contractor in suburban Dallas has a fundamentally different competitive landscape than a 40-person marketing agency in Austin, but both show up as "small business, Texas" in generic surveys. The consultant needs to benchmark total compensation packages (base + benefits + PTO + retirement match) holistically, not salary in isolation. Existing tools don't aggregate across the consultant's own anonymized client data — the single richest source of ground-truth benchmarks for their market segment.

## Impact If Solved
Transforms benefits advisory from a 4-6 hour research project per client into a 30-minute data-driven recommendation, increasing the consultant's advisory capacity by 3-4 clients per week during renewal season.
