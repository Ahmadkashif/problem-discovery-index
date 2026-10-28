# The Valet Runner's Saturday Night

**Industry:** [[parking-operators|Parking Operators]]
**Type:** Worker Life Changing
**One-liner:** A valet runner sprints cars between a hotel or restaurant door and a garage three blocks away all night, and is blamed for every scratch the car may already have had, because nobody recorded its condition at the handoff.
**Tags:** #cnns #semantic-segmentation #contrastive-learning #worker-facing #automation #quick-win

## The Problem
On a busy Saturday a hotel or restaurant valet stand parks ~300–600 cars (estimate). A runner takes the keys, hands over a paper or text-message claim ticket, drives the car to a garage or lot sometimes several blocks away, parks it, hangs the keys on a board or in a lockbox, and runs back. When the guest texts for the car, the runner does the same in reverse, against a clock the guest and the hotel are both watching. The pay is an hourly wage of around $15–16 (parking attendants averaged $15.72 an hour in May 2023, search summary) plus tips. The runner might cover 8–12 miles on foot in a shift (estimate).

The damage claim is the worst part of the job. A guest finds a scuff on a bumper or a curb rash on a wheel and says the valet did it. The captain asks the runner what happened. The runner does not remember the car among four hundred, and the only record is a tick-box on the claim ticket that says "no visible damage", if anyone filled it in. Some operators require runners to walk around the car and take photos with a phone. That takes ~60–90 seconds a car (estimate), which nobody has on a Saturday night, and the photos are taken from wherever the runner happens to be standing.

## Why It Matters to the Worker
A claim is personal. Runners are written up, lose shifts or are dismissed after a few claims, whether or not they caused the damage. Operators and their insurers pay many claims without contesting them because there is no evidence either way, and some pass the cost back to the stand's tip pool or its bonus. The runner who is fastest and most careful has no way to prove it.

The work is also physically hard and fragmented. Sprinting in heat, rain or snow, finding a car in a garage that is full by 8 pm, and carrying a ring of keys whose wrong hook can strand a guest for twenty minutes. The captain decides who runs which car by shouting across the stand.

## What a Solution Looks Like
Cameras at the valet stand capture each car as it pulls in and as it leaves, from fixed angles, linked to the claim ticket. A model compares the two sets of images panel by panel and flags new damage, separating rain, reflections and dirt from scratches and dents. Anything already on the car at drop-off is in the record with a timestamp, so the runner does not need to photograph it. A digital key box tells the runner which hook and which level, and the retrieval queue shows the captain who is closest. The runner's phone shows only the next car.

## Impact If Solved
If even half of contested claims can be resolved from handoff images, a stand parking 100,000 cars a year at 1–3 claims per 10,000 avoids ~5–15 disputed claims at ~$500–2,500 each (estimate). For the runners, it removes the main cause of write-ups and lost shifts and gives back the 60–90 seconds of manual photos per car.
