# Matching Under Bad Capture

**Niche:** [[niches/identity-verification-vendors/document-and-biometric-matching/profile|Document & Biometric Matching]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The model is excellent on clean images and the applicant is in a car park at night with a five-year-old phone.
**Tags:** #cnns #object-detection #contrastive-learning #transfer-learning #evaluation-metrics #confidence-intervals #diffusion-models #semantic-segmentation
**Contested on:** Every serious competitor in this niche is fighting to tell a genuine document from a good forgery and a live person from a presentation attack, on a photograph taken by whoever happens to be holding the phone — and whoever does it best under bad capture conditions wins the populations everyone else rejects.

## The Problem
Benchmark performance is achieved on well-lit, well-framed, high-resolution captures of modern documents. Production input is a worn licence photographed at an angle under fluorescent light on an old device with a cracked screen, by someone who has never done this before. The gap between benchmark and production is where rejections come from, and it falls hardest on people with older documents and older phones — which is not a random population. Meanwhile generative tools are making synthetic documents and replayed faces steadily cheaper.

## Why Nobody Has Built This
Capture quality was treated as an input condition rather than as part of the system, so improving it was the applicant's job — and a model team measured on model accuracy has no mandate over the camera. Training data skews toward successful captures, which are the easy ones. Error rates by device and condition are not published, so the gap is undocumented. And the adversary's improvement is faster than the retraining cadence.

## What to Build
Treat capture as part of the model. Guide capture actively in real time rather than rejecting afterwards, which is the core and converts a rejection into a successful attempt. Train explicitly on degraded, unusual and older documents rather than on the images that already pass, since the failures are the population worth improving on. Model the device and condition as context, because a score from an old phone in poor light means something different from the same score in ideal conditions. Detect synthetic and generated documents and faces as a first-class task, as the adversary's capability is improving and detection has to be developed against it deliberately. Use retry sequences as training signal, since a person who failed three times and succeeded on the fourth provides a labelled pair of the same identity under different conditions. Report error rates by device class, document age and capture condition, which is where the exclusion concentrates and is measurable today. Offer graceful degradation — a lower-confidence result routed to review rather than a refusal — because a binary output on a noisy input is the wrong shape. Support alternative capture paths for people whose device cannot produce an adequate image. Red-team against current generative tools continuously, since the threat moves monthly. And measure improvement on the worst-served conditions rather than on the average, because average improvement can leave those populations exactly where they were.

## Target Customer
Computer vision and product leadership, customers whose rejections concentrate in particular populations, applicants with older documents and devices, and biometric component vendors.

## Impact If Built
Capture quality was treated as an input condition rather than as part of the system, so a model team measured on accuracy has no mandate over the camera. Active guidance and training on degraded captures address exactly where the rejections fall.
