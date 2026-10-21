# Rest of the Industries

The vault covers 298 of the 1012 official industries in the 2022 North American Industry Classification System (NAICS, US Census Bureau). The other 714 are listed below, by sector, for research. NAICS is the finest standard list in common use; the UN's global ISIC has about 460 classes and maps onto it.

## For the agent picking this up

- **Each row is an industry the vault does not have yet.** Add it the way existing industries are built: `industries/<slug>.md`, `problems/<slug>/` (7 files) and `niches/<slug>/` (an `_overview.md` plus sub-niches, each with `profile.md` and, where they qualify, `build.md`, `buy.md` and `fix.md`). Follow the templates in `CLAUDE.md` and `_context/formats/`.
- **Merge rows that share operators, buyers and workflows.** NAICS splits some trades very finely (for example, several separate crop and machinery codes). Where the work is the same, make one vault industry and record in its profile which NAICS codes it covers.
- **Check "Already covered" before adding anything,** and never edit an existing vault file. New work is additive.
- **Score each new industry on the three lenses** (`lenses/_method.md`) so it slots into the AI-proof, value clarity and digital nature rankings.
- **Coverage is judged by firm type.** A code counts as covered when a vault industry's typical firm would be classified under it, not when a vault industry sells to it. The vault's 181 covering industries are often finer than NAICS, so many digital vault industries share one code, such as 513210 Software Publishers.

## Remaining industries (714)

### 11 Agriculture, Forestry, Fishing and Hunting: 22 of 64 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 112511 | Finfish Farming and Fish Hatcheries | `finfish-farms` |
| 112512 | Shellfish Farming | `shellfish-farms` |
| 112519 | Other Aquaculture | `aquaculture-operations` |
| 112910 | Apiculture | `beekeeping-operations` |
| 112920 | Horses and Other Equine Production | `horse-breeding-farms` |
| 112930 | Fur-Bearing Animal and Rabbit Production | `fur-and-rabbit-farms` |
| 112990 | All Other Animal Production | `specialty-animal-farms` |
| 113110 | Timber Tract Operations | `timber-tract-operators` |
| 113210 | Forest Nurseries and Gathering of Forest Products | `forest-nurseries` |
| 113310 | Logging | `logging-companies` |
| 114111 | Finfish Fishing | `finfish-fishing-vessels` |
| 114112 | Shellfish Fishing | `shellfish-fishing-vessels` |
| 114119 | Other Marine Fishing | `marine-fishing-operations` |
| 114210 | Hunting and Trapping | `hunting-and-trapping-outfits` |
| 115111 | Cotton Ginning | `cotton-gins` |
| 115112 | Soil Preparation, Planting, and Cultivating | `soil-preparation-contractors` |
| 115113 | Crop Harvesting, Primarily by Machine | `custom-harvesting-crews` |
| 115114 | Postharvest Crop Activities (except Cotton Ginning) | `postharvest-processors` |
| 115115 | Farm Labor Contractors and Crew Leaders | `farm-labor-contractors` |
| 115116 | Farm Management Services | `farm-management-firms` |
| 115210 | Support Activities for Animal Production | `animal-production-support-services` |
| 115310 | Support Activities for Forestry | `forestry-support-services` |

### 21 Mining, Quarrying, and Oil and Gas Extraction: 19 of 21 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 211120 | Crude Petroleum Extraction | `crude-oil-producers` |
| 211130 | Natural Gas Extraction | `natural-gas-producers` |
| 212114 | Surface Coal Mining | `surface-coal-mines` |
| 212115 | Underground Coal Mining | `underground-coal-mines` |
| 212210 | Iron Ore Mining | `iron-ore-mines` |
| 212220 | Gold Ore and Silver Ore Mining | `gold-and-silver-mines` |
| 212230 | Copper, Nickel, Lead, and Zinc Mining | `base-metal-mines` |
| 212290 | Other Metal Ore Mining | `other-metal-mines` |
| 212311 | Dimension Stone Mining and Quarrying | `dimension-stone-quarries` |
| 212312 | Crushed and Broken Limestone Mining and Quarrying | `limestone-quarries` |
| 212313 | Crushed and Broken Granite Mining and Quarrying | `granite-quarries` |
| 212319 | Other Crushed and Broken Stone Mining and Quarrying | `crushed-stone-quarries` |
| 212321 | Construction Sand and Gravel Mining | `sand-and-gravel-pits` |
| 212322 | Industrial Sand Mining | `industrial-sand-miners` |
| 212323 | Kaolin, Clay, and Ceramic and Refractory Minerals Mining | `clay-and-ceramic-mineral-miners` |
| 212390 | Other Nonmetallic Mineral Mining and Quarrying | `nonmetallic-mineral-miners` |
| 213113 | Support Activities for Coal Mining | `coal-mining-support-services` |
| 213114 | Support Activities for Metal Mining | `metal-mining-support-services` |
| 213115 | Support Activities for Nonmetallic Minerals (except Fuels) Mining | `nonmetallic-mining-support-services` |

### 22 Utilities: 12 of 14 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 221111 | Hydroelectric Power Generation | `hydroelectric-plants` |
| 221112 | Fossil Fuel Electric Power Generation | `fossil-fuel-power-plants` |
| 221113 | Nuclear Electric Power Generation | `nuclear-power-plants` |
| 221114 | Solar Electric Power Generation | `solar-power-producers` |
| 221115 | Wind Electric Power Generation | `wind-farm-operators` |
| 221116 | Geothermal Electric Power Generation | `geothermal-power-plants` |
| 221117 | Biomass Electric Power Generation | `biomass-power-plants` |
| 221118 | Other Electric Power Generation | `other-power-generators` |
| 221121 | Electric Bulk Power Transmission and Control | `transmission-grid-operators` |
| 221122 | Electric Power Distribution | `electric-distribution-utilities` |
| 221210 | Natural Gas Distribution | `gas-distribution-utilities` |
| 221330 | Steam and Air-Conditioning Supply | `district-energy-suppliers` |

### 23 Construction: 18 of 31 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 237210 | Land Subdivision | `land-developers` |
| 237310 | Highway, Street, and Bridge Construction | `highway-and-bridge-contractors` |
| 237990 | Other Heavy and Civil Engineering Construction | `heavy-civil-contractors` |
| 238110 | Poured Concrete Foundation and Structure Contractors | `concrete-contractors` |
| 238120 | Structural Steel and Precast Concrete Contractors | `structural-steel-erectors` |
| 238130 | Framing Contractors | `framing-contractors` |
| 238140 | Masonry Contractors | `masonry-contractors` |
| 238150 | Glass and Glazing Contractors | `glazing-contractors` |
| 238170 | Siding Contractors | `siding-contractors` |
| 238190 | Other Foundation, Structure, and Building Exterior Contractors | `exterior-structure-contractors` |
| 238290 | Other Building Equipment Contractors | `building-equipment-installers` |
| 238310 | Drywall and Insulation Contractors | `drywall-and-insulation-contractors` |
| 238330 | Flooring Contractors | `flooring-contractors` |
| 238340 | Tile and Terrazzo Contractors | `tile-contractors` |
| 238350 | Finish Carpentry Contractors | `finish-carpentry-contractors` |
| 238390 | Other Building Finishing Contractors | `building-finishing-contractors` |
| 238910 | Site Preparation Contractors | `site-preparation-contractors` |
| 238990 | All Other Specialty Trade Contractors | `specialty-trade-contractors` |

