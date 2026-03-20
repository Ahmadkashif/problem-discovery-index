# Predictive Maintenance from Field Tech Sensory Signals

**Industry:** [[oil-gas-field-services|Oil & Gas Field Services]]
**Type:** High Impact
**One-liner:** Wellsite equipment failures are predicted days before they happen by encoding the sensory pattern recognition that veteran field techs have spent decades internalizing.
**Tags:** #lstms-and-grus #cnns #rnns #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #activation-functions #tacit-knowledge-ml #revenue-impact

## The Problem
A veteran pumper walks up to a rod pump unit and within seconds knows something is wrong — the rhythm of the polished rod is slightly off, the fluid coming from the separator has shifted from black to a milky brown (rising water cut), there is a faint high-pitched whine from the gearbox, or a subtle vibration pattern in the wellhead tells them a downhole rod is about to part. These observations happen constantly across tens of thousands of wellsites, but they live entirely inside the heads of experienced field technicians. When those techs retire — and the oilfield workforce is aging rapidly — the knowledge vanishes. Meanwhile, SCADA systems only trigger alarms when a threshold is already breached, meaning the failure is often already in progress. A single ESP failure can cost $50,000-$150,000 to pull and replace, plus $10,000+/day in lost production during the workover.

## Why It's Unsolved
Three compounding challenges make this genuinely hard. First, **data collection**: you must instrument the expert performing the observation — mounting accelerometers, microphones, and cameras at wellsites while simultaneously recording what the tech notices and what they decide. Most wellsites are remote, have intermittent connectivity, and lack power for edge compute. Second, **labeling**: a veteran tech's judgment is probabilistic and contextual. Two techs may disagree on whether a sound indicates a bearing issue or a stuffing box leak, and the same tech may assess the same sound differently depending on well history, weather, or recent workover activity. Ground truth comes only after the equipment is pulled, which may be weeks later. Third, **deployment**: the model must operate at the edge on solar-powered RTUs with limited bandwidth, and it must deliver faster, more reliable assessments than the experienced human — otherwise field techs will ignore it.

## What a Solution Looks Like
Multi-modal sensor arrays (accelerometer, microphone, camera) are installed at wellsites and capture the same signals a field tech would observe. An edge-deployed model fuses vibration spectra, acoustic signatures, and visual fluid analysis to produce equipment health scores and predicted time-to-failure for each major component (rods, ESP, gearbox, separator internals, compressor valves). Alerts are prioritized by production impact and routed to the nearest available field tech with a specific diagnosis and recommended action, replacing the current system of generic SCADA threshold alarms.

## Impact If Solved
Reduces unplanned downtime by 40-60% across a typical operator's well portfolio. For a mid-size operator running 500 wells, preventing even 10% of unplanned failures per year saves $5-15M in workover costs and lost production, while simultaneously preserving the diagnostic expertise of a retiring workforce in a durable, scalable system.
