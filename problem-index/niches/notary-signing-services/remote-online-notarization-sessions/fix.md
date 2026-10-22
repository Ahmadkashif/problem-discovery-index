# Two Failed KBA Attempts and a 24-Hour Lockout

**Niche:** [[niches/notary-signing-services/remote-online-notarization-sessions/profile|Remote Online Notarization Sessions]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Fix (Pain Point)
**One-liner:** A genuine 80-year-old seller cannot recall the amount of a car loan from 2009, fails knowledge-based authentication twice and is locked out until tomorrow's closing deadline has passed.
**Tags:** #logistic-regression #evaluation-metrics #compliance #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to clear genuine signers through remote identity proofing on the first attempt while refusing impostors, with a session record that survives a later forgery claim, and whoever has the best trade-off between false rejects and false accepts takes the platforms' and title companies' session volume.

## The Problem
Vendor descriptions of the MISMO-based process describe two KBA attempts followed by a 24-hour wait. Thin-file signers, recent immigrants, the elderly and people whose records contain errors fail at higher rates, and the closing slips or moves to an in-person signing at short notice.

## Why It's Still Broken
Some state rules prescribe KBA, platforms inherit the lockout rule, and nobody tracks who fails or why.

## What a Fix Looks Like
Predict likely KBA failure before the session from file thinness and age, and route those signers to an allowed alternative — credential analysis plus biometrics where the state permits, or an in-person signing scheduled in advance — rather than letting them fail twice on the day. Track fail rates by signer group.

## Who Feels the Pain
Elderly and thin-file signers; closing coordinators re-booking at the last minute; RON notaries who sat through failed sessions unpaid.

## Impact If Fixed
Fewer failed sessions and missed deadlines, and evidence for regulators that KBA-only rules exclude real signers.
