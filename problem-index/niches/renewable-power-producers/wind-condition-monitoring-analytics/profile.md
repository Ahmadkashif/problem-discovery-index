# Wind Turbine Condition Monitoring & SCADA Analytics Vendors

**Parent Industry:** [[industries/renewable-power-producers|Renewable Power Producers]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Independent vendors that monitor turbine drivetrains with vibration sensors and SCADA analytics, and whose diagnostic engineers review alerts and send owners reports on bearing, gearbox and generator condition with recommended actions. ONYX Insight, Clir Renewables, bearing and gearbox makers' remote diagnostic services and condition monitoring hardware vendors are representative (named from recall). Owners pay subscriptions or per-turbine service fees, often after OEM warranty ends.

## Insight Function
**Size:** ~10–60 diagnostic engineers and data scientists per vendor (estimate)
**Output:** Fault diagnoses and condition reports per turbine, remaining-life estimates, end-of-warranty inspection evidence, fleet benchmarking dashboards
**Proprietary data:** Fault libraries built from many owners' turbines, with vibration signatures matched to confirmed failures
**Clock:** OEM warranty expiry and end-of-warranty inspection windows, which are contract dates between the owner and the OEM
**Buyer:** Head of Diagnostics or Chief Technology Officer

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 4 |
| Q2 Labor mass + repeatable | ×2 | 4 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 3 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **44/60** |

**Kill switches:** live on the diagnostic-service half — turbine vibration and SCADA data belong to the owners and are held under service agreements whose terms were not checked for product rights; undetermined on the analytics-software half, whose subscription terms were not read. The fault library is built from the service half, so the switch sits on the corpus.
**Verdict:** Logged — kill switch (diagnostic-service half, which builds the fault library). The analytics-software half is undetermined (terms unread) and below threshold at the same 44. This tests turbine SCADA fault diagnosis as tacit knowledge, and the tacit read is real: diagnostic engineers grade spectra case by case. Its closest twin is [[niches/industrial-distributors/condition-monitoring-services/profile|🔍 Rotating-Equipment Condition Monitoring Services]] (44, kill switch), with the same service-versus-subscription split. It also scores level with [[niches/solar-installers/solar-asset-performance-monitoring/profile|🔍 Solar Asset Management & Performance Monitoring]] (44; that pocket names a client-data switch and its overview row shows a kill switch, but its own verdict line reads below threshold), with a different mix: the diagnosis report is itself what owners pay for (Q1 4 against 3), while a drivetrain fault library is narrower than full-fleet generation data (Q3 4 against 5).