### 31-33 Manufacturing: 272 of 346 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 311811 | Retail Bakeries | `retail-bakeries` |
| 312111 | Soft Drink Manufacturing | `soft-drink-bottlers` |
| 312112 | Bottled Water Manufacturing | `bottled-water-producers` |
| 312113 | Ice Manufacturing | `ice-manufacturers` |
| 312120 | Breweries | `breweries` |
| 312130 | Wineries | `wineries` |
| 312140 | Distilleries | `distilleries` |
| 312230 | Tobacco Manufacturing | `tobacco-manufacturers` |
| 313110 | Fiber, Yarn, and Thread Mills | `yarn-mills` |
| 313210 | Broadwoven Fabric Mills | `fabric-weaving-mills` |
| 313220 | Narrow Fabric Mills and Schiffli Machine Embroidery | `narrow-fabric-mills` |
| 313230 | Nonwoven Fabric Mills | `nonwoven-fabric-mills` |
| 313240 | Knit Fabric Mills | `knit-fabric-mills` |
| 313310 | Textile and Fabric Finishing Mills | `textile-finishers` |
| 313320 | Fabric Coating Mills | `fabric-coaters` |
| 314110 | Carpet and Rug Mills | `carpet-mills` |
| 314120 | Curtain and Linen Mills | `curtain-and-linen-makers` |
| 314910 | Textile Bag and Canvas Mills | `textile-bag-makers` |
| 314994 | Rope, Cordage, Twine, Tire Cord, and Tire Fabric Mills | `rope-and-cordage-makers` |
| 314999 | All Other Miscellaneous Textile Product Mills | `misc-textile-product-makers` |
| 315120 | Apparel Knitting Mills | `apparel-knitting-mills` |
| 315250 | Cut and Sew Apparel Manufacturing (except Contractors) | `apparel-manufacturers` |
| 315990 | Apparel Accessories and Other Apparel Manufacturing | `apparel-accessory-makers` |
| 316110 | Leather and Hide Tanning and Finishing | `tanneries` |
| 316210 | Footwear Manufacturing | `footwear-manufacturers` |
| 316990 | Other Leather and Allied Product Manufacturing | `leather-goods-makers` |
| 321113 | Sawmills | `sawmills` |
| 321114 | Wood Preservation | `wood-preservers` |
| 321211 | Hardwood Veneer and Plywood Manufacturing | `hardwood-veneer-plywood-manufacturing` |
| 321212 | Softwood Veneer and Plywood Manufacturing | `softwood-veneer-plywood-manufacturing` |
| 321215 | Engineered Wood Member Manufacturing | `engineered-wood-manufacturers` |
| 321219 | Reconstituted Wood Product Manufacturing | `reconstituted-wood-manufacturers` |
| 321911 | Wood Window and Door Manufacturing | `wood-window-door-makers` |
| 321912 | Cut Stock, Resawing Lumber, and Planing | `lumber-planing-mills` |
| 321918 | Other Millwork (including Flooring) | `millwork-and-flooring-makers` |
| 321920 | Wood Container and Pallet Manufacturing | `pallet-manufacturers` |
| 321991 | Manufactured Home (Mobile Home) Manufacturing | `manufactured-home-builders` |
| 321992 | Prefabricated Wood Building Manufacturing | `prefab-wood-building-makers` |
| 321999 | All Other Miscellaneous Wood Product Manufacturing | `misc-wood-product-makers` |
| 322110 | Pulp Mills | `pulp-mills` |
| 322120 | Paper Mills | `paper-mills` |
| 322130 | Paperboard Mills | `paperboard-mills` |
| 322211 | Corrugated and Solid Fiber Box Manufacturing | `corrugated-box-makers` |
| 322212 | Folding Paperboard Box Manufacturing | `folding-carton-makers` |
| 322219 | Other Paperboard Container Manufacturing | `paperboard-container-makers` |
| 322220 | Paper Bag and Coated and Treated Paper Manufacturing | `paper-bag-makers` |
| 322230 | Stationery Product Manufacturing | `stationery-manufacturers` |
| 322291 | Sanitary Paper Product Manufacturing | `tissue-and-sanitary-paper-makers` |
| 322299 | All Other Converted Paper Product Manufacturing | `converted-paper-manufacturers` |
| 324110 | Petroleum Refineries | `petroleum-refineries` |
| 324121 | Asphalt Paving Mixture and Block Manufacturing | `asphalt-plants` |
| 324122 | Asphalt Shingle and Coating Materials Manufacturing | `asphalt-shingle-manufacturers` |
| 324191 | Petroleum Lubricating Oil and Grease Manufacturing | `lubricant-blenders` |
| 324199 | All Other Petroleum and Coal Products Manufacturing | `petroleum-coal-product-makers` |
| 325110 | Petrochemical Manufacturing | `petrochemical-plants` |
| 325120 | Industrial Gas Manufacturing | `industrial-gas-producers` |
| 325130 | Synthetic Dye and Pigment Manufacturing | `dye-pigment-manufacturers` |
| 325180 | Other Basic Inorganic Chemical Manufacturing | `inorganic-chemical-plants` |
| 325193 | Ethyl Alcohol Manufacturing | `ethanol-plants` |
| 325194 | Cyclic Crude, Intermediate, and Gum and Wood Chemical Manufacturing | `gum-wood-chemical-makers` |
| 325199 | All Other Basic Organic Chemical Manufacturing | `organic-chemical-plants` |
| 325211 | Plastics Material and Resin Manufacturing | `resin-manufacturers` |
| 325212 | Synthetic Rubber Manufacturing | `synthetic-rubber-makers` |
| 325220 | Artificial and Synthetic Fibers and Filaments Manufacturing | `synthetic-fiber-makers` |
| 325311 | Nitrogenous Fertilizer Manufacturing | `nitrogen-fertilizer-plants` |
| 325312 | Phosphatic Fertilizer Manufacturing | `phosphate-fertilizer-plants` |
| 325314 | Fertilizer (Mixing Only) Manufacturing | `fertilizer-blenders` |
| 325315 | Compost Manufacturing | `compost-producers` |
| 325320 | Pesticide and Other Agricultural Chemical Manufacturing | `pesticide-manufacturers` |
| 325411 | Medicinal and Botanical Manufacturing | `botanical-drug-makers` |
| 325412 | Pharmaceutical Preparation Manufacturing | `pharmaceutical-manufacturers` |
| 325413 | In-Vitro Diagnostic Substance Manufacturing | `diagnostic-reagent-makers` |
| 325414 | Biological Product (except Diagnostic) Manufacturing | `biologics-manufacturers` |
| 325510 | Paint and Coating Manufacturing | `paint-manufacturers` |
| 325520 | Adhesive Manufacturing | `adhesive-manufacturers` |
| 325611 | Soap and Other Detergent Manufacturing | `soap-detergent-makers` |
| 325612 | Polish and Other Sanitation Good Manufacturing | `cleaning-product-makers` |
| 325613 | Surface Active Agent Manufacturing | `surfactant-makers` |
| 325620 | Toilet Preparation Manufacturing | `cosmetics-manufacturers` |
| 325910 | Printing Ink Manufacturing | `printing-ink-makers` |
| 325920 | Explosives Manufacturing | `explosives-manufacturers` |
| 325992 | Photographic Film, Paper, Plate, Chemical, and Copy Toner Manufacturing | `photo-chemical-and-toner-makers` |
| 325998 | All Other Miscellaneous Chemical Product and Preparation Manufacturing | `specialty-chemical-blenders` |
| 326111 | Plastics Bag and Pouch Manufacturing | `plastic-bag-makers` |
| 326112 | Plastics Packaging Film and Sheet (including Laminated) Manufacturing | `packaging-film-makers` |
| 326113 | Unlaminated Plastics Film and Sheet (except Packaging) Manufacturing | `plastic-film-extruders` |
| 326121 | Unlaminated Plastics Profile Shape Manufacturing | `plastic-profile-extruders` |
| 326122 | Plastics Pipe and Pipe Fitting Manufacturing | `plastic-pipe-manufacturers` |
| 326130 | Laminated Plastics Plate, Sheet (except Packaging), and Shape Manufacturing | `laminated-plastic-makers` |
| 326140 | Polystyrene Foam Product Manufacturing | `foam-packaging-makers` |
| 326150 | Urethane and Other Foam Product (except Polystyrene) Manufacturing | `urethane-foam-makers` |
| 326160 | Plastics Bottle Manufacturing | `plastic-bottle-makers` |
| 326191 | Plastics Plumbing Fixture Manufacturing | `plastic-fixture-makers` |
| 326199 | All Other Plastics Product Manufacturing | `plastic-product-molders` |
| 326211 | Tire Manufacturing (except Retreading) | `tire-manufacturers` |
| 326212 | Tire Retreading | `tire-retreaders` |
| 326220 | Rubber and Plastics Hoses and Belting Manufacturing | `rubber-hose-belt-makers` |
| 326291 | Rubber Product Manufacturing for Mechanical Use | `mechanical-rubber-makers` |
| 326299 | All Other Rubber Product Manufacturing | `rubber-product-makers` |
| 327110 | Pottery, Ceramics, and Plumbing Fixture Manufacturing | `ceramics-manufacturers` |
| 327120 | Clay Building Material and Refractories Manufacturing | `brick-and-refractory-makers` |
| 327211 | Flat Glass Manufacturing | `flat-glass-makers` |
| 327212 | Other Pressed and Blown Glass and Glassware Manufacturing | `glassware-manufacturers` |
| 327213 | Glass Container Manufacturing | `glass-container-makers` |
| 327215 | Glass Product Manufacturing Made of Purchased Glass | `glass-fabricators` |
| 327310 | Cement Manufacturing | `cement-plants` |
| 327320 | Ready-Mix Concrete Manufacturing | `ready-mix-concrete-plants` |
| 327331 | Concrete Block and Brick Manufacturing | `concrete-block-makers` |
| 327332 | Concrete Pipe Manufacturing | `concrete-pipe-makers` |
| 327390 | Other Concrete Product Manufacturing | `precast-concrete-makers` |
| 327410 | Lime Manufacturing | `lime-plants` |
| 327420 | Gypsum Product Manufacturing | `gypsum-product-makers` |
| 327910 | Abrasive Product Manufacturing | `abrasive-manufacturers` |
| 327991 | Cut Stone and Stone Product Manufacturing | `stone-fabricators` |
| 327992 | Ground or Treated Mineral and Earth Manufacturing | `ground-mineral-processors` |
| 327993 | Mineral Wool Manufacturing | `mineral-wool-makers` |
| 327999 | All Other Miscellaneous Nonmetallic Mineral Product Manufacturing | `nonmetallic-mineral-product-makers` |
| 331110 | Iron and Steel Mills and Ferroalloy Manufacturing | `steel-mills` |
| 331210 | Iron and Steel Pipe and Tube Manufacturing from Purchased Steel | `steel-pipe-mills` |
| 331221 | Rolled Steel Shape Manufacturing | `rolled-steel-shape-makers` |
| 331222 | Steel Wire Drawing | `steel-wire-drawers` |
| 331313 | Alumina Refining and Primary Aluminum Production | `aluminum-smelters` |
| 331314 | Secondary Smelting and Alloying of Aluminum | `aluminum-recyclers` |
| 331315 | Aluminum Sheet, Plate, and Foil Manufacturing | `aluminum-sheet-mills` |
| 331318 | Other Aluminum Rolling, Drawing, and Extruding | `aluminum-extruders` |
| 331410 | Nonferrous Metal (except Aluminum) Smelting and Refining | `nonferrous-smelters` |
| 331420 | Copper Rolling, Drawing, Extruding, and Alloying | `copper-mills` |
| 331491 | Nonferrous Metal (except Copper and Aluminum) Rolling, Drawing, and Extruding | `nonferrous-rolling-mills` |
| 331492 | Secondary Smelting, Refining, and Alloying of Nonferrous Metal (except Copper and Aluminum) | `nonferrous-metal-recyclers` |
| 331511 | Iron Foundries | `iron-foundries` |
| 331512 | Steel Investment Foundries | `investment-casting-foundries` |
| 331513 | Steel Foundries (except Investment) | `steel-foundries` |
| 331523 | Nonferrous Metal Die-Casting Foundries | `die-casting-foundries` |
| 331524 | Aluminum Foundries (except Die-Casting) | `aluminum-foundries` |
| 331529 | Other Nonferrous Metal Foundries (except Die-Casting) | `nonferrous-foundries` |
| 332111 | Iron and Steel Forging | `steel-forging-shops` |
| 332112 | Nonferrous Forging | `nonferrous-forging-shops` |
| 332117 | Powder Metallurgy Part Manufacturing | `powder-metallurgy-shops` |
| 332215 | Metal Kitchen Cookware, Utensil, Cutlery, and Flatware (except Precious) Manufacturing | `cookware-and-cutlery-makers` |
| 332216 | Saw Blade and Handtool Manufacturing | `handtool-makers` |
| 332431 | Metal Can Manufacturing | `metal-can-makers` |
| 332439 | Other Metal Container Manufacturing | `metal-container-makers` |
| 332510 | Hardware Manufacturing | `hardware-manufacturers` |
| 332722 | Bolt, Nut, Screw, Rivet, and Washer Manufacturing | `fastener-manufacturers` |
| 332911 | Industrial Valve Manufacturing | `industrial-valve-makers` |
| 332912 | Fluid Power Valve and Hose Fitting Manufacturing | `fluid-power-fitting-makers` |
| 332913 | Plumbing Fixture Fitting and Trim Manufacturing | `plumbing-fitting-makers` |
| 332919 | Other Metal Valve and Pipe Fitting Manufacturing | `valve-and-pipe-fitting-makers` |
| 332991 | Ball and Roller Bearing Manufacturing | `bearing-manufacturers` |
| 332992 | Small Arms Ammunition Manufacturing | `small-arms-ammo-makers` |
| 332993 | Ammunition (except Small Arms) Manufacturing | `ordnance-ammo-makers` |
| 332994 | Small Arms, Ordnance, and Ordnance Accessories Manufacturing | `firearms-manufacturers` |
| 333111 | Farm Machinery and Equipment Manufacturing | `farm-equipment-makers` |
| 333112 | Lawn and Garden Tractor and Home Lawn and Garden Equipment Manufacturing | `lawn-equipment-makers` |
| 333120 | Construction Machinery Manufacturing | `construction-equipment-makers` |
| 333131 | Mining Machinery and Equipment Manufacturing | `mining-equipment-makers` |
| 333132 | Oil and Gas Field Machinery and Equipment Manufacturing | `oilfield-equipment-makers` |
| 333241 | Food Product Machinery Manufacturing | `food-machinery-makers` |
| 333242 | Semiconductor Machinery Manufacturing | `semiconductor-equipment-makers` |
| 333243 | Sawmill, Woodworking, and Paper Machinery Manufacturing | `woodworking-machinery-makers` |
| 333248 | All Other Industrial Machinery Manufacturing | `industrial-machinery-makers` |
| 333310 | Commercial and Service Industry Machinery Manufacturing | `commercial-machinery-makers` |
| 333413 | Industrial and Commercial Fan and Blower and Air Purification Equipment Manufacturing | `fan-and-air-purifier-makers` |
| 333414 | Heating Equipment (except Warm Air Furnaces) Manufacturing | `heating-equipment-makers` |
| 333415 | Air-Conditioning and Warm Air Heating Equipment and Commercial and Industrial Refrigeration Equipment Manufacturing | `hvac-equipment-manufacturers` |
| 333511 | Industrial Mold Manufacturing | `mold-makers` |
| 333514 | Special Die and Tool, Die Set, Jig, and Fixture Manufacturing | `tool-and-die-shops` |
| 333515 | Cutting Tool and Machine Tool Accessory Manufacturing | `cutting-tool-makers` |
| 333517 | Machine Tool Manufacturing | `machine-tool-builders` |
| 333519 | Rolling Mill and Other Metalworking Machinery Manufacturing | `metalworking-machinery-makers` |
| 333611 | Turbine and Turbine Generator Set Units Manufacturing | `turbine-manufacturers` |
| 333612 | Speed Changer, Industrial High-Speed Drive, and Gear Manufacturing | `gear-manufacturers` |
| 333613 | Mechanical Power Transmission Equipment Manufacturing | `power-transmission-makers` |
| 333618 | Other Engine Equipment Manufacturing | `engine-manufacturers` |
| 333912 | Air and Gas Compressor Manufacturing | `compressor-manufacturers` |
| 333914 | Measuring, Dispensing, and Other Pumping Equipment Manufacturing | `pump-manufacturers` |
| 333921 | Elevator and Moving Stairway Manufacturing | `elevator-manufacturers` |
| 333922 | Conveyor and Conveying Equipment Manufacturing | `conveyor-manufacturers` |
| 333923 | Overhead Traveling Crane, Hoist, and Monorail System Manufacturing | `crane-and-hoist-makers` |
| 333924 | Industrial Truck, Tractor, Trailer, and Stacker Machinery Manufacturing | `forklift-manufacturers` |
| 333991 | Power-Driven Handtool Manufacturing | `power-tool-makers` |
| 333992 | Welding and Soldering Equipment Manufacturing | `welding-equipment-makers` |
| 333993 | Packaging Machinery Manufacturing | `packaging-machinery-makers` |
| 333994 | Industrial Process Furnace and Oven Manufacturing | `industrial-furnace-makers` |
| 333995 | Fluid Power Cylinder and Actuator Manufacturing | `hydraulic-cylinder-makers` |
| 333996 | Fluid Power Pump and Motor Manufacturing | `hydraulic-pump-makers` |
| 333998 | All Other Miscellaneous General Purpose Machinery Manufacturing | `general-machinery-makers` |
| 334111 | Electronic Computer Manufacturing | `computer-manufacturers` |
| 334112 | Computer Storage Device Manufacturing | `storage-device-makers` |
| 334118 | Computer Terminal and Other Computer Peripheral Equipment Manufacturing | `computer-peripheral-makers` |
| 334210 | Telephone Apparatus Manufacturing | `telephone-equipment-makers` |
| 334220 | Radio and Television Broadcasting and Wireless Communications Equipment Manufacturing | `wireless-equipment-makers` |
| 334290 | Other Communications Equipment Manufacturing | `communications-equipment-makers` |
| 334310 | Audio and Video Equipment Manufacturing | `audio-video-equipment-makers` |
| 334412 | Bare Printed Circuit Board Manufacturing | `pcb-fabricators` |
| 334413 | Semiconductor and Related Device Manufacturing | `semiconductor-fabs` |
| 334416 | Capacitor, Resistor, Coil, Transformer, and Other Inductor Manufacturing | `passive-component-makers` |
| 334417 | Electronic Connector Manufacturing | `connector-manufacturers` |
| 334419 | Other Electronic Component Manufacturing | `electronic-component-makers` |
| 334511 | Search, Detection, Navigation, Guidance, Aeronautical, and Nautical System and Instrument Manufacturing | `navigation-instrument-makers` |
| 334512 | Automatic Environmental Control Manufacturing for Residential, Commercial, and Appliance Use | `thermostat-and-controls-makers` |
| 334513 | Instruments and Related Products Manufacturing for Measuring, Displaying, and Controlling Industrial Process Variables | `process-instrument-makers` |
| 334514 | Totalizing Fluid Meter and Counting Device Manufacturing | `meter-manufacturers` |
| 334515 | Instrument Manufacturing for Measuring and Testing Electricity and Electrical Signals | `test-instrument-makers` |
| 334516 | Analytical Laboratory Instrument Manufacturing | `lab-instrument-makers` |
| 334519 | Other Measuring and Controlling Device Manufacturing | `measuring-device-makers` |
| 334610 | Manufacturing and Reproducing Magnetic and Optical Media | `media-duplicators` |
| 335131 | Residential Electric Lighting Fixture Manufacturing | `residential-lighting-makers` |
| 335132 | Commercial, Industrial, and Institutional Electric Lighting Fixture Manufacturing | `commercial-lighting-makers` |
| 335139 | Electric Lamp Bulb and Other Lighting Equipment Manufacturing | `lamp-and-bulb-makers` |
| 335210 | Small Electrical Appliance Manufacturing | `small-appliance-makers` |
| 335220 | Major Household Appliance Manufacturing | `major-appliance-makers` |
| 335311 | Power, Distribution, and Specialty Transformer Manufacturing | `transformer-manufacturers` |
| 335312 | Motor and Generator Manufacturing | `motor-and-generator-makers` |
| 335313 | Switchgear and Switchboard Apparatus Manufacturing | `switchgear-manufacturers` |
| 335314 | Relay and Industrial Control Manufacturing | `industrial-control-makers` |
| 335910 | Battery Manufacturing | `battery-manufacturers` |
| 335921 | Fiber Optic Cable Manufacturing | `fiber-optic-cable-makers` |
| 335929 | Other Communication and Energy Wire Manufacturing | `wire-and-cable-makers` |
| 335931 | Current-Carrying Wiring Device Manufacturing | `wiring-device-makers` |
| 335932 | Noncurrent-Carrying Wiring Device Manufacturing | `noncurrent-wiring-device-makers` |
| 335991 | Carbon and Graphite Product Manufacturing | `carbon-graphite-makers` |
| 335999 | All Other Miscellaneous Electrical Equipment and Component Manufacturing | `electrical-component-makers` |
| 336110 | Automobile and Light Duty Motor Vehicle Manufacturing | `automakers` |
| 336120 | Heavy Duty Truck Manufacturing | `heavy-truck-manufacturers` |
| 336211 | Motor Vehicle Body Manufacturing | `truck-body-builders` |
| 336212 | Truck Trailer Manufacturing | `trailer-manufacturers` |
| 336213 | Motor Home Manufacturing | `motor-home-builders` |
| 336214 | Travel Trailer and Camper Manufacturing | `travel-trailer-builders` |
| 336310 | Motor Vehicle Gasoline Engine and Engine Parts Manufacturing | `engine-parts-suppliers` |
| 336320 | Motor Vehicle Electrical and Electronic Equipment Manufacturing | `auto-electronics-suppliers` |
| 336330 | Motor Vehicle Steering and Suspension Components (except Spring) Manufacturing | `steering-suspension-suppliers` |
| 336340 | Motor Vehicle Brake System Manufacturing | `brake-system-suppliers` |
| 336350 | Motor Vehicle Transmission and Power Train Parts Manufacturing | `powertrain-parts-suppliers` |
| 336360 | Motor Vehicle Seating and Interior Trim Manufacturing | `auto-seating-suppliers` |
| 336370 | Motor Vehicle Metal Stamping | `auto-stamping-suppliers` |
| 336390 | Other Motor Vehicle Parts Manufacturing | `auto-parts-suppliers` |
| 336411 | Aircraft Manufacturing | `aircraft-manufacturers` |
| 336412 | Aircraft Engine and Engine Parts Manufacturing | `aircraft-engine-makers` |
| 336413 | Other Aircraft Parts and Auxiliary Equipment Manufacturing | `aircraft-parts-makers` |
| 336414 | Guided Missile and Space Vehicle Manufacturing | `space-vehicle-makers` |
| 336415 | Guided Missile and Space Vehicle Propulsion Unit and Propulsion Unit Parts Manufacturing | `rocket-propulsion-makers` |
| 336419 | Other Guided Missile and Space Vehicle Parts and Auxiliary Equipment Manufacturing | `missile-parts-makers` |
| 336510 | Railroad Rolling Stock Manufacturing | `railcar-manufacturers` |
| 336611 | Ship Building and Repairing | `shipyards` |
| 336612 | Boat Building | `boat-builders` |
| 336991 | Motorcycle, Bicycle, and Parts Manufacturing | `bicycle-and-motorcycle-makers` |
| 336992 | Military Armored Vehicle, Tank, and Tank Component Manufacturing | `armored-vehicle-makers` |
| 336999 | All Other Transportation Equipment Manufacturing | `transport-equipment-makers` |
| 337110 | Wood Kitchen Cabinet and Countertop Manufacturing | `kitchen-cabinet-makers` |
| 337121 | Upholstered Household Furniture Manufacturing | `upholstered-furniture-makers` |
| 337122 | Nonupholstered Wood Household Furniture Manufacturing | `wood-furniture-makers` |
| 337126 | Household Furniture (except Wood and Upholstered) Manufacturing | `metal-furniture-makers` |
| 337127 | Institutional Furniture Manufacturing | `institutional-furniture-makers` |
| 337211 | Wood Office Furniture Manufacturing | `wood-office-furniture-makers` |
| 337212 | Custom Architectural Woodwork and Millwork Manufacturing | `custom-millwork-shops` |
| 337214 | Office Furniture (except Wood) Manufacturing | `office-furniture-makers` |
| 337215 | Showcase, Partition, Shelving, and Locker Manufacturing | `shelving-and-locker-makers` |
| 337910 | Mattress Manufacturing | `mattress-manufacturers` |
| 337920 | Blind and Shade Manufacturing | `blind-and-shade-makers` |
| 339116 | Dental Laboratories | `dental-laboratories` |
| 339910 | Jewelry and Silverware Manufacturing | `jewelry-makers` |
| 339920 | Sporting and Athletic Goods Manufacturing | `sporting-goods-manufacturers` |
| 339930 | Doll, Toy, and Game Manufacturing | `toy-manufacturers` |
| 339940 | Office Supplies (except Paper) Manufacturing | `office-supply-makers` |
| 339950 | Sign Manufacturing | `sign-makers` |
| 339991 | Gasket, Packing, and Sealing Device Manufacturing | `gasket-and-seal-makers` |
| 339992 | Musical Instrument Manufacturing | `musical-instrument-makers` |
| 339993 | Fastener, Button, Needle, and Pin Manufacturing | `button-and-pin-makers` |
| 339994 | Broom, Brush, and Mop Manufacturing | `broom-and-brush-makers` |
| 339995 | Burial Casket Manufacturing | `casket-manufacturers` |
| 339999 | All Other Miscellaneous Manufacturing | `misc-manufacturers` |

