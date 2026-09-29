# Creative Production and Testing on the Treadmill

**Industry:** [[app-marketing-firms|App Marketing Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Networks consume dozens of video and playable variants a week and report which one spent, which under aggregated attribution is not the same as which one worked.
**Tags:** #cnns #transformers #contrastive-learning #transfer-learning #gradient-boosting #causal-inference #evaluation-metrics #feature-engineering

## The Problem
Mobile user acquisition creative fatigues quickly. A video that performs this week is exhausted in ten days, and the networks' algorithms need a continuous supply of variants to allocate between. A mid-sized app ships dozens of new concepts and variants weekly across video, playable and static formats, in multiple aspect ratios and languages.

The selection loop is broken in two places. First, the network chooses how much to spend on each variant and then reports the outcome of its own choice, so the best-performing creative is partly a statement about what the network's optimiser liked. Second, under SKAN the outcome data is aggregated and delayed, and creative-level breakdowns are frequently below the privacy threshold, so the granular read the team needs is exactly the one the system suppresses.

The production side is a pure volume problem. Concepts are briefed, storyboarded, animated, localised, versioned per aspect ratio, and quality-checked against each network's specification. Most of that work is mechanical variation on a small number of ideas, and the ideas are chosen from what won recently — which, given the above, may be a statement about an optimiser.

## What Already Exists
Creative automation tools — Smartly, Vidmob, Consumer Acquisition, AppLovin's own creative tooling — handle variant generation, resizing and localisation at volume. Generative video and image tools have cut production cost substantially. Playable ad builders like Luna and Mintegral's tools reduce engineering involvement. Creative analytics products tag assets and report performance by attribute. Networks run their own creative optimisation internally and share conclusions selectively.

## The Customisation Gap
The generic tools solve production; the decision problem is unaddressed. What a team needs is an estimate of creative effect that is not confounded by the network's own allocation, and that requires either deliberate balanced rotation — expensive, and the networks discourage it — or an explicit experimental structure with creative as the treatment.

The transferable learning is the second gap, and it is specific to this industry in a useful way. Mobile creative has a well-defined vocabulary: the hook in the first three seconds, whether gameplay is shown or simulated, the presence of a false-tap mechanic, UI prominence, reward framing, pacing, end-card design. Those attributes are codeable and their effects plausibly transfer across apps in a genre, which means a firm working across many apps can learn something a single app never can — and creative decisions in this discipline are made at the concept stage, where transferable knowledge is worth most.

Per-app customisation then constrains it: the genre, the art direction, the monetisation model and the platform policy limits — Apple and Google both restrict misleading gameplay depiction, and the line is enforced unevenly and consequentially.

And measurement granularity has to be designed around the privacy threshold rather than defeated by it. Structuring campaigns so creative comparisons remain above threshold, or accepting coarser comparisons with honest intervals, is a design decision teams make implicitly and badly.

## Impact If Solved
Creative is the largest remaining controllable variable in mobile UA now that bidding has been absorbed by network automation, and the current feedback loop rewards whatever the network's optimiser favoured. An attribute-level model learned across a portfolio of apps, evaluated against experimentally clean comparisons, changes what gets briefed rather than what gets picked — which is the only intervention point that compounds.
