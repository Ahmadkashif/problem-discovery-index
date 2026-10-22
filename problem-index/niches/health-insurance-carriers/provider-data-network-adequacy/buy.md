# Customer Master Data Management Configured for Provider Rosters

**Niche:** [[niches/health-insurance-carriers/provider-data-network-adequacy/profile|Provider Data, Directories & Network Adequacy]]
**Industry:** [[industries/health-insurance-carriers|Health Insurance Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Enterprise MDM platforms already match and merge customer records across systems; provider data needs the same engine with field-level trust rules a regulator can audit.
**Tags:** #k-nearest-neighbors #logistic-regression #feature-engineering #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to keep each directory entry matching what the provider's office would say on the phone, within the No Surprises Act's 90-day verification cycle, and whoever's directory passes a regulator's secret-shopper sample with the fewest wrong listings takes the account.

## The Problem
A clinician appears in the credentialing system, the contract system, the claims platform, CAQH and two group rosters, each with slightly different names, locations and identifiers. Plans maintain a "golden record" by hand.

## What Already Exists
Enterprise master data management platforms (Informatica, Reltio and others), which provide entity resolution, survivorship rules and stewardship workflows for customer and product data.

## The Customization Gap
Provider data needs several layers the generic platform lacks. A data model of clinician × location × group × contract × product × network. Survivorship by field and recency: claims activity outranks old attestations on location, and rosters outrank call results on participation. NPI, TIN and CAQH identifiers handled as native keys. Network and product participation derived from contract terms. Ninety-day verification timers per field. And a per-field audit history in the form directory regulators ask for.

## Target Customer
Provider data management leaders at plans with multiple core platforms after mergers, or with large delegated-credentialing groups.

## Impact If Solved
One provider record that every downstream system uses, verified on a regulator-ready trail, without stewards reconciling by hand.
