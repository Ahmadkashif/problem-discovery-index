# The LMS Reports Course Completion; The Question Was Whether Anyone Can Mix a Formula

**Niche:** [[niches/hair-salons-independent/manufacturer-education-technical-teams/profile|Professional Brand Education & Technical Teams]]
**Industry:** [[industries/hair-salons-independent|Hair Salons (Independent)]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Learning platforms, field CRM and distributor sales feeds are all bought and all measure the wrong thing — attendance, visits and cases shipped — while the outcome that matters happens at a chair the brand cannot see.
**Tags:** #k-nearest-neighbors #dimensionality-reduction #feature-engineering #data-integration #evaluation-metrics

## The Problem
A professional brand's education organisation is substantial and is tooled like a corporate training and field sales function. There is a learning management system for course catalogues, registration and certification. There is a CRM for the field educators and technical artists who visit salons. There is distributor sell-in and, sometimes partially, sell-through reporting. There is a digital asset library of technique videos and formulation guides, and a technical support ticketing system.

Every one of these was built for a business where the customer transacts with the company directly and the outcome is a purchase. Here the customer is a stylist who buys through a distributor, works in a salon the brand has no system of record for, and produces an outcome — a colour result on a client's head — that no bought tool has any concept of.

## What Already Exists
LMS platforms handle catalogue, enrolment, completion and certification well. Field CRM tracks visits, accounts and activity. Distributor data exchanges provide sell-in and, in some territories, sell-through. Digital asset management serves the video library. Ticketing platforms run technical support. Marketing automation reaches stylists directly where the brand has captured them. Consumer colour-matching apps exist and are built for at-home box colour.

## The Customization Gap
**Completion is not capability.** An LMS certifies that a stylist attended and passed a quiz. The organisation's actual question is whether that stylist can now predict a result on a difficult head, and whether their corrections went down afterwards. Nothing in the bought stack connects a training record to any downstream behaviour, because there is no downstream signal in the stack at all.

**The distributor sits in the join.** Sell-through data, where it exists, is aggregated, delayed and inconsistently structured across distributors and territories. Resolving it to a salon, and a salon to the stylists the education organisation trained, is an entity resolution problem across parties with no shared key and, often, no interest in supplying one. Every attempt to measure education against purchasing runs aground here.

**Shade space is not a product catalogue.** Colour products relate to each other perceptually — this shade is two levels lighter and a half-step cooler than that one — and every system in the stack treats them as SKUs in a hierarchy. Substitution, cross-brand conversion and "what should I use instead" questions are geometry in a colour space, and no commerce or CRM data model represents it.

**Ticketing throws away the case.** Technical support platforms are optimised for resolution time and are indifferent to content. The formulation details in the call — starting condition, history, formula, outcome — go into a free-text note field and are never structured, because ticketing was never meant to build a dataset.

**Consumer colour-matching tools solve a different problem.** They match a person to a box shade under generous tolerances. Professional formulation needs starting level and porosity assessment accurate enough to plan a chemical process, under salon lighting, against a professional shade library. The tolerance gap is large enough that the consumer tooling is not a starting point.

**Field visits are recorded as activity.** The CRM tells the organisation which salons an educator visited. It does not represent what the salon's colour business looks like, what it is struggling with, or whether the visit changed anything — so route and priority decisions are made on account size and relationship.

## Target Customer
VP of Education or Head of Professional Digital at a colour brand. The sensible split is to keep the LMS, CRM, DAM and ticketing platform as the systems of record, and build three things nothing supplies: a structured technical case corpus out of the support queue, a colour-space representation of the shade library, and the resolution layer that ties trained stylists to salons to purchasing.

## Impact If Solved
The professional division's largest investment is education, its defensibility rests on that education, and every system it uses to run it reports attendance and cases shipped because that is what the software was built to count.
