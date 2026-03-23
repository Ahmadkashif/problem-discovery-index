# Voice Dictation Adapted for TCM Clinical Terminology

**Niche:** [[niches/acupuncture-practices/intake-documentation/profile|Patient Intake & Treatment Documentation]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Medical dictation tools like Dragon Medical recognize Western clinical terminology but consistently fail on TCM terms — pinyin point names, pulse quality descriptors, and pattern diagnoses.
**Tags:** #transformer #speech-recognition #speech-processing #nlp #worker-facing

## The Problem
Acupuncturists who try voice dictation to speed up charting discover that no medical speech recognition tool understands their clinical vocabulary. Dictating "Liver Qi stagnation, needled Tai Chong, Qi Men, and He Gu with even technique" produces garbled output. The practitioner spends as much time correcting transcription errors as they would have spent typing. TCM terminology includes: pinyin point names (Zu San Li, San Yin Jiao), alphanumeric codes (ST-36, SP-6), pulse qualities (wiry, slippery, choppy, leather), tongue descriptors (red body, thin white coat, scalloped edges), and pattern diagnoses (Kidney Yin Deficiency with Empty Heat).

## What Already Exists
Dragon Medical One, Nuance DAX, and Deepgram offer medical-grade speech recognition with high accuracy for Western clinical terminology. General-purpose dictation (Apple Dictation, Google Voice) handles English well but not medical terms. None have been trained on TCM clinical vocabulary, and no TCM-specific vocabulary add-on exists for any major platform.

## The Customization Gap
The speech recognition model needs a TCM vocabulary layer: a custom dictionary of 1,500-2,000 terms covering point names (pinyin and alphanumeric), herb names, pulse qualities, tongue descriptors, TCM pattern diagnoses, and treatment modality terms. Beyond vocabulary, the model needs context-aware disambiguation — "He Gu" should transcribe as "LI-4 (He Gu)" in a treatment note context, not as two random syllables. This is achievable with fine-tuning on 50-100 hours of TCM clinical dictation audio.

## Target Customer
Acupuncturists who have tried and abandoned voice dictation due to TCM terminology errors, and practitioners seeking to eliminate keyboard-based charting.

## Impact If Solved
Reduces charting time by 40-60% for practitioners who adopt voice workflows, saving 1-2 hours daily. Makes dictation-based charting viable for a specialty that was previously locked out of the medical dictation revolution.
