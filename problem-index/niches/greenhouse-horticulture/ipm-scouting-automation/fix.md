# Sticky Trap Counting and Threshold Alert Automation

**Niche:** [[niches/greenhouse-horticulture/ipm-scouting-automation/profile|IPM Scouting Automation]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Fix (Pain Point)
**One-liner:** IPM scouts manually count insects on yellow and blue sticky traps at 50-200 trap stations per greenhouse, spending 4-8 hours per week on a repetitive counting task that is perfectly suited for computer vision but is still done by eye because no affordable, accurate tool exists.
**Tags:** #cnn #object-detection #computer-vision #worker-facing #automation

## The Problem
Yellow and blue sticky traps are the universal monitoring tool for flying greenhouse pests — whitefly, fungus gnats, thrips, and shore flies. The IPM scout replaces or inspects 50-200 traps weekly, manually counting the number of each pest species per trap and recording the count on a scouting sheet. This counting task is tedious, error-prone (inter-observer agreement on counts drops below 70% above 50 insects per trap), and time-consuming (2-5 minutes per trap x 100 traps = 3-8 hours per scouting session). The resulting counts are compared to treatment thresholds (e.g., "more than 10 thrips per trap per week in Zone 3 triggers a beneficial release"). Miscounts — whether from fatigue, rushing, or difficulty distinguishing species on a crowded trap — lead to missed threshold crossings and delayed treatment.

## Why It's Still Broken
Automated sticky trap readers have been attempted (Trapview for outdoor crops, FAUNAPHOTONICS for livestock) but greenhouse-specific solutions are scarce and expensive ($200-$500 per smart trap). At 100+ trap stations per greenhouse, the per-trap cost makes a smart-trap-at-every-station approach prohibitive. The alternative — a portable camera-and-app solution where the scout photographs each trap and CV counts the insects — is technically feasible but has not been commercialized because the training data (photographs of sticky traps with per-species labeled counts) does not exist in sufficient quantity for the greenhouse pest complex.

## What a Fix Looks Like
A smartphone app that the scout uses during normal trap rounds: photograph the sticky trap against a standardized background (a clip-on backing card with alignment markers and color calibration), and the app returns per-species counts within 5 seconds. A CNN trained on 20,000+ annotated sticky trap images classifies and counts thrips (tiny, elongated, tan), whitefly (small, white, winged), fungus gnats (medium, dark, leggy), and shore flies (medium, dark, robust) — the four species groups that constitute 90%+ of sticky trap captures. Counts feed directly into the scouting record system with automatic threshold alerts. Training data is collected through a bootstrap program: the app captures images and the scout enters manual counts for the first 3 months, building the labeled dataset through use.

## Who Feels the Pain
IPM scouts who spend 30-50% of their scouting time on the mechanical task of counting insects rather than the diagnostic task of understanding pest dynamics. IPM managers who review counts of questionable accuracy and make treatment decisions on unreliable data. Greenhouse owners paying $15-$20/hour for 4-8 hours/week of a skilled scout's time on a task a phone camera should handle.

## Impact If Fixed
Trap counting time reduced from 2-5 minutes per trap to 15-30 seconds per trap, saving 3-6 hours per scouting session. Count accuracy improves from 70% inter-observer agreement to 90%+ CV consistency. Threshold alerts trigger reliably rather than being missed due to counting errors, preventing 2-4 delayed treatments per season worth $3K-$10K each in escalated pest damage. Scout time recaptured for higher-value plant-level scouting that cannot be automated.
