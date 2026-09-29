# Build, Certification and Platform Pipelines

**Industry:** [[indie-game-studios|Indie Game Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Shipping to four platforms means four build pipelines, four certification regimes and four sets of requirements written for studios with a compliance department.
**Tags:** #gradient-boosting #large-language-models #change-point-detection #bert #evaluation-metrics #automation #workflow-orchestration #compliance

## The Problem
A game that launches on PC and consoles must satisfy each platform holder's technical requirements: save data behaviour, suspend and resume handling, controller disconnection, achievement implementation, storage messaging, localisation of system text, age rating declarations, accessibility statements and dozens of others per platform, each with its own document and its own submission process.

Certification failures are routine and expensive in time. A submission is rejected for a requirement the team did not know applied, the fix takes a day, resubmission takes a week, and a launch date built on a publisher's marketing commitment slips. For a two-person studio with no console experience, the first submission is an education conducted under deadline.

Around it sits the build infrastructure: platform-specific toolchains under NDA, separate build machines, asset variants, and a release process that is manual for most small teams. Performance regressions and content bugs surface late because nobody has capacity to run automated testing across every target.

## What Already Exists
Unity and Unreal both provide multi-platform build support and handle a large part of the abstraction. Platform holders publish their requirement documentation and provide submission portals and test tooling. Porting studios exist as a service and are frequently the practical answer. Continuous integration for games runs on general-purpose CI plus game-specific services. Automated testing frameworks for games exist and are adopted mainly by larger teams. Middleware handles some requirements — achievements, save systems — generically.

## The Customisation Gap
Requirement checking is the obvious unbuilt piece. Platform requirements are structured documents and most of them describe testable behaviours; checking a build against them automatically, and reporting which requirement a failure maps to, is a well-defined task nobody has assembled because the documentation is under NDA and each platform is a separate integration.

The customisation is per engine and per project structure. A requirement about suspend-and-resume behaviour is checked differently in a Unity project than an Unreal one, and differently again in a custom engine, so the useful tool is engine-aware rather than generic.

Failure prediction is the second gap and is where the experience gap is largest. Which requirements a given project is most likely to fail is predictable from its characteristics — genre, save system design, multiplayer presence, platform mix, team's prior submission history — and that prediction is exactly the expertise a porting studio sells. Surfacing it before the first submission, rather than after, is where the time is saved.

And the release process itself should be automated to a degree that a two-person team can sustain, which mostly means someone doing the tedious integration work once for the common engine and platform combinations rather than each studio doing it badly alone.

## Impact If Solved
Certification failures and manual release processes consume weeks of a small studio's schedule at exactly the point where schedule pressure is highest and money is shortest. Automated requirement checking with engine-aware mapping, and a prediction of which requirements this project is likely to fail, converts a rite of passage into a checklist — and reduces the dependence on porting studios for teams who cannot afford one.
