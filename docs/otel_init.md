### Set Up Splunk Enterprise Indexes and HEC Endpoints
1. Create the two required indexes: an index for traces `apm_traces` (see [Create events indexes](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes#Create_events_indexes)), and an index for metrics `apm_metrics` (see [Create metrics indexes](https://docs.splunk.com/Documentation/Splunk/latest/Indexer/Setupmultipleindexes#Create_metrics_indexes)).

2. Setup 2 Splunk HEC tokens, one for `apm_traces` and one for `apm_metrics`. See [Configure HTTP Event Collector on Splunk Enterprise](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Enterprise) or on [Splunk Cloud](https://docs.splunk.com/Documentation/SplunkCloud/8.2.2202/Data/UsetheHTTPEventCollector#Configure_HTTP_Event_Collector_on_Splunk_Cloud_Platform). Steps summarized below.

- Login to Splunk and go to `Settings` > `Data inputs` (under "Data") > `HTTP Event Collector`.
- At the top-right, click `Global Settings` and set "All Tokens" to `Enabled`, and uncheck "Enable SSL" (if not using HTTPS). Ensure the "HTTP Port Number" is set to `8088`. Click `Save`.
- At the top-right, create `New Token`, and enter a Name. Click `Next`. Next to "Select Allowed Indexes", select `apm_traces`. Click `Review`, and then `Submit`. You should now see a "Token Value", which we'll need in the next section.
- To ingest metrics, create another HEC token and assign it to the `apm_metrics` index. Make sure to copy the "Token Value" here as well.

### Install the OTel Collector Gateway
3. On your Linux VM, install the OTel Collector. If the VM does not have internet access, download these files separately and manually copy them to the VM. **Note**: If you wish to run the OTel Collector in *agent* mode, simply replace `gateway` with `agent` in the commands below.
```bash
sudo apt install wget
wget https://github.com/signalfx/splunk-otel-collector/releases/download/v0.57.0/otelcol_linux_amd64
chmod a+x otelcol_linux_amd64
wget https://raw.githubusercontent.com/signalfx/splunk-otel-collector/main/cmd/otelcol/config/collector/gateway_config.yaml
sudo mkdir /etc/otel
sudo mkdir /etc/otel/collector
sudo mv gateway_config.yaml /etc/otel/collector/
```