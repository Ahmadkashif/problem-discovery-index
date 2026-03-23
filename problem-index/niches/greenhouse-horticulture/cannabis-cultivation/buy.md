# Environmental Monitoring with VPD-Based Climate Control

**Niche:** [[niches/greenhouse-horticulture/cannabis-cultivation/profile|Cannabis Cultivation Facilities]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Traditional greenhouse climate computers (Priva, Ridder) control to temperature and humidity setpoints, but cannabis cultivation requires VPD (vapor pressure deficit) control — a derived metric that no legacy climate controller optimizes natively.
**Tags:** #reinforcement-learning #time-series-forecasting #signal-processing #automation #revenue-impact

## The Problem
Cannabis plants respond to VPD (the difference between the air's moisture capacity and its actual moisture content, measured in kPa) more predictably than to temperature or humidity alone. Experienced cannabis growers manage to VPD targets that change through the growth cycle: 0.8-1.0 kPa during vegetative growth, 1.0-1.2 kPa during early flower, 1.2-1.5 kPa during late flower. Maintaining target VPD requires coordinating temperature, humidity, and air circulation simultaneously — a multi-variable control problem. Most cannabis facilities run basic environmental controllers (InkBird, TrolMaster, Growlink) that control temperature and humidity independently, creating VPD oscillations that stress plants and reduce yield by 5-15%.

## What Already Exists
Priva, Ridder, and Argus climate computers provide sophisticated multi-variable control for commercial greenhouses but cost $50K-$200K per zone and are designed for large greenhouse structures, not the 10-20 separate grow rooms typical of indoor cannabis facilities. Cannabis-specific controllers (TrolMaster, Growlink, Aroya's Cropsteering platform) provide environmental monitoring and basic control but do not optimize to VPD targets across the HVAC-dehumidification-ventilation system as a coordinated unit.

## The Customization Gap
A cannabis-adapted climate control system needs: (1) VPD as the primary control variable rather than temperature or humidity independently, (2) growth-stage-aware VPD targets that shift automatically as the crop transitions from veg to flower to late flower, (3) coordinated control of HVAC, dehumidification, and supplemental CO2 to maintain VPD within +/- 0.05 kPa of target, (4) room-by-room management (cannabis facilities run 10-20 rooms at different growth stages simultaneously), and (5) energy optimization that minimizes the cost of maintaining VPD targets — cannabis facilities spend $200K-$1M/year on climate control energy.

## Target Customer
Cultivation directors and facility managers at indoor cannabis operations with 5+ grow rooms and $50K+ annual energy spend on climate control. Approximately 3,000-5,000 US facilities at this scale.

## Impact If Solved
VPD stability improvement from +/- 0.3 kPa to +/- 0.1 kPa reduces plant stress events by 40-60%, improving yield by 5-10% and terpene consistency by 15-20%. Energy optimization through coordinated HVAC/dehumidification control saves 10-20% on climate energy costs ($20K-$200K/year depending on facility size). Combined annual impact of $50K-$400K per facility.
