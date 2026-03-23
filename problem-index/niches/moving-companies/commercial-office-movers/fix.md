# IT Equipment Disconnect/Reconnect Coordination

**Niche:** [[niches/moving-companies/commercial-office-movers/profile|Commercial Office Movers]]
**Industry:** [[industries/moving-companies|Moving Companies]]
**Type:** Fix (Pain Point)
**One-liner:** IT disconnect/reconnect is the single most common phase-delay trigger in commercial moves because coordination between movers, client IT, and cabling contractors happens via email chains and phone calls with no shared timeline.
**Tags:** #workflow-orchestration #automation #data-integration #worker-facing

## The Problem
In every commercial office move, IT equipment (desktop computers, monitors, phones, printers, network switches) must be disconnected by the client's IT team or a contracted IT vendor before movers can pack and transport it, then reconnected at the destination before employees return to work. This creates a three-party coordination problem: the mover needs IT disconnected by a specific time to stay on schedule, the client's IT team has their own priorities and availability constraints, and cabling contractors at the destination need lead time to patch network drops. When IT disconnect runs late — which happens on 40-60% of commercial moves — the entire phase schedule cascades, crews sit idle at overtime rates, and the move bleeds margin.

## Why It's Still Broken
Each party (mover, client IT, cabling vendor) manages their own schedule independently. The mover's phase schedule lives in a spreadsheet, the IT team tracks their tasks in their own ticketing system, and the cabling contractor works from a separate work order. No shared view exists, and status updates flow through email or phone calls that are easily missed. The mover's project manager spends 20-30% of their time on move-week chasing IT status updates instead of managing the physical move.

## What a Fix Looks Like
A shared coordination timeline that all three parties access, with IT disconnect/reconnect tasks linked as dependencies to the mover's phase schedule. The IT team marks equipment as disconnected per floor/zone, which automatically unblocks the mover's pack-and-load tasks for that zone. Automated alerts fire when IT tasks are approaching their deadline without completion. Post-move, the reconnect checklist tracks which workstations are live and which are still pending, giving the client a real-time view of when each department will be operational.

## Who Feels the Pain
Move project managers who absorb overtime costs when IT delays cascade, and client facilities managers who take the blame from department heads when employees can't work on Monday morning because their equipment isn't reconnected.

## Impact If Fixed
Eliminates the 4-8 hours of idle crew time per phase that IT delays cause on the average commercial move, saving $2,000-6,000 per move. Reduces post-move "not working" tickets by 50-70% through systematic reconnect verification.
