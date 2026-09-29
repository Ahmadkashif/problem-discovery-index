# Please Retake the Photograph

**Niche:** [[niches/identity-verification-vendors/document-and-biometric-matching/profile|Document & Biometric Matching]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The applicant is told the image was not acceptable, not why, and not what to do differently.
**Tags:** #worker-facing #quick-win #cnns #evaluation-metrics #automation #object-detection #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to tell a genuine document from a good forgery and a live person from a presentation attack, on a photograph taken by whoever happens to be holding the phone — and whoever does it best under bad capture conditions wins the populations everyone else rejects.

## The Problem
The capture fails. The message says the image could not be processed and asks the person to try again. They try again in exactly the same conditions, because nothing told them the problem was glare, or the angle, or that a finger was covering a corner, or that the light behind them was too strong. After three attempts most people stop. The system knows precisely what was wrong with each image and says none of it.

## Why It's Still Broken
The capture check was implemented as a gate that returns pass or fail, so the diagnostic information it computes is discarded at the boundary — a component designed to answer one question throws away everything else it learned. Specific guidance was seen as help content rather than as part of the decision. Abandonment after failed capture is not reported. And the applicant is not the vendor's customer.

## What a Fix Looks Like
Say what was wrong and guide the retry. Return the specific capture failure reason and show it plainly, which is the fix and uses information the system already computes. Guide during capture rather than judging afterwards, since real-time framing, glare and focus feedback prevent the failure entirely. Show what a good capture looks like, because many people have never done this and a picture is worth the whole instruction. Detect the repeated identical failure and change the instruction rather than repeating it, as saying the same thing three times is how abandonment happens. Offer an alternative path after repeated failure — a different document, a different device, a human review — instead of a loop. Report capture failure reasons and abandonment rates, which nobody currently produces and which will show exactly where people are being lost. Break the reporting down by device and document type, since the pattern will concentrate. Allow upload from a different device, because the phone in hand is sometimes simply not capable. Keep partial progress so a retry is not a restart, as losing the whole application is what turns a retry into an abandonment. And test the flow with people who are not employees of the vendor, since almost none of these problems survive contact with a real user.

## Who Feels the Pain
Applicants abandoning at a capture screen with no idea what went wrong; customers losing conversions they attribute to intent; support teams fielding calls they cannot resolve; and people with older devices, disproportionately.

## Impact If Fixed
A component designed to answer one question discards everything else it learned at the boundary. Returning the specific failure reason and guiding capture in real time prevents the loop that produces most abandonment.
