# Drug Interaction Database with International Brand Name Cross-Reference

**Niche:** [[niches/pharmacy-independents/non-english-communities/profile|Non-English Community Pharmacy]]
**Industry:** [[industries/pharmacy-independents|Independent Pharmacies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Drug interaction databases (First Databank, Medi-Span) use US NDC numbers exclusively — they cannot identify a medication by its Indian, Mexican, or Chinese brand name, leaving pharmacists unable to check interactions when patients report taking foreign-purchased medications.
**Tags:** #data-integration #feature-engineering #quick-win #compliance

## The Problem
Patients in immigrant communities frequently take medications purchased in their home countries — either brought during visits, shipped by family, or obtained from informal importers. These medications are identified by foreign brand names (e.g., "Crocin" for acetaminophen in India, "Tempra" for acetaminophen in Mexico, "Baijiahei" for a Chinese cough syrup containing dextromethorphan and chlorpheniramine), use different dosage forms and strengths than US equivalents, and have packaging in non-Latin scripts. When a patient says "I also take Crocin for pain," the pharmacist must identify the active ingredient to check for interactions with newly prescribed medications. Currently, this identification relies on the pharmacist's personal knowledge of foreign pharmacopeias or internet searches — an unreliable process that takes 5-10 minutes per foreign medication and may not yield accurate results, especially for herbal/traditional medicines from Asian countries.

## What Already Exists
First Databank (FDB) and Medi-Span are the standard drug interaction databases integrated into US pharmacy PMS systems. They contain comprehensive US NDC data with interaction checking, but their coverage of international brand names is minimal. The WHO's International Nonproprietary Names (INN) database maps generic names across countries but does not include brand names. Individual country pharmacopeias exist (India's CDSCO, Mexico's COFEPRIS) but are not integrated into any US pharmacy workflow tool.

## The Customization Gap
The gap is an international drug cross-reference layer that maps foreign brand names to US-equivalent active ingredients and enables interaction checking: (1) a searchable database of common foreign brand names (top 500 medications by country for the 10 most common origin countries of US immigrant populations) mapped to their active ingredients using INN nomenclature, (2) input support for non-Latin scripts — the pharmacist types the name as the patient spells it, or photographs the foreign medication label for identification, (3) automatic interaction checking once the active ingredient is identified — routing through the existing FDB/Medi-Span engine in the PMS, and (4) documentation of the foreign medication in the patient's profile for future reference. This cross-reference database requires initial curation by pharmacists familiar with each country's pharmacopeia, with ongoing community-contributed additions. A PMS plugin or standalone web tool priced at $99-149/month fills this gap.

## Target Customer
Pharmacies serving immigrant communities where 20%+ of patients report taking foreign-purchased medications, currently relying on the pharmacist's personal knowledge or internet searches to identify active ingredients.

## Impact If Solved
Reduces foreign medication identification time from 5-10 minutes to under 30 seconds, enables reliable interaction checking for the estimated 15-25% of immigrant patients taking foreign medications concurrently with US prescriptions, and documents foreign medication use in the patient profile — eliminating a significant blind spot in medication safety for this population.
