# Designing the Same Interface Again

**Niche:** [[niches/saas-implementation-partners/integration-architecture/profile|Integration Architecture]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** The architect is mapping the same two systems the firm mapped for four other clients last year.
**Tags:** #quick-win #data-integration #workflow-orchestration #evaluation-metrics #descriptive-statistics #automation #sets-and-logic #compliance
**Contested on:** Every serious competitor in this niche is fighting to connect the same dozen enterprise systems without designing the integration from scratch on every engagement — and whoever industrialises that takes the account.

## The Problem
An architect starts a mapping between two well-known enterprise systems. The firm has done this several times recently. The previous mappings exist in project documentation the architect cannot find, under client names that mean nothing, with no indication of which were troublesome afterwards. So the design is done again, the same subtleties are rediscovered in testing, and the same production incidents happen for the fifth time.

## Why It's Still Broken
Past mappings are not findable — a design document filed under a client name in a project folder cannot be found by an architect searching for a system pair, so every mapping starts empty. Nobody indexes by endpoint. Post-go-live incidents are not fed back. And rediscovering takes days rather than weeks, so it never becomes a project.

## What a Fix Looks Like
Index the past mappings by system pair and record what went wrong. Keep a register of integrations delivered, indexed by the two systems involved, which is the fix and is a list rather than a product. Attach the mapping document and the eventual incident history to each entry, since the incidents are the most valuable part. Note the volume and the pattern used, so sizing decisions have a reference. Record the subtleties discovered in testing, which are currently rediscovered every time. Make the register searchable by system pair rather than by client. Have the architect check it before designing, as a mandatory first step. Add to it at go-live and again after ninety days, when the incident history exists. Cover the sandbox and environment approach alongside the mapping. Flag the system pairs the firm has struggled with, which is commercially useful at proposal stage too. And keep it to a page per integration, since anything longer will not be written.

## Who Feels the Pain
Architects redesigning what colleagues designed last year; clients paying for rediscovered subtleties; delivery teams hitting the same production incidents; and the firm, whose integration experience never compounds.

## Impact If Fixed
A design document filed under a client name cannot be found by an architect searching for a system pair, so every mapping starts empty. A register indexed by endpoint with the incident history attached is a list, not a product.
