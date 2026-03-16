# Policy-to-Carrier Matching for Commercial Lines

**Industry:** [[independent-insurance-agents|Independent Insurance Agents]]
**Type:** High Impact
**One-liner:** Producers stop spending 30-60 minutes per commercial account guessing which carriers will write the risk and instead get ranked carrier recommendations in seconds.
**Tags:** #gradient-boosting #ranking #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
When a commercial lines prospect walks in — a restaurant needing GL/liquor liability, a contractor needing a wrap-up program, a manufacturer needing product liability — the producer must mentally cross-reference the risk profile against appetite guides from 15-30 appointed carriers. These appetite guides are PDF documents updated quarterly (at best), and the real appetite is shaped by underwriter relationships, recent loss experience in the carrier's book, and soft-market vs. hard-market dynamics that no document captures. Experienced producers develop an intuition for "Carrier X is hungry for this class right now" that takes 5-10 years to build; newer producers waste submissions on carriers that will decline, costing days of turnaround time and losing the prospect to a faster-moving agency.

## Why It's Unsolved
Carrier appetite is partially documented (published guides, NAICS/SIC preferences, state filings) but the actionable signal — which underwriter at which carrier is actively writing which class in which geography this quarter — lives in producers' heads and in the pattern of recent submissions and bind rates. No single data source captures this. Appetite guides are marketing documents, not operational truth. Building a training set requires linking submission records (often trapped in carrier portals or emailed as PDFs) to outcomes (quote, decline, bind, premium level), and most agencies lack structured submission-outcome tracking. The labeling problem is asymmetric: a declination is clear, but a "quoted but not bound" may reflect price, coverage terms, or the insured's choice — not carrier appetite mismatch.

## What a Solution Looks Like
A model ingests the risk profile (industry class, revenue, employee count, loss history, geography, coverage lines requested) and outputs a ranked list of carriers with estimated quote probability and predicted premium range. The ranking is trained on historical submission-to-outcome data across agencies (anonymized and aggregated), supplemented by structured appetite guide data and real-time signals like carrier rate filings and loss ratio trends. The producer reviews the top 3-5 recommendations, makes 3 targeted submissions instead of 8 speculative ones, and gets quotes back in days instead of weeks.

## Impact If Solved
Reduces commercial lines placement time by 50-70%, allowing producers to handle 2x the volume of new business. Newer producers perform at the level of 10-year veterans on carrier selection, compressing the onboarding timeline from years to months and directly increasing agency revenue per producer.
