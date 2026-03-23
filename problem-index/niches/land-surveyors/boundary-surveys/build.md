# Monument Evidence Interpretation Assistant

**Niche:** [[niches/land-surveyors/boundary-surveys/profile|Boundary Surveys]]
**Industry:** [[industries/land-surveyors|Land Surveyors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps a surveyor weigh conflicting boundary evidence — when the iron pin is 3 feet from where the deed says it should be, the surveyor relies on 20 years of experience to decide which evidence controls, and no technology captures or augments that judgment.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #computer-vision

## The Problem
A boundary surveyor finds a 1950s iron pipe 2.8 feet northeast of the position described in the deed. A fence has followed this pipe's position for 40+ years. The deed's bearing and distance would place the corner elsewhere. A neighboring survey from 1985 used the pipe as the corner. The surveyor must decide: is the pipe the original monument (placed inaccurately but accepted by practice), or is it a misplaced marker (requiring the surveyor to establish the "true" corner per the deed)? This decision — which evidence controls — is the core intellectual work of boundary surveying, and it relies entirely on tacit knowledge built through thousands of field encounters.

## Why Nobody Has Built This
The decision process combines spatial reasoning (how do physical features relate to recorded geometry?), historical analysis (what was standard practice when this monument was set?), legal interpretation (which state's rules of construction apply, and how has case law evolved?), and pattern recognition (does this look like an original monument or a replacement?). No dataset exists of surveyor boundary decisions with labeled reasoning — the profession has never systematically recorded why a surveyor chose one interpretation over another. Building training data requires extracting tacit knowledge from experienced surveyors who often can't articulate their reasoning.

## What to Build
A decision-support system that takes field evidence (monument type, condition, position relative to deed calls, occupation evidence, neighboring survey data) and produces: a ranked list of possible boundary interpretations, the legal and evidentiary basis for each, precedent cases from the jurisdiction, and a confidence assessment. The system is trained on historical boundary decisions from completed surveys — input: field evidence + deed data, output: the licensed surveyor's final boundary opinion. It augments the surveyor's judgment rather than replacing it — presenting the options and evidence, not making the decision.

## Target Customer
Licensed land surveyors performing boundary surveys, particularly mid-career surveyors (5-15 years experience) who have measurement skills but are still developing boundary interpretation expertise. Firm owners who need to scale their senior surveyors' judgment across more projects.

## Impact If Built
Accelerates the development of boundary interpretation skills from 15-20 years to 5-7 years. Reduces boundary opinion errors that lead to litigation (estimated 3-5% of boundary surveys result in disputes). Enables firms to assign boundary surveys to mid-level staff with AI-assisted decision support, increasing senior surveyor capacity by 30-40%.
