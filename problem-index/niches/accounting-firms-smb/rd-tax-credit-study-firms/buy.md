# Technical Interview Capture Adapted to Four-Part-Test Evidence

**Niche:** [[niches/accounting-firms-smb/rd-tax-credit-study-firms/profile|R&D Tax Credit Study Firms]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Meeting transcription is a solved commodity, but no transcription product knows that an engineer saying "we tried three different alloys before one held" is the single most valuable sentence in the interview.
**Tags:** #transformers #bert #large-language-models #transfer-learning #evaluation-metrics #automation #worker-facing #compliance

## The Problem
The raw material of every R&D credit study is a series of interviews with the client's engineers, typically 45-90 minutes each across a handful of technical staff. The specialist is doing three jobs simultaneously: keeping a technical conversation moving, listening for the specific admissions that establish the four-part test, and taking notes good enough to write from weeks later. The third job always loses. Specialists come away with partial notes, and the details that would have made a narrative concrete — how many iterations, what failed, what was uncertain at the outset — are reconstructed from memory or quietly generalized. When examination comes years later, the contemporaneous record is thin exactly where it needed to be thick.

## What Already Exists
Transcription and meeting-capture products are mature, cheap, and accurate. Otter, Fireflies, and the native transcription in Zoom and Teams produce reliable transcripts with speaker attribution. Several offer summarization, action-item extraction, and keyword search across a meeting archive. Generic AI note-takers will produce a competent summary of any technical conversation.

## The Customization Gap
None of these products has a model of what constitutes evidence under §41, so their summaries optimize for the wrong thing — they compress the conversation, discarding precisely the specifics that carry evidentiary weight. What the study workflow needs is the inverse of summarization: a system that listens against the four-part-test structure, flags in real time which elements have been established and which remain unsupported, and prompts the specialist mid-interview with the follow-up that would close the gap. Afterward it should emit not a summary but a structured evidence record — statements mapped to test elements, with timestamps and verbatim quotes preserved for the contemporaneous documentation file. That mapping layer is the entire adaptation, and it is worthless without the domain model behind it.

## Target Customer
R&D credit specialists conducting client technical interviews, and the practice leaders responsible for documentation quality across a team of interviewers of uneven experience.

## Impact If Solved
Turns the interview from a lossy input into the strongest artifact in the file. Gaps get closed while the engineer is still in the room rather than discovered during drafting, which removes the most common reason studies go back to the client. A junior specialist conducts an interview closer to the standard of a senior one, because the structural knowledge of what to ask next is in the tool rather than only in the interviewer.
