# ERP Order Management with Production Scheduling Integration

**Niche:** [[niches/greenhouse-horticulture/ornamental-wholesale-growers/profile|Ornamental Wholesale Growers]]
**Industry:** [[industries/greenhouse-horticulture|Greenhouse Horticulture]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Greenhouse ERP systems (BloomMaster, Picas, Argus ERP) manage orders and shipping but do not connect back to production scheduling — the head grower must manually translate customer orders into planting dates, zone assignments, and cultural protocols.
**Tags:** #data-integration #workflow-orchestration #automation #revenue-impact

## The Problem
When a wholesale ornamental grower takes a customer order — "10,000 6-inch red poinsettias, delivery week 48, FOB grower's dock" — the order enters the ERP system for invoicing and shipping. But the production implications of that order (plant cuttings by week 30, pot by week 33, pinch by week 36, short-day treatment by week 38, space to finish zone 4B by week 42) are calculated by the head grower and communicated verbally to production staff. The ERP knows what the customer wants and when; the greenhouse knows what is growing and where. But these two information systems are not connected, and the gap is bridged entirely by the head grower's mental model.

## What Already Exists
BloomMaster handles order management, invoicing, and shipping logistics for ornamental growers. Picas provides similar ERP functionality for European growers expanding into the US market. These systems track the commercial side of the business (customer, product, quantity, ship date, price) but have no production planning module that translates orders into growing schedules. Separately, the climate computer manages the growing environment but has no awareness of what crops are where or what their target ship dates are.

## The Customization Gap
The integration gap requires: (1) a production planning module that translates ship-date orders into backward-scheduled growing timelines using crop-specific production recipes (cultivar + pot size → weeks to finish, photoperiod protocol, spacing requirements), (2) zone assignment optimization that minimizes crop moves while matching environmental needs to available zones, (3) a propagation and materials planning view that aggregates all orders into cutting/plug procurement schedules and pot/soil/label purchase orders, and (4) bidirectional connection to the climate computer so that zone-level crop assignments inform climate setpoints.

## Target Customer
Operations managers at ornamental wholesale greenhouses with $2M+ in annual sales who currently bridge the order-to-production gap manually. Approximately 2,000-3,000 US operations at this scale.

## Impact If Solved
Production planning time reduced from 8-12 hours/week of manual scheduling to 2-3 hours of reviewing automated recommendations. Over-production (growing 10% extra "just in case") reduced by 30-50%, recovering $50K-$200K annually in materials and space cost. Under-production (discovering in week 44 that an order cannot be filled) reduced by 60-80%, preserving customer relationships worth $20K-$100K per retained account.
