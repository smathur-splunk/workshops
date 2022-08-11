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

### Use cURL to Validate OTel Collector Gateway functioning correctly
7. Again, you may want to run this cURL command to ensure the OTel gateway is running properly (port `4318` must be accessible on the VM):
```bash
curl -X POST http://<GATEWAY_IP>:4318/v1/traces
   -H 'Content-Type: application/json'
   -d '{"resourceSpans": [{"resource": {"attributes": [{"key": "service.name","value": {"stringValue": "curl-test-otel-pipeline"}}]},"instrumentationLibrarySpans": [{"spans": [{"traceId": "71699b6fe85982c7c8995ea3d9c95df2","spanId": "3c191d03fa8be065","name": "test-span","kind": 1,"droppedAttributesCount": 0,"events": [],"droppedEventsCount": 0,              "status": {"code": 1}}],"instrumentationLibrary": {"name": "local-curl-example"}}]}] }'
```