# Lineage: Identity Verification Vendors

**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** no single tool — the remote check reads borrowed artefacts, chief among them the ICAO Doc 9303 machine-readable zone and the AAMVA PDF417 licence barcode, and adds one of its own, the selfie matched against the document portrait; see the dated table
**Builder:** no single builder
**Builder in vault:** n/a
**Verification:** partial — see Sources

## The Problem That Came First

A bank opening an account online had to establish who was on the other side, without anyone seeing them.

In a branch a clerk compared the face with the licence photo. Online there was only what the applicant typed. After the USA PATRIOT Act, that gap became a legal obligation. Section 326 required financial institutions to verify customers' identities, and the implementing Customer Identification Program rule, published 9 May 2003 with compliance due by 1 October 2003, required banks to verify identity by documentary methods, non-documentary methods, or both, and to keep records. It said what had to be established, not how to do it remotely.

## What Got Built

No founding artefact — the industry assembled itself from parts made for other readers:

| Year | Tool | Builder | Place | What it was for |
|---|---|---|---|---|
| **1980** | Doc 9303, *A Passport with Machine Readable Capability* — two OCR-B lines of 44 characters with check digits, the MRZ | ICAO | Montreal | Faster, more reliable border inspection |
| **1991** | PDF417 stacked barcode | Symbol Technologies | United States | Carrying a data file in a printed symbol |
| **2000** | AAMVA DL/ID-2000 standard — licence data encoded in PDF417 on the card's back | AAMVA | United States | A common machine-readable licence format across jurisdictions |
| **26 Oct 2001** | USA PATRIOT Act §326 | US Congress | Washington | Customer identification at financial institutions |
| **9 May 2003** | Customer Identification Program final rule | Treasury and the federal banking regulators | Washington | Documentary and non-documentary verification, record-keeping |
| **2010** | Jumio, whose Netverify compared a camera-captured ID with a selfie | Jumio | Sunnyvale | Online ID checks from a webcam or phone |
| **19 Dec 2019** | NISTIR 8280, *FRVT Part 3: Demographic Effects* | NIST | Gaithersburg | Measuring face-recognition error rates by sex, age and race |

**Read the purpose column.** The MRZ was designed for a border officer's reader; the licence barcode was standardised by motor-vehicle administrators for their own jurisdictions. Neither was made for an applicant's phone camera, and neither says whether the holder is the owner.

## Who Built It, And Why Them

No single party, because of who owns the documents. Governments issue them; ICAO and AAMVA specify them, for their own inspectors. A vendor cannot change what is printed on a licence; it can only read it. So the vendors built what they controlled — capture on the applicant's device, classification of many document templates, and the step no issuer supplies: comparing a live face with the document portrait.

That comparison is the industry's own artefact; Jumio sold webcam and smartphone ID capture with a selfie compared to the ID photo. The builders were start-ups rather than banks because only a vendor spreading the work across many clients could maintain the document-template library.

## What It Cost

The industry inherited documents it cannot redesign. Every licence format and worn card is a template to learn, and coverage is uneven by geography and document age.

It also inherited an evaluation built for the algorithm, not the flow. NIST's 2019 report measured demographic error differentials for hundreds of face-recognition algorithms — not any vendor's end-to-end pipeline of capture, document reading, database checks and review, on the people who fail it.

**What none of it built: a count of the rejected.** Law mandated verification, standards made documents readable, vendors built matching. Nobody recorded who was turned away, or whether they were who they said.

## What You Still Touch

Every "hold your licence flat, then take a selfie" prompt reads a 2000 barcode or 1980 MRZ, then asks for what no issuer supplied.

- [[problems/identity-verification-vendors/high-impact|🔴 The False Rejects Nobody Counts]] — the table's missing row
- [[problems/identity-verification-vendors/low-impact-1|🟡 Document and Geography Coverage]] — the cost of reading documents built for other readers
- [[problems/identity-verification-vendors/worker-life-1|🟢 The Document Reviewer Judging a Photograph]]
- [[niches/identity-verification-vendors/error-distribution-accounting/profile|Error Distribution Accounting]]
- [[niches/identity-verification-vendors/document-and-biometric-matching/profile|Document & Biometric Matching]]
- [[niches/identity-verification-vendors/failed-applicant-remediation/profile|Failed-Applicant Remediation]]

**Sources:** ICAO, *Doc 9303 Machine Readable Travel Documents*, Part 1 (1968 panel; 1980 first edition titled "A Passport with Machine Readable Capability"; OCR-B chosen as the reading technology) and Wikipedia, *Machine-readable passport* (two lines of 44 characters; check digits); Wikipedia, *PDF417* (invented by Ynjiun P. Wang at Symbol Technologies, 1991); AAMVA, *DL/ID Card Design Standard* (2020 edition) and parser documentation from PDF417/Dynamsoft (DL/ID-2000 as barcode Version 01); OCC Bulletin 2003-22 and FinCEN interagency guidance (CIP final rule published 9 May 2003, compliance by 1 October 2003, 31 CFR 103.121, documentary and non-documentary methods, five-year retention); Wikipedia, *Jumio* (founded 2010 in Sunnyvale by Daniel Mattes; Chapter 11 in March 2016); TechCrunch, 10 May 2012, and search summaries (webcam/phone capture of cards and IDs; selfie-to-ID match); NIST, *Face Recognition Vendor Test Part 3: Demographic Effects*, NISTIR 8280, 19 December 2019, Grother, Ngan and Hanaoka. ⚠️ **Not established:** the first commercial selfie-to-ID-portrait product. Jumio is named as an early, well-documented example, not the originator; its Netverify launch year is given only as "around 2012" in search summaries and is left undated here. Whether any US bank ran remote document-and-selfie checks before the vendors did was not researched. The AAMVA standard's use of PDF417 before 2000 in individual states was not traced.
