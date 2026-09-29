# The Fight: Stuxnet, and the Discovery of OT as Its Own Discipline

**Origin:** [[origins/process-manufacturing/profile|Process Manufacturing]]
**Outcome:** Roughly 1,000 centrifuges destroyed at Natanz; the permanent separation of operational-technology security from IT security as a discipline.

## Why This Origin's Fight Is Different Again

Airlines fought a competitor. Retail banking fought the fixed cost of automation. Electric utilities fought their own alarm software. Railroads fought over a scheduling philosophy. Process manufacturing's defining fight was an **actual attack** — the clearest case in this vault of a cyberattack causing deliberate, physical, mechanical damage, and the moment the industry learned the control systems descended from [[origins/process-manufacturing/origin-story|the Data Hiway]] could be turned against the plant they ran.

## What Happened

**Stuxnet**, publicly discovered in **June 2010** and active roughly from November 2009 into early 2010, targeted **Siemens S7-300/400 programmable logic controllers (PLCs)** controlling uranium-enrichment centrifuges at Iran's **Natanz facility**. It drove the centrifuges through destructive resonance speeds while **feeding plant operators falsified nominal readings on the human-machine interface** — the control room saw normal operation while the equipment was being destroyed. The attack damaged an estimated **~1,000 IR-1 centrifuges, roughly 10% of the facility's operating stock**.

Stuxnet propagated via **USB removable media**, exploiting the informal human bridge that connects air-gapped operational networks to the outside world — the plant's control network was not directly internet-connected, and the attack still reached it, because a person carried it in.

## Why This Is the Landmark Case

Stuxnet is the first widely accepted proof that a cyberattack can cause **deliberate physical damage** to industrial equipment, not merely steal or corrupt data. It permanently reframed how the industry secures systems descended from the DCS: process-control networks have a different threat model from office IT — uptime and physical safety outrank confidentiality, controllers are frequently unpatched for years by design, and the consequence of compromise is not a data breach but a possible explosion, release or catastrophic equipment failure.

## Two Corrections Worth Making Precisely

**"Stuxnet hacked a nuclear plant" is imprecise.** It targeted **uranium-enrichment centrifuges** at a fuel-cycle facility, not a power reactor — a materially different target with a different physical failure mode, and conflating the two overstates and mischaracterises what happened.

**"Stuxnet proved air-gapping doesn't work" is also imprecise.** The network genuinely was isolated from the general internet. The attack succeeded specifically at the **human and removable-media layer** — a person carrying an infected USB drive across the boundary the network itself maintained. The correct, narrower lesson: **an air gap protects against network-borne attacks and does nothing against a person crossing it physically.**

## What Survives

**The assumption that "this system isn't networked so it's safe" only holds if you have also secured every human being who is allowed to touch it.** Every OT environment this vault touches — process plants, but also the SCADA-descended control layers in [[origins/electric-utilities/profile|electric utilities]] — inherits this exact exposure, and most were designed assuming a boundary that a USB drive, a laptop, or a contractor's device quietly erases.

**Sources:** Symantec, *W32.Stuxnet Dossier* (2010–2011); ICS-CERT technical advisories on Stuxnet and Siemens S7-300/400 PLCs; widely corroborated public reporting on the Natanz centrifuge damage estimate (~1,000 IR-1 units, ~10% of operating stock); ISA/OT-security literature on the IT/OT threat-model distinction.
