# A Field-Fix Ledger Joined to the Piece Mark

**Niche:** [[niches/drafting-services/structural-steel-detailing/profile|Structural Steel Detailing]]
**Industry:** [[industries/drafting-services|Drafting Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Fabricators back-charge detailers for field fixes and nobody keeps the record that would show which detailers, connection types, checkers and design conditions cause them.
**Tags:** #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #data-integration #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to deliver checked, approval-ready shop and erection drawings inside the fabricator's schedule with the fewest errors reaching the shop floor, and whoever can prove the lowest field-fix rate per ton takes the fabricator's account.

## The Problem
When a beam will not bolt up at erection, the erector reports it, the fabricator sends a crew or a replacement piece, and the cost is argued out: design error, detailing error, fabrication error or erection error. If it lands on the detailer, the bureau is back-charged. The event is documented in emails, a field report and an invoice. It is almost never joined to the piece mark, the connection type, the detailer who modelled it, the checker who passed it, or the design revision in force at the time. A fabricator using four bureaus cannot say which one produces fewer field fixes per thousand tons, and a bureau cannot say which of its checkers or connection types are leaking errors.

## Why Nobody Has Built This
The data crosses organisations: the field report is the erector's, the back-charge the fabricator's, the model the detailer's. Field fixes are contentious, so neither side is eager to create a permanent record. And each fabricator's volume of field fixes is small enough that nobody treats it as data.

## What to Build
A ledger owned by the fabricator, or shared by agreement between fabricator and detailer, that logs every shop query and field fix against the piece mark in the model, classifies the root cause from the report and photos, and attaches the design revision, detailer, checker and connection type. On top, error-rate statistics per thousand tons by vendor, connection type and design condition, and a ranking of which connection types and checkers most often let errors through.

## Target Customer
Detailing managers at AISC-member fabricators buying from several bureaus; larger detailing bureaus that want to prove their quality with data rather than references.

## Impact If Built
Detailing would be bought on measured quality rather than on price and anecdote. Bureaus would see where their checking fails, and the ledger would become the label set for any learned checking model.
