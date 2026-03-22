# Patient Flow Optimization

**Parent Industry:** [[industries/urgent-care|Urgent Care]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1-2B embedded (touches all UC segments)
**Share of Parent Industry:** Cross-cutting operational function
**Digital Adoption:** Medium — Experity captures timestamps at each workflow step but does not visualize flow, detect bottlenecks, or predict wait times
**Target Buyer:** Operations director, site manager, or chain VP Operations
**Automation Potential:** Very High — every step from check-in to discharge has measurable timestamps, and bottleneck detection and wait time prediction are well-defined optimization problems

## What Makes This a Distinct Niche
Door-to-door time is the single most important operational metric in urgent care. It determines patient satisfaction (patients who wait over 30 minutes to see a provider rate satisfaction 40% lower), online reviews (which drive 60%+ of new patient acquisition for UCs), left-without-being-seen rates (each LWBS patient is $150-400 in lost revenue), and throughput capacity (faster door-to-door means more patients per provider per shift). The workflow has 5-7 measurable steps: arrival/check-in, registration, triage, rooming, provider evaluation, procedures/testing, discharge. Each step has a handoff point where patients wait. Bottlenecks shift throughout the day — mornings may bottleneck at registration, afternoons at provider availability, evenings at X-ray turnaround. No current tool visualizes this flow in real time or predicts where the next bottleneck will form.

## Current Tools & Gaps
Experity captures timestamps for each workflow step but displays them as individual patient records, not as a flow visualization. A site manager who wants to know "where is my bottleneck right now?" must mentally aggregate the status of 8-12 patients across their journey stages. Digital check-in kiosks (Clockwise, Phreesia) handle the front-end arrival step but do not monitor downstream flow. Patient tracking boards exist in some UCs as whiteboards or simple digital displays, but they show current status, not predicted wait times or flow velocity. No product provides real-time bottleneck detection and wait time prediction specific to UC workflow.

## Problems
- [[niches/urgent-care/patient-flow-optimization/build|🔨 Build: Real-Time Patient Flow Tracker with Bottleneck Detection]]
- [[niches/urgent-care/patient-flow-optimization/buy|🛒 Buy: Predictive Wait Time Estimation for Patient Communication]]
- [[niches/urgent-care/patient-flow-optimization/fix|🔧 Fix: Lobby-to-Room Transition Bottleneck Elimination]]
