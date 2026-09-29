# Buy: Reporting Platforms the Small Firms Never Adopted

**Niche:** Report Production
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Purpose-built penetration test reporting platforms exist, work, and have penetrated the large firms while most of the market still writes in a word processor.
**Tags:** #large-language-models #bert #word-embeddings #evaluation-metrics #data-integration #workflow-orchestration #automation
**Contested on:** Whether the document is assembled from structured findings captured during the engagement, or retyped into a different client's template every time.

## The Problem

This is an unusual case: the product exists and the market did not take it.

Penetration test reporting platforms have been available for over a decade. They structure findings, maintain reusable finding libraries, generate documents from templates, manage evidence, handle review workflow and export to client systems. They solve most of the write-up burden and are used seriously by large consultancies and mature practices.

The majority of the market — the boutiques, the small specialist firms, the independents, who collectively do a large share of the testing — still writes reports in a word processor from a copy of the previous engagement. They have heard of the platforms. Many have trialled one. They went back to the document.

So the interesting question is not what to build but why adoption failed, because the answer determines whether any version of this succeeds.

## What Already Exists

Purpose-built: Dradis, PlexTrac, AttackForge, Ghostwriter, Pwndoc and the reporting modules inside delivery platforms such as Cobalt's. Finding libraries, evidence management, template-driven generation, collaboration and review, client portals and exports.

Adjacent document automation: proposal and legal assembly platforms, with mature clause libraries, conditional assembly and consistency features far beyond what the security-specific tools offer.

Evidence capture: the intercepting proxies testers already use hold complete request history; screenshot tooling is universal; some platforms integrate with scanner output.

Reporting standards: several efforts have proposed structured finding formats, none has become the convention.

## The Customization Gap

**Setup cost against a small firm's tolerance.** The platforms need configuration — templates, finding libraries, workflow — measured in days. A five-person firm has no operations function and will abandon anything not useful within an afternoon. This is the primary adoption failure and it is a packaging problem rather than a capability one.

**Workflow rigidity versus how testers actually work.** The platforms assume findings are entered as the engagement proceeds, in their interface. Testers work in a terminal and a proxy and write up afterwards. A tool that requires them to context-switch into a web form during testing will not be used, and the platforms' value proposition depends on exactly that.

**Evidence still arrives by hand.** Even in these platforms, screenshots are captured manually and request-response pairs are pasted. Automatic ingestion from the proxy history — the obvious integration — is largely absent, and it is where most of the mechanical time goes.

**Client template rendering is the weak point.** Most support templating and most firms report fighting it for enterprise client formats, which is precisely when the effort matters most.

**Finding libraries are shipped generic and rarely personalised.** Out-of-the-box libraries produce reports that read like boilerplate, and testers reject them. Learning the firm's own language from its historical reports, rather than shipping a generic set, would change the reception entirely and is now straightforwardly possible.

**Pricing targets the firms that already adopted.** Per-seat enterprise pricing fits a large consultancy and excludes a five-person boutique, which is the unserved majority of the market.

## Target Customer

The existing vendors — PlexTrac, AttackForge, Dradis — could reach the unserved segment with a genuinely self-serve, low-configuration tier whose finding library is bootstrapped from the firm's own past reports rather than shipped generic. The capability is built; the packaging is not.

The proxy vendors are the more interesting adapter, because they sit where the evidence is and automatic capture is the missing integration that would make any of these platforms work the way testers actually operate.

Buyers are boutique and mid-size firm leadership, and independent testers at a consumer-grade price point.

## Impact If Solved

The largest unbilled cost in this industry has a working solution that most of the market has not adopted, which makes this a distribution and packaging problem with an unusually short path to value.

Automatic evidence ingestion from the proxy is the single feature that would make the existing platforms fit how testers actually work, and it is a smaller build than anything else in this niche.

And bootstrapping the finding library from a firm's own reports would remove the boilerplate objection that has caused most trial abandonments, turning a generic tool into one that writes in the firm's voice from the first day.
