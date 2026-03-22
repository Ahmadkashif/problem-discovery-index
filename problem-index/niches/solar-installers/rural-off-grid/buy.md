# Grid-Tied Design Tools Adapted for Off-Grid

**Niche:** [[niches/solar-installers/rural-off-grid/profile|Rural & Off-Grid Solar]]
**Industry:** [[industries/solar-installers|Solar Installers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aurora Solar is the industry-standard design tool but assumes grid-tied operation — adding an off-grid mode with battery bank sizing, generator integration, and autonomy-based design methodology would capture the underserved off-grid installer market without building a separate product.
**Tags:** #data-integration #automation #quick-win #gradient-boosting

## The Problem
Off-grid installers who use Aurora Solar for their grid-tied projects must switch to spreadsheets for off-grid design because Aurora's design philosophy assumes grid interconnection. Specifically, Aurora sizes systems to offset a percentage of the utility bill, not to meet a standalone load requirement. Aurora's battery module sizes for backup duration or TOU arbitrage, not for multi-day autonomy. And Aurora's production modeling doesn't flag the design month (worst-month production) that determines off-grid array sizing.

## What Already Exists
Aurora handles 3D roof modeling, shade analysis, production simulation, and electrical design (string sizing, inverter selection). The production modeling engine is excellent. The battery module supports various configurations. What's missing is the off-grid design methodology — sizing to meet 100% of load through the worst production month rather than optimizing against a utility bill.

## The Customization Gap
An off-grid mode within Aurora that: (1) replaces the utility bill input with a load profile input — daily kWh requirement by season; (2) changes the sizing methodology from "offset X% of utility bill" to "meet 100% of daily load in the design month (lowest production month)"; (3) sizes the battery bank for autonomy rather than backup — "3 days of autonomy at 50% depth of discharge" rather than "10 hours of backup power"; (4) integrates generator sizing and annual run-hour estimation; and (5) produces an off-grid system specification document that includes array size, battery bank configuration, charge controller sizing, inverter sizing, and generator recommendations. This leverages Aurora's existing production modeling and electrical design infrastructure while adding the off-grid-specific design methodology.

## Target Customer
Off-grid solar installers already using Aurora for grid-tied projects who want one platform for all their design work. Aurora as a platform seeking to serve the growing off-grid/resilience market.

## Impact If Solved
Eliminates the dual-tool workflow for installers doing both grid-tied and off-grid work. Captures 2,000-5,000 off-grid installers currently using spreadsheets. Produces more accurate off-grid designs by leveraging Aurora's superior production modeling rather than simplified spreadsheet calculations. Enables Aurora to market to the resilience/independence customer segment beyond grid-tied economics.
