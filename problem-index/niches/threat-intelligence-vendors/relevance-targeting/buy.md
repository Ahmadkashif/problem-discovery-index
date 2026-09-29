# Buy: Attack Surface Data as a Targeting Input

**Niche:** Relevance & Customer Targeting
**Industry:** [[industries/threat-intelligence-vendors|Threat Intelligence Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Attack surface management already determines what an organisation exposes and what technology it runs, and threat intelligence assesses relevance from a dropdown.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #data-integration #automation #change-point-detection
**Contested on:** Whether relevance is assessed against what the customer actually runs and faces, or approximated by a sector label.

## The Problem

Determining what an organisation exposes to the internet, and fingerprinting the technology behind it, is a mature commercial capability. Attack surface management platforms enumerate domains, hosts, services, certificates and applications continuously from outside, identify the software and versions running, and track changes.

That output is exactly the customer half of a relevance assessment. Whether a threat targeting a particular remote access product is relevant to a customer depends on whether the customer runs it, which attack surface scanning frequently determines directly.

The two capabilities sit in different products. Attack surface management is sold to security teams for exposure reduction. Threat intelligence is sold to security teams for awareness. Nobody joins them, so a vendor with detailed knowledge of what a customer exposes does not use it to decide what intelligence to send, and a vendor sending intelligence has no idea what the customer runs.

Some vendors own both capabilities and still do not connect them, because the products were built by different teams for different buyers.

## What Already Exists

Attack surface management: Randori, Censys, Detectify, Cortex Xpanse, Defender EASM and the ASM modules in the large platforms — continuous external discovery with service and technology fingerprinting.

Internet-wide scan data: Shodan and Censys, providing broad technology and exposure data across the internet, queryable by attribute.

Technology profiling: BuiltWith, Wappalyzer and similar, identifying the technology stack behind public-facing services.

Supply chain mapping: the emerging third-party and fourth-party mapping products, and SBOM data where available.

Threat intelligence: sector and geography tagging on indicators and reports, adversary profiles describing targeting in prose.

## The Customization Gap

**No join exists between exposure and threat.** ASM produces an exposure inventory. Threat intelligence produces threat descriptions. Matching one against the other is the product and neither vendor builds it.

**Threat targeting is unstructured.** ASM output is structured data. Adversary targeting is prose in a report. The matching requires extracting targeting attributes into a comparable form, which is the missing layer.

**ASM is oriented to vulnerability, not to adversary.** It reports what is exposed and potentially vulnerable. Relevance asks whether a specific adversary targets this profile, which requires the threat side and is outside what ASM covers.

**Internal estate is invisible from outside.** External scanning covers the perimeter. A great deal of relevant technology — endpoint software, internal applications — is not externally observable, which means observation must be combined with declaration or telemetry.

**Supply chain relevance is unhandled by both.** A threat targeting a critical supplier matters to the customer and appears in neither product's model.

**Consent and framing are undesigned.** Using a customer's exposure data to target their intelligence requires permission and an explanation, and no vendor has built the flow.

## Target Customer

Vendors owning both capabilities — the large security platforms with intelligence arms and ASM products — for whom this is an internal integration rather than a partnership, and which they have not performed.

ASM vendors as adapters, adding a threat-relevance layer over an exposure inventory they already maintain, which would differentiate them in a converging category.

Security operations leadership as the buyer, for whom intelligence filtered by what they actually run is straightforwardly more useful than intelligence filtered by sector.

## Impact If Solved

The customer half of the relevance assessment already exists as a commercial product and is not being used for the purpose it most obviously serves.

Extracting adversary targeting into structured attributes is the missing layer, and it is a text extraction task over the vendors' own report corpora rather than a research problem.

And joining exposure to threat would let a vendor say, specifically, that this campaign targets software the customer is running on an exposed host — which is a categorically more useful statement than a sector tag.
