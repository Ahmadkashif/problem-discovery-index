# Adoption Tracking Adapted to Jurisdictional Fragmentation

**Niche:** [[niches/engineering-consultants/building-code-publishers/profile|Building Code Publishers]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Legislative tracking services cover state legislatures well and stop there; code adoption happens in municipal ordinances, county resolutions, and building department policy memos that no tracker follows.
**Tags:** #bert #transformers #large-language-models #change-point-detection #word-embeddings #evaluation-metrics #transfer-learning #automation #compliance #data-integration

## The Problem
Knowing which edition is in force where is the foundation of everything downstream, and it is genuinely hard to establish. States adopt statewide in some cases and delegate to localities in others; municipalities adopt by ordinance on their own schedules, sometimes years behind, sometimes with amendments that arrive separately from the adopting ordinance; and building departments issue policy interpretations that function as amendments without being enacted as ones. Tracking is done by staff watching sources manually and by asking, which forces prioritization toward large jurisdictions and leaves the long tail — where a firm working out of state is most likely to be caught out — unmaintained.

## What Already Exists
Legislative and regulatory tracking is a real market. The commercial tracking services cover state legislatures and major agency rulemaking comprehensively; municipal code hosting platforms publish ordinances for many jurisdictions in structured form; web change detection is commodity infrastructure.

## The Customization Gap
Existing services are built around legislatures and agencies with published calendars. Code adoption is a municipal administrative act, frequently recorded only as an ordinance number amending a chapter of a municipal code, with the substantive content in an incorporated document. Detecting it requires knowing what an adoption looks like in each jurisdiction's ordinance style — which is a domain model, not a keyword. The adaptation is adoption-specific monitoring: municipal code platforms and jurisdiction sites treated as first-class sources, ordinance text classified as adoption, amendment, or unrelated, and the adopted edition and effective date extracted with the amendment content resolved to provisions of the base code. Coverage completeness must be estimated and reported per state, because a national adoption map whose reliability is unstated is worse than one that says which jurisdictions it is confident about. And building department policy interpretations need a channel of their own, since they change what is enforced without changing what is adopted.

## Target Customer
Directors of code development and government relations at code publishers, and the multi-state engineering firms who currently confirm the applicable edition by telephoning building departments.

## Impact If Solved
Makes the amendment layer possible, since the amendments cannot be assembled without knowing what was adopted. Measured adoption coverage is also directly valuable to the publisher's own advocacy, which currently argues for adoption without being able to state precisely where its codes stand.
