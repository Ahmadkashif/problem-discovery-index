# The Diagnostic Bundle Missing the One Thing

**Niche:** [[niches/developer-tools-vendors/support-engineer-reproduction/profile|Support Engineer Reproduction]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The diagnostic command collects a fixed set of files chosen years ago, and the failure being investigated depends on something outside that set, which is discovered three exchanges later.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #k-means-clustering #quick-win #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to let a support engineer see the environment a failure happened in rather than imagining it — and whoever does that takes the support organisation, because reproduction is where the entire cost of developer tool support sits.

## The Problem
The support engineer asks the customer to run the diagnostic command. It produces a bundle containing versions, the main log and the primary configuration file. The failure turns out to depend on a proxy setting in an environment variable, a second configuration file at a user-level path, and a plugin the bundle does not enumerate. Each discovery is a round trip of a day or more with a customer whose enthusiasm is declining. The bundle's contents were specified when the feature was built and have not been revisited since, despite the support team knowing exactly what is missing.

## Why It's Still Broken
The diagnostic bundle is a build-time decision owned by engineering and its inadequacy is experienced by support, which is a classic split that leaves the feedback unconnected to the change. Nobody analyses which additional artefacts get requested after a bundle arrives, though every one of those requests is in the ticket history and the aggregate is a specification for the next version. Adding to the bundle also increases the privacy surface, which is a genuine consideration and has functioned as a reason to leave it alone.

## What a Fix Looks Like
Let the ticket history specify the bundle. Analyse follow-up requests across tickets — what did support ask for after receiving a bundle — which is a straightforward text analysis over the support corpus and produces a ranked list of what is missing. Add the top of that list, with redaction, and repeat the analysis quarterly, which turns a static artefact into a maintained one. Make the bundle adaptive rather than fixed: collect more for a failure class known to depend on proxy configuration, less for one that does not, driven by the symptom the user selected. Validate the bundle at collection and tell the user what could not be gathered and why, since a bundle with a silently missing file is worse than one that says permission denied on this path. Include the dependency graph and plugin inventory, which are the two most frequently requested additions in practically every vendor's history. And measure round trips per ticket as a first-class support metric, because that is the number this fix moves and almost no vendor tracks it.

## Who Feels the Pain
Support engineers conducting a three-day conversation to assemble information that could have arrived at once; customers asked repeatedly for another file; and vendors whose resolution times are dominated by round trips nobody measures.

## Impact If Fixed
The follow-up request analysis is a query over the support corpus and produces the missing-artefact list directly. Round trips per ticket is the metric that would make the problem visible, and adding the dependency graph alone removes a large share of the exchanges.
