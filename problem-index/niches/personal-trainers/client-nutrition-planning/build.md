# Constraint-Aware Meal Plan Generator for Trainers

**Niche:** [[niches/personal-trainers/client-nutrition-planning/profile|Client Nutrition Planning]]
**Industry:** [[industries/personal-trainers|Personal Trainers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool generates complete weekly meal plans that simultaneously hit specific macro targets, respect client food preferences and allergies, account for cooking skill and prep time, and adapt when the trainer adjusts macros — forcing 1-3 hours of manual plan creation per client.
**Tags:** #reinforcement-learning #recommendation #automation #ai-agent #quick-win

## The Problem
A trainer creating a meal plan for a client must satisfy 5-8 simultaneous constraints: hit 2,200 calories with 165g protein, 245g carbs, 73g fat (exact ratios matter for body composition goals), avoid dairy and gluten (allergies), include only foods the client likes (picky eater), use recipes that take under 30 minutes (busy schedule), cost under $80/week (budget), and be different enough day-to-day that the client doesn't get bored. This is a complex constraint-satisfaction problem that trainers solve manually, often taking 1-3 hours per client to build a 7-day plan. When the trainer adjusts macros (drop carbs by 25g, increase protein by 10g), the entire plan must be rebuilt.

## Why Nobody Has Built This
EatThisMuch attempts automated meal planning but uses simple calorie-matching without precise macro control, produces repetitive meals, and doesn't integrate with coaching workflows. Building a meal plan generator that hits exact macros while respecting food preferences requires a large food/recipe database with accurate nutritional data (most databases have 10-20% error rates on macros), a constraint solver that can compose meals into daily and weekly plans, and enough variety to generate non-repetitive plans week over week. The nutritional accuracy requirement alone eliminates most general-purpose recipe databases.

## What to Build
A meal plan engine that: (1) intakes client constraints (macro targets, allergies, food preferences, cooking skill, budget, family size), (2) generates 7-day meal plans that hit macro targets within 5g tolerance per macro per day, (3) uses a curated recipe database with verified nutritional data, (4) produces variety across days while maintaining macro consistency, (5) auto-regenerates when the trainer adjusts macros (just change the numbers, the plan rebuilds), (6) generates shopping lists with quantities and estimated cost, and (7) outputs in a client-ready format (PDF, app, or integration with coaching platforms).

## Target Customer
Personal trainers with nutrition certifications who offer meal planning to 10-30 clients and spend 15-30 hours/month on manual plan creation.

## Impact If Built
Reduces meal plan creation from 1-3 hours to 10-15 minutes per client, enabling trainers to serve 3-5x more nutrition clients — increasing nutrition coaching revenue from $2K-5K/month to $8K-15K/month without additional work hours.
