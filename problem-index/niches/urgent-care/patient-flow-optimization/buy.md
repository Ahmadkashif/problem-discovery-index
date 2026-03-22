# Predictive Wait Time Estimation for Patient Communication

**Niche:** [[niches/urgent-care/patient-flow-optimization/profile|Patient Flow Optimization]]
**Industry:** [[industries/urgent-care|Urgent Care]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Patients see an accurate, real-time estimated wait time before and after they arrive — replacing the frustrating "we'll get to you as soon as we can" with a specific, trustworthy prediction that reduces walkouts and manages expectations.
**Tags:** #gradient-boosting #time-series-forecasting #feature-engineering #evaluation-metrics #cross-validation #revenue-impact #quick-win

## The Problem
A patient Googles "urgent care near me," finds a clinic, and drives 15 minutes to discover a packed waiting room. They sit for 20 minutes, see no movement, and leave for a competitor. Alternatively, they check-in online, receive a "you're next in line" status update, but are not seen for 45 minutes because "next in line" does not account for the patient ahead of them needing a laceration repair. Urgent care cannot predict wait times because throughput depends on patient acuity (a sprained ankle is 20 minutes, a laceration is 45 minutes), provider speed (varies 2x between providers), and concurrent bottlenecks (X-ray backlog, single triage nurse). Patients experience UC wait times as unpredictable and uncontrolled, driving LWBS rates of 5-15% at busy clinics — each a lost patient and potential negative review.

## What Already Exists
Queue management tools (QLess, Waitwhile) provide virtual queuing and estimated wait times for retail and service businesses, but their time estimates are based on simple queue position math (N people ahead x average service time) that does not account for UC-specific variables: varying patient acuity, provider specialization, procedure complexity, and multi-step workflow. UC-specific online check-in tools (Clockwise, Solv) show real-time patient counts but not predicted wait times. Google Maps shows "busy times" based on historical data but not real-time queue state.

## The Customization Gap
A UC-specific wait time prediction system needs to ingest: current patients in each workflow stage (lobby, triage, room, with provider), their estimated acuity (from chief complaint or triage score), provider-specific throughput rates (Dr. A sees 3.2 patients/hour, NP B sees 2.5), known procedure requirements (X-ray ordered, laceration repair in progress), and historical time-of-day patterns. The prediction model must account for the high variance in UC visit duration — a simple average is misleading when visit times range from 15 to 90 minutes. Output must be patient-facing: displayed on the clinic website, texted to patients who check in online, and shown in the lobby. Accuracy matters — patients tolerate a 5-minute prediction error but lose trust if the estimate is off by 20 minutes, which generic queue tools routinely produce in UC settings.

## Target Customer
UC operators with online check-in capability seeking to reduce LWBS rates and improve patient satisfaction scores by providing accurate, real-time wait time estimates.

## Impact If Solved
Reduces LWBS rates by 15-30% by giving patients a specific, trusted time estimate that anchors their expectations. Increases online check-in conversion by 20-40% when patients can see "estimated wait: 18 minutes" rather than an opaque queue position. A 3% LWBS reduction at a clinic seeing 40 patients per day recovers $150-400 per saved patient, translating to $54K-146K in annual revenue recovery per site.
