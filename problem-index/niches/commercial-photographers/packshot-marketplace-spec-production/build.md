# Colour-Measured Packshots

**Niche:** [[niches/commercial-photographers/packshot-marketplace-spec-production/profile|Packshot & Marketplace-Spec Production]]
**Industry:** [[industries/commercial-photographers|Commercial Photographers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Studios promise "colour accurate" images and judge colour by eye against a sample under studio light, while the retailer's return data counts every item that "didn't match the picture".
**Tags:** #gaussian-processes #linear-regression #feature-engineering #evaluation-metrics #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver every SKU's images right first time against each retailer's specification and the physical sample's true colour before the listing date, and whoever posts the lowest reshoot and rejection rate per SKU takes the account.

## The Problem
Colour is the most common way a technically perfect packshot fails the shopper. A navy that reads purple or a beige that reads grey means returns across every unit sold. About one in eight UK online shoppers has returned an item because it looked different from its pictures (Royal Mail, 2016), and six in ten German online shoppers name a mismatch with the description or images as a return reason (KPMG, 2025). Studios shoot with a colour target and retouchers match by eye to a reference shot, but nobody measures the delivered image against the physical sample, so the error is invisible until returns arrive weeks after the sample has gone back.

## Why Nobody Has Built This
Measuring samples adds a step at check-in, and studios are paid per SKU, not per accuracy point. Brands rarely share return reasons with their studios. Colour science tools exist for print and textile labs, not for photography workflows.

## What to Build
Sample check-in with a handheld spectrophotometer reading stored against the SKU and colourway; a model that predicts the colour difference (ΔE) of the delivered image from capture settings, lighting, material and retouch adjustments; automatic flags while the sample is still on the shelf; and a per-client report of measured accuracy that the studio can sell as a guarantee.

## Target Customer
Directors of high-volume ecommerce studios competing for apparel, home and beauty accounts where colour-driven returns are a known cost.

## Impact If Built
Out-of-tolerance colourways are caught before delivery, return rates attributable to colour fall measurably, and the studio has a number to compete on instead of a promise.
