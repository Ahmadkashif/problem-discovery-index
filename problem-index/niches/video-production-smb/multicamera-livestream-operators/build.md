# AI-Assisted Camera Switching for Under-Crewed Livestreams

**Niche:** [[niches/video-production-smb/multicamera-livestream-operators/profile|Multicamera Livestream Operators]]
**Industry:** [[industries/video-production-smb|Video Production SMB]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product provides intelligent automatic camera switching for multicamera livestreams — selecting the best camera angle based on who is speaking, audience reaction, and presentation content — enabling a 2-person crew to produce broadcast-quality multicam output.
**Tags:** #cnn #object-detection #computer-vision #tacit-knowledge-ml #ai-agent

## The Problem
A skilled technical director (TD) watching 6 camera feeds makes 200–400 camera switching decisions per hour during a live event: cut to the speaker when they start talking, take a wide shot when the audience laughs, switch to the screen share when a slide appears, cut to Camera 2 for a different angle every 8–12 seconds to maintain visual interest. This expertise is developed over hundreds of live events — the TD learns the rhythm of a presentation, anticipates transitions, and reacts to audio cues (applause, laughter, silence). Hiring an experienced TD costs $500–$1,500 per event. Many small livestream operators can't afford a TD and operate with the owner doing everything — switching cameras, monitoring audio, managing graphics, and watching stream health simultaneously. The result is a technically functional but visually static stream that loses viewers.

## Why Nobody Has Built This
Automatic camera switching exists at the basic level: audio-follow-speaker (switch to the camera whose microphone is active) is built into some switchers. But audio-following produces robotic switching with no visual variety, no reaction shots, no audience cutaways, and no aesthetic rhythm. The TD's value is editorial judgment — knowing when to hold on a speaker's face during an emotional moment rather than cutting away, when to take a wide shot for context, when to show the audience. This is tacit knowledge that has never been modeled for live production. The training data challenge is significant: you need thousands of hours of multicamera feeds with a skilled TD's switching decisions labeled as ground truth.

## What to Build
An AI switching assistant that ingests all camera feeds and makes real-time switching recommendations (or auto-switches with TD override) based on: (1) audio activity detection (who is speaking, audience reaction sounds), (2) speaker tracking (identify the active speaker across multiple cameras and select the best-framed shot), (3) presentation detection (when slides appear on screen, cut to the screen-share camera), (4) switching rhythm rules (don't hold a single shot longer than 15 seconds, alternate between tight and wide angles, include periodic audience cutaways), and (5) event-type templates (conference keynote rhythm differs from worship service rhythm differs from panel discussion rhythm). The TD can override any decision with a manual cut, and the system learns from overrides to improve its pattern matching. The minimum viable product: a "smart auto-switch" that produces noticeably better output than basic audio-following.

## Target Customer
Livestream operators producing 5+ events per month who operate with under-crewed teams (no dedicated TD) and want broadcast-quality multicam output.

## Impact If Built
Enables a 2-person crew to produce output that currently requires a 3–4 person crew, saving $500–$1,000 per event in TD fees. Increases viewer retention by 20–30% through more dynamic camera work (the #1 viewer complaint about small livestreams is "boring, static camera"). Expands the addressable market for multicam livestreaming by making it accessible to operators who can't afford or find experienced TDs.
