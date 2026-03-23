# LED Lighting Recipe Management Across Growth Stages

**Niche:** [[niches/greenhouse-horticulture/urban-vertical-farms/profile|Urban & Vertical Farms]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** Vertical farms run 5-10 different LED light recipes (spectrum, intensity, photoperiod) across growth stages and crop types, but recipe management is manual — a grower must physically reprogram controllers or adjust settings at each tier every time a new crop batch enters a stage, leading to missed transitions and inconsistent lighting.
**Tags:** #workflow-orchestration #automation #worker-facing #quick-win

## The Problem
A leafy greens vertical farm growing 4 crop types (butterhead lettuce, romaine, basil, arugula) with 3 growth stages each (germination, vegetative, finish) requires 12 distinct LED recipes. Each recipe specifies: photoperiod (hours on/off), light intensity (PPFD in micromoles/sq meter/second), and spectrum (ratio of blue, red, far-red, and white channels). When a crop tray transitions from vegetative to finish stage — which happens at different rates depending on the crop and the individual batch — the LED recipe must change. In a facility with 200+ growing positions across 8 tiers, recipe transitions happen 20-40 times per day. The grower or production assistant must identify which positions need recipe changes, walk to the physical controllers or access the control interface, and update settings. Missed or late transitions cause quality defects: lettuce that stays on a high-blue vegetative recipe too long becomes compact and fails to fill the package.

## Why It's Still Broken
LED controllers from major manufacturers (Fluence, Signify/Philips, Current/GE) provide zone-level scheduling but do not integrate with crop management systems. The controller knows what recipe to run and when, but it does not know what crop is growing at each position or when that crop will transition stages. The crop management side (whiteboard, spreadsheet, or basic software) tracks growth stages but does not communicate with the LED controller. The grower is the integration layer, manually translating crop stage information into lighting commands.

## What a Fix Looks Like
An automated recipe management system that: (1) maps growing positions to LED controller zones, (2) tracks crop type and growth stage at each position via the production management system, (3) automatically triggers LED recipe transitions when a crop batch enters a new stage (based on calendar days from planting, visual assessment via camera, or grower confirmation), and (4) validates that the correct recipe is running at every position with alerts for mismatches. The system integrates with LED controller APIs (Fluence has REST API capability, Signify supports DALI protocol) and eliminates the 30-60 minutes/day of manual recipe management.

## Who Feels the Pain
Production assistants who spend 30-60 minutes daily walking tiers to verify and adjust LED settings. Head growers who discover quality defects caused by missed or late recipe transitions — typically identified 3-5 days after the error when the crop is already affected. Operations managers who see energy wasted on incorrect lighting (running high-intensity finish recipes on newly seeded trays).

## Impact If Fixed
Recipe management labor eliminated: 30-60 minutes/day = 180-360 hours/year at $18-22/hour = $3,200-$7,900 saved. Quality defects from missed transitions reduced by 80-90%, recovering $20K-$60K/year in downgraded product. Energy waste from incorrect recipes reduced by 5-8%, saving $10K-$30K/year.
