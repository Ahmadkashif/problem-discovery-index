# A Go-Live Record for Every Throughput Projection

**Niche:** [[niches/logistics-consultants/warehouse-design-automation/profile|Warehouse Design & Automation Advisory]]
**Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every automation project starts with a projected throughput and ends with an achieved one, and no consultancy keeps the two side by side across its projects.
**Tags:** #survival-analysis #linear-regression #monte-carlo-methods #evaluation-metrics #feature-engineering #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to predict the throughput a redesigned or automated building will actually reach on the client's own order profile, and whoever's projections hold at go-live wins the next site.

## The Problem
The design phase produces a number — units per hour at peak, orders per day, labour hours per thousand units — and a ramp-up assumption for how fast the system reaches it. Go-live brings the real number, usually lower at first, sometimes permanently. The gap is explained in project meetings (a changed order profile, a software integration delay, staffing) and then forgotten. The next client asks how accurate the firm's projections are, and the firm answers with anecdotes.

## Why Nobody Has Built This
Achieved throughput is operating data that belongs to the owner and is collected after the consultant's scope usually ends. Projects are few per firm per year, so no single project feels like a dataset. And a published gap between projected and achieved throughput is uncomfortable for consultant and vendor alike.

## What to Build
A project ledger that stores each projection with its inputs — order profile, system configuration, ramp-up curve, labour assumptions — and collects achieved throughput, uptime and labour from the warehouse management and control systems at fixed points after go-live, under a data clause agreed at contract. Ramp-up is modelled as time-to-target, so projects still ramping count as censored rather than missing. Over time the ledger shows which assumptions and which system types run optimistic, and by how much.

## Target Customer
Vendor-neutral design and automation consultancies, and owners' engineering teams running multi-site automation programmes.

## Impact If Built
A consultancy that can show projected against achieved throughput across its projects sells its next design on evidence, and catches its own optimistic assumptions before the next client pays for them.
