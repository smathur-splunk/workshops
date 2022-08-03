## Configure Otel Collector to send data to Splunk Observability (part 2)
### Configure Otel Collector
14. In `/etc/otel/collector/gateway_config.yaml`, add a `splunk_hec/obs` exporter to point to Splunk Observability:
```yaml
exporters:
  splunk_hec/obs:
    token: "${SPLUNK_ACCESS_TOKEN}"
    endpoint: "https://ingest.${SPLUNK_REALM}.signalfx.com/v1/log"
```

15. In `/etc/otel/collector/gateway_config.yaml`, add the exporters in `service.pipelines` for Splunk Observability:
```yaml
service:
  pipelines:
    traces:
      exporters: [splunk_hec, sapm]
    metrics:
      exporters: [splunk_hec/metrics, signalfx]
    metrics/internal:
      exporters: [splunk_hec/metrics, signalfx]
    logs:
      exporters: [splunk_hec, signalfx]
    logs/profiling:
      exporters: [splunk_hec, splunk_hec/obs]
```

16. Run the Otel Collector, this time specifying your `SPLUNK_ACCESS_TOKEN` and `SPLUNK_REALM` for Splunk Observability Cloud:
```bash
SPLUNK_ACCESS_TOKEN=<ACCESS_TOKEN> SPLUNK_REALM=<REALM> ./otelcol_linux_amd64
```
To get your access token see [Create and manage organization access tokens using Splunk Observability Cloud](https://docs.splunk.com/observability/admin/authentication-tokens/org-tokens.html).

### Validate data in Splunk Observability Cloud
17. Login to Splunk Observability Cloud and check for [JVM metrics](https://docs.splunk.com/Observability/gdi/get-data-in/application/java/configuration/java-otel-metrics-attributes.html#jvm-metrics) in Metric Finder. Check for traces in APM (on the service map and in the traces view), and also check for Code Profiling data in APM. If using a database, check DB Query Perfomance in APM.