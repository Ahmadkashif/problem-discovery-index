# A Verified-Contact Graph for Employers Off the Databases

**Niche:** [[niches/investigation-and-screening-firms/employment-education-verification/profile|Employment, Education & Licence Verification]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The experienced verification specialist knows who actually answers for thousands of small and defunct employers, and that knowledge sits in their notes rather than in the firm's routing.
**Tags:** #tacit-knowledge-ml #graph-theory #k-nearest-neighbors #random-forests #evaluation-metrics #data-integration
**Contested on:** Every serious competitor in this niche is fighting to close an employment, education or licence verification without a human phone call, and whoever answers the most verifications from direct, instant sources takes the account.

## The Problem
Employers not covered by instant databases — small businesses, franchisees, companies acquired or closed, foreign employers — are verified by people. Finding the right contact is the hard part: the main number reaches a receptionist, HR is outsourced to a payroll provider, the acquired company's records went to the buyer's HR shared service. Senior specialists remember; their notes are free text in closed orders.

## Why Nobody Has Built This
Verification attempts are logged as activity, not as knowledge. Employer names are entered as the candidate typed them, so the same employer appears under dozens of spellings and its history cannot be pooled.

## What to Build
Resolve every employer name in past orders to an entity, link entities through acquisitions and franchises, and attach every successful route — contact, channel, response time, outcome — to the entity. The result is a graph the queue consults first: for a new verification it proposes the route that worked most recently and fastest, the successor custodian for a defunct employer, and an estimate of time to close.

## Target Customer
Operations leaders at screening firms with millions of past verifications in their logs.

## Impact If Built
More verifications close on the first attempt, new specialists perform like experienced ones, and the firm's most perishable operational knowledge becomes an asset.
