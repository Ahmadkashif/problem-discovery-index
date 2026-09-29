# Activity Tracking Adapted to Matter Attribution

**Niche:** [[niches/legal-practice-software/passive-timekeeping-reconstruction/profile|Passive Timekeeping & Billable Reconstruction]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Automatic time tracking is a mature consumer and agency product category, and the reason none of it works for law firms is a single missing step — attributing an activity to a matter — which nothing outside legal has any reason to solve.
**Tags:** #k-nearest-neighbors #gradient-boosting #word-embeddings #bert #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in legal timekeeping is fighting to produce a reconstructed timesheet a lawyer accepts with minimal editing — and whoever gets the accepted-unedited share highest takes the account.

## The Problem
A firm buys a well-regarded automatic time tracker. It captures activity beautifully and reports that the lawyer spent 2.1 hours in a word processor, 3.4 hours in email and 47 minutes in a browser. None of that is billable to anything, because billing requires a matter, and the tracker has no concept of one. The firm's administrator tries to map applications to matters, discovers that every matter uses the same three applications, and abandons the tool. This has happened at thousands of firms with a dozen products.

## What Already Exists
RescueTime, Timely, Toggl's automatic mode and the agency time-tracking category all provide robust activity capture with good privacy controls and mature clients across platforms. The capture problem is thoroughly solved, including the hard parts — idle detection, cross-device consolidation, low-overhead monitoring. Legal-specific passive capture exists in Smokeball and a few others, tied to those platforms. The generic tools are better at capture than the legal ones and useless without attribution.

## The Customization Gap
The adaptation is the attribution layer and the matter context that feeds it. It requires: (1) matter resolution from the artefacts activity touches — document paths and metadata, email participants and threads, calendar entries, phone records — using the firm's own matter database as the target, which is the piece no horizontal tool can have; (2) client and contact resolution, since the strongest available signal is usually who was on the email and matching that to matters reliably needs the firm's contact graph; (3) a learned per-timekeeper correction model, because a lawyer who fixes an attribution twice should not be asked a third time and personalisation here dominates any general model; (4) ambiguity handled by asking rather than guessing — a single well-placed question at the end of a session beats a wrong attribution that silently corrupts a bill; and (5) privacy design that is explicit and lawyer-controlled, since passive capture of a lawyer's machine is a trust question first, and products that get this wrong are uninstalled in a week regardless of accuracy.

## Target Customer
Practice management vendors who would rather integrate capture than build it, and mid-size firms already paying for a generic tracker that nobody uses.

## Impact If Solved
Attribution is the whole gap between a commodity tracker and a legal product, and building only that layer is a fraction of the cost of building capture as well. A firm that gets accurate matter attribution has most of the reconstruction benefit even before narration, because the lawyer can write a narrative quickly for a session they can see was on the right matter — which is not true today.
