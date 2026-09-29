# Lineage: Digital Forensics Firms

**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Wave:** [[series/eras/wave-04-client-server-erp|4 — Client–Server & ERP]]
**The tool:** EnCase and its E01 evidence file — a bit-for-bit disk image sealed with per-block CRCs and a whole-drive MD5 hash
**Builder:** Guidance Software
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A hard drive is not evidence until you can prove nobody changed it.

By the late 1990s investigators were routinely seizing computers, and the difficulty was not reading them. It was the courtroom that came afterwards. Opening a drive in its own operating system alters it — timestamps update, files are written. An examiner who worked directly on the original could be asked, under oath, how they knew the file they found had been there before they touched it. Copying the drive helped only if the copy could be shown to be exact, and stayed exact through months of handling and analysis.

So the expensive part of the work was defensibility: showing a chain from the seized disk to the exhibit that a hostile expert could not break.

## What Got Built

A single container file that carries the whole disk and the proof of its own integrity.

EnCase acquires a drive into the **Expert Witness file format (E01)**: a header of case information — examiner, case number, notes — followed by an exact bit-by-bit copy of the media, with a **CRC checksum every 64 sectors** by default and an **MD5 hash of the entire drive** appended as a footer. The examiner works on the image, never the original. At any point the hash can be recomputed and compared; if it matches, the copy is the disk.

The analysis environment was bolted to the container. Searching, file recovery and bookmarking all happened inside the same program that had verified the image, so the report and the proof came out of one tool.

## Who Built It, And Why Them

**Guidance Software**, founded by Shawn McCreight in Pasadena, California, in **1997**; the product shipped in **1998** as *Expert Witness for Windows*.

The why-them is clearer from the product than from the founder. The name said who the buyer was: someone who would have to testify. The format put the testimony into the file — case metadata in front, verification throughout — so an examiner could answer the chain-of-custody question by pointing at a hash rather than a memory. A general-purpose disk-copying tool made a copy; this made an exhibit.

The name did not last. It collided with the *Expert Witness* trademark held by **ASR Data**, Andy Rosen's company, which had built forensic software of that name, and the Windows product became EnCase. The format kept the old name — and its first version is **reportedly based on ASR Data's Expert Witness Compression Format**. The originator of the container may therefore be ASR Data rather than Guidance; see Sources. EnCase is keyed to Guidance because EnCase is what the courts saw: its output was used in cases including the BTK investigation and the murder of Danielle van Dam. Guidance was bought by OpenText in 2017.

## What It Cost

**The whole method assumed the evidence was a disk you could seize.**

E01's guarantees are about a fixed object: this drive, imaged at this time, unchanged since. That shaped the profession around acquisition — get the image, prove the hash, then analyse. It works when the attacker's traces sit on a laptop in an evidence bag.

It says nothing about evidence that was never written down. Logs that rolled over, endpoints nobody monitored, cloud audit trails left switched off: there is no drive to image and no hash to compute. A format built to prove *what is there* has no vocabulary for *what is missing*, and the reports the field produces still inherit that — a confident narrative about the evidence recovered, and silence about the evidence that did not exist.

## What You Still Touch

Examiners still acquire to E01, still record a hash, still build the case outward from the image. The harder modern question — what did the attacker access, when the logs were never kept — sits exactly where the container cannot reach.

- [[problems/digital-forensics-firms/high-impact|🔴 Establishing What Was Accessed From Logs Nobody Kept]] — the evidence an image-first method cannot represent
- [[problems/digital-forensics-firms/low-impact-1|🟡 Evidence Acquisition and Timeline Construction]] — acquisition solved, the timeline still assembled by hand
- [[niches/digital-forensics-firms/evidence-bounded-inference/profile|Evidence-Bounded Inference]]
- [[niches/digital-forensics-firms/timeline-assembly/profile|Evidence Collection & Timeline Assembly]]

**Sources:** Wikipedia, *EnCase* (E01 structure: case-data header, bit-by-bit copy, CRC per 64 sectors by default, MD5 footer; McCreight as creator; court cases; OpenText acquisition 2017) and *Guidance Software* (founded 1997, Pasadena, McCreight); SEC filing, Guidance Software proxy-settlement exhibit (company existence, not history); forensics.wiki, *EnCase image file format* (original name Expert Witness for Windows, 1998; rename over ASR Data's trademark; v1 "reportedly" based on ASR Data's Expert Witness Compression Format); HTCIA blog tag page naming Andy Rosen as creator of Expert Witness (secondary). ⚠️ **Not established:** whether ASR Data or Guidance Software originated the E01 container — the only source found says "reportedly," and the Library of Congress format description (loc.gov fdd000406) returned HTTP 403 this session, so the originator-over-inheritor question is open. If a primary source confirms ASR Data built the format, the builder key for the *format* should move to ASR Data. **Not established:** McCreight's professional background or stated motive — no source found beyond a physics degree and "founded in 1997 out of his home"; none is asserted above. The date or outcome of any legal action over the trademark was not found.
