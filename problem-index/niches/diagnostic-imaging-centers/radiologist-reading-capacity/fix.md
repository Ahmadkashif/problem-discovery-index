# Studies That Sit Unread Because the Licensed Reader Is Off

**Niche:** [[niches/diagnostic-imaging-centers/radiologist-reading-capacity/profile|Radiologist Reading Capacity]]
**Industry:** [[industries/diagnostic-imaging-centers|Diagnostic Imaging Centers]]
**Type:** Fix (Pain Point)
**One-liner:** A study from a centre in one state waits hours because the only radiologist on shift holding that state's licence and the centre's credentialing is on break.
**Tags:** #optimization-fundamentals #workflow-orchestration #automation #quick-win #compliance
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor here is fighting to get every study a centre acquires read and reported. But outsourced reading contracts are won by whoever covers the highest share of a centre's after-hours and overflow studies with major-discrepancy rates under the contract threshold, and reading software is won by whoever raises studies finalised per radiologist hour without more addenda. Different buyers, vendors and costs of failure, so the niche is decomposed into contested sub-niches below.

## The Problem
Remote reading pools serve centres across many states. A radiologist may read only studies from states where they hold a licence, and only for sites where they are credentialed. Worklists rarely enforce or show this until a study ages past its turnaround.

## Why It's Still Broken
Licence and credentialing records sit in HR and medical-staff systems, not in the PACS worklist, and are updated by hand.

## What a Fix Looks Like
Load licence, credentialing and expiry data into worklist routing. Show each study's eligible readers, and alert a coordinator when a site's eligible coverage drops to zero for an upcoming shift.

## Who Feels the Pain
Centre managers fielding referrer calls; radiologists blamed for backlogs they cannot legally read; patients waiting for results.

## Impact If Fixed
Ending "no eligible reader" delays removes a recurring cause of turnaround breaches at almost no cost. If such delays cause one breach in five at a multi-state pool (estimate), routing on licence data removes that fifth.
