# Pharma-Specific Temperature Excursion Analytics

**Niche:** [[niches/cold-chain-logistics/pharma-cold-chain-carriers/profile|Pharmaceutical Cold Chain Carriers]]
**Industry:** [[industries/cold-chain-logistics|Cold Chain Logistics]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic IoT analytics platforms like Controlant and Monnit capture temperature data and trigger threshold alerts, but they don't understand GDP excursion investigation requirements, MKT calculation, or the pharma-specific risk scoring that determines whether a temperature deviation is a reportable event or an acceptable transient.
**Tags:** #gradient-boosting #evaluation-metrics #compliance #data-integration

## The Problem
When a pharma shipment experiences a temperature excursion, the carrier must determine whether the deviation compromised product integrity. This assessment requires MKT calculation (a thermodynamic formula weighting temperature exposure over time), comparison to product-specific stability data, and classification of the event as reportable or non-reportable under the customer's quality agreement. Current monitoring platforms provide raw temperature data and threshold alerts but leave the investigation assessment — the scientifically and regulatory critical step — entirely to the compliance analyst.

## What Already Exists
Controlant, Sensitech ColdTrak, and Emerson GoTrack provide continuous temperature monitoring, threshold-based alerting, and basic temperature chart exports. These platforms are optimized for data capture and visualization, not for pharmaceutical regulatory analysis. They output data that a compliance analyst then manually processes into a GDP-compliant investigation.

## The Customization Gap
A pharma excursion analytics layer needs: (1) automated MKT calculation across multi-leg shipments with different temperature profiles per leg; (2) product-specific stability data integration — mapping each SKU to its validated temperature range and known stability profile to determine if MKT exceeded the product's validated limit; (3) event classification logic — distinguishing reportable excursions from transient deviations based on duration, magnitude, and MKT impact; (4) investigation report auto-generation in the customer's specified template format with pre-populated timeline, MKT values, and risk assessment narrative.

## Target Customer
Quality managers at pharma cold chain carriers and 3PLs with pharma divisions handling 500+ shipments/month, where excursion investigation volume justifies tooling investment.

## Impact If Solved
Reduces excursion investigation time from 2-3 hours to 20 minutes per event. Eliminates MKT calculation errors that currently cause false reportable events (creating unnecessary customer escalation) or missed reportable events (creating GDP compliance exposure). For a carrier handling 50 excursion investigations per month, this recovers 100+ compliance analyst hours monthly.
