# Automated Husbandry Monitoring System

**Niche:** [[niches/pet-services/exotic-pet-care/profile|Exotic & Non-Dog/Cat Pet Care]]
**Industry:** [[industries/pet-services|Pet Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** IoT environmental monitoring devices exist for home automation but aren't configured for exotic pet husbandry — where temperature, humidity, and lighting deviations of a few degrees or percent can be life-threatening.
**Tags:** #anomaly-detection #time-series-forecasting #signal-processing #automation

## The Problem
Reptile enclosures require precise temperature gradients (basking spot at 95-105F, cool side at 75-85F), specific humidity ranges (varies by species — 30% for arid species, 80% for tropical), and UVB lighting cycles (12 hours on/off, with bulb replacement every 6 months as output degrades). When a pet owner travels, these parameters are unmonitored — a heat lamp burns out at 2am, the enclosure drops to 65F, and the reptile enters dangerous hypothermia before the sitter's morning check. The same applies to aquariums (temperature, pH, ammonia) and bird environments (temperature, air quality).

## What Already Exists
Govee, SensorPush, and other IoT sensors monitor temperature and humidity with mobile alerts. Smart home systems (Hue, SmartThings) control lighting schedules. Aquarium controllers (Apex, Hydros) monitor water chemistry. But none of these are packaged for pet husbandry: the alert thresholds aren't species-specific, the lighting controls don't include UVB degradation tracking, and the monitoring dashboards don't tell a pet sitter what the readings mean or what to do when they're out of range.

## The Customization Gap
The monitoring system needs species-specific preset profiles (Ball Python: basking 88-92F, cool side 78-80F, humidity 50-60%) that auto-configure alert thresholds. Alerts should include context: "Temperature in enclosure dropped below 78F — this is dangerous for your Ball Python. Check that the heat mat is plugged in and the thermostat is set to 90F." A sitter-facing dashboard shows all enclosures/tanks with green/yellow/red status and plain-language instructions for each alert. UVB bulb tracking alerts when the bulb is approaching output degradation (based on manufacturer hours and install date).

## Target Customer
Exotic pet owners with 1-5+ enclosures or aquariums who travel 3-8 times per year and currently rely on sitters who may not understand what a temperature deviation means for a specific species.

## Impact If Solved
Prevents the #1 cause of exotic pet death during owner travel (environmental system failure), reduces sitter anxiety when caring for unfamiliar species, and provides remote monitoring that lets owners oversee husbandry conditions from anywhere.
