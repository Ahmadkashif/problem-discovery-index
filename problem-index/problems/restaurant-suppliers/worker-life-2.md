# Warehouse Order Accuracy for Custom-Cut and Portioned Products

**Industry:** [[restaurant-suppliers|Restaurant Suppliers]]
**Type:** Worker Life Changing
**One-liner:** Meat cutters and warehouse workers stop getting blamed for pick errors on custom orders that were set up to fail by illegible specs and time pressure.
**Tags:** #cnns #object-detection #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #worker-facing

## The Problem
Restaurant supply warehouses handle a mix of case-pick (grab a case of canned tomatoes) and custom-cut/portioned products (cut 40 lbs of NY strip into 12-oz portions, portion 25 lbs of salmon into 6-oz filets). Custom orders account for 15-25% of warehouse volume but generate 60-70% of picking errors. A meat cutter receives a printed ticket — often hand-annotated by a sales rep — specifying cut, portion size, trim level, and pack count. Under time pressure (orders ship by 4 AM for morning delivery), errors compound: wrong portion size, wrong cut specification, miscounted packs. Each error triggers a credit memo ($50-$200), a re-delivery, and a damaged customer relationship.

## Why It Matters to the Worker
Meat cutters and produce handlers are skilled tradespeople earning $18-$28/hour who take pride in their craft. When an error occurs — even one caused by an illegible order ticket or ambiguous spec — the cutter gets the blame. The overnight shift (10 PM - 6 AM) is physically demanding, and the constant pressure of error-driven callbacks erodes morale. Experienced cutters leave for grocery chains that offer day shifts and simpler specs. Turnover in warehouse custom-cut positions runs 40-60% annually, far above the 25% warehouse average.

## What a Solution Looks Like
A camera-based verification system at the cutting station that confirms portion weight, cut type, and pack count against the digital order spec before the product is sealed and labeled. The cutter places finished portions on a scale/camera platform; the system verifies count and approximate portion size via object detection, flags discrepancies in real-time ("Order calls for 12-oz portions — current average is 14.2 oz"), and prints a verified label. The order ticket itself is digitized and displayed on a screen at the station, eliminating the illegible-handwriting problem entirely.

## Impact If Solved
Custom-cut error rates drop from 8-12% to under 2%, eliminating $50K-$150K in annual credit memos at a mid-size distributor. Cutters work with confidence instead of anxiety, reducing turnover by an estimated 15-20 percentage points. Delivery drivers stop making costly re-runs for mis-picked custom orders.
