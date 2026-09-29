# The Gap Measured in Pixels Rather Than Transfer

**Niche:** [[niches/synthetic-data-providers/simulation-for-perception/profile|Simulation for Perception]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Simulators are evaluated on how real the frames look and what customers need to know is whether a model trained on them works on the real sensor, which is a different quantity nobody reports.
**Tags:** #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #cnns #confidence-intervals #cross-validation #contrastive-learning
**Contested on:** Every serious competitor in this sub-niche is fighting to close the gap between rendered imagery and the real sensor stream so that a model trained on synthetic frames holds up in deployment — and whoever closes it takes the account, because the simulator is only worth what the transfer is worth.

## The Problem
A perception team buys a million synthetic frames to cover the night-time pedestrian cases they cannot collect safely. The frames are photorealistic and the vendor's evidence is a perceptual similarity score and a side-by-side comparison that a human cannot distinguish. The model trained on them degrades on the real camera, and the team spends three months establishing that the cause was the exposure and motion blur behaviour of the actual sensor, which the renderer approximated. Nothing in the purchase measured the property that determined the outcome.

## Why Nobody Has Built This
Measuring transfer requires real data from the customer's own sensor with real labels, which is exactly what the customer bought synthetic data to avoid — so the measurement is expensive and the vendor rarely has access. Visual similarity is cheap, demos beautifully and sells. The rendering community's benchmarks are rendering benchmarks. And a transfer measurement will show that the simulator's contribution is smaller than the marketing suggests, which nobody is eager to publish.

## What to Build
Measure and close the gap that determines deployment. Make the standing metric the performance of a model trained on synthetic and tested on a small real held-out set from the customer's own sensor, which is the number that predicts deployment and requires only a modest real set — far less than training would. Report the gap decomposed by cause: appearance, sensor characteristics, scene content distribution, and label definition differences, since each has a different remedy and the undifferentiated gap tells an engineer nothing about what to change. Model the sensor properly rather than approximately — noise characteristics, exposure and rolling shutter behaviour, lens distortion, dynamic range, compression artefacts — because this is consistently where the gap lives and it is the part renderers treat as a finishing pass. Support calibrating the simulator against the customer's specific sensor, since the same simulator serves cameras with different failure behaviour and the transfer is sensor-specific. Report which synthetic conditions transfer well and which do not, so the team knows where to trust the coverage. And track the mixture question directly — how much synthetic data added to how much real data improves what — because the real deployment question is almost never synthetic alone and almost always the mix.

## Target Customer
Perception and autonomy teams in automotive, robotics, drones, industrial inspection and security, and the simulation vendors selling into them.

## Impact If Built
The simulator is worth exactly what the transfer is worth and the category reports visual similarity. Decomposing the gap by cause tells an engineer what to fix, and sensor-specific calibration addresses where the gap almost always turns out to be.
