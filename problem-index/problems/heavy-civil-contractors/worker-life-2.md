# The Leverman's Twelve-Hour Watch

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]
**Type:** Worker Life Changing
**One-liner:** The leverman at the controls of a cutter suction dredge watches gauges for twelve hours a shift, keeping slurry density high without plugging a mile of pipeline, and carries the whole project's production on their attention. A system that sees the plug coming gives them back a margin for error.
**Tags:** #time-series-forecasting #lstms-and-grus #change-point-detection #gradient-boosting #worker-facing #tacit-knowledge-ml #revenue-impact

## The Problem
On a cutter suction dredge the leverman (the operator) swings the cutterhead across the face on its spuds or anchors, sets ladder depth and swing speed, and runs the pumps. Their eyes are on vacuum and discharge pressure gauges, the density and velocity meters, the cutter and swing motor loads and the GPS display of the cut against the channel template. The aim is to keep as much material in the slurry as the line will carry. Push density too high, or let velocity fall below what the material needs to stay suspended, and solids settle in the pipeline. That might be a mile or more of floating and shore pipe to the placement area. A plugged line stops the dredge and can take hours to clear (~2–8 hours, estimate), sometimes by breaking the line apart. The material changes under the cutter without warning: silt, then shell, then a clay ball or a log.

Levermen typically work 12-hour watches on multi-week hitches (estimate), living aboard. Production is the project's revenue. On a Corps contract the dredge is paid per cubic yard, its sensors report to the Corps' Dredging Quality Management office every day (search summary), and the project manager and superintendent see the shift's numbers the next morning.

## Why It Matters to the Worker
The pressure is constant and personal. A good leverman reads the gauges and the sound and vibration of the dredge and senses a plug forming before the numbers show it. That skill takes years. Simulator courses exist, and the IHC and TID courses expect about a year at the controls before a student starts (search summary). A newer leverman plays it safe and moves less material, or pushes and plugs the line. Either shows up on the shift report with their name on it. Twelve hours of vigilance on a moving platform is exhausting, and the cost of a lapse is a stopped dredge and a crew turned out to clear the line at night.

## What a Solution Looks Like
A display at the leverman's station that learns from the dredge's own sensor history: vacuum, discharge pressure, density, velocity, pump speed and motor loads, swing and ladder position, and line length. It forecasts the next few minutes of line velocity and density against the critical velocity for the current material, flags a plug risk early enough to back off, and suggests swing speed and ladder depth that hold production up. It never takes the controls. It shows why it is warning, logs which warnings the leverman acted on, and learns from the plugs that happened and the ones that didn't.

## Impact If Solved
If plug events fall by half (estimate) and a newer leverman's production comes closer to a senior's, the dredge gains several productive hours a week (estimate). The leverman ends the watch with fewer night call-outs to clear a line and a shift report that reflects skill rather than luck.
