# Defect Prediction Before Delivery

**Niche:** [[niches/commercial-photographers/retouching-post-production/profile|Retouching & Post-Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Post-production houses either check every image twice or ship defects for the client to find, because nothing tells them which few hundred of tonight's ten thousand images are likely wrong.
**Tags:** #semantic-segmentation #cnns #evaluation-metrics #gradient-boosting #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to return brand-consistent, spec-compliant edits overnight at a defect rate the client's QA never sees, and whoever automates the routine edit without letting errors escape takes the account.

## The Problem
A retouching house processes thousands of images a night for dozens of brands, mixing automated passes and human edits. Defects (a halo on a clipping path, a missed lint fleck, a ghost-mannequin seam, a colour off-spec) are rare per image but certain across the batch. Full second-pass QA doubles the cost; sampling lets defects through, and the client's QA rejection is what the house is judged on.

## Why Nobody Has Built This
Retouching houses compete on per-image price and have treated QA as headcount. The labels that would train a defect model, client rejections with reasons, sit in emails and portals rather than linked to the image and the edit history.

## What to Build
A model that scores every finished image for defect risk from the image itself (edge quality, residual background, colour against the reference), the edit history (automated or manual, which retoucher, time spent) and the product category, trained on historical client rejections. High-risk images go to a second-pass reviewer, and the threshold is set per client to match their tolerance.

## Target Customer
Operations heads at retouching and post-production houses and at retailers' in-house post-production teams.

## Impact If Built
QA effort concentrates where defects are, client-visible defect rates fall, and the house can sell a measured quality level rather than a price.
