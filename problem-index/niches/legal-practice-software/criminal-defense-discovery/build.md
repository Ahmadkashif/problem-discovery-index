# A Reviewable Timeline from Every Camera in the Case

**Niche:** [[niches/legal-practice-software/criminal-defense-discovery/profile|Criminal Defense & Digital Discovery]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Six officers' body cameras record the same twenty minutes from six angles and arrive as six unsynchronised files, and the defense lawyer's tool for reconstructing what happened is a video player and a legal pad.
**Tags:** #transformers #seq2seq #object-detection #large-language-models #evaluation-metrics #confidence-intervals #automation #worker-facing
**Contested on:** Every serious competitor in criminal defense case management is fighting to make a terabyte of body-worn camera and digital discovery reviewable by one lawyer before the next hearing — and whoever gets time-to-reviewable lowest takes the account.

## The Problem
The discovery drop contains 340 hours of media. The decisive question in the case is what was said and done in a ninety-second window, and the answer is distributed across six cameras with clock offsets, a dash camera, a CAD log with its own timestamps, and a station video. To find that window a lawyer scrubs through footage. With a hearing in three weeks and a caseload in the hundreds, the honest outcome is that most of the media is never watched, by anybody, on either side — and the defense is the side for whom that is a constitutional problem rather than an inconvenience.

## Why Nobody Has Built This
The buyer is poor and fragmented. Public defender offices buy through county procurement on budgets set by people with no incentive to fund defense capability, and private criminal defense is a low-fee, high-volume practice. The vendors with the technical capability sell to the prosecution side, where the money is, and the same company frequently supplies the agency that produces the footage — which makes a defense-side product a conflict rather than an adjacency. There is also a genuine engineering problem: synchronising sources whose clocks disagree, whose formats are proprietary, and whose metadata is inconsistent is real work with no standards to lean on.

## What to Build
An ingest-and-index layer that takes a discovery drop in whatever form it arrives and returns a synchronised, searchable timeline. Every audio source is transcribed with speaker separation; every source is placed on a common clock using metadata where reliable and audio cross-correlation where not, because the same shouted sentence appearing in four recordings is the anchor that aligns them; entities, names, times and locations are extracted and linked across sources; and the lawyer gets a single scrubbable timeline where selecting a moment shows every camera that saw it and every word spoken. Search is the product — a lawyer types a name or a phrase and lands on the seconds that matter. Provenance is preserved absolutely: every derived artefact points to the original file, byte range and timestamp, because a transcript that cannot be traced to the source is useless in court.

## Target Customer
Public defender offices and county indigent defense programmes, private criminal defense firms handling serious cases, and the criminal-practice case management vendors who currently treat media as attachments.

## Impact If Built
Reducing time-to-reviewable from weeks of scrubbing to an afternoon of searching changes what a defense lawyer can actually do with a caseload — not marginally, but in kind. The specific consequence is that exculpatory material in hour 200 of the footage gets found, which is currently a matter of luck. This is the clearest case in the vault of mature, cheap technology withheld from the party that needs it most by the structure of who pays.
