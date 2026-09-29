# Assessment Content Development and Item Security

**Industry:** [[talent-assessment-platforms|Talent Assessment Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Items take months to develop and psychometrically validate, and circulate publicly within weeks of deployment.
**Tags:** #bert #large-language-models #transformers #bayesian-inference #confidence-intervals #change-point-detection #evaluation-metrics #compliance

## The Problem
Assessment content is expensive. An item must be written, reviewed for bias and clarity, pilot tested on a sample large enough to estimate its psychometric properties, and calibrated within a scale. Established publishers maintain substantial content development functions for exactly this reason.

Exposure destroys it. Candidates share items on forums, in study groups and on commercial preparation sites, and a widely-circulated item stops measuring what it was calibrated to measure — it measures whether the candidate saw it beforehand. Technical assessment is particularly exposed, since coding problems circulate rapidly and comprehensively.

Detection of compromise is weak. The signal is present in the data — an item's difficulty drifting, response times falling, the correlation between an item and the rest of the test weakening — and monitoring for it is inconsistent.

Generative tooling has changed both sides. Producing draft items is now fast, which addresses the cost of content development; and candidates have access to systems that can answer many assessment items directly, which undermines unproctored assessment of anything with a determinable answer. The industry is in the middle of that adjustment.

## What Already Exists
Item response theory provides the psychometric machinery for calibration, item banking and adaptive testing, and established publishers use it properly. Item banks with rotation are standard. Proctoring services — remote proctoring, lockdown browsers, identity verification — attempt to constrain the testing environment, with their own well-documented problems around privacy, accessibility and false accusations. Some vendors have moved toward assessment formats less amenable to lookup, such as work samples and structured behavioural interviews.

## The Customisation Gap
Compromise detection should be continuous and automatic. Item parameter drift, response time distribution shifts, and unusual response patterns are all detectable from the response stream, and a compromised item should be retired automatically rather than after someone notices. This is standard psychometric monitoring applied continuously rather than periodically.

Item generation with psychometric validation is the interesting opportunity. Generating candidate items is now cheap; the expensive part is establishing that a generated item measures the intended construct with acceptable properties and no differential functioning across groups. A pipeline that generates, pilots, calibrates and screens automatically — rejecting most of what it produces — would change the economics of item banking substantially, and the screening rather than the generation is where the work is.

Differential item functioning screening deserves particular emphasis for generated content. An item that is harder for one demographic group for reasons unrelated to the construct is a fairness problem at the item level, and generated items carry whatever associations the generating model absorbed — which makes automated differential functioning analysis a requirement rather than a refinement.

And the format question is the strategic one. Assessment formats whose answers can be looked up are increasingly measuring access to tools rather than the construct, and the shift toward work samples, structured interviews and process-observable tasks is the response — which changes what the industry sells.

## Impact If Solved
Item compromise silently degrades assessments into measures of preparation access, and detection is inconsistent while remediation is slow. Continuous compromise monitoring with automatic retirement protects the instrument, and a generate-pilot-calibrate-screen pipeline with mandatory differential functioning analysis makes item banking affordable enough to rotate content at the rate exposure now requires.
