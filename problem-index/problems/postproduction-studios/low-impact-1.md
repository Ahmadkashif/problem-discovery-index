# Pre-Flight QC Against Each Platform's Delivery Spec

**Industry:** [[postproduction-studios|Postproduction Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Automated QC tools already scan masters for technical defects, but none of them learns which checks this studio's masters fail on which platform, so redeliveries keep arriving days before air.
**Tags:** #gradient-boosting #autoencoders #feature-engineering #evaluation-metrics #compliance #automation #workflow-orchestration

## The Problem
A finished episode leaves the post house as a set of deliverables: an IMF package with Dolby Vision HDR and SDR versions, a 5.1 and Atmos mix, stems, subtitles and captions, plus broadcast masters or a DCP for festivals and theatrical. Each platform has its own specification and its own inspection. Netflix runs IMF packages through Photon checks at upload and rejects the whole delivery if any track referenced in the CPL fails. A Dolby Vision metadata file with the wrong edit rate, a mix measured at -24 LKFS instead of -27 dialog-gated, a missing frame of black at a segment boundary, a subtitle that overlaps a burned-in title: any of these sends the package back. The redelivery is due against a premiere date the post house did not set, and the work is done overnight by the same online editors and QC operators who prepared it.

## What Already Exists
Automated QC platforms (Interra BATON, Venera Pulsar and Quasar, Telestream's Vidchecker and Qualify) check video, audio and container parameters against templates, and several ship Netflix-oriented and broadcaster templates. Loudness meters from iZotope and Dolby measure the mix. Netflix publishes its specs and error codes on its Backlot help site. Larger facilities orchestrate the pipeline with SDVI Rally or in-house scripts, and human QC operators watch the programme in real time.

## The Customisation Gap
The generic tools check what a template says; they do not know this studio's history. The studio-specific logic is: a ruleset per platform, per spec version and per deliverable type, kept current as specs change; the studio's own rejection history mapped to the root cause (a particular conform path, a colorist's metadata export habit, a mixer's measurement setting); risk-ranking each package before upload, so human QC time goes to the deliverables most likely to fail; and a fix list written in the language of the department that has to act on it, not a QC report full of timecodes and parameter names. Platform rejection reports arrive as emails and portal notices and are never classified, so the same failure recurs across shows.

## Impact If Solved
A pre-flight layer tuned to the studio's own failure history could cut first-submission rejections by roughly a third to a half (estimate). On a facility delivering a few hundred episodes a year, that removes dozens of overnight redeliveries and the late-delivery penalties and lost goodwill that come with them.
