# Lineage: Insurance Third-Party Administrators (TPAs)

**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Wave:** [[series/eras/wave-01-mainframe-batch|1 — Mainframe & Batch]]
**The tool:** the IAIABC EDI Claims standard — the FROI and SROI transaction records a claims administrator files with each state
**Builder:** IAIABC
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A TPA is the party of record. That is the sentence the whole artefact hangs on.

When a self-insured employer hands its workers' compensation programme to an administrator, it hands over the *filing* as well as the cheque-writing. The administrator becomes the entity each state's board expects to hear from: that an injury occurred, that indemnity started, that a benefit changed, that payment was suspended and why, that the claim closed.

Every one of those events had a form, and every state had its own — its own definition of a reportable injury, its own clock, its own paper. A TPA in a dozen states was not doing one job twelve times. It was maintaining twelve clerical disciplines in parallel and reconciling none of them.

## What Got Built

Two flat-file record types and an acknowledgement.

The **FROI**, First Report of Injury, opens the claim with the jurisdiction. The **SROI**, Subsequent Report of Injury, reports everything afterwards. Neither is a form; both are fixed-layout records of numbered data elements.

The decision that makes it work is the **maintenance type code** — a two-character field on every record saying what *event* is reported rather than what document is sent. An original report, a change, a denial, an initial payment, a suspension, a reinstatement, a closure: each is a code, not a different piece of paper. One layout, many events.

The jurisdiction answers with an **acknowledgement record**: accepted, accepted with errors, or rejected, naming the data element that failed. That loop is the actual product. Before it, a TPA learned a filing was wrong when a penalty arrived.

Release 1 was in production use by the mid-1990s. Release 3 succeeded it, and Release 3.1 is current, republished every 1 January.

## Who Built It, And Why Them

The regulators built it — and that is the finding.

**The IAIABC was formed on 14–15 April 1914, when representatives of seven newly created state industrial accident boards met in Lansing, Michigan**, as the National Association of Industrial Accident Boards and Commissions. It exists because the states that had just invented workers' compensation had nobody to compare notes with except each other.

Why them and not a carrier, a TPA or a claims-system vendor: **the fifty-regime problem is agony for the filer and invisible to any single state.** Each board sees only its own inbox and has no reason to change a form that works. A TPA suffers all fifty and can compel none. A vendor can implement a standard, but a standard a vendor owns is a product feature — one a jurisdiction adopts is a filing requirement with law behind it.

The only body positioned to act was a trade association of *governments*, already eighty years old by the time the problem became electronic.

## What It Cost

The standard standardised the envelope, not the contents.

Adoption is jurisdiction by jurisdiction, and each publishes its own implementation guide, element requirement table and event table. A TPA implements the same standard forty-odd times, and the variation it was meant to remove reappears one level down as configuration.

The acknowledgement loop had its own cost: it made the edit the unit of work. A rejection returns the record, the examiner fixes a field, refiles, waits again — while the benefit clock that matters to an injured person keeps running. Error correction became a permanent staffed function, not an exception.

And the standard is sold, not published: Release 1.0 lists at $295 to non-members. A filing requirement behind a paywall is why most public knowledge of the code sets lives in state guides rather than in the standard.

## What You Still Touch

An injured worker's first payment waits on an accepted FROI. Not on the injury, not on the adjuster — on a record clearing a state's edits.

- [[problems/insurance-tpa/high-impact|🔴 Claims Adjudication Speed and Accuracy]] — clocks this standard made visible, not shorter
- [[problems/insurance-tpa/worker-life-1|🟢 Claims Examiner Decision Fatigue]] — the examiner who fixes the rejected element
- [[niches/insurance-tpa/regulatory-reporting/profile|Regulatory Reporting & Compliance]] — forty-odd implementations of one standard
- [[niches/insurance-tpa/state-workers-comp-boards/profile|State Workers' Compensation Boards]] — the builder's members, each profiling the spec differently
- [[niches/insurance-tpa/workers-comp-claims/profile|Workers' Comp Claims TPA]]
- [[niches/insurance-tpa/auto-adjudication-engine/profile|Auto-Adjudication Engine]]

**Sources:** IAIABC, *Mission & History* (formation 14–15 April 1914, Lansing, Michigan, by representatives of seven industrial accident boards, as the National Association of Industrial Accident Boards and Commissions); IAIABC, *EDI Claims* and *EDI Claims Release 1.0 Standard* pages (FROI/SROI purpose; Releases 1.0, 3.0 and 3.1; Release 3.1 documentation republished each 1 January; Release 1.0 priced at $295 for non-members) — read directly; state implementation guides and event tables from Montana, Kentucky, Virginia, New York, Tennessee, South Carolina and Colorado for the maintenance-type-code and acknowledgement mechanics, and for the jurisdiction-by-jurisdiction adoption pattern; this vault's `industries/insurance-tpa.md` and `history/insurance-tpa.md` (cited as vault material, not independent corroboration — the history note establishes ERISA and the fifty-state constraint, which this note takes as its premise rather than restating). ⚠️ **Not established:** the year IAIABC EDI Claims Release 1 was first published. The IAIABC's own page gives only a "final publication" date of 15 February 2002 for Release 1.0, which post-dates live use of it; Montana's implementation guide records a Release 1 flat-file database completed 17 April 1995, and Minnesota is described as starting EDI with one trading partner in 1993. Those are floor dates from state documents, not a publication date from the standards body, so **"in production use by the mid-1990s" is the strongest claim this note will make** and no founding year for the standard is asserted. ⚠️ **Read at second hand:** the maintenance type codes and the three acknowledgement outcomes are taken from state implementation guides, because the standard itself is paywalled and was not purchased for this note.
