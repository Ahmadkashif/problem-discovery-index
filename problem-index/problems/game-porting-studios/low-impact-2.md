# Cross-Platform Regression Testing

**Industry:** [[game-porting-studios|Game Porting Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every change must be verified on every platform, verification is people playing the game, and the client keeps shipping updates that require doing it all again.
**Tags:** #cnns #change-point-detection #contrastive-learning #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #confidence-intervals

## The Problem
A port is a continuous stream of changes that must not break anything, on several platforms, against an original that keeps moving. Verification is predominantly manual: QA testers play through content on each target, looking for visual differences, performance regressions, crashes, input problems and platform-specific failures.

The coverage problem is severe. A game has more content than can be tested exhaustively per build, so testing is sampled, and regressions appear in the parts nobody played that week. Visual differences are the hardest class — a shader behaving differently, a texture missing on one platform, a lighting change — because they require someone to notice that something looks wrong rather than to observe a failure.

Client churn multiplies everything. When the original team ships an update, the port merges it and retests, and the work previously verified is no longer verified.

And certification testing sits on top as a separate regime with its own requirements, run near submission, discovering problems that have been present for months.

## What Already Exists
Automated testing frameworks for games exist — engine-level test harnesses, automated playthrough bots, screenshot comparison tools — and are adopted mainly by larger studios with the resources to build and maintain them. Cloud build systems handle multi-platform compilation. Performance testing harnesses measure frame times across builds. Crash reporting and telemetry are standard. Platform holders provide certification test tools. QA outsourcing is widely used and is the dominant approach to coverage.

## The Customisation Gap
Screenshot comparison is the standard automated visual check and it is too brittle for real use: non-deterministic rendering, dynamic lighting, animation timing and post-processing make pixel comparison produce constant false positives, so teams disable it. The workable version compares at a perceptual and structural level, tolerant of the differences that do not matter and sensitive to the ones that do — a materially harder problem and the one that would unlock visual regression testing.

Cross-platform difference detection is the specific form that matters here. The question is not whether a frame changed between builds but whether it differs between platforms in a way that indicates a defect rather than an expected hardware difference, and that distinction requires knowing what differences are expected — which a studio's own portfolio history can teach.

Test prioritisation is the third gap. With sampled coverage, which content to test given the changes in this build is a prediction problem — which areas the changed code touches, which have regressed historically, which are platform-sensitive — and it is currently decided by a QA lead's judgement.

And certification requirements should be verified continuously rather than at submission. Most are testable behaviours, and running them on every build turns a late discovery into an immediate one, which is where most of the schedule damage comes from.

## Impact If Solved
Verification consumes a large share of a port's budget and its coverage gaps produce the defects that reach certification and clients. Perceptually-tolerant visual comparison makes automated visual regression usable for the first time; change-aware test prioritisation puts sampled coverage where the risk is; and continuous certification checking moves a class of late-discovered failures to the day they are introduced.
