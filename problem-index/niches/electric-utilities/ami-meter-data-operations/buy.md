# Meter Data Management With Connectivity Correction

**Niche:** [[niches/electric-utilities/ami-meter-data-operations/profile|AMI Meter Data Operations]]
**Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Meter data management systems validate reads for billing and ignore the voltage data that would fix the grid model.
**Tags:** #k-means-clustering #pca #graph-theory #feature-engineering #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every exception in interval meter data into a correct bill and a correct grid model without a truck roll, and whoever resolves the most exceptions automatically, without a billing error reaching a customer, takes the account.

## The Problem
GIS often has meters assigned to the wrong transformer or phase. That corrupts outage prediction, transformer loading and hosting capacity, all of which assume the model is right. The AMI voltage data that would reveal the errors is collected but stored, if at all, for power quality complaints.

## What Already Exists
Meter data management (Itron, Oracle, Siemens) with VEE and billing determinants; GIS from Esri with ArcFM or Utility Network; some vendors' phase-identification add-ons; academic methods for voltage-correlation clustering.

## The Customization Gap
The adaptation: routine collection and retention of interval voltage; correlation-based grouping of meters to transformers and phases; confidence-scored correction proposals written to the GIS editing workflow for a technician to verify; transformer loading computed from corrected groups; and feedback from field verification into the model.

## Target Customer
Meter operations and GIS managers at utilities using AMI data for outage management and DER planning.

## Impact If Solved
Connectivity errors corrected on ~5%–10% of meters (an assumed error rate, estimate) lift every downstream analytic, from outage prediction to hosting capacity and transformer loading, that depends on the model.
