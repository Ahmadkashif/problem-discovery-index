# Identity Resolution Products Assume a Consumer, Not a Court Record from 1997

**Niche:** [[niches/childcare-centers/childcare-background-check-vendors/profile|Childcare Background Check & Screening Vendors]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Entity resolution, document extraction and case management are all mature markets, and every one of them is built for clean commercial data rather than fifty state court systems, a legally binding determination and an applicant who cannot work until it clears.
**Tags:** #bert #word-embeddings #feature-engineering #evaluation-metrics #compliance

## The Problem
A screening vendor's operation decomposes into recognisable pieces: ingest an application, resolve an identity, pull records from many sources, extract meaning from unstructured documents, apply rules, route exceptions to a human, issue a determination, retain the file. Each piece has a mature vendor market. Screening organisations have bought into several of them.

The result is a stack that handles the easy sixty per cent and hands the rest to adjudicators, who are the actual cost centre and the actual source of variance.

## What Already Exists
Entity resolution and master data management platforms match identities across sources at scale. Document AI and OCR services extract fields from scanned records. Workflow and case management systems route exceptions and hold audit trails. Rules engines encode decision logic without code. Compliance platforms manage FCRA notice, dispute and retention obligations. Court record aggregators and data brokers supply the underlying records.

All of it is real, and none of it was built for this.

## The Customization Gap
**The records are fifty incompatible systems, not a data source.** A criminal history record is produced by a state repository fed by county courts, each with its own disposition vocabulary, its own abbreviations, its own decades of drift. "Adjudication withheld," "nolle prosequi," "deferred," "PBJ" and a dozen state-specific dispositions carry different legal weight in different jurisdictions. Off-the-shelf document AI extracts the text. It has no model of what the text means, and meaning is the entire adjudication.

**Entity resolution is tuned for the wrong error.** Commercial matching optimises for a balance appropriate to marketing or fraud, where a missed match costs a little and a false match costs a little. Here the two errors are morally asymmetric and in opposite directions — a missed match risks clearing someone who should be barred, a false match denies a person their livelihood on someone else's record. Neither error is acceptable and no vendor default encodes that. The matching also runs on the worst inputs in the industry: name changes, common names, records decades old with partial identifiers.

**The rules are not rules.** A rules engine assumes the logic can be written down. Fifty statutory disqualification lists mapped onto thousands of offence codes across jurisdictions is a mapping problem, and it is genuinely ambiguous at the edges — which is why adjudicators exist. Codifying it is not configuration, it is the multi-year project the vendor is already doing by hand.

**The registries are not databases.** Child abuse and neglect registries and sex offender registries vary enormously in structure, access, currency and search interface, state by state. Several are effectively manual. No integration platform covers them, and the interstate search a federal statute requires is stitched together individually.

**FCRA sits underneath everything.** Adverse action notice, dispute handling, accuracy obligations and reinvestigation are legal requirements with real liability, and compliance platforms built for consumer lending map onto them imperfectly. The dispute process in particular — where a person contests a record — is the one place where the vendor's matching accuracy becomes a legal question, and it is generally handled outside the bought tooling entirely.

**Nothing measures the adjudicator.** The bought stack routes exceptions to humans and records what they decided. It does not tell anyone whether two adjudicators would decide the same file the same way, which is the single most useful number the operation could have.

## Target Customer
VP of Operations or Chief Compliance Officer at a national screening vendor or a state-contracted processor. The realistic case is to keep the workflow, retention and notice layer that is bought and working, and rebuild the two pieces that decide everything: disposition interpretation across jurisdictions, and identity matching calibrated for asymmetric harm.

## Impact If Solved
Clearance time keeps qualified people out of childcare jobs in a sector that cannot staff itself, and matching errors bar individuals on records that were never theirs. Both failures live in the sixty per cent of the process that was bought off the shelf and the forty per cent that had to be done by hand because nothing fit.
