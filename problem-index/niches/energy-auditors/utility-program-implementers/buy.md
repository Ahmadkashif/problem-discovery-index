# Verify the Installation, at Volume, Mostly by Looking at a Photograph

**Niche:** [[niches/energy-auditors/utility-program-implementers/profile|Utility Efficiency Programme Implementers]]
**Industry:** [[industries/energy-auditors|Energy Auditors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every rebate requires proof that the measure was installed and qualifies, and proof arrives as invoices, model numbers and phone photographs.
**Tags:** #cnns #transformers #object-detection #workflow-orchestration #compliance

## The Problem
A rebate is paid against evidence. The contractor submits an invoice, equipment model numbers, and photographs of the installation. Programme staff verify that the measure qualifies under the programme rules, that the equipment meets the efficiency tier, that the quantity is plausible for the property, and that the installation appears to have actually happened.

At programme scale this is an enormous processing operation, and it is the implementer's main cost line outside contractor incentives. It is also the integrity control: rebate fraud and unqualified claims are a persistent problem, and a share of applications are sampled for field inspection precisely because paper verification is weak.

The evidence resists automation as currently handled. Model numbers are transcribed by contractors and frequently wrong or ambiguous across manufacturer naming conventions. Qualifying equipment lists are maintained by third-party certification bodies and updated continuously. Invoices are freeform. Photographs are taken in attics and mechanical rooms at odd angles, and what they need to prove — that this specific unit was installed at this address — is not what a general image model extracts.

## What Already Exists
Document extraction platforms handle invoices well. Qualified product lists are published in structured form by the certification bodies. Field service and inspection apps with photo capture are commodity. Image classification for equipment identification exists in adjacent maintenance applications.

None assembles into verification. Invoice extraction gets the line items and cannot say whether the model qualifies under this programme's tier this quarter. Product lists are published and are not joined to the messy model strings contractors actually type. And no general image tool is asked the specific question here: does this photograph evidence this installation at this property.

## The Customization Gap
**Model string resolution against a moving qualified list is the core problem.** Contractor-typed model numbers must resolve to a certification record with an efficiency tier that was in effect on the installation date. Time-awareness is essential and is what generic matching lacks.

**Programme rules are the target, and they differ per utility and per year.** Eligibility, tiers, caps, stacking rules and documentation requirements are contract-specific. The rule layer must be versioned so the implementer can show which rule it applied to which application.

**Photographs prove installation, not identification.** The useful signals are nameplate legibility, evidence of the surrounding installation, and consistency with the property — a narrow, domain-specific set of checks rather than general object recognition.

**Fraud risk should direct field inspection.** Field verification is the expensive control and is sampled. Directing it at high-risk applications rather than at random is the largest available efficiency gain, and the historical inspection results are the training label.

**Confidence must triage, not decide.** Wrongly denying a legitimate rebate damages the contractor relationship the programme depends on; wrongly paying an unqualified one is an audit finding. Ambiguity goes to a reviewer with the evidence assembled.

**Contractor submission quality is itself signal.** Contractors differ systematically in documentation quality, and that pattern predicts both errors and fraud.

## Target Customer
VP of Programme Operations or Chief Technology Officer at an efficiency programme implementer.

## Impact If Solved
Verification is the largest controllable cost in programme delivery and the control on which programme integrity rests, in a business competitively bid on cost per unit of savings. Automating the resolvable share and directing field inspection by risk attacks both at once — and produces the installation-quality record the realisation modelling above requires.
