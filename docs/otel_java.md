### Add Java Auto-Instrumentation Library
8. On the host running your Java app, go to the root directory of the app and download the auto-instrumentation library:
```bash
curl -L https://github.com/signalfx/splunk-otel-java/releases/latest/download/splunk-otel-javaagent.jar -o splunk-otel-javaagent.jar
```
9. Set the following environment variables (replace `<APP_NAME>`, `<ENV_NAME>`, and `<GATEWAY_IP>`):
```bash
export OTEL_SERVICE_NAME='<APP_NAME>'
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=<ENV_NAME>'
export OTEL_EXPORTER_OTLP_ENDPOINT='http://<GATEWAY_IP>:4317'
```

10. Finally, run your app with the `javaagent` tag added to specify the auto-instrumentation library (`<GATEWAY_IP>` may be `localhost` if the OTel collector is running on the same VM):
```bash
java -javaagent:./splunk-otel-javaagent.jar -Dsplunk.profiler.enabled=true -Dsplunk.metrics.enabled=true -Dsplunk.metrics.endpoint='http://<GATEWAY_IP>:9943' \
-jar myapp.jar
```
If you are using the [Spring PetClinic](https://github.com/spring-projects/spring-petclinic) app, run this command instead, from the app's root directory:
```bash
java -javaagent:./splunk-otel-javaagent.jar -Dsplunk.profiler.enabled=true -Dsplunk.metrics.enabled=true -Dsplunk.metrics.endpoint='http://<GATEWAY_IP>:9943' -jar target/spring-petclinic-*-SNAPSHOT.jar
```

### Validate Data in Splunk Enterprise
11. Trace search (in Splunk/SPL) for validating ingestion and search:
```sql
index = apm_traces (last 15 minutes)
```
12. Metric search for validating ingestion:
```sql
| mcatalog values(metric_name) WHERE index=apm_metrics
```
Metric search for validating search:
```sql
| mstats avg(_value) prestats=t WHERE index=apm_metrics AND metric_name="runtime.jvm.memory.*" span=1m by metric_name | timechart avg(_value) as "Avg" span=1m by metric_name
```

13. Learn how to work with metric data in Splunk Enterprise/Cloud. See:

- [Splunk Enterprise/Cloud docs: Visualize metrics in the Analytics Workspace](https://docs.splunk.com/Documentation/Splunk/8.2.6/Metrics/Visualize)

- [Metrics and attributes collected by the Splunk OTel Java agent (JVM metrics)](https://docs.splunk.com/Observability/gdi/get-data-in/application/java/configuration/java-otel-metrics-attributes.html#jvm-metrics)


### Validate Data in Splunk Observability Cloud
17. Login to Splunk Observability Cloud and check for [JVM metrics](https://docs.splunk.com/Observability/gdi/get-data-in/application/java/configuration/java-otel-metrics-attributes.html#jvm-metrics) by searching `jvm` in Metric Finder. 

18. Check for traces in APM (on the service map and in the traces view), and also check for Code Profiling data in APM. If using a database, check DB Query Perfomance in APM.