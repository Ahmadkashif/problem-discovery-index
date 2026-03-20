# SME Knowledge Extraction for Course Authoring

**Industry:** [[corporate-training|Corporate Training]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic AI writing tools can generate text, but they cannot conduct a structured knowledge extraction interview with a subject matter expert and produce a pedagogically sound course outline with assessments.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #entropy-cross-entropy-kl-divergence #automation

## The Problem
Instructional designers spend 40–80 hours per course extracting knowledge from subject matter experts (SMEs) who are busy, impatient, and untrained in articulating what they know. The process involves scheduling multiple interview sessions, transcribing unstructured conversations, identifying the core concepts and decision frameworks buried in rambling explanations, sequencing them into a learning path, and writing assessment questions that test genuine understanding rather than recall. SMEs frequently skip steps they consider obvious, use jargon inconsistently, and contradict earlier statements — all of which the instructional designer must catch and resolve.

## What Already Exists
General-purpose AI writing assistants (ChatGPT, Jasper, Writer) can generate text from prompts, and tools like Otter.ai transcribe meetings. Authoring platforms like Articulate 360 provide templates for e-learning modules. However, none of these tools understand instructional design principles — they cannot identify prerequisite relationships between concepts, generate Bloom's taxonomy-aligned learning objectives from raw SME dialogue, or flag knowledge gaps in an interview transcript where the expert skipped a critical step.

## The Customisation Gap
The missing layer is an instructional-design-aware knowledge extraction pipeline: an LLM fine-tuned on or prompted with ID frameworks (ADDIE, SAM, Merrill's First Principles) that can process SME interview transcripts, identify the implicit decision trees and procedural knowledge, flag gaps requiring follow-up questions, and output a structured course blueprint with objectives, content sections, practice activities, and assessment items. It needs to handle domain-specific terminology mapping and detect when the SME's mental model has inconsistencies that would confuse learners.

## Impact If Solved
Reduces course development time from 40–80 hours to 10–15 hours per course, allowing a 3-person instructional design team to maintain a catalog that currently requires 6–8 designers. More importantly, it captures SME knowledge that is frequently lost when key employees leave the organization.
