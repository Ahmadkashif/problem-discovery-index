# Alert Threshold Configuration

**Industry:** [[observability-vendors|Observability Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Alerting is a mature feature in every platform and thresholds are numbers a person guessed once, on a service whose normal behaviour nobody characterised, producing a stream that gets muted.
**Tags:** #change-point-detection #time-series-forecasting #gaussian-mixture-models #hypothesis-testing #confidence-intervals #evaluation-metrics #automation

## The Problem
Alerting turns telemetry into a page. Every platform supports thresholds, multi-condition rules, anomaly detection options and routing.

The thresholds are set by an engineer at the moment a monitor is created, from a rough sense of what looks bad. Latency above five hundred milliseconds. Error rate above one per cent. Queue depth above a thousand. These are guesses, they are rarely revisited, and the service's behaviour changes underneath them as traffic grows and the architecture evolves.

The consequences are the two familiar failure modes. Alerts that fire constantly during normal operation, which teams mute or route to a channel nobody reads. And alerts that never fire because the threshold is far outside anything the service ever does, which nobody notices because absence of alerts looks like health.

Both converge on the same place: an on-call rota where pages are not trusted, which is precisely the state alerting exists to prevent. Alert fatigue is one of the most-cited contributors to on-call burnout and it originates in numbers somebody guessed.

## What Already Exists
Threshold, composite and multi-window alerting is standard across all platforms. Anomaly detection alert types are offered by most vendors and adopted cautiously. SLO-based alerting with burn rate windows is a genuine improvement and is well documented. Alert grouping and deduplication exist in incident response tools. Maintenance windows and silencing are universal.

## The Customisation Gap
Baselining is offered generically and rarely models what real service metrics actually look like: strong daily and weekly seasonality, deploy-related step changes, growth trends, and multi-modal behaviour where a service has genuinely different regimes. A detector that flags every Monday morning is worse than a static threshold.

Alert quality measurement is absent, which is the deeper problem. No platform reports which alerts have fired and led to action, which fired and were ignored, which fired during incidents nobody had alerted on, and which have never fired at all. That report would let a team prune its alerting in an afternoon and it does not exist.

Threshold recommendation from history is the constructive fix: given this service's observed behaviour and the incidents it has actually had, what threshold would have caught the real events without firing on the ordinary ones. That is a backtest, it is entirely computable, and no vendor offers it.

Symptom-level rather than cause-level alerting is the design principle the discipline settled on years ago and the tooling does not encourage, which is why so many alerts describe internal states nobody can act on.

## Impact If Solved
Alert fatigue is a leading cause of on-call burnout and originates in guessed numbers that nobody revisits. Measuring alert quality and recommending thresholds by backtest against actual incidents turns alerting from folklore into something maintainable, using the platform's own history.
