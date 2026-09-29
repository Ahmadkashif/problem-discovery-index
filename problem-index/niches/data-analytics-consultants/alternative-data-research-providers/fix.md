# Analyst Adjustments Are the Product and Are Stored as Numbers

**Niche:** [[niches/data-analytics-consultants/alternative-data-research-providers/profile|Alternative Data Research Providers]]
**Industry:** [[industries/data-analytics-consultants|Data Analytics Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** What separates the firm's estimate from a panel extrapolation is an analyst knowing the company opened stores, changed its fiscal calendar, or shifted channel mix — and the adjustment is saved without the reason.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #feature-engineering #descriptive-statistics #data-integration #worker-facing

## The Problem
A covered name's estimate is a modelled panel signal plus analyst judgment. The judgment carries the coverage: knowing that a company's e-commerce mix shifted and the panel over-weights online, that a fiscal calendar quirk makes the prior comparison misleading, that a promotional period distorts the observed pattern. Those adjustments are applied every cycle and recorded as adjusted values. The reasoning lives in the analyst. So coverage quality is entirely personal — when an analyst covering twenty names leaves, those names degrade in ways that surface at the next earnings release, and the successor inherits numbers they cannot interrogate. The firm's differentiator against a competitor with similar panel access is precisely this layer, and it is the layer with no institutional record.

## Why It's Still Broken
Estimate production runs on a fixed earnings calendar where every additional keystroke is a real cost paid by the analyst under deadline. Where a notes field exists it is used inconsistently and written for personal recall. And the prevailing view is that covering a name well is craft — which is true and has been taken to mean it cannot be recorded, rather than that recording it is the way to keep it.

## What a Fix Looks Like
Structured capture of the adjustment at the moment it is made, costing seconds rather than minutes: the adjustment, a reason from a controlled vocabulary grown from what analysts already write, the evidence consulted, and free text that is parsed rather than merely stored. Once adjustments carry reasons, three things become possible in a business where every estimate resolves within weeks. The firm can measure which adjustment types improved accuracy and which made it worse, which turns craft into evidence faster than in any other domain in this vault. Recurring adjustment patterns — the same reason applied across structurally similar companies by different analysts — become candidates for the model, so judgment consistently applied stops being manual forever. And a client asking why an estimate moved receives the actual reasoning, which is a materially better answer than a revised number.

## Who Feels the Pain
Analysts whose coverage knowledge leaves with them; research leadership unable to measure or transfer the thing clients are paying for; the coverage expansion plan, which is bottlenecked on analyst ramp time; and clients positioning on estimates whose analytical basis is undocumented.

## Impact If Fixed
Converts the firm's real differentiator from personal expertise into institutional capital, and shortens analyst ramp on new names — which is the direct constraint on coverage growth. Because every adjustment resolves against a reported figure within weeks, this is the rare case where the value of the captured reasoning can be demonstrated within a single quarter rather than argued for.