### 42 Wholesale Trade: 59 of 69 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 423110 | Automobile and Other Motor Vehicle Merchant Wholesalers | `automobile-motor-vehicle-wholesalers` |
| 423120 | Motor Vehicle Supplies and New Parts Merchant Wholesalers | `motor-vehicle-supplies-new-parts` |
| 423130 | Tire and Tube Merchant Wholesalers | `tire-tube-wholesalers` |
| 423140 | Motor Vehicle Parts (Used) Merchant Wholesalers | `motor-vehicle-parts-used-wholesalers` |
| 423210 | Furniture Merchant Wholesalers | `furniture-wholesalers` |
| 423220 | Home Furnishing Merchant Wholesalers | `home-furnishing-wholesalers` |
| 423310 | Lumber, Plywood, Millwork, and Wood Panel Merchant Wholesalers | `lumber-plywood-millwork-wood-panel` |
| 423320 | Brick, Stone, and Related Construction Material Merchant Wholesalers | `brick-stone-construction-material-wholesalers` |
| 423330 | Roofing, Siding, and Insulation Material Merchant Wholesalers | `roofing-siding-insulation-material-wholesalers` |
| 423390 | Other Construction Material Merchant Wholesalers | `construction-material-wholesalers` |
| 423410 | Photographic Equipment and Supplies Merchant Wholesalers | `photographic-equipment-supplies-wholesalers` |
| 423420 | Office Equipment Merchant Wholesalers | `office-equipment-wholesalers` |
| 423430 | Computer and Computer Peripheral Equipment and Software Merchant Wholesalers | `computer-computer-peripheral-equipment-software` |
| 423440 | Other Commercial Equipment Merchant Wholesalers | `commercial-equipment-wholesalers` |
| 423450 | Medical, Dental, and Hospital Equipment and Supplies Merchant Wholesalers | `medical-dental-hospital-equipment-supplies` |
| 423460 | Ophthalmic Goods Merchant Wholesalers | `ophthalmic-goods-wholesalers` |
| 423490 | Other Professional Equipment and Supplies Merchant Wholesalers | `professional-equipment-supplies-wholesalers` |
| 423510 | Metal Service Centers and Other Metal Merchant Wholesalers | `metal-service-centers-metal-wholesalers` |
| 423520 | Coal and Other Mineral and Ore Merchant Wholesalers | `coal-mineral-ore-wholesalers` |
| 423610 | Electrical Apparatus and Equipment, Wiring Supplies, and Related Equipment Merchant Wholesalers | `electrical-apparatus-equipment-wiring-supplies` |
| 423620 | Household Appliances, Electric Housewares, and Consumer Electronics Merchant Wholesalers | `household-appliances-electric-housewares-consumer` |
| 423690 | Other Electronic Parts and Equipment Merchant Wholesalers | `electronic-parts-equipment-wholesalers` |
| 423710 | Hardware Merchant Wholesalers | `hardware-wholesalers` |
| 423720 | Plumbing and Heating Equipment and Supplies (Hydronics) Merchant Wholesalers | `plumbing-heating-equipment-supplies-hydronics` |
| 423730 | Warm Air Heating and Air-Conditioning Equipment and Supplies Merchant Wholesalers | `warm-air-heating-air-conditioning` |
| 423740 | Refrigeration Equipment and Supplies Merchant Wholesalers | `refrigeration-equipment-supplies-wholesalers` |
| 423810 | Construction and Mining (except Oil Well) Machinery and Equipment Merchant Wholesalers | `construction-mining-oil-well-machinery` |
| 423820 | Farm and Garden Machinery and Equipment Merchant Wholesalers | `farm-garden-machinery-equipment-wholesalers` |
| 423830 | Industrial Machinery and Equipment Merchant Wholesalers | `industrial-machinery-equipment-wholesalers` |
| 423840 | Industrial Supplies Merchant Wholesalers | `industrial-supplies-wholesalers` |
| 423860 | Transportation Equipment and Supplies (except Motor Vehicle) Merchant Wholesalers | `transportation-equipment-supplies-motor-vehicle` |
| 423910 | Sporting and Recreational Goods and Supplies Merchant Wholesalers | `sporting-recreational-goods-supplies-wholesalers` |
| 423920 | Toy and Hobby Goods and Supplies Merchant Wholesalers | `toy-hobby-goods-supplies-wholesalers` |
| 423930 | Recyclable Material Merchant Wholesalers | `recyclable-material-wholesalers` |
| 423940 | Jewelry, Watch, Precious Stone, and Precious Metal Merchant Wholesalers | `jewelry-watch-precious-stone-precious` |
| 423990 | Other Miscellaneous Durable Goods Merchant Wholesalers | `miscellaneous-durable-goods-wholesalers` |
| 424110 | Printing and Writing Paper Merchant Wholesalers | `printing-writing-paper-wholesalers` |
| 424120 | Stationery and Office Supplies Merchant Wholesalers | `stationery-office-supplies-wholesalers` |
| 424130 | Industrial and Personal Service Paper Merchant Wholesalers | `industrial-personal-service-paper-wholesalers` |
| 424210 | Drugs and Druggists' Sundries Merchant Wholesalers | `drugs-druggists-sundries-wholesalers` |
| 424310 | Piece Goods, Notions, and Other Dry Goods Merchant Wholesalers | `piece-goods-notions-dry-goods` |
| 424340 | Footwear Merchant Wholesalers | `footwear-wholesalers` |
| 424350 | Clothing and Clothing Accessories Merchant Wholesalers | `clothing-clothing-accessories-wholesalers` |
| 424510 | Grain and Field Bean Merchant Wholesalers | `grain-field-bean-wholesalers` |
| 424520 | Livestock Merchant Wholesalers | `livestock-wholesalers` |
| 424590 | Other Farm Product Raw Material Merchant Wholesalers | `farm-product-raw-material-wholesalers` |
| 424610 | Plastics Materials and Basic Forms and Shapes Merchant Wholesalers | `plastics-materials-basic-forms-shapes` |
| 424690 | Other Chemical and Allied Products Merchant Wholesalers | `chemical-allied-products-wholesalers` |
| 424710 | Petroleum Bulk Stations and Terminals | `petroleum-bulk-stations-terminals` |
| 424720 | Petroleum and Petroleum Products Merchant Wholesalers (except Bulk Stations and Terminals) | `petroleum-petroleum-products-wholesalers-bulk` |
| 424810 | Beer and Ale Merchant Wholesalers | `beer-ale-wholesalers` |
| 424820 | Wine and Distilled Alcoholic Beverage Merchant Wholesalers | `wine-distilled-alcoholic-beverage-wholesalers` |
| 424910 | Farm Supplies Merchant Wholesalers | `farm-supplies-wholesalers` |
| 424920 | Book, Periodical, and Newspaper Merchant Wholesalers | `book-periodical-newspaper-wholesalers` |
| 424930 | Flower, Nursery Stock, and Florists' Supplies Merchant Wholesalers | `flower-nursery-stock-florists-supplies` |
| 424940 | Tobacco Product and Electronic Cigarette Merchant Wholesalers | `tobacco-product-electronic-cigarette-wholesalers` |
| 424950 | Paint, Varnish, and Supplies Merchant Wholesalers | `paint-varnish-supplies-wholesalers` |
| 424990 | Other Miscellaneous Nondurable Goods Merchant Wholesalers | `miscellaneous-nondurable-goods-wholesalers` |
| 425120 | Wholesale Trade Agents and Brokers | `wholesale-trade-agents-brokers` |

