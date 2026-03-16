# Dietary Restriction & Allergen Management Across Multi-Event Days

**Industry:** [[catering-companies|Catering Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Allergen tracking tools exist for restaurants, but none handle the catering-specific challenge of managing dietary matrices across multiple simultaneous events with different menus, shared kitchen prep, and cross-contact risk from batch production.
**Tags:** #bert #text-classification #nlp #compliance

## The Problem
A catering company running a multi-event day may have 15-30 distinct dietary restriction flags across events — gluten-free, dairy-free, nut allergy, shellfish allergy, vegan, kosher, halal, low-sodium, keto — each requiring menu-level accommodation and kitchen-level cross-contact prevention. The restriction information arrives in different formats: a corporate event planner sends a spreadsheet with employee names and restrictions, a wedding client mentions "three guests are celiac" in an email thread, a cocktail reception host says "make everything gluten-free" verbally during a tasting. The kitchen must consolidate these into a single production reality where the nut-free dessert for Event A is not prepped on the same surface used for the almond-crusted chicken for Event B, and the vegan entree for Event C does not share a warming pan with the butter-finished sauce for Event D.

## What Already Exists
MenuCalc and Nutritics provide allergen labeling for restaurant menus with ingredient-level allergen flagging. Toast and Square handle allergen alerts at POS for dine-in restaurants. FDA allergen labeling requirements (FALCPA/FASTER Act) are well-codified. These tools assume a fixed menu served in a single location with consistent ingredient sourcing — none model the catering scenario of multiple custom menus produced simultaneously in a shared kitchen with batch prep that creates cross-contact risk pathways not present in single-menu restaurant operations.

## The Customisation Gap
A catering-specific allergen management system needs: (1) NLP extraction of dietary restrictions from unstructured client communications — emails, PDF guest lists, proposal notes, verbal tasting notes transcribed by the sales manager — and classification into standardized allergen/dietary categories; (2) cross-event conflict detection that maps allergen-containing ingredients across all events sharing a production day and flags cross-contact risk from shared equipment, prep surfaces, and storage; (3) production-plan-level allergen sequencing that ensures allergen-free items are prepped before allergen-containing items on shared equipment, with cleaning protocols inserted into the production schedule. The extraction from unstructured client communication and the multi-event cross-contact risk modeling are the domain-specific components that restaurant allergen tools do not address.

## Impact If Solved
Prevents allergen incidents that carry both liability exposure (a single anaphylaxis event can generate six-figure lawsuits) and reputation destruction in a referral-driven business. Reduces the 20-30 minutes per event that kitchen managers spend manually cross-referencing dietary matrices against production plans and equipment assignments.
