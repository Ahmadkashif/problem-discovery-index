# Rate Comparison Engine Adapted for Overlay-Aware Routing

**Niche:** [[niches/mortgage-brokers/lender-submission-routing/profile|Lender Submission & Routing]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Optimal Blue and Mortech compare wholesale rates but don't filter by lender overlays — the broker sees the best rate from a lender that will deny their file.
**Tags:** #bert #text-classification #nlp #data-integration #tabular-ml #compliance

## The Problem
A broker pricing a loan on Optimal Blue sees 15-20 lenders sorted by rate. But the rate display doesn't show that Lender A's 6.125% rate comes with a 700 minimum credit score overlay on 2-4 unit properties (the borrower has 690 and is buying a duplex), or that Lender B at 6.25% requires full tax returns for self-employed borrowers but the borrower only has 1 year filed. The broker must mentally cross-reference the rate output against overlay knowledge for each lender — or submit and discover the overlay violation after days of processing.

## What Already Exists
Optimal Blue is the dominant wholesale rate comparison platform, aggregating rate sheets from 100+ wholesale lenders with scenario-based pricing (credit score, LTV, property type, lock period). Mortech (Zillow) provides similar functionality. Both output accurate rate quotes but assume the lender's agency guidelines with no visibility into lender-specific overlays that further restrict eligibility.

## The Customization Gap
An overlay compliance layer that sits on top of rate comparison output and flags scenarios where the borrower's profile violates a specific lender's overlay — even though the rate is technically available for that loan type. This requires maintaining a structured database of lender overlays (parsed from guidelines PDFs and update bulletins), mapping overlay parameters to borrower scenario fields, and filtering or annotating rate comparison results in real-time. The challenge is that overlays are published in unstructured PDF guidelines that change monthly.

## Target Customer
Any broker using Optimal Blue or Mortech who has experienced the frustration of submitting to the "best rate" lender only to be denied for an overlay violation that the rate engine didn't surface. Most common with newer loan officers who don't have the overlay matrix memorized.

## Impact If Solved
Eliminates overlay-related submission failures (estimated at 8-12% of broker submissions). Saves the 3-5 days of processing time lost to each failed submission. Levels the playing field between experienced loan officers (who carry overlay knowledge in their heads) and newer staff, enabling brokerage growth without proportional senior hiring.