### 44-45 Retail Trade: 44 of 57 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 441110 | New Car Dealers | `new-car-dealers` |
| 441222 | Boat Dealers | `boat-dealers` |
| 441227 | Motorcycle, ATV, and All Other Motor Vehicle Dealers | `motorcycle-atv-motor-vehicle-dealers` |
| 441330 | Automotive Parts and Accessories Retailers | `automotive-parts-accessories-retailers` |
| 441340 | Tire Dealers | `tire-dealers` |
| 444110 | Home Centers | `home-centers` |
| 444120 | Paint and Wallpaper Retailers | `paint-wallpaper-retailers` |
| 444140 | Hardware Retailers | `hardware-retailers` |
| 444180 | Other Building Material Dealers | `building-material-dealers` |
| 444230 | Outdoor Power Equipment Retailers | `outdoor-power-equipment-retailers` |
| 444240 | Nursery, Garden Center, and Farm Supply Retailers | `nursery-garden-center-farm-supply` |
| 445110 | Supermarkets and Other Grocery Retailers (except Convenience Retailers) | `supermarkets-grocery-retailers-convenience-retailers` |
| 445131 | Convenience Retailers | `convenience-retailers` |
| 445132 | Vending Machine Operators | `vending-machine-operators` |
| 445320 | Beer, Wine, and Liquor Retailers | `beer-wine-liquor-retailers` |
| 449110 | Furniture Retailers | `furniture-retailers` |
| 449121 | Floor Covering Retailers | `floor-covering-retailers` |
| 449122 | Window Treatment Retailers | `window-treatment-retailers` |
| 449129 | All Other Home Furnishings Retailers | `home-furnishings-retailers` |
| 449210 | Electronics and Appliance Retailers | `electronics-appliance-retailers` |
| 455110 | Department Stores | `department-stores` |
| 455211 | Warehouse Clubs and Supercenters | `warehouse-clubs-supercenters` |
| 455219 | All Other General Merchandise Retailers | `general-merchandise-retailers` |
| 456120 | Cosmetics, Beauty Supplies, and Perfume Retailers | `cosmetics-beauty-supplies-perfume-retailers` |
| 456130 | Optical Goods Retailers | `optical-goods-retailers` |
| 456191 | Food (Health) Supplement Retailers | `food-health-supplement-retailers` |
| 457110 | Gasoline Stations with Convenience Stores | `gasoline-stations-with-convenience-stores` |
| 457120 | Other Gasoline Stations | `gasoline-stations` |
| 457210 | Fuel Dealers | `fuel-dealers` |
| 458210 | Shoe Retailers | `shoe-retailers` |
| 458310 | Jewelry Retailers | `jewelry-retailers` |
| 458320 | Luggage and Leather Goods Retailers | `luggage-leather-goods-retailers` |
| 459110 | Sporting Goods Retailers | `sporting-goods-retailers` |
| 459120 | Hobby, Toy, and Game Retailers | `hobby-toy-game-retailers` |
| 459130 | Sewing, Needlework, and Piece Goods Retailers | `sewing-needlework-piece-goods-retailers` |
| 459140 | Musical Instrument and Supplies Retailers | `musical-instrument-supplies-retailers` |
| 459210 | Book Retailers and News Dealers | `book-retailers-news-dealers` |
| 459310 | Florists | `florists` |
| 459410 | Office Supplies and Stationery Retailers | `office-supplies-stationery-retailers` |
| 459510 | Used Merchandise Retailers | `used-merchandise-retailers` |
| 459910 | Pet and Pet Supplies Retailers | `pet-pet-supplies-retailers` |
| 459920 | Art Dealers | `art-dealers` |
| 459930 | Manufactured (Mobile) Home Dealers | `manufactured-mobile-home-dealers` |
| 459991 | Tobacco, Electronic Cigarette, and Other Smoking Supplies Retailers | `tobacco-electronic-cigarette-smoking-supplies` |

### 48-49 Transportation and Warehousing: 40 of 57 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 481111 | Scheduled Passenger Air Transportation | `scheduled-passenger-air-transportation` |
| 481112 | Scheduled Freight Air Transportation | `scheduled-freight-air-transportation` |
| 481211 | Nonscheduled Chartered Passenger Air Transportation | `nonscheduled-chartered-passenger-air-transportation` |
| 481212 | Nonscheduled Chartered Freight Air Transportation | `nonscheduled-chartered-freight-air-transportation` |
| 481219 | Other Nonscheduled Air Transportation | `nonscheduled-air-transportation` |
| 482111 | Line-Haul Railroads | `line-haul-railroads` |
| 482112 | Short Line Railroads | `short-line-railroads` |
| 483111 | Deep Sea Freight Transportation | `deep-sea-freight-transportation` |
| 483112 | Deep Sea Passenger Transportation | `deep-sea-passenger-transportation` |
| 483113 | Coastal and Great Lakes Freight Transportation | `coastal-great-lakes-freight-transportation` |
| 483114 | Coastal and Great Lakes Passenger Transportation | `coastal-great-lakes-passenger-transportation` |
| 483211 | Inland Water Freight Transportation | `inland-water-freight-transportation` |
| 483212 | Inland Water Passenger Transportation | `inland-water-passenger-transportation` |
| 484122 | General Freight Trucking, Long-Distance, Less Than Truckload | `general-freight-trucking-long-distance` |
| 485111 | Mixed Mode Transit Systems | `mixed-mode-transit-systems` |
| 485112 | Commuter Rail Systems | `commuter-rail-systems` |
| 485119 | Other Urban Transit Systems | `urban-transit-systems` |
| 485210 | Interurban and Rural Bus Transportation | `interurban-rural-bus-transportation` |
| 485410 | School and Employee Bus Transportation | `school-employee-bus-transportation` |
| 485999 | All Other Transit and Ground Passenger Transportation | `transit-ground-passenger-transportation` |
| 486110 | Pipeline Transportation of Crude Oil | `pipeline-transportation-crude-oil` |
| 486210 | Pipeline Transportation of Natural Gas | `pipeline-transportation-natural-gas` |
| 486910 | Pipeline Transportation of Refined Petroleum Products | `pipeline-transportation-refined-petroleum-products` |
| 486990 | All Other Pipeline Transportation | `pipeline-transportation` |
| 487110 | Scenic and Sightseeing Transportation, Land | `scenic-sightseeing-transportation-land` |
| 487210 | Scenic and Sightseeing Transportation, Water | `scenic-sightseeing-transportation-water` |
| 487990 | Scenic and Sightseeing Transportation, Other | `scenic-sightseeing-transportation` |
| 488111 | Air Traffic Control | `air-traffic-control` |
| 488119 | Other Airport Operations | `airport-operations` |
| 488190 | Other Support Activities for Air Transportation | `support-activities-air-transportation` |
| 488210 | Support Activities for Rail Transportation | `support-activities-rail-transportation` |
| 488310 | Port and Harbor Operations | `port-harbor-operations` |
| 488320 | Marine Cargo Handling | `marine-cargo-handling` |
| 488330 | Navigational Services to Shipping | `navigational-services-to-shipping` |
| 488390 | Other Support Activities for Water Transportation | `support-activities-water-transportation` |
| 488490 | Other Support Activities for Road Transportation | `support-activities-road-transportation` |
| 488991 | Packing and Crating | `packing-crating` |
| 488999 | All Other Support Activities for Transportation | `support-activities-for-transportation` |
| 491110 | Postal Service | `postal-service` |
| 493130 | Farm Product Warehousing and Storage | `farm-product-warehousing-storage` |

### 51 Information: 19 of 29 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 512120 | Motion Picture and Video Distribution | `film-distributors` |
| 512131 | Motion Picture Theaters (except Drive-Ins) | `movie-theaters` |
| 512132 | Drive-In Motion Picture Theaters | `drive-in-theaters` |
| 512191 | Teleproduction and Other Postproduction Services | `postproduction-studios` |
| 512199 | Other Motion Picture and Video Industries | `film-archives-and-stock-footage` |
| 512230 | Music Publishers | `music-publishers` |
| 512240 | Sound Recording Studios | `recording-studios` |
| 512290 | Other Sound Recording Industries | `audio-production-services` |
| 513140 | Directory and Mailing List Publishers | `directory-publishers` |
| 513191 | Greeting Card Publishers | `greeting-card-publishers` |
| 516110 | Radio Broadcasting Stations | `radio-stations` |
| 516120 | Television Broadcasting Stations | `television-stations` |
| 517111 | Wired Telecommunications Carriers | `wired-telecom-carriers` |
| 517112 | Wireless Telecommunications Carriers (except Satellite) | `wireless-carriers` |
| 517121 | Telecommunications Resellers | `telecom-resellers` |
| 517122 | Agents for Wireless Telecommunications Services | `wireless-retail-agents` |
| 517410 | Satellite Telecommunications | `satellite-operators` |
| 517810 | All Other Telecommunications | `telecom-service-providers` |
| 519210 | Libraries and Archives | `libraries-and-archives` |

