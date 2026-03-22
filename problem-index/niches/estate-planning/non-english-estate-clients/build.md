# Cross-Border Estate Planning Intake & Documentation

**Niche:** [[niches/estate-planning/non-english-estate-clients/profile|Non-English Estate Clients]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Attorneys serving immigrant families capture foreign assets, inheritance law context, and cultural expectations in a structured intake process — instead of discovering cross-border complications mid-engagement when it's expensive to course-correct.
**Tags:** #large-language-models #bert #feature-engineering #evaluation-metrics #data-integration #compliance

## The Problem
When an immigrant client comes to an estate planning attorney, the standard intake questionnaire misses critical information: real estate owned in their home country (which may be subject to forced heirship rules), bank accounts abroad (which trigger FBAR and Form 3520 reporting), business interests in foreign entities (which may create foreign trust reporting obligations), and inheritance expectations shaped by their home country's legal and cultural norms. A Mexican-American client may expect equal division among all children (reflecting Mexican civil law defaults) without realizing that US law allows complete disinheritance of adult children. A client from India may have inherited agricultural land that cannot be sold to non-agricultural persons under Indian law. These complications surface 3-4 meetings into the engagement, requiring the attorney to restart the planning process.

## Why Nobody Has Built This
The intake problem is intensely multidimensional: the system must know enough about dozens of countries' inheritance laws, property rules, and tax treaty provisions to ask the right questions. It must handle cultural sensitivity (asking about family dynamics, prior marriages, illegitimate children) in culturally appropriate ways. The market is fragmented — attorneys serving Chinese immigrant communities in San Francisco need different intake logic than attorneys serving Dominican communities in New York. No vendor has attempted to build a cross-cultural, cross-jurisdictional intake system because the domain knowledge required is vast and the addressable market per cultural segment is small.

## What to Build
A structured cross-border intake platform organized by country of origin. For each country, the system includes: (1) a country-specific questionnaire module that asks about asset types common in that country, inheritance law defaults, and family structure norms, (2) a foreign asset documentation checklist (FBAR, Form 3520, Form 8938 requirements based on asset types and values), (3) a cultural expectations mapping that translates the client's inheritance wishes into US legal options ("equal division among all children" maps to per stirpes distribution; "eldest son gets the house" maps to specific bequest with equalization provisions for other children), and (4) a conflict identifier that flags where the client's home country laws may create issues (forced heirship rules that override the US will for in-country assets, community property rules from civil law marriages). Available in the attorney's primary language and the client's primary language for parallel review.

## Target Customer
Bilingual estate planning attorneys in metro areas (LA, NYC, Miami, Houston, San Francisco, Chicago) serving immigrant communities, currently handling 5-15 cross-border cases per month using ad hoc intake processes and personal knowledge of their clients' home country laws.

## Impact If Built
Reduces cross-border estate planning engagement time by 30-40% by capturing foreign asset and cultural context in the first meeting rather than discovering it over multiple sessions. Prevents foreign trust reporting penalties ($10,000+ per missed Form 3520) by identifying reporting obligations at intake. Enables non-specialist attorneys to serve immigrant clients with confidence, expanding the addressable market for underserved communities.
