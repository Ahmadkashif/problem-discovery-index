# The Modelled Conversion Counted as Observed

**Niche:** [[niches/marketing-attribution-vendors/path-based-attribution/profile|Path-Based Attribution]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A growing share of the conversions feeding the model are themselves estimates produced by the platforms, each modelled in its own favour, and the attribution model treats them as observations.
**Tags:** #compliance #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #quick-win #bayesian-inference #causal-inference
**Contested on:** Every serious competitor in this niche is fighting to say something defensible about journeys that are now mostly unobservable — and whoever handles the missing paths honestly replaces a method that survives on familiarity.

## The Problem
The attribution model ingests conversion data from each platform. A substantial and growing share of those conversions were not observed by the platform either — they are the platform's own model's estimate of conversions it believes occurred but could not measure, produced by a model the platform does not document and which is not disinterested. The attribution vendor's model treats these as data. So a model built to adjudicate between platforms is fed each platform's own estimate of its own performance, and the layering is invisible in the output.

## Why It's Still Broken
Modelled conversions arrive through the same interface as observed ones and are frequently not flagged, so the distinction is invisible unless someone goes looking — the data pipeline erases a distinction that matters enormously. Excluding them would reduce the conversion counts clients expect to see. Platforms have no reason to make the share prominent. And the attribution vendor's model has no field for the difference.

## What a Fix Looks Like
Separate estimated from observed. Flag modelled conversions at ingestion wherever the platform discloses them, which is the fix and is a field-level change that makes an invisible layering visible. Report the modelled share per platform as a standing disclosure, since it varies enormously and is the single most important fact about the input data. Weight or exclude modelled conversions in the model deliberately, with the choice stated, rather than accepting them as observations by default. Test sensitivity by re-running with and without them, which is cheap and frequently changes the channel ranking — a result every client should see. Treat a platform's modelled estimate as a claim rather than as evidence, since it is produced by an interested party about its own performance. Reconcile total conversions against the client's own records, which bounds how much modelling can be absorbed before the numbers become incoherent. Track the modelled share over time, because it is rising and a model whose input composition is changing will drift without anyone noticing. Ask platforms for methodology and report which ones disclose, since transparency varies and the difference is worth knowing. Document the layering plainly for clients, most of whom have never been told that a model is being fed another model's output. And validate against experiments, because the layering is precisely the kind of problem that only external ground truth can catch.

## Who Feels the Pain
Clients whose adjudicating model is fed each platform's self-assessment; vendors whose inputs are silently degrading; and the category, whose independence is compromised by its own data pipeline.

## Impact If Fixed
Modelled conversions arrive through the same interface as observed ones, so the pipeline erases a distinction that matters enormously. Flagging them at ingestion and reporting the modelled share per platform makes the layering visible, and a with-and-without sensitivity run frequently changes the channel ranking.
