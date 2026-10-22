# Digital Copy Approval Against Face-Level Rules

**Industry:** [[outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Digital signage software checks that a creative file is the right size and format; nobody's software checks that it is legal on this face, near this school, under this landlord's lease and next to this competitor in the loop.
**Tags:** #large-language-models #transformers #cnns #k-nearest-neighbors #compliance #workflow-orchestration #automation

## The Problem
A digital billboard rotates ~6–8 advertisers in a loop (estimate), each for a fixed dwell time. Tennessee's eight-second minimum, two-second change and ban on animation are typical of state rules written after FHWA's 2007 guidance. Every creative that goes into a loop must clear rules that vary face by face. Cannabis ads are barred within 1,000 feet of schools, playgrounds and parks in Washington, and San Diego's ordinance left only 352 of 644 billboard locations open to them. Alcohol faces sensitive-site buffers in some states. Political ads need the right paid-for disclosure for the jurisdiction. Lease clauses bar categories at specific sites. Advertisers buy category exclusivity or separation from competitors in the same loop. Digital ad operations staff check this by reading the creative, looking up the face and remembering the rules, several hundred times a week at a large market. Programmatic buying makes it harder: creatives now arrive through supply platforms hours before they run.

## What Already Exists
Digital out-of-home content management systems such as Broadsign Control schedule loops and play creatives; supply platforms such as Vistar Media run creative approval queues for programmatic buys; operators keep internal copy policies and legal review for sensitive categories.

## The Customisation Gap
The tools check file specifications, dwell slots and flight dates. They don't hold a face-level rule set. What needs to be layered on: a rules registry per face built from state and local codes, proximity to schools and parks (computed from GIS layers), lease restrictions and sold exclusivities; classification of each creative's category, claims and disclosures from the image and text, including small type a person misses at a glance; checks for legibility at the face's read distance (word count, type size against viewing time); and a decision record of who approved what against which rule, for the day a city or a landlord complains. The same registry should block a sale that the face can't legally run, before the contract rather than at upload.

## Impact If Solved
Copy approval drops from minutes of lookup per creative to seconds of review on the flagged few. Programmatic campaigns can be accepted close to air time without risking a cannabis ad beside an elementary school or a competitor beside an exclusive advertiser. Those are mistakes that cost a makegood and sometimes the permit conversation with the city.
