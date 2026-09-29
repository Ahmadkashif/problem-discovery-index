# Coding Support for Forty Hours of Video

**Niche:** [[niches/player-research-firms/session-data-analysis/profile|Session Data Analysis]]
**Industry:** [[industries/player-research-firms|Player Research Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The part of the study that determines the quality of the finding is the part the deadline compresses.
**Tags:** #large-language-models #transformers #automation #evaluation-metrics #word-embeddings #data-integration #object-detection #k-means-clustering
**Contested on:** Every serious competitor in this niche is fighting to turn forty hours of gameplay video, think-aloud audio and observer notes into findings in the three days before the readout — and whoever automates that coding takes the account.

## The Problem
After the sessions comes the analysis: watching back, transcribing, coding utterances and behaviours against a scheme, identifying patterns across participants, and assembling findings. It is the largest single cost in a study and it happens in the days before the readout. When the schedule tightens it is compressed, which means the finding is produced from a partial reading of the evidence — and nobody says so in the deck.

## Why Nobody Has Built This
Qualitative analysis software was built for interview transcripts rather than for synchronised gameplay video, audio and telemetry. Researchers are rightly protective of interpretive work. The material is multimodal and messy. And the cost is billable, so the firm's incentive to remove it is weak.

## What to Build
Automate the mechanical layers and leave the interpretation. Transcribe and align think-aloud audio to gameplay video and telemetry on a common timeline automatically, which is the core and removes the largest block of undifferentiated work. Detect candidate events from telemetry and behaviour — deaths, retries, long pauses, backtracking, menu confusion — so the researcher's attention starts where something happened. Cluster similar moments across participants, since the finding is almost always a repeated pattern and finding it is what the watching is for. Suggest codes against the study's scheme for a researcher to confirm rather than assigning them, which keeps the interpretation where it belongs. Reuse coding schemes across studies so the firm's method accumulates rather than being rebuilt. Surface disconfirming instances explicitly, because a rushed analysis systematically finds what it expects. Report coverage honestly — how much of the material actually informed the finding — which is the quality signal nobody currently has. Support collaborative coding with agreement measurement across researchers. Generate a first-pass structure for the readout from the coded material. And keep every automated suggestion traceable to the moment it came from, since a finding that cannot be shown on video will not be believed.

## Target Customer
Games user research firms and platforms, in-house research functions, playtesting platforms, and qualitative research software vendors.

## Impact If Built
The part of the study that determines the finding's quality is the part the deadline compresses, and nobody reports how much of the material was actually read. Automatic alignment and candidate event detection puts the researcher's attention where something happened.
