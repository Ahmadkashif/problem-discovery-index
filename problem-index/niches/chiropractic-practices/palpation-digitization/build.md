# Tactile Palpation Capture and Quantification System

**Niche:** [[niches/chiropractic-practices/palpation-digitization/profile|Palpation & Tactile Assessment Digitization]]
**Industry:** [[industries/chiropractic-practices|Chiropractic Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No device captures what a chiropractor's hands detect during palpation — tissue compliance, joint end-feel, fascial restriction, and muscle tone changes — and converts these tactile findings into quantitative, comparable data.
**Tags:** #cnn #multiclass-classification #signal-processing #tacit-knowledge-ml

## The Problem
A 20-year veteran chiropractor palpates a patient's spine and detects information invisible to any existing diagnostic instrument: the quality of joint end-feel (springy versus hard), tissue texture changes in the paraspinal musculature (boggy, fibrous, hypertonic), fascial restriction patterns that connect distant body regions, and the millimeter-level positional asymmetry of a vertebral segment. This information drives the adjustment decision — which segment to adjust, in which direction, and with how much force. None of this information is captured digitally. When the DC retires, their 20 years of tactile expertise vanishes. When they teach students, they say "feel for this" — but the student's hands lack the sensitivity to detect what the expert feels.

## Why Nobody Has Built This
Capturing tactile information requires sensors that can detect the same variables the human hand detects: pressure distribution across the fingertips (sub-millimeter resolution), tissue compliance (how much the tissue deforms under pressure), and dynamic response (how the tissue "springs back"). The human hand has approximately 17,000 mechanoreceptors — matching this sensitivity in a wearable sensor is an engineering challenge at the frontier of haptic technology. Additionally, training data is sparse because the "ground truth" is the expert's assessment, which is itself subjective.

## What to Build
A thin, flexible sensor array worn on the chiropractor's fingertips during palpation that captures pressure distribution, tissue compliance, and force-displacement curves at each palpation point. The sensor data is transmitted to a processing unit that maps the readings to a spinal diagram, creating a "tactile fingerprint" of each segment's tissue characteristics. Over thousands of palpation sessions, a CNN-based model learns to classify tissue states (normal, hypertonic, fibrous, inflamed) and joint mobility (normal, hypomobile, hypermobile) from the sensor data — effectively encoding the expert's tactile knowledge in a machine learning model.

## Target Customer
Chiropractic colleges and research institutions initially, followed by experienced DCs (10+ years) who want to document their findings objectively and train associates.

## Impact If Built
Transforms chiropractic from a subjective art to an evidence-based discipline. Enables objective pre/post treatment measurements (tissue state before and after adjustment). Accelerates training — a student can see the quantified findings that an expert detects, bridging the 10-year "develop your hands" gap. Creates the data foundation for evidence-based chiropractic research.
