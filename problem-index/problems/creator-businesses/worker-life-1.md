# The Editor in an Infinite Queue

**Industry:** [[creator-businesses|Creator Businesses]]
**Type:** Worker Life Changing
**One-liner:** Video editors work to a publishing schedule that never pauses, on feedback delivered as timestamps in a message thread, for a business whose success they cannot see themselves in.
**Tags:** #cnns #object-detection #large-language-models #bert #transfer-learning #evaluation-metrics #worker-facing #automation

## The Problem
The editor receives hours of raw footage and returns a finished video on a schedule. Every week, or more often. The schedule is set by the algorithm's preference for consistency and does not move.

The work has a long mechanical component. Syncing, culling, cutting filler and silences, assembling a rough structure, colour and audio cleanup, adding b-roll, building graphics, captioning. Then the part that requires judgement: pacing, comedic timing, when to cut away, how to structure the opening.

Feedback arrives as a list of timestamps. Tighten here. This joke does not land. Different music. The editor implements, returns, and receives another list. Two or three rounds is normal and each is a full pass.

Style is tacit. Every creator has one and none of them can articulate it. The editor learns it over months of corrections, and that learning is entirely specific to that creator.

The hours are shaped by the schedule, which means they are bad before every publish, which is always.

And the editor is usually a contractor, often remote, paid per video, without visibility into how the video performed or what the channel earns.

## Why It Matters to the Worker
The queue does not empty. There is no version of this job where the work is finished, because the next video is already being filmed.

Feedback is corrective rather than instructive. A list of timestamps says what to change and not what principle was violated, so the editor learns the creator's preferences by accumulation rather than by understanding.

Credit is structurally limited. The creator is the brand and the editor is invisible, which is fair in one sense and makes it very hard to build a portfolio or a reputation that transfers.

The economics are disconnected from the outcome. Per-video pay means an editor whose work materially improved a video's performance earns exactly the same as one who did the minimum, and neither knows which they were.

And the dependency is total. One client, one relationship, no notice period, no contract in many cases.

## What a Solution Looks Like
Automate the mechanical pass completely. Syncing, culling unusable takes, removing filler and silence, assembling a rough cut from the transcript, initial colour and audio, captioning — this is a substantial share of the hours and it is all now technically routine.

Learn the creator's style from the corrections. Every past project contains the raw footage and the final cut, which is a paired dataset of what was kept, what was cut, how long shots ran and where cuts fell. A rough cut that already matches the creator's established rhythm removes most of the first feedback round.

Interpret timestamped feedback into edit operations rather than requiring a human to translate each one.

Assemble b-roll and asset suggestions from the transcript against the creator's own library, which is a retrieval problem currently solved by scrolling through folders.

Show the editor the outcome. Performance data on the videos they cut, and retention graphs against their editing decisions, is both the professional feedback they never receive and the basis for arguing their own value.

## Impact If Solved
Editing is the largest labour cost in a creator business and the role with the worst working conditions, driven by a schedule that cannot pause and a feedback loop that teaches nothing. Automating the mechanical pass and learning style from past projects removes most of the hours and most of the revision rounds, and returns the editor to the judgement that is actually their craft.