### 52 Finance and Insurance: 20 of 35 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 521110 | Monetary Authorities-Central Bank | `central-banks` |
| 522110 | Commercial Banking | `commercial-banks` |
| 522180 | Savings Institutions and Other Depository Credit Intermediation | `savings-institutions` |
| 522210 | Credit Card Issuing | `credit-card-issuers` |
| 522220 | Sales Financing | `sales-finance-companies` |
| 522292 | Real Estate Credit | `real-estate-lenders` |
| 522299 | International, Secondary Market, and All Other Nondepository Credit Intermediation | `secondary-market-lenders` |
| 522390 | Other Activities Related to Credit Intermediation | `credit-intermediation-services` |
| 523160 | Commodity Contracts Intermediation | `commodity-brokers` |
| 523991 | Trust, Fiduciary, and Custody Activities | `trust-and-custody-banks` |
| 524113 | Direct Life Insurance Carriers | `life-insurance-carriers` |
| 524114 | Direct Health and Medical Insurance Carriers | `health-insurance-carriers` |
| 524126 | Direct Property and Casualty Insurance Carriers | `property-casualty-insurers` |
| 524127 | Direct Title Insurance Carriers | `title-insurance-carriers` |
| 524128 | Other Direct Insurance (except Life, Health, and Medical) Carriers | `specialty-insurance-carriers` |
| 524130 | Reinsurance Carriers | `reinsurers` |
| 525110 | Pension Funds | `pension-funds` |
| 525120 | Health and Welfare Funds | `health-and-welfare-funds` |
| 525190 | Other Insurance Funds | `insurance-funds` |
| 525920 | Trusts, Estates, and Agency Accounts | `trusts-and-agency-accounts` |

### 53 Real Estate and Rental and Leasing: 16 of 24 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 531130 | Lessors of Miniwarehouses and Self-Storage Units | `self-storage-operators` |
| 532111 | Passenger Car Rental | `car-rental-companies` |
| 532112 | Passenger Car Leasing | `car-leasing-companies` |
| 532120 | Truck, Utility Trailer, and RV (Recreational Vehicle) Rental and Leasing | `truck-and-rv-rental` |
| 532210 | Consumer Electronics and Appliances Rental | `electronics-rental-companies` |
| 532281 | Formal Wear and Costume Rental | `formal-wear-rental` |
| 532282 | Video Tape and Disc Rental | `video-rental-stores` |
| 532283 | Home Health Equipment Rental | `home-medical-equipment-rental` |
| 532284 | Recreational Goods Rental | `recreational-equipment-rental` |
| 532289 | All Other Consumer Goods Rental | `consumer-goods-rental` |
| 532310 | General Rental Centers | `general-rental-centers` |
| 532411 | Commercial Air, Rail, and Water Transportation Equipment Rental and Leasing | `aircraft-and-rail-leasing` |
| 532412 | Construction, Mining, and Forestry Machinery and Equipment Rental and Leasing | `construction-equipment-rental` |
| 532420 | Office Machinery and Equipment Rental and Leasing | `office-equipment-leasing` |
| 532490 | Other Commercial and Industrial Machinery and Equipment Rental and Leasing | `industrial-equipment-leasing` |
| 533110 | Lessors of Nonfinancial Intangible Assets (except Copyrighted Works) | `intellectual-property-licensors` |

### 54 Professional, Scientific, and Technical Services: 23 of 49 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 541120 | Offices of Notaries | `notaries` |
| 541191 | Title Abstract and Settlement Offices | `title-and-settlement-offices` |
| 541199 | All Other Legal Services | `legal-support-services` |
| 541214 | Payroll Services | `payroll-service-bureaus` |
| 541310 | Architectural Services | `architecture-firms` |
| 541320 | Landscape Architectural Services | `landscape-architecture-firms` |
| 541340 | Drafting Services | `drafting-services` |
| 541360 | Geophysical Surveying and Mapping Services | `geophysical-survey-firms` |
| 541380 | Testing Laboratories and Services | `testing-laboratories` |
| 541410 | Interior Design Services | `interior-design-firms` |
| 541430 | Graphic Design Services | `graphic-design-studios` |
| 541490 | Other Specialized Design Services | `specialty-design-studios` |
| 541614 | Process, Physical Distribution, and Logistics Consulting Services | `logistics-consultants` |
| 541713 | Research and Development in Nanotechnology | `nanotechnology-labs` |
| 541714 | Research and Development in Biotechnology (except Nanobiotechnology) | `biotech-research-labs` |
| 541715 | Research and Development in the Physical, Engineering, and Life Sciences (except Nanotechnology and Biotechnology) | `physical-and-life-science-labs` |
| 541820 | Public Relations Agencies | `public-relations-agencies` |
| 541840 | Media Representatives | `media-representatives` |
| 541850 | Indoor and Outdoor Display Advertising | `outdoor-advertising-companies` |
| 541860 | Direct Mail Advertising | `direct-mail-agencies` |
| 541870 | Advertising Material Distribution Services | `ad-material-distributors` |
| 541921 | Photography Studios, Portrait | `portrait-photography-studios` |
| 541922 | Commercial Photography | `commercial-photographers` |

### 55 Management of Companies and Enterprises: 3 of 3 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 551111 | Offices of Bank Holding Companies | `bank-holding-companies` |
| 551112 | Offices of Other Holding Companies | `holding-companies` |
| 551114 | Corporate, Subsidiary, and Regional Managing Offices | `corporate-headquarters` |

### 56 Administrative and Support and Waste Management and Remediation Services: 29 of 44 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 561210 | Facilities Support Services | `facilities-support-services` |
| 561312 | Executive Search Services | `executive-search-firms` |
| 561330 | Professional Employer Organizations | `professional-employer-organizations` |
| 561410 | Document Preparation Services | `document-preparation-services` |
| 561421 | Telephone Answering Services | `answering-services` |
| 561431 | Private Mail Centers | `private-mail-centers` |
| 561450 | Credit Bureaus | `credit-bureaus` |
| 561491 | Repossession Services | `repossession-services` |
| 561492 | Court Reporting and Stenotype Services | `court-reporting-firms` |
| 561510 | Travel Agencies | `travel-agencies` |
| 561520 | Tour Operators | `tour-operators` |
| 561591 | Convention and Visitors Bureaus | `visitors-bureaus` |
| 561599 | All Other Travel Arrangement and Reservation Services | `travel-reservation-services` |
| 561611 | Investigation and Personal Background Check Services | `private-investigation-firms` |
| 561613 | Armored Car Services | `armored-car-services` |
| 561621 | Security Systems Services (except Locksmiths) | `security-system-installers` |
| 561622 | Locksmiths | `locksmiths` |
| 561910 | Packaging and Labeling Services | `packaging-and-labeling-services` |
| 561990 | All Other Support Services | `misc-business-support-services` |
| 562111 | Solid Waste Collection | `waste-haulers` |
| 562112 | Hazardous Waste Collection | `hazardous-waste-collectors` |
| 562119 | Other Waste Collection | `other-waste-collectors` |
| 562211 | Hazardous Waste Treatment and Disposal | `hazardous-waste-facilities` |
| 562212 | Solid Waste Landfill | `landfill-operators` |
| 562213 | Solid Waste Combustors and Incinerators | `waste-incinerators` |
| 562219 | Other Nonhazardous Waste Treatment and Disposal | `waste-treatment-facilities` |
| 562920 | Materials Recovery Facilities | `recycling-facilities` |
| 562991 | Septic Tank and Related Services | `septic-service-companies` |
| 562998 | All Other Miscellaneous Waste Management Services | `misc-waste-management-services` |

### 61 Educational Services: 10 of 17 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 611210 | Junior Colleges | `community-colleges` |
| 611310 | Colleges, Universities, and Professional Schools | `colleges-universities` |
| 611410 | Business and Secretarial Schools | `business-secretarial-schools` |
| 611420 | Computer Training | `computer-training-schools` |
| 611512 | Flight Training | `flight-schools` |
| 611610 | Fine Arts Schools | `fine-arts-schools` |
| 611620 | Sports and Recreation Instruction | `sports-instruction-schools` |
| 611692 | Automobile Driving Schools | `driving-schools` |
| 611699 | All Other Miscellaneous Schools and Instruction | `specialty-instruction-schools` |
| 611710 | Educational Support Services | `educational-support-services` |

### 62 Health Care and Social Assistance: 21 of 39 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 621111 | Offices of Physicians (except Mental Health Specialists) | `physician-practices` |
| 621320 | Offices of Optometrists | `optometry-practices` |
| 621391 | Offices of Podiatrists | `podiatry-practices` |
| 621410 | Family Planning Centers | `family-planning-centers` |
| 621491 | HMO Medical Centers | `hmo-medical-centers` |
| 621492 | Kidney Dialysis Centers | `dialysis-centers` |
| 621498 | All Other Outpatient Care Centers | `outpatient-care-centers-other` |
| 621511 | Medical Laboratories | `medical-laboratories` |
| 621512 | Diagnostic Imaging Centers | `diagnostic-imaging-centers` |
| 621910 | Ambulance Services | `ambulance-services` |
| 621991 | Blood and Organ Banks | `blood-organ-banks` |
| 621999 | All Other Miscellaneous Ambulatory Health Care Services | `ambulatory-health-services-other` |
| 622110 | General Medical and Surgical Hospitals | `hospitals-general` |
| 622210 | Psychiatric and Substance Abuse Hospitals | `psychiatric-hospitals` |
| 622310 | Specialty (except Psychiatric and Substance Abuse) Hospitals | `specialty-hospitals` |
| 623110 | Nursing Care Facilities (Skilled Nursing Facilities) | `nursing-homes` |
| 623210 | Residential Intellectual and Developmental Disability Facilities | `developmental-disability-residential-facilities` |
| 623220 | Residential Mental Health and Substance Abuse Facilities | `residential-treatment-centers` |
| 623311 | Continuing Care Retirement Communities | `continuing-care-retirement-communities` |
| 623312 | Assisted Living Facilities for the Elderly | `assisted-living-facilities` |
| 623990 | Other Residential Care Facilities | `group-homes` |

### 71 Arts, Entertainment, and Recreation: 22 of 25 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 711110 | Theater Companies and Dinner Theaters | `theater-companies` |
| 711120 | Dance Companies | `dance-companies` |
| 711130 | Musical Groups and Artists | `musical-groups` |
| 711190 | Other Performing Arts Companies | `performing-arts-companies-other` |
| 711211 | Sports Teams and Clubs | `sports-teams` |
| 711212 | Racetracks | `racetracks` |
| 711219 | Other Spectator Sports | `spectator-sports-other` |
| 711310 | Promoters of Performing Arts, Sports, and Similar Events with Facilities | `venue-event-promoters` |
| 711320 | Promoters of Performing Arts, Sports, and Similar Events without Facilities | `event-promoters` |
| 712110 | Museums | `museums` |
| 712120 | Historical Sites | `historical-sites` |
| 712130 | Zoos and Botanical Gardens | `zoos-botanical-gardens` |
| 712190 | Nature Parks and Other Similar Institutions | `nature-parks` |
| 713110 | Amusement and Theme Parks | `theme-parks` |
| 713120 | Amusement Arcades | `amusement-arcades` |
| 713210 | Casinos (except Casino Hotels) | `casinos` |
| 713290 | Other Gambling Industries | `gambling-operators-other` |
| 713910 | Golf Courses and Country Clubs | `golf-clubs` |
| 713920 | Skiing Facilities | `ski-resorts` |
| 713930 | Marinas | `marinas` |
| 713950 | Bowling Centers | `bowling-centers` |
| 713990 | All Other Amusement and Recreation Industries | `recreation-businesses-other` |

### 72 Accommodation and Food Services: 8 of 15 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 721120 | Casino Hotels | `casino-hotels` |
| 721191 | Bed-and-Breakfast Inns | `bed-and-breakfasts` |
| 721211 | RV (Recreational Vehicle) Parks and Campgrounds | `rv-parks-campgrounds` |
| 721214 | Recreational and Vacation Camps (except Campgrounds) | `recreational-camps` |
| 721310 | Rooming and Boarding Houses, Dormitories, and Workers' Camps | `rooming-houses-workers-camps` |
| 722310 | Food Service Contractors | `food-service-contractors` |
| 722410 | Drinking Places (Alcoholic Beverages) | `bars-taverns` |
| 722514 | Cafeterias, Grill Buffets, and Buffets | `cafeterias-buffets` |

