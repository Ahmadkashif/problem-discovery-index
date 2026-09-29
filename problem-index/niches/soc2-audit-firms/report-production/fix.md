# Fix: The Report Is a PDF Sent by Email

**Niche:** Report Production & Distribution
**Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Type:** Fix (Pain Point)
**One-liner:** A confidential, use-restricted document goes to hundreds of the client's customers as an email attachment, and nobody knows where any copy is.
**Tags:** #compliance #evaluation-metrics #data-integration #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether the report is generated from the engagement record or assembled by hand from last year's document.

## The Problem

The report is issued. It carries a restriction on its use and distribution, states that it is intended for specified parties, and is confidential.

The client emails it to a prospect. The prospect's vendor risk team stores it in their platform. Their security team receives a copy. It goes into a due diligence data room for an acquisition. Someone forwards it to a consultant. Over a year it reaches hundreds of parties in dozens of organisations, each holding a PDF, indefinitely.

Nobody knows where any of it is. The firm that issued it has no view. The client has a rough sense of who they sent it to and none of what happened afterwards. And an out-of-date report continues circulating alongside the current one, because there is no mechanism to mark it superseded.

Meanwhile each recipient extracts the content by hand, because the artefact is a PDF and there is no structured form.

The restriction on the document is not enforceable in any practical sense. It is stated, it is understood as a formality, and the document circulates as any attachment does.

## Why It's Still Broken

**Email is the path of least resistance.** The client needs to send it to a prospect today, and attaching it is one action.

**The firm's relationship ends at issuance.** The auditor issues to the client and distribution is the client's decision, so the firm has no standing and no incentive to control it.

**Recipients want a file.** A vendor risk team storing hundreds of reports wants files in their system, not portal logins to hundreds of suppliers' document services.

**Trust centres exist and cover only some suppliers.** Some companies publish through a portal with access requests, which is better, and most still email on request.

**Supersession has no channel.** Even a client wanting to notify previous recipients of a reissue has no list of who they are.

**Nobody has been harmed visibly.** The restriction is unenforced and no consequence has followed publicly, which keeps the practice in place.

## What a Fix Looks Like

**Distribute through a portal with access grants.** The client grants access to a named recipient rather than sending a file. This is what trust centre products do and adoption is partial.

**Log who received it.** Even without preventing onward sharing, knowing who was granted access gives the client a distribution list they currently do not have.

**Mark superseded versions.** When a new report is issued, previous holders can be notified. This requires only the access log and is impossible without it.

**Offer a structured companion alongside the PDF.** Recipients want data they can ingest. Giving them a structured export reduces the pressure to circulate the document itself and is more useful to them.

**Watermark per recipient.** Standard practice for confidential documents, cheap, and it changes onward-sharing behaviour without preventing anything.

**Set an access expiry.** A report accessed a year after its period ended is frequently out of date. An expiry that prompts a request for the current one is more useful to the recipient than an indefinitely valid stale file.

**Recipients should ask for current access rather than storing files.** A vendor risk team holding a two-year-old PDF has a worse artefact than one with a portal link to the current report, and the shift is available to them.

## Who Feels the Pain

The client, whose confidential report is in an unknown number of places, including organisations they never sent it to.

The audit firm, whose work product circulates under a restriction that is not enforced and that names them.

The recipient holding a superseded report, making a supplier decision on a document that has been replaced and not knowing.

And every relying party, extracting content by hand from a PDF because no structured form exists.

## Impact If Fixed

Portal distribution with access grants gives the client a distribution list they have never had, and it is a product that already exists and is partially adopted.

Supersession notification becomes possible the moment the access log exists, and it addresses the specific failure where decisions are made on a report that has been replaced.

And offering a structured companion alongside the PDF reduces both the friction for the recipient and the pressure to circulate the document, which makes it the change that helps every party at once.
