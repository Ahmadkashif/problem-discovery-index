# Sensor Data Quality Assessment Gap

**Niche:** [[niches/data-analytics-consultants/manufacturing-analytics/profile|Manufacturing Analytics & Industry 4.0]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Analytics consultants build models on manufacturing sensor data without knowing which sensors are trustworthy — drifted sensors, stuck readings, and miscalibrated instruments produce analyses that factory managers immediately reject because "those numbers don't match what we see on the floor."
**Tags:** #anomaly-detection #time-series-forecasting #signal-processing #tacit-knowledge-ml

## The Problem
A consultant builds a predictive maintenance model using temperature sensor data from a packaging line. The model performs well on historical data. The factory implements it. Within two weeks, the model triggers false alarms because the temperature sensor drifted 3 degrees after the last calibration — the model was trained on post-calibration data but deployed on pre-calibration data. Experienced plant engineers know which sensors to trust ("that thermocouple on Line 3 reads 2 degrees low, always has") but consultants do not have this institutional knowledge. They treat all sensor data as equally reliable, producing analytics that do not match floor reality.

## Why It's Still Broken
Sensor calibration and maintenance records are kept by maintenance departments in CMMS systems (Maximo, SAP PM) that are disconnected from analytics workflows. There is no standard "data quality profile" for manufacturing sensor data. The analytics consultant receives a data extract and assumes it is accurate — the factory does not volunteer which sensors are unreliable because they may not know themselves (calibration is done on schedule, not based on drift detection). Statistical tests for sensor drift exist (CUSUM, EWMA) but are not routinely applied as a preprocessing step in manufacturing analytics workflows.

## What a Fix Looks Like
A sensor data quality assessment tool that: (1) profiles each sensor's time-series for drift (gradual shift in baseline), flatlines (stuck readings indicating sensor failure), outliers (readings outside physical possibility), and noise (sudden increase in reading variability), (2) cross-references with calibration records if available (was the sensor recently calibrated? Is a calibration overdue?), (3) produces a per-sensor trust score and a data quality summary report, (4) recommends which sensors to exclude or correct before analytics, and (5) runs as a preprocessing step before any manufacturing analytics engagement. Takes 2-4 hours to run on a full historian extract.

## Who Feels the Pain
Analytics consultants whose factory insights are rejected because they are based on unreliable sensor data, and plant managers who lose trust in analytics when the numbers do not match operational reality.

## Impact If Fixed
Prevents 50-60% of "the analytics don't match the floor" rejections by identifying unreliable data before analysis. Saves 1-2 weeks of rework per engagement when analyses must be re-run after discovering data quality issues. Builds consultant credibility by demonstrating data rigor before presenting results.
