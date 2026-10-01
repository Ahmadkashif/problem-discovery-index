# Transcript Anonymisation and Entity Tagging

**Industry:** [[expert-networks|Expert Networks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Turning a recorded expert call into a sellable library transcript means removing every clue to who spoke and who asked while keeping every fact a reader needs, and generic transcription and redaction tools get both halves wrong.
**Tags:** #transformers #bert #large-language-models #graph-theory #evaluation-metrics #data-integration #automation

## The Problem
Transcript libraries sell compliance-reviewed transcripts of expert calls, often calls hosted by the library's own analysts. Each transcript must be anonymised — the expert's name, employer history detail that would identify them, the client's identity and the specific question pattern that would reveal a fund's position — while the substance stays intact. It must then be tagged to the public companies, private companies, products and industries discussed, so a subscriber searching a ticker or a private competitor finds it.

The work is done by transcription, an automated redaction pass, and then editors and content analysts who read every transcript. Over-redaction destroys value ("a large retailer" instead of the retailer whose dairy contracts were discussed); under-redaction exposes an expert whose former employer can be inferred from three details together.

## What Already Exists
Speech-to-text from several vendors with good general accuracy; generic named-entity redaction from privacy tooling; entity tagging and search from market-intelligence platforms; and company identifier databases from financial data vendors.

## The Customisation Gap
Generic redaction treats every name as personal data, whereas here company names must mostly stay and person-identifying combinations must go — the risk is quasi-identifiers (tenure, title, region, plant name) that jointly identify a person, which needs a re-identification check across the expert's own profile rather than a list of entity types.

Entity tagging has to resolve the long tail: private companies, subsidiaries, product names, and informal references ("the big Ohio player") to canonical identifiers, including mapping private companies to their public competitors and suppliers so a subscriber covering a ticker sees the call about its unlisted rival. Transcription needs the domain vocabulary — product codes, drug names, part numbers, acronyms specific to an industry — that general models mis-hear.

## Impact If Solved
Editorial review per transcript is the binding constraint on how fast a library grows and how quickly a call reaches subscribers. Automating re-identification checks and long-tail entity resolution cuts that review to exceptions and makes the long tail of private-company coverage — the part subscribers cannot get elsewhere — findable.
