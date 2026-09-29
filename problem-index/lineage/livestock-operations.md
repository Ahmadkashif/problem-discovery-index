# Lineage: Livestock Operations

**Industry:** [[industries/livestock-operations|Livestock Operations]]
**Wave:** [[series/eras/wave-02-departmental-item-level|2 — Departmental & Item-Level]]
**The tool:** no single tool — the electronic animal ID, a passive radio transponder carrying one animal's number, now the "840" ear tag USDA requires for interstate cattle, usually a 134.2 kHz ISO 11784/11785 transponder; see the dated table
**Builder:** no single builder
**Builder in vault:** n/a
**Verification:** partial — see Sources

## The Problem That Came First

A cow does not carry its own paperwork.

Whose animal, given what, moved where: a rancher had a hot-iron brand and a visual ear tag, both read by eye. A 1974 patent application put the complaint in one sentence: "An enduring problem in the livestock industry has been the lack of an adequate system of animal identification suitable for use in preventing rustling, aiding in disease control, and facilitating animal inventory during marketing and slaughter."

The Agriculture Department had a narrower version: making sure each animal got the right dose of hormones or medicine — and not a second by accident.

## What Got Built

Built several times, by parties who mostly did not raise cattle:

| Year | Tool | Builder | Place | What it was for |
|---|---|---|---|---|
| **1970s** | Passive UHF backscatter cow tag | Los Alamos, for the Agriculture Department | New Mexico | The right dose, given once |
| **filed April 25 1974** | Swallowed transponder capsule lodged in the reticulum — US 4,262,632 | John P. Hanton and Harley A. Leach | not established | Rustling, disease control, inventory at market and slaughter |
| **not established** | Electronic cow tag, now in the Smithsonian | Cornell University; made by Alfa-Laval | not established | not established |
| **by 1981** | Specification for a national implantable transponder: ID *and* subdermal temperature, read at three metres | Livestock Conservation Institute | United States | National ID and disease detection |
| **filed January 1981** | Passive label returning ID and temperature — US 4,399,441 | Unisearch | Australia | Meeting that specification |
| **1996** | ISO 11784/11785 — code structure and 134.2 kHz air interface | ISO | — | Compatible tags and readers |
| **November 5 2024** | Official ear tag, visually and electronically readable; "840" for US-born animals | USDA APHIS | — | Interstate movement of certain cattle and bison |

## Who Built It, And Why Them

**Read down the builder column: a weapons laboratory, two patentees, a university and a dairy-equipment maker, an Australian company, a standards body, a regulator.** No ranch.

Los Alamos had the radio. In **1973** Steven Depp, Alfred Koelle and Robert Freyman demonstrated backscatter tags there — a passive tag answers by reflecting the reader's own signal, so it needs no battery for the life of the animal. The Agriculture Department supplied the use.

The industry's own contribution was a demand, not a device: the Livestock Conservation Institute's specification for a tag that also reported temperature "for disease detection purposes." An Australian patent filed in January 1981 names it as its target.

Injectable transponders sold from 1986 were, by one account, mutually incompatible. **The 1996 ISO standard fixed the code and frequency; a regulator made the tag mandatory** — neither the party with the original problem.

## What It Cost

**The specification asked for a thermometer; the standard delivered a number.**

ISO 11784 specifies an identification code, and the 840 tag carries it. The temperature reading — the part aimed at finding a sick animal early — is not in the mandated tag.

So the tag solves the regulator's question, *where has this animal been?*, after an outbreak. It does not answer the rancher's, *which animal is getting sick?*, before one. Ranchers have challenged the rule in court.

## What You Still Touch

A wand reader at the chute beeps and returns fifteen digits beginning 840. Whether the animal in front of it has a fever is still judged by a rider on a horse.

- [[problems/livestock-operations/high-impact|🔴 Early Illness Detection from Animal Behavior Monitoring]] — the temperature the 1981 specification wanted and the mandate left out
- [[problems/livestock-operations/worker-life-2|🟢 Manual Pen Riding and Health Checking]] — detection still done by eye, 1,500–3,000 head a day
- [[problems/livestock-operations/low-impact-1|🟡 Livestock Record Keeping for USDA/State Compliance]] — the number the tag does carry, and the paperwork around it
- [[niches/livestock-operations/animal-health-regulatory-programs/profile|Animal Health Regulatory Programmes]] — the party the tag was finally built for

**Sources:** Google Patents, US 4,262,632, "Electronic livestock identification system" (Hanton and Leach; filed April 25 1974, issued April 21 1981; current assignee listed as Research Corporation Technologies, later Avid — original assignee not confirmed) for the "enduring problem" sentence and the reticulum capsule. Google Patents, US 4,399,441, "Apparatus for remote temperature reading" (Vaughan and Cole, Unisearch Ltd; filed January 19 1981, issued August 16 1983) for the US livestock industry's national EID effort and the Livestock Conservation Institute specification — three metres, ID plus subdermal temperature "for disease detection purposes" — and the 32-bit, 915 MHz design. RFID Journal, "The History of RFID Technology", for Los Alamos's passive UHF backscatter cow tag at the Agriculture Department's request and the dosing problem. Wikipedia, *Radio-frequency identification*, for the 1973 Depp–Koelle–Freyman demonstration. Wikipedia, *ISO 11784 and ISO 11785*, and a ScienceDirect abstract via search summary, for code structure vs. air interface, 134.2 kHz, the 1996 standardisation and incompatible chips 1986–1996. Federal Register (May 9 2024), AVMA and Agri-Pulse for the EID rule, effective November 5 2024, and the 840 prefix; search summaries of RFID Journal and tag-supplier guides (Valley Vet, Therio Dairy) for the 15-digit number and approved tags being 134.2 kHz ISO 11784/11785 or UHF; Beef Magazine for ranchers' court challenge. This vault's livestock problem notes for pen riding and 1,500–3,000 head a day (vault material). ⚠️ **Not established:** the Los Alamos cow tag's exact year and team — no source read names them; the Smithsonian "Electronic Cow Tag" record returned HTTP 403, so its Cornell and Alfa-Laval attribution rests on a search summary and its date and purpose are unknown; where Hanton and Leach worked; the Livestock Conservation Institute's founding and later history; and whether any of these early designs is a direct ancestor of today's 134.2 kHz ear tag — the table records parallel attempts, not a proven line of descent.
