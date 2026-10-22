# Placing Drawings Generated From the Structural Model and Pour Breaks

**Niche:** [[niches/drafting-services/rebar-detailing-bar-lists/profile|Rebar Detailing & Bar Lists]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Rebar detailers redraw reinforcement from the engineer's PDFs into 2D placing drawings even though the rules for laps, hooks and shapes could generate most of it.
**Tags:** #object-detection #transformers #decision-trees #graph-neural-networks #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to release placing drawings and bar lists pour by pour ahead of the concrete schedule with no shape, quantity or lap errors, and whoever keeps the rebar fabricator's shop fed without a short shipment takes the account.

## The Problem
The engineer's drawings show reinforcement as schedules, typical details and notes. The detailer interprets them for every element, applies development and lap lengths, breaks bars for stock lengths and shipping, assigns marks and shapes, and splits the work into pour releases. Most of the hours go on applying rules the code already specifies.

## Why Nobody Has Built This
Engineers' reinforcement information is rarely in a structured model, schedule formats vary by firm, and the interpretation of typical details is where errors hide.

## What to Build
A generator that reads the structural drawings (or the engineer's model where available), extracts schedules and typical details, applies ACI and fabricator rules to produce bars, marks and shapes, splits them by the contractor's pour breaks, and outputs draft placing drawings and bar lists for the detailer to check, with every interpretation of a typical detail flagged for review.

## Target Customer
Detailing managers at rebar fabricators and independent rebar detailing bureaus.

## Impact If Built
Detailing hours per ton cut sharply, faster releases ahead of the pour schedule, and checkers focused on interpretation rather than arithmetic.
