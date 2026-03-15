# AI-Assisted Conflict Checking

**Industry:** [[small-law-firms|Small Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Practice management systems can search their client database for matching names, but the legally meaningful conflict check — identifying corporate affiliates, related entities, adverse parties in prior matters, and the nuanced imputation rules for shared-office practitioners — requires legal judgment that simple name matching doesn't provide.
**Tags:** #bert #text-classification #nlp #automation #compliance

## The Problem
Before accepting a new client representation, the attorney must ensure no conflict of interest exists — with current clients (can't represent adverse parties against them), former clients (can't represent a new client against them in a substantially related matter), and certain other parties depending on jurisdiction. The conflict check involves searching the firm's records for: the new client's name and all related entities and individuals (principals, subsidiaries, parent companies, related parties), the adverse parties and their related entities, and the nature of the new matter to compare against prior matters. Current practice management system search functions do a name-match search — they find exact and approximate matches in the client database, but they don't understand corporate family relationships, don't know that "ABC Corp." and "ABC Corporation" are the same entity, and don't assist with the legal analysis of whether a found relationship constitutes an actual conflict.

## What Already Exists
Clio, PracticePanther, and most practice management systems have built-in conflict search functions. Thomson Reuters and LexisNexis offer more sophisticated corporate entity search tools (Intelligize, Corporate Affiliates) designed for large firm conflict checking. These enterprise tools are priced and designed for large firms. Practical Law and similar tools provide the rules for conflict analysis — what constitutes a substantial relationship, imputation rules for firm size — but don't automate the application of those rules to search results.

## The Customisation Gap
What's needed for a small firm conflict check tool is: (1) entity disambiguation (multiple spelling variations of the same party name, corporate form abbreviations, DBA names); (2) corporate affiliate lookup for corporate entities (who is the parent company? who are the subsidiaries?); (3) principal and officer lookup for the entities involved; (4) a plain-language analysis of whether identified relationships constitute a conflict, with the specific rule being applied. The customization for small firms is the pricing and integration layer — enterprise conflict checking tools cost $500-2,000/month, which is prohibitive for a solo or two-attorney firm.

## Impact If Solved
Reduces conflict check time from 20-40 minutes per new client intake to 5-10 minutes of reviewing flagged results. More importantly, reduces the risk of a missed conflict that results in disqualification, malpractice exposure, or bar discipline — the tail risk that makes thorough conflict checking professionally essential.
