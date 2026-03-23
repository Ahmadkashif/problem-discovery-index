# ML-Assisted Ink Key Calibration from Color Measurement

**Niche:** [[niches/printing-shops/commercial-offset-printers/profile|Commercial Offset Printers]]
**Industry:** [[industries/printing-shops|Printing Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product takes real-time spectrophotometer readings from a running press and recommends specific ink key adjustments to achieve target color — pressmen make these adjustments by eye and experience, and this skill is retiring with the current generation of press operators.
**Tags:** #gradient-boosting #linear-regression #tacit-knowledge-ml #worker-facing

## The Problem
Color matching on an offset press requires the pressman to read spectrophotometer measurements (L*a*b* values across the press width) and adjust individual ink keys (typically 20-32 keys per color, 4 colors = 80-128 total adjustments) to move the color toward the target. The relationship between ink key position and resulting color is nonlinear and varies with substrate absorbency, ink tack, blanket condition, and press speed. An experienced pressman reads a scan bar report and makes 3-5 targeted adjustments to achieve color match in 1-2 pull sheets; a junior operator makes 8-15 adjustments over 5-8 pulls, consuming 15-30 additional minutes and 100-200 additional waste sheets per job. This skill takes 5-10 years to develop, and the average pressman age is 50+.

## Why Nobody Has Built This
Press manufacturers (Heidelberg, Komori, manroland) have built closed-loop color control for their newest presses ($2M+), but 80% of installed offset presses lack this capability. The aftermarket opportunity — adding intelligent ink key recommendation to existing presses with inline spectrophotometers — requires modeling the specific ink/key/substrate/press interactions for each individual press. No vendor has built a cross-manufacturer ink key recommendation system.

## What to Build
A software layer that connects to the shop's existing inline spectrophotometer (X-Rite IntelliTrax, Techkon), ingests current color measurements and target values, and recommends specific ink key adjustments (key number, direction, magnitude) using a regression model trained on that press's historical adjustment patterns. The pressman sees a visual recommendation on a screen (key 7: +2 clicks, key 12: -1 click) and applies the adjustment — or overrides with their own judgment. Each adjustment and outcome refines the model.

## Target Customer
Owners and production managers at commercial offset shops with inline spectrophotometers but without closed-loop press control (presses 5-20 years old). Approximately 3,000-5,000 US offset shops with spectrophotometers. Average contract value: $10-20K/year per press.

## Impact If Built
Makeready waste decreases by 30-50% (100-200 fewer waste sheets per job). Color match time decreases by 40-60%. Junior pressmen achieve journeyman-level color performance within 6-12 months instead of 5-10 years. Press utilization increases by 5-10% from faster makeready.
