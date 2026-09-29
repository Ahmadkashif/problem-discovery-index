# Sponsor Bank Compliance Reporting

**Industry:** [[neobanks|Neobanks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every neobank builds the same compliance reporting pack from scratch in the format its particular sponsor bank happens to want, and rebuilds it when the bank changes.
**Tags:** #large-language-models #bert #evaluation-metrics #feature-engineering #data-integration #workflow-orchestration #compliance #automation

## The Problem
A neobank without its own charter operates under a sponsor bank's, and the sponsor bank is the party the regulator examines. What flows between them is a continuous reporting obligation: transaction monitoring statistics, alert and SAR volumes, customer identification programme exceptions, complaint logs, third-party vendor attestations, marketing review, capital and settlement positions, and whatever the bank's own examiners asked for last cycle.

None of it is standardised. One sponsor wants a monthly workbook with named tabs. Another wants files dropped to SFTP on a schedule. A third has a portal. The definitions differ — what counts as an alert, how a complaint is categorised, whether a restricted account is reported at restriction or at closure — so the same underlying facts are recomputed several ways.

After the 2023–24 consent orders, the volume and granularity of these requests increased sharply across the whole BaaS market, and many programmes ended up reporting to two sponsors simultaneously during a migration, in two incompatible formats, from one set of data.

The work is done by a small compliance team with SQL access and a deadline, often by hand, monthly.

## What Already Exists
Transaction monitoring platforms — Unit21, Hummingbird, Actimize — produce alert and case statistics. Complaint management runs in Zendesk or a case tool. Data warehouses hold everything. Reporting layers exist. Several BaaS middleware vendors ship a sponsor-reporting module covering the subset of fields their own platform generates.

## The Customisation Gap
The gap is definitional, not technical. Producing a number is easy; producing the number this sponsor means by that label is the work, and it requires a person who has read both the bank's request and the programme's data model. That mapping is held in a compliance analyst's head and in a folder of last month's workbooks.

Nothing reconciles the same concept across sponsors. A programme reporting to two banks during migration has no mechanism to confirm that its two alert counts are consistent, and inconsistency between them is exactly what an examiner notices.

Nothing tracks the provenance of a submitted figure. When the bank asks in March why January's number moved, reconstructing the query that produced it is archaeology.

And nothing reads the request. Sponsor requirements arrive as prose in an oversight agreement or an email, are interpreted once, and drift as the underlying data model changes underneath a mapping nobody revisits. Extracting structured reporting obligations from that prose, and flagging where a schema change has broken a mapping, is a well-shaped language task on a corpus every programme already holds.

## Impact If Solved
Compliance reporting consumes a large share of a small team's month and produces no insight, and its failure mode is a finding against the sponsor that ends the relationship and therefore the programme. Making the obligation-to-query mapping explicit, versioned and testable turns the most existentially risky piece of routine work in the business into something that runs itself and can be shown to an examiner.
