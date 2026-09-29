# Build: Delivery That Does Not Measure the Candidate's Circumstances

**Niche:** [[niches/talent-assessment-platforms/delivery-and-accessibility/profile|Assessment Delivery, Proctoring & Accessibility]]
**Industry:** [[industries/talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Make the administration robust to connection, device and environment so the score reflects the construct, and measure where it currently does not.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #compliance #change-point-detection #worker-facing #automation
**Contested on:** Whether delivery-induced measurement error can be detected and separated from the construct.

## The Problem

Two candidates with identical ability take the same assessment. One is on a laptop with a fixed connection in a quiet room. The other is on a phone on mobile data with two children present. Their scores differ, and the difference is not ability.

This is measurement error introduced by the delivery layer, and it is systematically correlated with the circumstances that correlate with income, housing and disability. It is also invisible: the score arrives with no indication that the administration was compromised, and the employer acts on it identically.

The platform records everything needed to detect it — connection events, device type, screen size, input method, session interruptions, time anomalies, tab switches — and uses some of it for proctoring flags rather than for measurement quality.

## Why Nobody Has Built This

Delivery is treated as solved because assessments render and submit. Whether they render equivalently across devices and conditions is a different question nobody asks.

Measuring the effect requires comparing scores across delivery conditions, which produces an uncomfortable finding — that the instrument scores mobile candidates lower, for instance — that would require action.

And the telemetry that would support it is routed to proctoring, where interruptions and anomalies are read as suspicion rather than as compromised administration. The same event is interpreted as cheating rather than as a bad connection.

## What to Build

Robust delivery, measured equivalence, and an administration quality record.

**Handle interruption gracefully.** Server-side state, resumable sessions, and time credited for connection loss rather than counted against the candidate. A timed assessment that punishes a dropped connection is measuring connectivity, and this is ordinary engineering.

**Establish device equivalence empirically.** Compare score distributions across device types, screen sizes and input methods, controlling for what can be controlled. If mobile scores lower on a given item type, the item is not device-equivalent and either the interface or the item needs changing. This is the measurement question and nobody runs it.

**Design for the worst realistic conditions.** Small screens, touch input, intermittent connectivity, low bandwidth. Building for a phone on mobile data and enhancing upward produces a fairer instrument than the reverse, and it is a design decision at the start rather than a remediation.

**Record administration quality per session.** Interruptions, device, connection stability, time anomalies, and any accommodation applied — attached to the score, so a compromised administration is visible to whoever interprets it and can be offered a retake.

**Separate proctoring flags from quality flags.** An interruption is evidence of a connection problem far more often than of misconduct, and conflating them punishes people for their circumstances. Distinguishing the two, with the benign interpretation as the default, is a policy decision with a large effect.

**Build accessibility in rather than beside.** Screen reader compatibility, keyboard navigation, contrast, text scaling and time extension as first-class capabilities of the item types rather than as an alternative version maintained separately — which is how alternative versions come to be out of date and not equivalent.

**Report the disparities.** Score distributions and completion rates by device type, connection quality and accommodation status. This is the evidence that delivery is or is not neutral, and it is a query.

## Target Customer

Vendors, for whom delivery-induced error undermines the validity claim their product rests on, and employers with legal exposure on accessibility and adverse impact. High-volume hiring for roles where candidates are least likely to have a laptop and a quiet room is where the effect is largest.

## Impact If Built

The score stops partly measuring the candidate's equipment, connection and living situation. Compromised administrations become visible and retakeable. And the disparities delivery introduces — which correlate with exactly the characteristics an employer must not select on — become measured rather than invisible.
