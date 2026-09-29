# Lineage: SMB Video Production

**Industry:** [[industries/video-production-smb|SMB Video Production]]
**Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — PC & the Spreadsheet]]
**The tool:** SMPTE timecode — the HH:MM:SS:FF address recorded against every frame of video, standardised by SMPTE as the time and control code now numbered ST 12, proposed in 1970 and approved in 1975
**Builder:** SMPTE
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A frame of videotape could not be named.

Videotape, in the words of a 1987 industry handbook, has "no sprocket holes... to keep the frame count consistent." Material was found with a footage counter that slipped as the tape stretched.

Cutting was worse: iron particles brushed on to make the tracks visible, the gap between frames found under a microscope, a razor blade, mylar tape. As the handbook puts it, "there was no way to preview an edit decision before cutting the tape."

Ampex's electronic Editec of 1963 stopped the cutting but marked edits with an audible cue beep, and it "wasn't frame accurate." **An edit was a physical event, not a record** — it could not be written down, repeated or handed to another suite.

## What Got Built

An address for every frame — hours, minutes, seconds, frames — written as an 80-bit word along a cue track and locked to the start of each frame so it could not slip.

The address turned a cut into two numbers. Timecode, the handbook says, "allowed each edit to be previewed and repeated." Two numbers make a list: the CMX 600 of 1971, from a CBS–Memorex joint venture, edited offline and produced an **edit decision list**, and by 1972 computer-controlled suites performed such lists automatically.

The PC wave inherited the address rather than replacing it. Avid/1, the first Media Composer, shipped in 1989 as an offline editor for the Macintosh II: the cut made on a desktop, conformed on tape by its timecodes.

## Who Built It, And Why Them

The code came first from a vendor. In 1967 EECO — the Electronic Engineering Company of California, "a major supplier of Time Code Generators and Timing Systems for government and scientific purposes" — adapted a method NASA used to time-tag telemetry tapes into its "On-Time" code and EECO-900 edit controller. Videotape was a new customer for something EECO already made.

Then, "other manufacturers began introducing their own time code systems, none of which were compatible." In 1969 the Society of Motion Picture and Television Engineers formed a committee; the standard was proposed in 1970, approved in 1975 and adopted by ANSI.

**That is why the key is a society and not a vendor.** An address is worth something only if every machine reads it, and any one vendor's code was a lock-in its rivals had reason to refuse. That reading is this note's inference, not a documented statement by SMPTE.

The inventor is contested: Wikipedia credits the adopted version to Leo O'Donnell at the National Film Board of Canada, and the EECO-sourced account omits him. Keying to the standard's owner avoids choosing.

## What It Cost

**Timecode is a label, not a clock.** Frame.io's blog, in 2022: "Two cameras with the same timecodes don't sync because their frames were captured at the same time—they sync because they have the same label." It wraps at 24 hours and carries no date.

It also lies about the time. Colour NTSC runs at 29.97 frames a second, so a 30-frame count falls 3.6 seconds behind the wall clock each hour. Drop-frame timecode repairs that by skipping frame numbers 00 and 01 every minute except each tenth — no pictures lost, only numbers.

And the list kept its hardware limits. In 2017 Premiere Pro was still refusing exports with "The maximum EDL event limit (999) for CMX 3600 has been exceeded."

## What You Still Touch

Frame.io made review comments frame-accurate. But the client who replies by email writes "the transition around 1:20 feels off" — a player's minutes and seconds, no frame — and the editor turns it back into timecode by hand:

- [[problems/video-production-smb/low-impact-1|🟡 Client Review & Approval Workflow for Video Production]] — mapping "around the middle" to timecodes via the edit decision list
- [[problems/video-production-smb/worker-life-1|🟢 Editor Rough Cut Review Cycles with Vague Client Feedback]] — the editor as "professional mind reader"
- [[niches/video-production-smb/legal-video-specialists/buy|Transcript-Video Synchronization for Small Legal Videographers]] — "every line of transcript must be linked to its exact video timecode"

**Sources:** Cipher Digital, *Time Code Handbook* (1987), bitsavers.org PDF, fetched and text-extracted, for the sprocket-hole and footage-counter passages, microscope-and-razor splicing, "no way to preview", Ampex "Editek" 1963 and its cue beep, the 1967 HH:MM:SS:FF method, "previewed and repeated", 1972 computer-controlled edit lists, and the 80-bit frame (via its EBU comparison); the handbook names no inventor. Videomaker, "Edit Suite: Once Upon a Time" and "Edit Points: A History of Videotape Editing", fetched, for the iron-particle solution, mylar splice, Editec 1963, EECO 1967, the NASA telemetry basis, incompatible codes and SMPTE's 1969 intervention. John Huntington, "A Bit of SMPTE Time Code History" (controlgeek.net, 2023), fetched, for EECO 1967, the 1969 committee and ANSI adoption, citing EECO's own *The Time Code Book* (1983). vtoldboys.com editing museum, EECO page, fetched, for the company description, "On-Time" code and EECO-900. Wikipedia, *SMPTE timecode*, *CMX Systems*, *Media Composer*, fetched. Frame.io Insider, "Timecode is Not Time" (July 11 2022), fetched, for the label quotation, 1970/1975, 24-hour wrap and no date. philrees.co.uk on drop-frame, fetched. Adobe Community thread (September 27 2017), fetched, for the CMX 3600 error text. This vault's video-production-smb problem and niche notes (vault material, not corroboration). ⚠️ **Not established:** the O'Donnell/National Film Board attribution rests on Wikipedia and one search summary; no primary source was read. vtoldboys dates "On Time" code's adaptation to television to 1966, against 1967 elsewhere. An exact ANSI approval date (a search summary gave April 2 1975), EECO's town, and a 1971 Emmy for EECO appeared only in search summaries and are omitted. Adobe's own EDL help page returned 403.
