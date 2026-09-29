# Simulation for Perception

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this sub-niche is fighting to close the gap between rendered imagery and the real sensor stream so that a model trained on synthetic frames holds up in deployment — and whoever closes it takes the account, because the simulator is only worth what the transfer is worth.

## Profile
**Market Size:** ~$240M US
**Share of Parent Industry:** ~16% of category revenue
**Digital Adoption:** High for rendering, low for transfer measurement
**Target Buyer:** Perception and autonomy engineering leads
**Automation Potential:** Very high — the value is that generation scales past collection

## What Makes This a Distinct Niche
Synthetic sensor data is generated to train perception models for autonomy, robotics, inspection and surveillance, where real data is expensive to collect, dangerous to collect for the cases that matter, and impossible to label at the precision the task needs. The contest is not visual realism — it is transfer. A rendered scene can look convincing and still train a model that fails on the real camera because the sensor noise, the lens characteristics, the exposure behaviour and the distribution of what actually appears in front of the vehicle are all different. The gap between rendered and real is the entire product, and nobody measures it in a way that predicts deployment performance.

## Current Tools & Gaps
Game engine and physics-based renderers, domain randomisation, procedural scene generation, sensor models of varying fidelity, and automatic ground truth that real data cannot match. The gaps: the sim-to-real gap is reported as image similarity rather than as transfer performance; sensor characteristics are modelled crudely relative to how much they matter; rare-event coverage — the reason to simulate at all — is not measured against the real-world distribution it is meant to extend; and the simulator's own failure modes are undocumented, so the model inherits them silently.

## Problems
- [[niches/synthetic-data-providers/simulation-for-perception/build|🔨 Build: The Gap Measured in Pixels Rather Than Transfer]]
- [[niches/synthetic-data-providers/simulation-for-perception/buy|🛒 Buy: Domain Adaptation and Sensor Modelling]]
- [[niches/synthetic-data-providers/simulation-for-perception/fix|🔧 Fix: Rare Events Generated Without a Target Distribution]]
