# Measuring the Identity Decision Instead of Assuming It

**Niche:** [[niches/notary-signing-services/remote-online-notarization-sessions/profile|Remote Online Notarization Sessions]]
**Industry:** [[industries/notary-signing-services|Notary & Signing Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** RON platforms know how many signers pass identity proofing; none can say how many genuine signers they turned away or how many impostors they let through.
**Tags:** #tacit-knowledge-ml #cnns #gradient-boosting #survival-analysis #evaluation-metrics #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to clear genuine signers through remote identity proofing on the first attempt while refusing impostors, with a session record that survives a later forgery claim, and whoever has the best trade-off between false rejects and false accepts takes the platforms' and title companies' session volume.

## The Problem
Every session ends in pass or fail, but the truth behind a pass arrives months later, if ever, when a deed is disputed. False rejects vanish: the signer gives up or goes to an in-person notary. Experienced RON notaries also end sessions on their own read — a signer reading answers off-screen, a voice prompting from another room — and that judgement is not recorded as data.

## Why Nobody Has Built This
Outcome data sits with title insurers and courts; platforms have no incentive to publish error rates; and fairness measurement needs demographic data platforms avoid collecting.

## What to Build
An evaluation layer: link sessions to downstream outcomes through title and lender partners; estimate false-accept rates from confirmed fraud and false-reject rates from signers who later completed elsewhere; break both out by age, document type and issuing state; and capture the notary's structured in-session observations so the experienced notary's read becomes a labelled signal. Use it to tune thresholds by transaction risk.

## Target Customer
RON platform trust and compliance leads; title underwriters approving RON for their agents.

## Impact If Built
Thresholds are set on evidence rather than habit, genuine signers stop being silently turned away, and the platform can show a regulator or underwriter how well its identity decision works.
