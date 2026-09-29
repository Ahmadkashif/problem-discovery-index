# The Colour Matcher's Reasoning Never Leaves the Bench

**Niche:** [[niches/auto-body-shops/paint-color-formulation-research/profile|Automotive Paint Colour Formulation Research]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Fix (Pain Point)
**One-liner:** The technical support archive is the only record of what actually goes wrong with colour in the field, and it is a ticket queue.
**Tags:** #tacit-knowledge-ml #large-language-models #evaluation-metrics #workflow-orchestration #worker-facing

## The Problem
When a match fails badly enough, the shop calls technical support. A colour specialist works the problem: which variant was tried, what the substrate is, whether the panel was previously repaired, what the blend technique was, what the lighting was, whether the vehicle has been repainted before. Sometimes it resolves in one call. Sometimes it becomes a field visit and a custom formula.

Those calls are the richest diagnostic record the company has. They document, case by case, the failure modes of its own product in the hands of real users — which colours are genuinely difficult, which vehicles arrive with undisclosed prior repairs, which shops have technique problems, and which library entries are simply wrong.

They are stored as tickets. Free text, closed when resolved, searchable by customer and date and effectively by nothing else. The specialist's reasoning — what they suspected first, what ruled it out, what the actual cause turned out to be — is a paragraph in a case note or is not written at all.

Three consequences follow. The library never learns systematically: a formula generating repeated field failures is discovered when a specialist happens to notice a pattern across their own calls. Specialists are the constraint, and their expertise takes years to build in a small, senior, ageing group. And the same problem is solved from first principles in three regions in the same week.

## Why It's Still Broken
Technical support is a cost centre measured on resolution time and case volume. Structured capture is time added to a call that somebody is waiting on.

The ticket system was bought to route and close cases, and its schema reflects that. There is a field for the customer and none for the failure mechanism.

And support is organised regionally, so the natural unit of learning is the individual specialist's territory rather than the product. Nobody owns the question "what is this colour doing in the field nationally".

## What a Fix Looks Like
**Give the case a diagnosis field, not just a resolution.** Failure mechanism, contributing factors, and the formula or variant implicated, from a controlled vocabulary. Under a minute per case, on cases that already take twenty.

**Route library implications automatically.** A formula named in repeated cases across unrelated shops is a library defect and should reach colour development as a queue item, not as an anecdote. That loop does not exist today.

**Make the archive retrievable by symptom.** Specialists reason from cases they remember. Retrieval over past cases by failure signature rather than by customer name is useful from the first week, which determines whether the capture habit holds.

**Feed it into the field.** The most common diagnoses, surfaced in the mixing software at the moment a painter is struggling, deflect calls entirely — which is the argument that makes support leadership fund the work.

**Measure specialist consistency.** Route a sample of cases to two specialists and compare diagnoses. It is uncomfortable, it is the only way to know whether the diagnosis vocabulary means the same thing across regions, and it produces the labelled set any assistance layer would need.

**Join to the field readings.** A support case where the spectrophotometer data is attached is a fully worked example linking measurement, variant choice, diagnosis and outcome — the exact record the prediction work above is missing.

## Who Feels the Pain
Colour specialists, who are few, senior and irreplaceable, and whose accumulated diagnostic knowledge is stored as closed tickets; painters, who wait for a callback on a problem three other shops solved last month; colour development, which cannot see its own field failure rate; and the company, whose competitive claim is match quality and whose only record of match failure is a support queue.

## Impact If Fixed
The support archive is a national field-failure study the company is already paying to conduct and not reading. Structuring it closes the loop between library and reality, deflects volume from a scarce specialist workforce, and produces the diagnosis-labelled corpus without which neither the variant prediction nor the reading-quality work can be properly evaluated.
