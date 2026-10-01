# Comps and Precedents for Companies Nobody Covers

**Industry:** [[investment-banking-boutiques|Investment Banking Boutiques]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Data terminals spread public comparables well, and a mid-market boutique's targets are private companies whose real peers are other private companies and whose precedent multiples were never disclosed.
**Tags:** #word-embeddings #k-nearest-neighbors #large-language-models #linear-regression #feature-engineering #data-integration #automation #quick-win

## The Problem
Every pitch and every valuation section needs trading comparables and precedent transactions. For a large public company the peer set is conventional and the terminal spreads it in minutes. For a mid-market private target — a $40M-EBITDA testing laboratory, a regional packaging converter — the analyst must decide which public companies are genuinely comparable, calendarise their fiscal years, strip one-off items, and then explain to the MD why a $9B public peer trading at 14x is relevant to a business a fiftieth its size.

Precedents are worse. Most mid-market transactions are private-to-private and undisclosed; the terminal shows a deal happened and leaves the multiple blank. The analyst fills the gap from press releases, from the firm's own past deals, from a colleague's recollection, and from paid surveys, and the precedent table that ends up in the book is a curated mixture of disclosed figures and estimates whose provenance nobody records.

## What Already Exists
S&P Capital IQ, FactSet, PitchBook and LSEG spread public comps, calendarise, and export to Excel; their screening tools find companies by industry code and size. Office plug-ins such as Macabacus and FactSet's own add-ins link spreads to slides. PitchBook and GF Data report private-market multiples in aggregate.

## The Customisation Gap
The generic tools answer "which companies share this industry code"; the banker needs "which companies would an informed buyer actually benchmark this business against", which turns on end-market, customer concentration, recurring revenue share and margin structure that industry codes do not capture. Peer selection from business-description similarity, weighted by financial profile, is a well-shaped retrieval task the terminals do not do for private targets.

The second gap is the firm's own precedent knowledge: multiples from its own closed deals, buyer-shared figures, and estimates of undisclosed transactions, held with their provenance and confidence. Today these sit in individual analysts' prior books. A precedent library that records where every number came from — disclosed, estimated, or from the firm's own mandate under what confidentiality — is the customisation, and it must respect that some of those figures cannot be shown to third parties.

## Impact If Solved
Comps and precedents are rebuilt for nearly every pitch and every process, by the most junior people, from scratch. A peer-selection and precedent library tuned to private mid-market targets turns a day of spreading and justifying into an hour of review, and makes the valuation pages consistent across pitches rather than dependent on which analyst built them.
