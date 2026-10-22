# Velocity Models That Learn the Senior Processor's Edits

**Niche:** [[niches/geophysical-survey-firms/seismic-processing-imaging/profile|Seismic Processing & Imaging]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The step that most decides image quality — editing the velocity model until gathers flatten and the image ties the wells — is done by a senior processor's eye, iteration after iteration, and none of those edits is kept as training data.
**Tags:** #tacit-knowledge-ml #cnns #gaussian-processes #bayesian-inference #transfer-learning #evaluation-metrics #worker-facing
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver a depth image whose velocity model ties the wells and that the client's interpreters trust, before the lease sale or drilling decision, and whoever gets there with the fewest re-runs takes the reprocessing work.

## The Problem
Velocity model building is iterative: migrate, inspect gathers and the image, edit velocities where events are not flat or where the image disagrees with well markers, re-migrate. Automated tomography and full-waveform inversion do much of it, but the decisions on where to trust the update, where a salt or channel boundary sits, and when the model is good enough are made by experienced processors. Each project consumes weeks of their time, and juniors learn by watching.

## Why Nobody Has Built This
The edits are recorded only as successive model versions, not as decisions with reasons. Data belongs to clients or libraries, which limits pooling across projects. And processing houses treat their senior processors' judgement as the product, not as a training set.

## What to Build
Capture each manual velocity edit with its context — the gather, image and well tie the processor was looking at — and train models that propose the next edit and flag regions where the current model contradicts the well markers already available or geological plausibility, with uncertainty. Keep the edit history with the delivered model, so the next reprocessing of the survey starts from the senior processor's reasoning rather than from the final velocities alone. Grading delivered images against wells drilled after delivery is a different record, held on the library side; it is described under [[niches/geophysical-survey-firms/multi-client-seismic-data-libraries/profile|Multi-Client Seismic Data Libraries]].

## Target Customer
Processing managers at imaging houses and in-house processing groups at large operators and libraries.

## Impact If Built
Fewer iterations per project shortens delivery against lease-sale and drilling dates, and a junior processor working with the senior's recorded edits reaches usable models years sooner.