### 81 Other Services (except Public Administration): 33 of 44 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 811122 | Automotive Glass Replacement Shops | `auto-glass-shops` |
| 811191 | Automotive Oil Change and Lubrication Shops | `oil-change-shops` |
| 811192 | Car Washes | `car-washes` |
| 811198 | All Other Automotive Repair and Maintenance | `tire-and-exhaust-shops` |
| 811210 | Electronic and Precision Equipment Repair and Maintenance | `electronics-repair-shops` |
| 811310 | Commercial and Industrial Machinery and Equipment (except Automotive and Electronic) Repair and Maintenance | `industrial-machinery-repair` |
| 811411 | Home and Garden Equipment Repair and Maintenance | `small-engine-repair` |
| 811412 | Appliance Repair and Maintenance | `appliance-repair` |
| 811420 | Reupholstery and Furniture Repair | `upholstery-repair` |
| 811430 | Footwear and Leather Goods Repair | `footwear-repair` |
| 812113 | Nail Salons | `nail-salons` |
| 812191 | Diet and Weight Reducing Centers | `weight-loss-centers` |
| 812220 | Cemeteries and Crematories | `cemeteries-crematories` |
| 812310 | Coin-Operated Laundries and Drycleaners | `laundromats` |
| 812320 | Drycleaning and Laundry Services (except Coin-Operated) | `drycleaners` |
| 812331 | Linen Supply | `linen-supply` |
| 812332 | Industrial Launderers | `industrial-launderers` |
| 812921 | Photofinishing Laboratories (except One-Hour) | `photofinishing-labs` |
| 812922 | One-Hour Photofinishing | `one-hour-photofinishing` |
| 812930 | Parking Lots and Garages | `parking-operators` |
| 812990 | All Other Personal Services | `personal-services-other` |
| 813211 | Grantmaking Foundations | `grantmaking-foundations` |
| 813212 | Voluntary Health Organizations | `voluntary-health-organizations` |
| 813219 | Other Grantmaking and Giving Services | `charitable-giving-organizations` |
| 813311 | Human Rights Organizations | `human-rights-organizations` |
| 813312 | Environment, Conservation and Wildlife Organizations | `conservation-organizations` |
| 813319 | Other Social Advocacy Organizations | `advocacy-organizations` |
| 813410 | Civic and Social Organizations | `civic-social-clubs` |
| 813920 | Professional Organizations | `professional-associations` |
| 813930 | Labor Unions and Similar Labor Organizations | `labor-unions` |
| 813940 | Political Organizations | `political-organizations` |
| 813990 | Other Similar Organizations (except Business, Professional, Labor, and Political Organizations) | `membership-organizations-other` |
| 814110 | Private Households | `private-households` |

### 92 Public Administration: 24 of 29 remaining

