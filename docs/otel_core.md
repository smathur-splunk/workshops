4. Configure OTel Collector exporters: On your VM running OTel, open `/etc/otel/collector/gateway_config.yaml` for editing. Add to exporters, replacing `<SPLUNK_IP>`, `<SPLUNK_HEC_TOKEN>`, and `<SPLUNK_METRICS_HEC_TOKEN>` (use `http` or `https` depending on how your HEC endpoint is configured in Splunk Enterprise/Cloud):
```yaml
exporters:
  splunk_hec:
    token: <SPLUNK_HEC_TOKEN>
    endpoint: "http://<SPLUNK_IP>:8088/services/collector/raw"
    source: otel
    sourcetype: otel
  splunk_hec/metrics:
    token: <SPLUNK_METRICS_HEC_TOKEN>
    endpoint: "http://<SPLUNK_IP>:8088/services/collector"
    source: otel
    sourcetype: otel_metrics
```
5. Configure OTel Collector pipelines. In `/etc/otel/collector/gateway_config.yaml`, add the exporters we created to `service.pipelines`:
```yaml
service:
  pipelines:
    traces:
      exporters: [splunk_hec]
    metrics:
      exporters: [splunk_hec/metrics]
    metrics/internal:
      exporters: [splunk_hec/metrics]
    logs:
      exporters: [splunk_hec]
    logs/profiling:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [splunk_hec]
```

6. Run the OTel Collector:
```bash
SPLUNK_ACCESS_TOKEN=0 SPLUNK_REALM=us0 ./otelcol_linux_amd64
```

### Use cURL to Validate OTel Collector Gateway functioning correctly
7. Run this cURL command to ensure the OTel gateway is running (port `4318` must be accessible on the VM):
```bash
curl -X POST http://<GATEWAY_IP>:4318/v1/traces
   -H 'Content-Type: application/json'
   -d '{"resourceSpans": [{"resource": {"attributes": [{"key": "service.name","value": {"stringValue": "curl-test-otel-pipeline"}}]},"instrumentationLibrarySpans": [{"spans": [{"traceId": "71699b6fe85982c7c8995ea3d9c95df2","spanId": "3c191d03fa8be065","name": "test-span","kind": 1,"droppedAttributesCount": 0,"events": [],"droppedEventsCount": 0,              "status": {"code": 1}}],"instrumentationLibrary": {"name": "local-curl-example"}}]}] }'
```