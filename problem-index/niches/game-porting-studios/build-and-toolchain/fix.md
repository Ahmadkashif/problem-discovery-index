# The SDK Update That Broke Every Build

**Niche:** [[niches/game-porting-studios/build-and-toolchain/profile|Build & Toolchain Management]]
**Industry:** [[industries/game-porting-studios|Game Porting Studios]]
**Type:** Fix (Pain Point)
**One-liner:** Somebody updated the platform SDK on the build machine and three projects stopped compiling.
**Tags:** #quick-win #automation #workflow-orchestration #compliance #evaluation-metrics #data-integration #descriptive-statistics #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to keep several platforms' builds working across every project, every SDK update and every client engine version — and whoever makes that reliable takes the account.

## The Problem
Platform SDK versions are not pinned per project. A machine is updated — because another project needed it, or because an update was applied routinely — and projects that were building yesterday no longer build. Engineers lose a day, the cause takes hours to identify because nobody logged the change, and the fix is either rolling back or updating every project at once.

## Why It's Still Broken
Nothing pins the version — a build environment shared across projects with no version isolation guarantees that one project's requirement becomes every project's problem. Changes to build machines are not logged. Rollback is manual. And the breakage is attributed to whatever was being worked on at the time.

## What a Fix Looks Like
Pin the versions and log the changes. Pin the SDK and toolchain version per project explicitly, which is the fix and prevents the class of failure outright. Isolate build environments per project so an update for one cannot affect another. Log every change to a build machine with who and when, since the diagnosis currently takes longer than the fix. Test an SDK upgrade on a copy before adopting it, which is standard practice everywhere else. Keep the previous version available so rollback is immediate. Schedule upgrades deliberately at project boundaries rather than applying them when they appear. Record which SDK version each build was produced with, which also matters for certification. Alert when a project's pinned version diverges from what a machine provides. Maintain a compatibility note per engine and SDK combination, since the same pairings recur. And make the pinned configuration part of the project rather than a property of a machine.

## Who Feels the Pain
Engineers who lost a day to a change they did not make; build engineers diagnosing an unlogged update; producers absorbing the delay; and every concurrent project sharing the machine.

## Impact If Fixed
A build environment shared across projects with no version isolation guarantees that one project's requirement becomes every project's problem. Pinning per project and logging machine changes removes the class of failure.
