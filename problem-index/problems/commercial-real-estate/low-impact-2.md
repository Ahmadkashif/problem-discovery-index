# Tenant Prospect Matching and Market Expansion Prediction

**Industry:** [[commercial-real-estate|Commercial Real Estate]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic business data platforms can identify companies that may be looking for space, but the CRE-specific signal — which companies are experiencing the employment growth, lease expiration timing, and industry expansion patterns that indicate an active space search — requires a CRE-specific model built on occupier behavior data.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #recommendation #revenue-impact

## The Problem

CRE leasing brokers who represent landlords (tenant rep and leasing assignment work) need to identify prospective tenants for vacant space. An experienced leasing broker knows: which tenants in the submarket have leases expiring in 12-18 months (from their CoStar subscription); which companies are growing their local headcount (from job posting data); and which companies in the same industry as current tenants are typically co-located in the same product type. Junior brokers and firms without CoStar do cold outreach based on business directory searches — low-precision and low-response-rate.

## What Already Exists

CoStar's tenant research tools provide lease expiration tracking. LinkedIn/Revinate provide employment growth signals. No tool combines lease expiration timing, employment growth, and industry expansion signals into a scored tenant prospect list for a specific vacant space and location.

## The Customisation Gap

A tenant prospect matching tool needs: (1) public lease expiration data (from CoStar public records, CMBS data, or deed/assignment records); (2) employment growth signals (LinkedIn job posting volume by company and location); (3) industry co-location patterns (what types of tenants cluster in which property types); (4) a scoring model that prioritizes tenants most likely to be actively searching and best suited for the specific space. The model's definition of a "good prospect" is specific to the property type, size, and location — not a generic classification problem.

## Impact If Solved

Enables leasing brokers without CoStar to target prospective tenants systematically rather than through cold-call lists. Reduces vacancy duration by improving prospecting precision. For a retail or office leasing broker, reducing a vacancy from 8 months to 5 months on a $200,000/year lease is worth $50,000 in rent and commission.
