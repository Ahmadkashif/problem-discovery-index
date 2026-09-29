# Software Licence Management Practice

**Niche:** [[niches/digital-goods-marketplaces/licence-expression-and-enforcement/profile|Licence Expression & Enforcement]]
**Industry:** [[industries/digital-goods-marketplaces|Digital Goods Marketplaces]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise software built entitlement systems, licence servers and compliance auditing because the same problem cost it money, and creative assets are sold with a paragraph.
**Tags:** #compliance #workflow-orchestration #automation #evaluation-metrics #data-integration #descriptive-statistics #revenue-impact #graph-theory
**Contested on:** Every serious competitor in this niche is fighting to make a licence something the delivery path can read and check rather than prose in an agreement — and whoever does that lets compliance happen by default instead of by goodwill.

## The Problem
Software licensing is a mature engineering discipline. Entitlement systems record precisely what was granted, licence servers check at runtime, usage metering supports consumption models, compliance tooling reconciles deployed against purchased, and true-up processes convert discovered overuse into revenue rather than into litigation. Open source licence scanning does the same for code dependencies in build pipelines. Creative assets have identical structure — grants, scopes, limits — and none of the machinery.

## What Already Exists
Entitlement management systems; licence servers with runtime checks; usage metering and consumption billing; compliance reconciliation and true-up processes; and open source licence scanning in build pipelines.

## The Customization Gap
The adaptation is from a vendor controlling its own runtime to a marketplace whose assets are consumed in other people's tools. It requires: (1) checks in tools the platform does not own — design software, game engines, build systems — which is a partnership and plugin problem rather than a licensing one and is the central obstacle; (2) grants expressed over use context rather than over seats and instances, since the question is what the asset appears in rather than how many machines ran it, and the entire enterprise vocabulary is the wrong shape; (3) terms authored by individual creators rather than by a legal department, so the vocabulary must be selectable in a minute with sane defaults or nobody will use it; (4) assets embedded and transformed inside derived works, which makes detection a provenance problem — the sibling niche — rather than an inventory scan; and (5) a true-up mechanic scaled to a thirty-dollar asset, where the enterprise audit process costs orders of magnitude more than the licence.

## Target Customer
Digital goods marketplaces, creative software vendors whose tools are where use happens, and licence management vendors for whom creative assets are unserved.

## Impact If Solved
Enterprise licensing assumes the vendor controls the runtime, and here the asset is consumed in other people's tools. Grants over use context rather than seats is the vocabulary change, and creator-authored terms must be selectable in a minute to exist at all.
