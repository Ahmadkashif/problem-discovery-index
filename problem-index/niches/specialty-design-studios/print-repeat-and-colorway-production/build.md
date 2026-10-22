# Strike-Off Prediction Before the Mill Prints

**Niche:** [[niches/specialty-design-studios/print-repeat-and-colorway-production/profile|Print Repeat & Colourway Production]]
**Industry:** [[industries/specialty-design-studios|Specialty Design Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A print designer approves colours on a screen, the mill prints them on a substrate that shifts every colour, and the first honest view of the print is a strike-off weeks later.
**Tags:** #gaussian-processes #cnns #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn an approved motif into mill-ready repeats, separations and colourways that strike off right first time, and whoever cuts strike-off rounds takes the account.

## The Problem
Screen colour, reference standards and printed result disagree. How a colour prints depends on substrate, base colour, ink or dye system, print method and the mill's process. Strike-off rounds are spent correcting colours that could have been predicted from the mill's previous jobs on the same fabric.

## Why Nobody Has Built This
The data — measured strike-off colour against target, by mill, substrate and method — sits at mills and is rarely shared with designers, and colour management tools stop at device profiles.

## What to Build
A predictor trained on paired targets and measured strike-offs for a mill and substrate: given artwork colours and print parameters, it predicts the printed colour and its difference from the standard, flags colours likely to fail, and proposes adjusted targets. A Gaussian process over colour space handles sparse data for each substrate.

## Target Customer
Print studios and brand print teams working with a few repeat mills, and mills offering it as a service.

## Impact If Built
Fewer strike-off rounds per print and colourway, and earlier warning when a palette cannot be printed on the chosen fabric.
