# Wave Solder Parameter Knowledge Capture System

**Niche:** [[niches/electronics-contract-mfg/legacy-through-hole-assemblers/profile|Legacy Through-Hole Assembly Houses]]
**Industry:** [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The wave solder operator's knowledge of how to adjust machine parameters for each board type — accumulated over decades and stored only in their head — has no capture or transfer mechanism, and these operators are retiring at 3-5% per year with no replacement pipeline.
**Tags:** #gradient-boosting #tacit-knowledge-ml #worker-facing #revenue-impact

## The Problem
Wave solder machine operation is one of the most experience-dependent tasks in electronics manufacturing. The operator adjusts conveyor speed, preheat zone temperatures, solder pot temperature, wave height, flux type and application rate, and pallet/fixture design for each board type — and the optimal settings depend on the board's copper weight, component density, thermal mass distribution, connector types, and hole-to-lead ratio. An experienced operator looks at a board and knows from experience which parameter adjustments are needed; a new operator follows the recipe book but produces 3-5x higher defect rates until they develop their own feel over 2-5 years. With the average wave solder operator age above 50 and few young technicians entering the trade, this knowledge is disappearing.

## Why Nobody Has Built This
The wave solder parameter space is complex (8-12 adjustable parameters interacting nonlinearly), and the correlation between parameters and outcomes (solder joint quality) requires destructive or microscopic inspection that is not automated at most THT shops. Building a predictive model requires logging parameter settings per board type and correlating with per-joint defect data — a data collection infrastructure that does not exist at shops running paper travelers.

## What to Build
A parameter capture system that logs wave solder machine settings (via PLC data connection or manual entry at a kiosk) for each board type, correlates settings with inspection outcomes (defect counts by category), and builds a per-board-type recipe database with the experienced operator's optimal settings. When a board type is run by a different operator, the system displays the proven recipe with the experienced operator's notes. Over time, with sufficient data, a regression model identifies which board characteristics predict which parameter adjustments, enabling recipe prediction for new board types.

## Target Customer
Owners and shop foremen at THT assembly shops with wave solder operations employing operators with 15+ years of experience approaching retirement. Approximately 200-300 US THT shops with dedicated wave solder operations. Average contract value: $15-25K/year.

## Impact If Built
New operator ramp time decreases from 2-5 years to 6-12 months. Wave solder defect rate for operators using the system decreases by 40-60%. Knowledge of the retiring workforce is preserved as a company asset. First-pass yield on wave solder improves by 3-5%.
