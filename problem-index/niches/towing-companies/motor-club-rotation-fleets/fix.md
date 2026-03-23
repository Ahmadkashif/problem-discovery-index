# Rotation Position Loss from Preventable SLA Failures

**Niche:** [[niches/towing-companies/motor-club-rotation-fleets/profile|Motor Club Rotation Fleets]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Companies lose their motor club rotation position — and 40-60% of call volume — because they can't see their performance score declining until it's too late to correct.
**Tags:** #gradient-boosting #time-series-forecasting #tabular-ml #revenue-impact

## The Problem
Motor clubs evaluate towing companies on a rolling performance window (typically 30-90 days). A company might be at 91% SLA compliance (threshold: 85%) and feel safe — but three bad days during a snowstorm drop them to 84%, triggering a rotation suspension that takes 30-60 days to reinstate. By the time the monthly scorecard reveals the problem, the suspension is already in effect. The company loses $30,000-$80,000 in monthly call volume because they couldn't see the trend declining in real time. The same pattern repeats seasonally: bad weather, staffing shortages, or equipment breakdowns cluster SLA failures in short windows that crater the rolling average.

## Why It's Still Broken
Motor clubs publish scorecards monthly or quarterly — lagging indicators of problems that needed real-time detection. The towing company's own dispatch records contain the data to calculate their rolling performance score daily, but no tool does this calculation. Towbook records call-received and job-completed timestamps, which is sufficient to compute SLA compliance per call and rolling average — but the analysis sits unbuilt in the raw data.

## What a Fix Looks Like
A daily performance tracker that calculates the company's rolling SLA compliance rate for each motor club program using dispatch record timestamps. Shows: current compliance %, trend over the last 30 days, projected compliance if current week's pattern continues, and a "danger zone" alert when the trend projects below threshold within 7 days. Includes root-cause analysis: "Your SLA misses this month cluster on Tuesday evenings (staffing gap) and during rain events (longer response times in east zone)."

## Who Feels the Pain
The owner who discovers in a monthly scorecard email that their AAA rotation has been suspended effective immediately — losing $40,000/month in call volume because 3 bad days last month pushed their 90-day rolling average below threshold, and nobody noticed at the time.

## Impact If Fixed
Early detection of performance decline enables corrective action (add a driver for Tuesday evenings, pre-stage trucks before forecasted rain) before the rolling average breaches threshold. Preventing one rotation suspension per year preserves $360,000-$960,000 in annual revenue.