| NAICS | Industry | Suggested slug |
| --- | --- | --- |
| 921110 | Executive Offices | `executive-government-offices` |
| 921120 | Legislative Bodies | `legislative-bodies` |
| 921130 | Public Finance Activities | `public-finance-agencies` |
| 921140 | Executive and Legislative Offices, Combined | `executive-legislative-offices` |
| 921150 | American Indian and Alaska Native Tribal Governments | `tribal-governments` |
| 922110 | Courts | `courts` |
| 922140 | Correctional Institutions | `correctional-institutions` |
| 922150 | Parole Offices and Probation Offices | `parole-probation-offices` |
| 922190 | Other Justice, Public Order, and Safety Activities | `public-safety-agencies-other` |
| 923110 | Administration of Education Programs | `education-program-agencies` |
| 923120 | Administration of Public Health Programs | `public-health-agencies` |
| 923130 | Administration of Human Resource Programs (except Education, Public Health, and Veterans' Affairs Programs) | `human-resource-program-agencies` |
| 923140 | Administration of Veterans' Affairs | `veterans-affairs-agencies` |
| 924110 | Administration of Air and Water Resource and Solid Waste Management Programs | `environmental-program-agencies` |
| 924120 | Administration of Conservation Programs | `conservation-agencies` |
| 925110 | Administration of Housing Programs | `housing-agencies` |
| 926110 | Administration of General Economic Programs | `economic-program-agencies` |
| 926120 | Regulation and Administration of Transportation Programs | `transportation-regulators` |
| 926130 | Regulation and Administration of Communications, Electric, Gas, and Other Utilities | `utility-regulators` |
| 926140 | Regulation of Agricultural Marketing and Commodities | `agricultural-commodity-regulators` |
| 926150 | Regulation, Licensing, and Inspection of Miscellaneous Commercial Sectors | `commercial-licensing-agencies` |
| 927110 | Space Research and Technology | `space-research-agencies` |
| 928110 | National Security | `national-security-agencies` |
| 928120 | International Affairs | `international-affairs-agencies` |

## Already covered (298)

| NAICS | Industry | Covered by |
| --- | --- | --- |
| 111110 | Soybean Farming | [[industries/crop-farming|Crop Farming]] |
| 111120 | Oilseed (except Soybean) Farming | [[industries/crop-farming|Crop Farming]] |
| 111130 | Dry Pea and Bean Farming | [[industries/crop-farming|Crop Farming]] |
| 111140 | Wheat Farming | [[industries/crop-farming|Crop Farming]] |
| 111150 | Corn Farming | [[industries/crop-farming|Crop Farming]] |
| 111160 | Rice Farming | [[industries/crop-farming|Crop Farming]] |
| 111191 | Oilseed and Grain Combination Farming | [[industries/crop-farming|Crop Farming]] |
| 111199 | All Other Grain Farming | [[industries/crop-farming|Crop Farming]] |
| 111211 | Potato Farming | [[industries/crop-farming|Crop Farming]] |
| 111219 | Other Vegetable (except Potato) and Melon Farming | [[industries/crop-farming|Crop Farming]] |
| 111310 | Orange Groves | [[industries/crop-farming|Crop Farming]] |
| 111320 | Citrus (except Orange) Groves | [[industries/crop-farming|Crop Farming]] |
| 111331 | Apple Orchards | [[industries/crop-farming|Crop Farming]] |
| 111332 | Grape Vineyards | [[industries/crop-farming|Crop Farming]] |
| 111333 | Strawberry Farming | [[industries/crop-farming|Crop Farming]] |
| 111334 | Berry (except Strawberry) Farming | [[industries/crop-farming|Crop Farming]] |
| 111335 | Tree Nut Farming | [[industries/crop-farming|Crop Farming]] |
| 111336 | Fruit and Tree Nut Combination Farming | [[industries/crop-farming|Crop Farming]] |
| 111339 | Other Noncitrus Fruit Farming | [[industries/crop-farming|Crop Farming]] |
| 111411 | Mushroom Production | [[industries/greenhouse-horticulture|Greenhouse Horticulture]] |
| 111419 | Other Food Crops Grown Under Cover | [[industries/greenhouse-horticulture|Greenhouse Horticulture]] |
| 111421 | Nursery and Tree Production | [[industries/greenhouse-horticulture|Greenhouse Horticulture]] |
| 111422 | Floriculture Production | [[industries/greenhouse-horticulture|Greenhouse Horticulture]] |
| 111910 | Tobacco Farming | [[industries/crop-farming|Crop Farming]] |
| 111920 | Cotton Farming | [[industries/crop-farming|Crop Farming]] |
| 111930 | Sugarcane Farming | [[industries/crop-farming|Crop Farming]] |
| 111940 | Hay Farming | [[industries/crop-farming|Crop Farming]] |
| 111991 | Sugar Beet Farming | [[industries/crop-farming|Crop Farming]] |
| 111992 | Peanut Farming | [[industries/crop-farming|Crop Farming]] |
| 111998 | All Other Miscellaneous Crop Farming | [[industries/crop-farming|Crop Farming]] |
| 112111 | Beef Cattle Ranching and Farming | [[industries/livestock-operations|Livestock Operations]] |
| 112112 | Cattle Feedlots | [[industries/livestock-operations|Livestock Operations]] |
| 112120 | Dairy Cattle and Milk Production | [[industries/livestock-operations|Livestock Operations]] |
| 112130 | Dual-Purpose Cattle Ranching and Farming | [[industries/livestock-operations|Livestock Operations]] |
| 112210 | Hog and Pig Farming | [[industries/livestock-operations|Livestock Operations]] |
| 112310 | Chicken Egg Production | [[industries/livestock-operations|Livestock Operations]] |
| 112320 | Broilers and Other Meat Type Chicken Production | [[industries/livestock-operations|Livestock Operations]] |
| 112330 | Turkey Production | [[industries/livestock-operations|Livestock Operations]] |
| 112340 | Poultry Hatcheries | [[industries/livestock-operations|Livestock Operations]] |
| 112390 | Other Poultry Production | [[industries/livestock-operations|Livestock Operations]] |
| 112410 | Sheep Farming | [[industries/livestock-operations|Livestock Operations]] |
| 112420 | Goat Farming | [[industries/livestock-operations|Livestock Operations]] |
| 213111 | Drilling Oil and Gas Wells | [[industries/oil-gas-field-services|Oil & Gas Field Services]] |
| 213112 | Support Activities for Oil and Gas Operations | [[industries/oil-gas-field-services|Oil & Gas Field Services]] |
| 221310 | Water Supply and Irrigation Systems | [[industries/municipal-services|Municipal Services]] |
| 221320 | Sewage Treatment Facilities | [[industries/municipal-services|Municipal Services]] |
| 236115 | New Single-Family Housing Construction (except For-Sale Builders) | [[industries/general-contractors|General Contractors]] |
| 236116 | New Multifamily Housing Construction (except For-Sale Builders) | [[industries/general-contractors|General Contractors]] |
| 236117 | New Housing For-Sale Builders | [[industries/general-contractors|General Contractors]] |
| 236118 | Residential Remodelers | [[industries/general-contractors|General Contractors]] |
| 236210 | Industrial Building Construction | [[industries/general-contractors|General Contractors]] |
| 236220 | Commercial and Institutional Building Construction | [[industries/general-contractors|General Contractors]] |
| 237110 | Water and Sewer Line and Related Structures Construction | [[industries/utility-contractors|Utility Contractors]] |
| 237120 | Oil and Gas Pipeline and Related Structures Construction | [[industries/utility-contractors|Utility Contractors]] |
| 237130 | Power and Communication Line and Related Structures Construction | [[industries/utility-contractors|Utility Contractors]] |
| 238160 | Roofing Contractors | [[industries/roofing-contractors|Roofing Contractors]] |
| 238210 | Electrical Contractors and Other Wiring Installation Contractors | [[industries/electrical-contractors|Electrical Contractors]], [[industries/solar-installers|Solar Installers]] |
| 238220 | Plumbing, Heating, and Air-Conditioning Contractors | [[industries/plumbing-contractors|Plumbing Contractors]], [[industries/hvac-contractors|HVAC Contractors]] |
| 238320 | Painting and Wall Covering Contractors | [[industries/painting-contractors|Painting Contractors]] |
| 311111 | Dog and Cat Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311119 | Other Animal Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311211 | Flour Milling | [[industries/food-manufacturing|Food Manufacturing]] |
| 311212 | Rice Milling | [[industries/food-manufacturing|Food Manufacturing]] |
| 311213 | Malt Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311221 | Wet Corn Milling and Starch Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311224 | Soybean and Other Oilseed Processing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311225 | Fats and Oils Refining and Blending | [[industries/food-manufacturing|Food Manufacturing]] |
| 311230 | Breakfast Cereal Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311313 | Beet Sugar Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311314 | Cane Sugar Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311340 | Nonchocolate Confectionery Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311351 | Chocolate and Confectionery Manufacturing from Cacao Beans | [[industries/food-manufacturing|Food Manufacturing]] |
| 311352 | Confectionery Manufacturing from Purchased Chocolate | [[industries/food-manufacturing|Food Manufacturing]] |
| 311411 | Frozen Fruit, Juice, and Vegetable Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311412 | Frozen Specialty Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311421 | Fruit and Vegetable Canning | [[industries/food-manufacturing|Food Manufacturing]] |
| 311422 | Specialty Canning | [[industries/food-manufacturing|Food Manufacturing]] |
| 311423 | Dried and Dehydrated Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311511 | Fluid Milk Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311512 | Creamery Butter Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311513 | Cheese Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311514 | Dry, Condensed, and Evaporated Dairy Product Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311520 | Ice Cream and Frozen Dessert Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311611 | Animal (except Poultry) Slaughtering | [[industries/food-manufacturing|Food Manufacturing]] |
| 311612 | Meat Processed from Carcasses | [[industries/food-manufacturing|Food Manufacturing]] |
| 311613 | Rendering and Meat Byproduct Processing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311615 | Poultry Processing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311710 | Seafood Product Preparation and Packaging | [[industries/food-manufacturing|Food Manufacturing]] |
| 311812 | Commercial Bakeries | [[industries/food-manufacturing|Food Manufacturing]] |
| 311813 | Frozen Cakes, Pies, and Other Pastries Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311821 | Cookie and Cracker Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311824 | Dry Pasta, Dough, and Flour Mixes Manufacturing from Purchased Flour | [[industries/food-manufacturing|Food Manufacturing]] |
| 311830 | Tortilla Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311911 | Roasted Nuts and Peanut Butter Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311919 | Other Snack Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311920 | Coffee and Tea Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311930 | Flavoring Syrup and Concentrate Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311941 | Mayonnaise, Dressing, and Other Prepared Sauce Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311942 | Spice and Extract Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311991 | Perishable Prepared Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 311999 | All Other Miscellaneous Food Manufacturing | [[industries/food-manufacturing|Food Manufacturing]] |
| 315210 | Cut and Sew Apparel Contractors | [[industries/contract-manufacturing|Contract Manufacturing]] |
| 323111 | Commercial Printing (except Screen and Books) | [[industries/printing-shops|Printing Shops]] |
| 323113 | Commercial Screen Printing | [[industries/printing-shops|Printing Shops]] |
| 323117 | Books Printing | [[industries/printing-shops|Printing Shops]] |
| 323120 | Support Activities for Printing | [[industries/printing-shops|Printing Shops]] |
| 325991 | Custom Compounding of Purchased Resins | [[industries/contract-manufacturing|Contract Manufacturing]] |
| 332114 | Custom Roll Forming | [[industries/metal-fabrication|Metal Fabrication]] |
| 332119 | Metal Crown, Closure, and Other Metal Stamping (except Automotive) | [[industries/metal-fabrication|Metal Fabrication]] |
| 332311 | Prefabricated Metal Building and Component Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332312 | Fabricated Structural Metal Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332313 | Plate Work Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332321 | Metal Window and Door Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332322 | Sheet Metal Work Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332323 | Ornamental and Architectural Metal Work Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332410 | Power Boiler and Heat Exchanger Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332420 | Metal Tank (Heavy Gauge) Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332613 | Spring Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332618 | Other Fabricated Wire Product Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332710 | Machine Shops | [[industries/metal-fabrication|Metal Fabrication]] |
| 332721 | Precision Turned Product Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332811 | Metal Heat Treating | [[industries/metal-fabrication|Metal Fabrication]] |
| 332812 | Metal Coating, Engraving (except Jewelry and Silverware), and Allied Services to Manufacturers | [[industries/metal-fabrication|Metal Fabrication]] |
| 332813 | Electroplating, Plating, Polishing, Anodizing, and Coloring | [[industries/metal-fabrication|Metal Fabrication]] |
| 332996 | Fabricated Pipe and Pipe Fitting Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 332999 | All Other Miscellaneous Fabricated Metal Product Manufacturing | [[industries/metal-fabrication|Metal Fabrication]] |
| 334418 | Printed Circuit Assembly (Electronic Assembly) Manufacturing | [[industries/electronics-contract-mfg|Electronics Contract Manufacturing]] |
| 334510 | Electromedical and Electrotherapeutic Apparatus Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 334517 | Irradiation Apparatus Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 339112 | Surgical and Medical Instrument Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 339113 | Surgical Appliance and Supplies Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 339114 | Dental Equipment and Supplies Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 339115 | Ophthalmic Goods Manufacturing | [[industries/medical-device-mfg|Medical Device Manufacturing]] |
| 423850 | Service Establishment Equipment and Supplies Merchant Wholesalers | [[industries/restaurant-suppliers|Restaurant Suppliers]] |
| 424410 | General Line Grocery Merchant Wholesalers | [[industries/food-distributors|Food Distributors]], [[industries/restaurant-suppliers|Restaurant Suppliers]] |
| 424420 | Packaged Frozen Food Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424430 | Dairy Product (except Dried or Canned) Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424440 | Poultry and Poultry Product Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424450 | Confectionery Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424460 | Fish and Seafood Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424470 | Meat and Meat Product Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424480 | Fresh Fruit and Vegetable Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 424490 | Other Grocery and Related Products Merchant Wholesalers | [[industries/food-distributors|Food Distributors]] |
| 441120 | Used Car Dealers | [[industries/auto-dealers-independent|Independent Auto Dealers]] |
| 441210 | Recreational Vehicle Dealers | [[industries/rv-dealerships|RV Dealerships]] |
| 445230 | Fruit and Vegetable Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 445240 | Meat Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 445250 | Fish and Seafood Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 445291 | Baked Goods Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 445292 | Confectionery and Nut Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 445298 | All Other Specialty Food Retailers | [[industries/specialty-food-retail|Specialty Food Retail]] |
| 456110 | Pharmacies and Drug Retailers | [[industries/pharmacy-independents|Independent Pharmacies]] |
| 456199 | All Other Health and Personal Care Retailers | [[industries/medical-supply-retail|Medical Supply Retail]] |
| 458110 | Clothing and Clothing Accessories Retailers | [[industries/independent-retailers|Independent Retailers]] |
| 459420 | Gift, Novelty, and Souvenir Retailers | [[industries/independent-retailers|Independent Retailers]] |
| 459999 | All Other Miscellaneous Retailers | [[industries/independent-retailers|Independent Retailers]] |
| 484110 | General Freight Trucking, Local | [[industries/owner-operator-trucking|Owner-Operator Trucking]] |
| 484121 | General Freight Trucking, Long-Distance, Truckload | [[industries/owner-operator-trucking|Owner-Operator Trucking]] |
| 484210 | Used Household and Office Goods Moving | [[industries/moving-companies|Moving Companies]] |
| 484220 | Specialized Freight (except Used Goods) Trucking, Local | [[industries/owner-operator-trucking|Owner-Operator Trucking]] |
| 484230 | Specialized Freight (except Used Goods) Trucking, Long-Distance | [[industries/owner-operator-trucking|Owner-Operator Trucking]] |
| 485113 | Bus and Other Motor Vehicle Transit Systems | [[industries/municipal-services|Municipal Services]] |
| 485310 | Taxi and Ridesharing Services | [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]] |
| 485320 | Limousine Service | [[industries/rideshare-fleet-operators|Rideshare Fleet Operators]] |
| 485510 | Charter Bus Industry | [[industries/charter-bus-operators|Charter Bus Operators]] |
| 485991 | Special Needs Transportation | [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]] |
| 488410 | Motor Vehicle Towing | [[industries/towing-companies|Towing Companies]] |
| 488510 | Freight Transportation Arrangement | [[industries/freight-brokerage|Freight Brokerage]], [[industries/customs-brokers|Customs Brokers]] |
| 492110 | Couriers and Express Delivery Services | [[industries/last-mile-delivery|Last-Mile Delivery]] |
| 492210 | Local Messengers and Local Delivery | [[industries/last-mile-delivery|Last-Mile Delivery]] |
| 493110 | General Warehousing and Storage | [[industries/warehouse-3pl|Warehouse & 3PL]] |
| 493120 | Refrigerated Warehousing and Storage | [[industries/warehouse-3pl|Warehouse & 3PL]], [[industries/cold-chain-logistics|Cold Chain Logistics]] |
| 493190 | Other Warehousing and Storage | [[industries/warehouse-3pl|Warehouse & 3PL]] |
| 512110 | Motion Picture and Video Production | [[industries/video-production-smb|SMB Video Production]] |
| 512250 | Record Production and Distribution | [[industries/music-distribution-platforms|Music Distribution Platforms]] |
| 513110 | Newspaper Publishers | [[industries/news-media-local|Local News Media]] |
| 513120 | Periodical Publishers | [[industries/digital-native-publishers|Digital Native Publishers]], [[industries/newsletter-media|Newsletter Media]], [[industries/independent-publishers|Independent Publishers]] |
| 513130 | Book Publishers | [[industries/independent-publishers|Independent Publishers]] |
| 513199 | All Other Publishers | [[industries/independent-publishers|Independent Publishers]], [[industries/digital-native-publishers|Digital Native Publishers]] |
| 513210 | Software Publishers | [[industries/crm-platforms|CRM Platforms]], [[industries/developer-tools-vendors|Developer Tools Vendors]], [[industries/bi-analytics-platforms|BI & Analytics Platforms]], [[industries/hr-tech-platforms|HR Tech Platforms]], [[industries/legal-practice-software|Legal Practice Software]], [[industries/mobile-game-publishers|Mobile Game Publishers]] |
| 516210 | Media Streaming Distribution Services, Social Networks, and Other Media Networks and Content Providers | [[industries/streaming-video-platforms|Streaming Video Platforms]], [[industries/podcasting-networks|Podcasting Networks]], [[industries/ugc-video-platforms|UGC Video Platforms]], [[industries/digital-audio-platforms|Digital Audio Platforms]], [[industries/newsletter-media|Newsletter Media]], [[industries/membership-community-platforms|Membership & Community Platforms]] |
| 518210 | Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services | [[industries/edge-cdn-providers|Edge & CDN Providers]], [[industries/ai-inference-providers|AI Inference Providers]], [[industries/game-hosting-providers|Game Hosting Providers]], [[industries/api-infrastructure-providers|API Infrastructure Providers]], [[industries/web-data-extraction-firms|Web Data Extraction Firms]], [[industries/digital-bpo-operations|Digital BPO Operations]] |
| 519290 | Web Search Portals and All Other Information Services | [[industries/financial-data-vendors|Financial Data Vendors]], [[industries/data-marketplace-brokers|Data Marketplace Brokers]] |
| 522130 | Credit Unions | [[industries/credit-unions|Credit Unions]] |
| 522291 | Consumer Lending | [[industries/lending-marketplaces|Lending Marketplaces]], [[industries/bnpl-providers|BNPL Providers]], [[industries/neobanks|Neobanks]] |
| 522310 | Mortgage and Nonmortgage Loan Brokers | [[industries/mortgage-brokers|Mortgage Brokers]] |
| 522320 | Financial Transactions Processing, Reserve, and Clearinghouse Activities | [[industries/payment-processors|Payment Processors]], [[industries/embedded-finance-platforms|Embedded Finance Platforms]] |
| 523150 | Investment Banking and Securities Intermediation | [[industries/investment-banking-boutiques|Investment Banking Boutiques]] |
| 523210 | Securities and Commodity Exchanges | [[industries/crypto-exchanges|Crypto Exchanges]] |
| 523910 | Miscellaneous Intermediation | [[industries/private-equity-firms|Private Equity Firms]] |
| 523940 | Portfolio Management and Investment Advice | [[industries/wealth-management-rias|Wealth Management RIAs]], [[industries/asset-managers|Asset Managers]], [[industries/robo-advisors|Robo-Advisors]], [[industries/hedge-funds|Hedge Funds]], [[industries/sell-side-equity-research|Sell-Side Equity Research]] |
| 523999 | Miscellaneous Financial Investment Activities | [[industries/crypto-exchanges|Crypto Exchanges]], [[industries/hedge-funds|Hedge Funds]] |
| 524210 | Insurance Agencies and Brokerages | [[industries/independent-insurance-agents|Independent Insurance Agents]] |
| 524291 | Claims Adjusting | [[industries/public-adjusters|Public Adjusters]] |
| 524292 | Pharmacy Benefit Management and Other Third Party Administration of Insurance and Pension Funds | [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]] |
| 524298 | All Other Insurance Related Activities | [[industries/insurtech-platforms|Insurtech Platforms]] |
| 525910 | Open-End Investment Funds | [[industries/asset-managers|Asset Managers]] |
| 525990 | Other Financial Vehicles | [[industries/private-equity-firms|Private Equity Firms]], [[industries/hedge-funds|Hedge Funds]] |
| 531110 | Lessors of Residential Buildings and Dwellings | [[industries/short-term-rentals|Short-Term Rentals]] |
| 531120 | Lessors of Nonresidential Buildings (except Miniwarehouses) | [[industries/commercial-real-estate|Commercial Real Estate]] |
| 531190 | Lessors of Other Real Estate Property | [[industries/commercial-real-estate|Commercial Real Estate]] |
| 531210 | Offices of Real Estate Agents and Brokers | [[industries/commercial-real-estate|Commercial Real Estate]] |
| 531311 | Residential Property Managers | [[industries/property-management|Property Management]], [[industries/hoa-management|HOA Management]] |
| 531312 | Nonresidential Property Managers | [[industries/property-management|Property Management]], [[industries/commercial-real-estate|Commercial Real Estate]] |
| 531320 | Offices of Real Estate Appraisers | [[industries/real-estate-appraisers|Real Estate Appraisers]] |
| 531390 | Other Activities Related to Real Estate | [[industries/proptech-platforms|Proptech Platforms]] |
| 541110 | Offices of Lawyers | [[industries/small-law-firms|Small Law Firms (Solo and 2-10 Attorney Practices)]], [[industries/immigration-law|Immigration Law Firms]], [[industries/personal-injury-law|Personal Injury Law Firms]], [[industries/estate-planning|Estate Planning Law Firms]] |
| 541211 | Offices of Certified Public Accountants | [[industries/accounting-firms-smb|SMB Accounting Firms]], [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]] |
| 541213 | Tax Preparation Services | [[industries/tax-prep-firms|Tax Prep Firms]] |
| 541219 | Other Accounting Services | [[industries/accounting-firms-smb|SMB Accounting Firms]] |
| 541330 | Engineering Services | [[industries/engineering-consultants|Engineering Consultants]] |
| 541350 | Building Inspection Services | [[industries/home-inspection|Home Inspection]] |
| 541370 | Surveying and Mapping (except Geophysical) Services | [[industries/land-surveyors|Land Surveyors]] |
| 541420 | Industrial Design Services | [[industries/product-design-studios|Product Design Studios]] |
| 541511 | Custom Computer Programming Services | [[industries/software-dev-agencies|Software Development Agencies]] |
| 541512 | Computer Systems Design Services | [[industries/data-platform-integrators|Data Platform Integrators]], [[industries/saas-implementation-partners|SaaS Implementation Partners]], [[industries/software-dev-agencies|Software Development Agencies]], [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]], [[industries/fractional-cto-services|Fractional CTO Services]] |
| 541513 | Computer Facilities Management Services | [[industries/it-managed-services|IT Managed Services]], [[industries/cybersecurity-mssp|Cybersecurity MSSPs]] |
| 541519 | Other Computer Related Services | [[industries/penetration-testing-firms|Penetration Testing Firms]], [[industries/digital-forensics-firms|Digital Forensics Firms]], [[industries/digital-accessibility-firms|Digital Accessibility Firms]], [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]], [[industries/ai-red-teaming-firms|AI Red Teaming Firms]], [[industries/data-analytics-consultants|Data Analytics Consultants]] |
| 541611 | Administrative Management and General Management Consulting Services | [[industries/revops-consultancies|RevOps Consultancies]], [[industries/fractional-cto-services|Fractional CTO Services]], [[industries/compliance-consulting|Compliance Consulting Firms]] |
| 541612 | Human Resources Consulting Services | [[industries/hr-consultants|HR Consultants]] |
| 541613 | Marketing Consulting Services | [[industries/marketing-agencies-smb|SMB Marketing Agencies]], [[industries/performance-marketing-agencies|Performance Marketing Agencies]], [[industries/conversion-optimization-firms|Conversion Optimization Firms]], [[industries/app-marketing-firms|App Marketing Firms]] |
| 541618 | Other Management Consulting Services | [[industries/compliance-consulting|Compliance Consulting Firms]], [[industries/expert-networks|Expert Networks]], [[industries/revops-consultancies|RevOps Consultancies]] |
| 541620 | Environmental Consulting Services | [[industries/environmental-consultants|Environmental Consultants]] |
| 541690 | Other Scientific and Technical Consulting Services | [[industries/energy-auditors|Energy Auditors]], [[industries/engineering-consultants|Engineering Consultants]], [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]] |
| 541720 | Research and Development in the Social Sciences and Humanities | [[industries/player-research-firms|Player Research Firms]], [[industries/ux-research-agencies|UX Research Agencies]] |
| 541810 | Advertising Agencies | [[industries/marketing-agencies-smb|SMB Marketing Agencies]], [[industries/performance-marketing-agencies|Performance Marketing Agencies]], [[industries/developer-relations-agencies|Developer Relations Agencies]], [[industries/technical-content-agencies|Technical Content Agencies]], [[industries/app-marketing-firms|App Marketing Firms]] |
| 541830 | Media Buying Agencies | [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]] |
| 541890 | Other Services Related to Advertising | [[industries/influencer-marketing-platforms|Influencer Marketing Platforms]], [[industries/creator-talent-agencies|Creator Talent Agencies]], [[industries/affiliate-networks|Affiliate Networks]], [[industries/game-user-acquisition-firms|Game User Acquisition Firms]], [[industries/retail-media-networks|Retail Media Networks]], [[industries/audio-adtech-networks|Audio Adtech Networks]] |
| 541910 | Marketing Research and Public Opinion Polling | [[industries/player-research-firms|Player Research Firms]], [[industries/ux-research-agencies|UX Research Agencies]] |
| 541930 | Translation and Interpretation Services | [[industries/localization-services|Localization Services]] |
| 541940 | Veterinary Services | [[industries/veterinary-practices|Veterinary Practices]] |
| 541990 | All Other Professional, Scientific, and Technical Services | [[industries/brand-protection-firms|Brand Protection Firms]], [[industries/expert-networks|Expert Networks]] |
| 561110 | Office Administrative Services | [[industries/virtual-assistant-services|Virtual Assistant Services]] |
| 561311 | Employment Placement Agencies | [[industries/staffing-agencies|Staffing Agencies]] |
| 561320 | Temporary Help Services | [[industries/staffing-agencies|Staffing Agencies]], [[industries/it-staffing-firms|IT Staffing Firms]] |
| 561422 | Telemarketing Bureaus and Other Contact Centers | [[industries/digital-bpo-operations|Digital BPO Operations]], [[industries/content-moderation-services|Content Moderation Services]], [[industries/data-labeling-services|Data Labeling Services]] |
| 561439 | Other Business Service Centers (including Copy Shops) | [[industries/printing-shops|Printing Shops]] |
| 561440 | Collection Agencies | [[industries/collections-agencies|Collections Agencies]] |
| 561499 | All Other Business Support Services | [[industries/digital-bpo-operations|Digital BPO Operations]] |
| 561612 | Security Guards and Patrol Services | [[industries/security-guard-firms|Security Guard Firms]] |
| 561710 | Exterminating and Pest Control Services | [[industries/pest-control|Pest Control]] |
| 561720 | Janitorial Services | [[industries/cleaning-companies|Cleaning Companies]] |
| 561730 | Landscaping Services | [[industries/landscaping|Landscaping]] |
| 561740 | Carpet and Upholstery Cleaning Services | [[industries/cleaning-companies|Cleaning Companies]] |
| 561790 | Other Services to Buildings and Dwellings | [[industries/cleaning-companies|Cleaning Companies]] |
| 561920 | Convention and Trade Show Organizers | [[industries/event-planning|Event Planning]] |
| 562910 | Remediation Services | [[industries/insurance-restoration|Insurance Restoration]], [[industries/environmental-consultants|Environmental Consultants]] |
| 611110 | Elementary and Secondary Schools | [[industries/k12-private-schools|K-12 Private Schools]] |
| 611430 | Professional and Management Development Training | [[industries/corporate-training|Corporate Training]] |
| 611511 | Cosmetology and Barber Schools | [[industries/vocational-schools|Vocational Schools]] |
| 611513 | Apprenticeship Training | [[industries/vocational-schools|Vocational Schools]] |
| 611519 | Other Technical and Trade Schools | [[industries/vocational-schools|Vocational Schools]] |
| 611630 | Language Schools | [[industries/language-schools|Language Schools]] |
| 611691 | Exam Preparation and Tutoring | [[industries/tutoring-centers|Tutoring Centers]] |
| 621112 | Offices of Physicians, Mental Health Specialists | [[industries/behavioral-health-clinics|Behavioral Health Clinics]] |
| 621210 | Offices of Dentists | [[industries/dental-practices|Dental Practices]] |
| 621310 | Offices of Chiropractors | [[industries/chiropractic-practices|Chiropractic Practices]] |
| 621330 | Offices of Mental Health Practitioners (except Physicians) | [[industries/behavioral-health-clinics|Behavioral Health Clinics]] |
| 621340 | Offices of Physical, Occupational and Speech Therapists, and Audiologists | [[industries/physical-therapy|Physical Therapy]] |
| 621399 | Offices of All Other Miscellaneous Health Practitioners | [[industries/acupuncture-practices|Acupuncture Practices]] |
| 621420 | Outpatient Mental Health and Substance Abuse Centers | [[industries/behavioral-health-clinics|Behavioral Health Clinics]] |
| 621493 | Freestanding Ambulatory Surgical and Emergency Centers | [[industries/urgent-care|Urgent Care Centers]] |
| 621610 | Home Health Care Services | [[industries/home-health-agencies|Home Health Agencies]] |
| 624110 | Child and Youth Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624120 | Services for the Elderly and Persons with Disabilities | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624190 | Other Individual and Family Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624210 | Community Food Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624221 | Temporary Shelters | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624229 | Other Community Housing Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624230 | Emergency and Other Relief Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624310 | Vocational Rehabilitation Services | [[industries/nonprofits-social-services|Social Services Nonprofits]] |
| 624410 | Child Care Services | [[industries/childcare-centers|Childcare Centers]] |
| 711410 | Agents and Managers for Artists, Athletes, Entertainers, and Other Public Figures | [[industries/creator-talent-agencies|Creator Talent Agencies]] |
| 711510 | Independent Artists, Writers, and Performers | [[industries/creator-businesses|Creator Businesses]] |
| 713940 | Fitness and Recreational Sports Centers | [[industries/gyms-independent|Independent Gyms]] |
| 721110 | Hotels (except Casino Hotels) and Motels | [[industries/hotels-boutique|Boutique Hotels]] |
| 721199 | All Other Traveler Accommodation | [[industries/short-term-rentals|Short-Term Rentals]] |
| 722320 | Caterers | [[industries/catering-companies|Catering Companies]] |
| 722330 | Mobile Food Services | [[industries/food-trucks|Food Trucks]] |
| 722511 | Full-Service Restaurants | [[industries/independent-restaurants|Independent Restaurants]] |
| 722513 | Limited-Service Restaurants | [[industries/independent-restaurants|Independent Restaurants]] |
| 722515 | Snack and Nonalcoholic Beverage Bars | [[industries/coffee-shops-independent|Independent Coffee Shops]] |
| 811111 | General Automotive Repair | [[industries/auto-repair-shops|Auto Repair Shops]] |
| 811114 | Specialized Automotive Repair | [[industries/auto-repair-shops|Auto Repair Shops]] |
| 811121 | Automotive Body, Paint, and Interior Repair and Maintenance | [[industries/auto-body-shops|Auto Body Shops]] |
| 811490 | Other Personal and Household Goods Repair and Maintenance | [[industries/alterations-tailoring|Alterations & Tailoring]] |
| 812111 | Barber Shops | [[industries/hair-salons-independent|Hair Salons (Independent)]] |
| 812112 | Beauty Salons | [[industries/hair-salons-independent|Hair Salons (Independent)]] |
| 812199 | Other Personal Care Services | [[industries/tattoo-studios|Tattoo Studios]], [[industries/med-spas|Med Spas]] |
| 812210 | Funeral Homes and Funeral Services | [[industries/funeral-homes|Funeral Homes]] |
| 812910 | Pet Care (except Veterinary) Services | [[industries/pet-services|Pet Services]] |
| 813110 | Religious Organizations | [[industries/faith-organizations|Faith Organizations]] |
| 813910 | Business Associations | [[industries/trade-associations|Trade Associations]] |
| 921190 | Other General Government Support | [[industries/municipal-services|Municipal Services]] |
| 922120 | Police Protection | [[industries/municipal-services|Municipal Services]] |
| 922130 | Legal Counsel and Prosecution | [[industries/public-defenders|Public Defenders]] |
| 922160 | Fire Protection | [[industries/municipal-services|Municipal Services]] |
| 925120 | Administration of Urban Planning and Community and Rural Development | [[industries/municipal-services|Municipal Services]] |
