# OTel Gateway Setup

PoC - Auto Instrumenting a Java App to send trace and metric data to Splunk Enterprise & Observability Cloud

## Requirements
### Components
- Java app
- Linux VM to be used as the OTel collector gateway
- Splunk Cloud/Enterprise
- Splunk Observability Cloud trial/license

### Networking Ports
- Splunk Cloud/Enterprise: 
  - `8088` (HEC endpoint)
- VM for OTel Gateway: 
  - `4317` (OpenTelemetry Protocol - OTLP - gRPC endpoints for logs)
  - `9943` (for app metrics)
  - `4318` (Used for cURL Validation Testing to ensure Otel Gateway is working properly)