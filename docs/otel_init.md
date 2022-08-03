### Splunk Enterprise Setup
1. Create required indexes for HEC:
- Create an index for traces `apm_poc_traces`: See [Create events indexes](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes#Create_events_indexes)
- Create an index for metrics `apm_poc_metrics`: See [Create metrics indexes](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes#Create_metrics_indexes)

2. Setup 2 Splunk HEC tokens, one for `apm_poc_traces` and one for `apm_poc_metrics`: See [Configure HTTP Event Collector on Splunk Enterprise](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Enterprise) or [Splunk Cloud Platform](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Cloud_Platform)

### OpenTelemetry Gateway Setup
3. Install Otel Collector. If VM does not have internet access, download files separately and copy to VM.
```bash
sudo apt install wget
wget https://github.com/signalfx/splunk-otel-collector/releases/download/v0.48.0/otelcol_linux_amd64
chmod a+x otelcol_linux_amd64
wget https://raw.githubusercontent.com/signalfx/splunk-otel-collector/main/cmd/otelcol/config/collector/gateway_config.yaml
sudo mkdir /etc/otel
sudo mkdir /etc/otel/collector
sudo mv gateway_config.yaml /etc/otel/collector/
```
4. Configure Otel Collector exporters: Open `/etc/otel/collector/gateway_config.yaml` for editing. Add to exporters, replacing `<SPLUNK_IP>`, `<SPLUNK_HEC_TOKEN>`, and `<SPLUNK_METRICS_HEC_TOKEN>` (use `http` or `https` depending on how your HEC endpoint is configured in Splunk Enterprise):
```yaml
exporters:
  splunk_hec:
    token: <SPLUNK_HEC_TOKEN>
    endpoint: "https://<SPLUNK_IP>:8088/services/collector/raw"
    source: otel
    sourcetype: otel
  splunk_hec/metrics:
    token: <SPLUNK_METRICS_HEC_TOKEN>
    endpoint: "https://<SPLUNK_IP>:8088/services/collector"
    source: otel
    sourcetype: otel_metrics
```
5. Configure Otel Collector pipelines. In `/etc/otel/collector/gateway_config.yaml`, add the exporters we created to `service.pipelines`:
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

6. Run the Otel Collector:
```bash
SPLUNK_ACCESS_TOKEN=0 SPLUNK_REALM=us0 ./otelcol_linux_amd64
```

## Validate Otel Collector Gateway functioning correctly
### Use cURL for Validation Testing
7. Run this cURL command to test the gateway is running (port `4318` must be accessible on the VM):
```bash
curl -X POST http://<GATEWAY_IP>:4318/v1/traces
   -H 'Content-Type: application/json'
   -d '{"resourceSpans": [{"resource": {"attributes": [{"key": "service.name","value": {"stringValue": "curl-test-otel-pipeline"}}]},"instrumentationLibrarySpans": [{"spans": [{"traceId": "71699b6fe85982c7c8995ea3d9c95df2","spanId": "3c191d03fa8be065","name": "test-span","kind": 1,"droppedAttributesCount": 0,"events": [],"droppedEventsCount": 0,              "status": {"code": 1}}],"instrumentationLibrary": {"name": "local-curl-example"}}]}] }'
```