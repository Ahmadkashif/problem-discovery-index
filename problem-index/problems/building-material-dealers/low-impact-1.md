# Special-Order Windows and Doors Re-Keyed From the Configurator

**Industry:** [[building-material-dealers|Building Material Dealers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Configure-price-quote software and manufacturers' own configurators produce a correct window quote; nothing checks that quote against the plan's window schedule and rough openings, carries it into the dealer's ERP without re-keying, or catches the acknowledgement that came back different.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #random-forests #data-integration #automation #workflow-orchestration

## The Problem
Windows, exterior doors, interior doors and millwork are about a quarter of a pro dealer's sales (Builders FirstSource reported $3.8B, 25.3%, in 2025), and much of it is special-order. The dealer's window specialist reads the plan's window schedule, configures each unit in the manufacturer's software — size, rough opening, frame and jamb depth, glass package, grille pattern, handing, hardware, exterior colour — quotes the builder, then re-keys the order into the dealer's ERP and submits it to the manufacturer. A whole-house package can run to 25–60 units (estimate), each a dozen attributes long.

Errors are cheap to make and expensive to discover. A swapped handing, a jamb depth for 2x4 walls on a 2x6 house, a tempered-glass requirement missed beside a tub, or a unit sized to the masonry opening rather than the rough opening shows up when the window arrives on site weeks later. The remake takes another lead time (~2–12 weeks depending on the manufacturer, estimate), the framer leaves the opening wrapped, and the dealer usually eats the cost. Manufacturer acknowledgements, which should catch the mismatch, arrive as PDFs that nobody compares line by line with the quote.

## What Already Exists
Manufacturers' configurators (Andersen, Pella, Marvin, JELD-WEN, ProVia, Therma-Tru and others) price and validate units against their own rules. Integrators such as Saberis bridge configurator quotes into dealer ERPs, and takeoff services such as Paradigm can pass window takeoffs into dealer quoting. General configure-price-quote platforms exist for manufacturers. Dealer ERPs (Epicor BisTrack, DMSi Agility, ECI Spruce) hold the special order once keyed.

## The Customisation Gap
The missing layer is dealer-side and cross-manufacturer: reading the plan's window and door schedule and elevations into a list of openings; checking each configured unit against its opening (rough opening, wall thickness, egress size in bedrooms, tempered glazing near doors and tubs, wind-zone or energy-code requirements the jurisdiction imposes); flagging handing and swing against the floor plan; carrying the configured lines into the ERP without re-keying; and comparing every manufacturer acknowledgement with the quote and the order before production starts. It has to work across five or six manufacturers' formats at once, because a single house often mixes brands. Generic CPQ validates a unit against a catalogue; the dealer needs the unit validated against the house.

## Impact If Solved
If plan-to-configuration checks and acknowledgement matching cut remakes from ~3% of special-order units to ~1% (estimate), a dealer selling ~$20M a year of special-order windows and doors avoids ~$300,000–$500,000 of remake cost and weeks of job-site delay (estimate), and the specialist stops re-keying every package twice.
