# Floor Condition Assessment & Chemical Selection App

**Niche:** [[niches/cleaning-companies/carpet-floor-care/profile|Carpet & Floor Care Specialists]]
**Industry:** [[industries/cleaning-companies|Cleaning Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps a floor care technician photograph a surface, identify the material, and receive the correct chemical and technique protocol.
**Tags:** #cnn #multiclass-classification #computer-vision #tacit-knowledge-ml

## The Problem
Experienced floor care technicians identify carpet fiber types (nylon, polyester, olefin, wool) and hard floor materials (marble, granite, VCT, LVP) by sight and touch, then select chemicals and techniques accordingly. Junior technicians lack this pattern recognition and frequently select wrong chemicals — using an alkaline cleaner on wool (causes browning), an acidic cleaner on marble (causes etching), or too-hot water on olefin carpet (causes texture loss). These mistakes result in $500-$5,000 damage claims per incident.

## Why Nobody Has Built This
Floor material identification requires distinguishing visually similar materials (e.g., natural stone vs. engineered stone, nylon vs. polyester carpet) under variable lighting with dirty surfaces. The chemical selection decision tree is complex — it depends on material, soil type, soil level, and existing treatments. This knowledge lives in IICRC training manuals and experienced technicians' heads, not in digital systems.

## What to Build
A mobile app where the technician photographs the floor surface and any stains. Computer vision identifies the material type and stain category. The app outputs the recommended chemical, dilution ratio, dwell time, extraction method, and any warnings (e.g., "test in inconspicuous area first — possible dye instability"). Each job's outcome data (before/after photos, chemical used, result) trains the model.

## Target Customer
Floor care company owners with 3+ junior technicians who average 1-2 damage claims per quarter from chemical misapplication.

## Impact If Built
Reduces chemical damage incidents by 70-80% (saving $2,000-$10,000/year in claims) and accelerates junior technician onboarding from 6 months to 6 weeks.
