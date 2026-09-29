# IT Inheriting Orphaned Applications

**Industry:** [[no-code-app-builders|No-Code App Builders]]
**Type:** Worker Life Changing
**One-liner:** IT administrators stop being handed undocumented applications that a department depends on, built by someone who left, with no way to understand what they do before deciding whether they can be changed.
**Tags:** #large-language-models #bert #graph-neural-networks #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #worker-facing

## The Problem
An application built by an employee who has left is now broken, or needs to change, or has failed a security review. It reaches IT.

The administrator receiving it faces a specific and unpleasant task. Read a no-code application built by a non-engineer with no comments, no naming conventions, no separation of concerns and no documentation, and work out what it does and why. Determine which of its connections are live and what credentials they use. Establish who depends on it and what happens if it stops. Decide whether to fix it, rebuild it or retire it — knowing that retiring it will break a process nobody can describe.

The department involved is not helpful in the way they intend to be. They can describe what the app does for them and not how it does it, and they are usually under pressure because something has stopped working.

This is not occasional. Any organisation with several years of no-code adoption has a steady flow of these, and each one is an unplanned project landing on a team that had no visibility until the moment it became a problem.

## Why It Matters to the Worker
IT teams absorb the consequences of a category whose premise was that they would not be involved. They were not consulted at creation, they had no way to know the app existed, and they inherit it at its worst moment — broken, critical and unowned.

The work is also archaeology, which is the least satisfying form of engineering. Reconstructing intent from someone else's undocumented logic is slow and error-prone, and the reward for doing it well is that a process nobody thanked you for continues to work.

There is a relationship cost as well. IT is experienced as the function that arrives to impose controls after the fact, and every inherited orphan reinforces that, when in fact the sequence was determined by a tool that was sold on the promise of avoiding them.

And it is unplannable. These arrive without warning, at whatever priority the affected department can command, into a backlog that was already committed.

## What a Solution Looks Like
Automatic documentation of any application, generated from its structure and logic, so the archaeology is done before the handover rather than after. This is entirely mechanical — the app is a machine-readable specification — and its absence is the single largest cause of the pain.

Dependency mapping: what this app reads, what it writes, which systems it touches, and which other apps or processes consume its output. Turning it off safely requires knowing this and nobody currently does.

Usage and criticality evidence, so the decision to retire, rebuild or maintain is made against who actually uses it rather than against whoever objects most loudly.

Early handover rather than crisis handover. If criticality is detected as it rises, the conversation with the department happens while the builder is still present, which is dramatically cheaper for everyone and changes IT's role from undertaker to partner.

And rebuild assistance, since the honest answer for many inherited apps is to rebuild properly — and the existing app is a complete specification of the requirements, which is normally the hardest part of a rebuild.

## Impact If Solved
Orphaned no-code applications arrive at IT as unplanned archaeology projects at their worst moment, and the documentation that would prevent that is derivable from the app itself. Generating it continuously turns an inherited crisis into a routine transfer, and moves IT's involvement from after the failure to before it.
