# Buy: Attack Surface Management Wired to the Policy

**Niche:** Scope Specification
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Attack surface management platforms continuously enumerate exactly what an organisation exposes, and the bounty scope page is still maintained by hand.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #change-point-detection #data-integration #automation #compliance
**Contested on:** Whether what counts as in-bounds is machine-checkable before a researcher starts, or a paragraph of prose interpreted after they finish.

## The Problem

A bounty programme's scope is a statement about which assets belong to the organisation and are eligible for testing. Maintaining an accurate, current list of what an organisation exposes to the internet is precisely what attack surface management platforms do, continuously, and they routinely find substantially more than their customers' own inventories contain.

The two are not connected. The ASM platform runs in the security team's tooling, producing a live inventory. The bounty scope page is a document someone edits when they remember. The gap between them is where most scope disputes live: a researcher finds something on an asset the organisation genuinely owns, which ASM has known about for months, and which the scope page does not mention.

The same disconnect runs the other way. Decommissioned assets stay on the scope page for months, so researchers spend time on targets that no longer matter and programmes pay for findings on systems already being removed.

## What Already Exists

Attack surface management: Randori, Censys, Detectify, Palo Alto Cortex Xpanse, Microsoft Defender EASM, Group-IB, and the ASM modules inside the larger security platforms. Continuous external discovery, asset attribution, service fingerprinting and change detection.

Cloud asset inventory: Wiz, Orca and the CSPM category, with comprehensive asset enumeration where cloud access is granted, plus the cloud providers' own inventory services.

Service catalogues: Backstage and its commercial peers, mapping services to owners inside engineering organisations.

Bounty platforms: structured asset lists in programme configuration at the larger platforms, maintained manually, sometimes with tagging by asset tier.

Standards: `security.txt` for disclosure contact, and the vulnerability disclosure policy conventions, which cover announcement rather than scope specification.

## The Customization Gap

**No integration exists in either direction.** ASM knows the assets; the bounty platform holds the scope. Connecting them is a straightforward integration nobody has built, because neither vendor's customer has asked — the security team using ASM and the programme manager running the bounty are often not the same person.

**ASM output is a risk inventory, not a scope definition.** Assets come with risk signals for a defender. A scope definition needs eligibility tiers, technique permissions and payout bands attached to each asset class, which is a different overlay on the same data.

**Attribution confidence is not expressed.** ASM platforms attribute assets to organisations with varying confidence and present the result as an inventory. A scope definition needs the confidence surfaced, because a low-confidence attribution is exactly the case where a researcher and a programme will disagree about ownership.

**Change is not propagated as policy change.** ASM detects a new asset appearing. Nothing turns that into a scope update with a version and an effective date, which is what a researcher needs to know what rules applied when they started.

**Nothing checks a submission against the inventory.** The single highest-value integration: a submitted target evaluated against the live asset inventory and the eligibility overlay before a triager sees it.

**Programmes may not want their full surface published.** A complete, current, public asset list is a reconnaissance gift. The adaptation needs a query interface that answers about a specific target without publishing the enumeration — which is a design constraint, and a solvable one.

## Target Customer

The bounty platforms are the natural buyers of an ASM integration, since submission-time scope checking is the feature that reduces their largest operational cost.

Randori and Detectify are the most plausible ASM adapters, both having offensive security heritage and a natural affinity with the bounty world.

Programme managers at organisations already running ASM are the immediate users, and the internal argument is simply that two systems describing the same assets should agree.

## Impact If Solved

Scope stops being stale, which removes the most common category of scope dispute — a genuine asset that was never on the page.

A query interface answering about a specific target, without publishing the full inventory, gives researchers the pre-work answer they need while protecting the programme's reconnaissance surface.

And submission-time checking against a live inventory is the mechanical fix for a triage burden currently absorbed by skilled people reading submissions that were never eligible.
