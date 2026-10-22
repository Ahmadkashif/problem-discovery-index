# Watching ITU and FCC Filings That Touch Your Networks

**Industry:** [[satellite-operators|Satellite Operators]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every two weeks the ITU publishes new satellite filings, and an operator has four months to object to any that could interfere with its networks, so a small regulatory team reads hundreds of filings by hand against a calendar kept in a spreadsheet.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #feature-engineering #compliance #workflow-orchestration #automation

## The Problem
An operator's right to use an orbital slot or a constellation's frequencies depends on its place in the ITU's coordination queue. The ITU's Radiocommunication Bureau publishes the BR IFIC (Space Services) every two weeks. Each issue carries advance publication information, coordination requests and notifications from administrations worldwide. An operator whose networks could suffer interference must comment within four months of the relevant special section, using the ITU's SpaceCom software and e-Submission, or it loses leverage in the coordination that follows. Domestic clocks run in parallel: FCC applications go on public notice with a pleading cycle, and FCC deployment milestones, now under the Part 100 rules adopted on 22 July 2026, govern when satellites must be in orbit.

The regulatory engineer at a mid-size operator reads each circular, filters the filings whose frequency bands, orbital positions and service areas overlap the operator's own, runs or commissions interference analyses (equivalent power flux-density, ΔT/T and C/I checks), drafts objections, and tracks hundreds of open coordinations, each with its own correspondence chain and deadlines. Missing a window is rarely noticed until a coordination meeting goes badly years later.

## What Already Exists
The ITU's own tools — SpaceCap for preparing filings, SpaceQry and SNS for querying, GIBC for interference checks, SpaceCom for comments — and the FCC's online licensing systems. Interference analysis software such as Transfinite Visualyse and the operator's own spreadsheets. General legal docketing and regulatory-tracking products used by law firms. Large operators keep in-house spectrum teams; smaller ones rely on consultancies and regulatory counsel.

## The Customisation Gap
The generic tools hold the data but do not answer the operator's question: which of this fortnight's filings matter to us, and by when must we act? The industry-specific logic is: matching new filings to the operator's own networks by band, orbit, service area and coordination arc; screening for the filings that the ITU's own examination flags as requiring coordination with the operator's administration; carrying each coordination's history — letters, agreed parameters, meeting minutes — so the engineer sees the whole thread; computing every deadline from the circular's publication date and the Radio Regulations' provisions; and tying FCC milestones and ITU bringing-into-use dates to the launch schedule. Docketing tools built for courts know none of this.

## Impact If Solved
A filing watch that reduces each circular to the handful of entries the operator must assess, with deadlines computed and the coordination history attached, cuts days of reading per issue to hours, removes the risk of a silently missed four-month window, and gives a two- or three-person regulatory team the coverage that only the largest operators now have.
