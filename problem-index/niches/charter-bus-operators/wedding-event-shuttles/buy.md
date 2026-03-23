# Event-Aware Charter Quoting Tool

**Niche:** [[niches/charter-bus-operators/wedding-event-shuttles/profile|Wedding & Event Shuttles]]
**Industry:** [[industries/charter-bus-operators|Charter Bus Operators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Generic charter quoting tools calculate point-to-point costs but cannot price multi-leg, multi-bus event shuttles with wait time, overtime risk, and premium service surcharges.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
Wedding shuttles involve pricing complexity that standard charter quoting tools cannot handle: multiple legs with different distances and wait times between them, overtime risk when events run late (common — 40% of receptions extend past the contracted end time), premium vehicle surcharges for newer/luxury buses that wedding clients expect, and variable bus counts tied to guest RSVPs that change up to 2 weeks before the event. Operators either over-quote (losing to competitors) or under-quote (absorbing overtime and fuel costs when the event runs long).

## What Already Exists
BusHive, CharterBus.com instant quote tools, and operator spreadsheet templates calculate base costs (distance x rate + fuel + driver time). Wedding planning platforms (The Knot, Zola) list transportation vendors but provide no quoting tools. General-purpose proposal software (PandaDoc, Proposify) handles document creation but not charter-specific cost modeling.

## The Customization Gap
Wedding charter quoting requires a multi-leg cost model that accounts for: wait time between ceremony and reception (1-3 hours where the driver is idle but on the clock), overtime probability based on historical event patterns (Saturday evening weddings run 30 minutes late 60% of the time), luxury vehicle premium pricing, group size uncertainty buffers, and gratuity/parking fee inclusion that wedding clients expect in an all-inclusive quote. The tool must output a client-facing proposal with visual route maps and a clear timeline — not a spreadsheet.

## Target Customer
Charter operators who handle 20+ wedding/event bookings per year and currently spend 30-60 minutes building each wedding quote manually.

## Impact If Solved
Reduces wedding quote preparation from 45 minutes to under 10 minutes while improving margin protection on overtime scenarios by 15-20%, recovering $500-$2,000 per event in previously unquoted costs.
