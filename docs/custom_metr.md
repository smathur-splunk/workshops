## Metric Demystified
### What's the difference between a gauge and a counter?

- **Gauge metric** = value of a measurement at a specific point in time
	- Examples: fan speed, CPU utilization, and memory usage
	- One way to tell that a metric is a gauge is if it makes more sense to **average** the metric's values over time, rather than sum them.
		- In fact, this is what is happening behind the scenes. Observability Cloud applies the SignalFlow `average()` function to data points for gauge metrics. When you specify a 10 second resolution for a chart, and Observability Cloud is receiving data for the metric every 1 second, each point on the line represents the *average* of 10 data points, as opposed to the sum. It wouldn't make sense to sum the CPU utilization, for example, or the resulting value might be >100% and not reflective of the metric's true value.
	- Reporting frequency is most important for gauges, as higher frequency is typically associated with higher accuracy.
- **Counter metric** = number of new occurrences or items since the last measurement
	- Examples: number of requests handled, emails sent, and errors encountered
	- One way to tell that a metric is a counter is if it makes more sense to **sum** the metric's values over time, rather than average them.
		- This is what is happening behind the scenes. Observability Cloud applies the SignalFlow `sum()` function to data points for counter metrics. When you specify a 10 second resolution for a chart, and Observability Cloud is receiving data for the metric every 1 second, each point on the line represents the sum of 10 data points. It wouldn't make sense to average the count of errors, for example, or the resulting value would be lower than the true count of errors in any given timeframe.
	- Counters can only take integer values of zero or greater and are reset to zero at the conclusion of each reporting interval.

... But wait, there's more!

- **Cumulative counter metric** = total number of occurrences or items since the measurement began
	- Examples: number of successful jobs, number of logged-in users, and number of warnings
	- *Cumulative counter* metrics differ from *counter* metrics in the following ways:
		- Cumulative counters only reset to 0 when the monitored machine or application restarts or when the counter value reaches the maximum value representable (2 32 or 2 64 ).
		- In most cases, you’re interested in how much the metric value changed between measurements.
		- Observability Cloud applies the SignalFlow `delta()` function to data points for cumulative counter metrics. When you specify a 10 second resolution for a chart, and Observability Cloud is receiving data for the metric every 1 second, each point on the line represents the change between the first data point received and the 10th data point received.

Sources:
- [Identify metric types](https://docs.splunk.com/Observability/metrics-and-metadata/metric-types.html)
- [Metrics, data points, and metric time series](https://docs.splunk.com/observability/metrics-and-metadata/metrics.html)

### Metric Dimensions, Custom Properties, and Tags

|Metadata|Created|Format|Used for?|Group by?|
|:-:|-|-|-|-|-|
|Dimensions|When Observability Cloud ingests data|Key-value pair|Metrics|Yes|
|Custom properties|After ingest, through the user interface or REST API|Key-value pair|Metrics, dimensions, tags, charts, and detectors|Yes|
|Tags|After ingest, through the user interface or REST API|String|Dimensions, charts, and detectors|No|

**Dimensions** = *immutable* key-value pairs sent in with metrics **at the time of ingest** to add context to the metrics
	- Examples: `"hostname":"server1"`, `"host_location":"Tokyo"`
	- A data point can have one or more dimensions. For example, a dimension can be a host or instance for infrastructure metrics, or it can be an application component or service tier for application metrics.
	- This is what determines a metric time series (MTS), which is a collection of data points that have the same metric AND the same dimension key-value pairs.
	- **When do I apply dimensions?** When you need to define a unique metric time series (remember that each unique combination of dimensions counts as 1 MTS), or when you want to keep track of historical values for your metadata (e.g. adding a dimension for `version`).
	- You can define up to 36 dimensions per MTS. See full list of dimension criteria [here](https://docs.splunk.com/observability/metrics-and-metadata/metrics-dimensions-mts.html#dimensions-criteria).

**Custom properties** = key-value pairs applied to metrics or dimensions **after ingest** to add context to the metrics or dimensions
	- Examples: 
	- When Splunk Observability Cloud assigns a different name to a dimension coming from an integration or monitor, the dimension becomes a custom property as it is assigned to the metric after ingest. 
		- For example, the AWS EC2 integration sends the `instance-id` dimension, and Observability Cloud renames the dimension to `aws_instance_id`. This *renamed* dimension is now a *custom property*. See [Guidance for metric and dimension names](https://docs.splunk.com/observability/metrics-and-metadata/metric-names.html) for more.
	- You can also assign your own custom properties to dimensions of existing metrics. 
		- For example, you can add the custom property `use: QA` to the host dimension of your metrics to indicate that the host that is sending the data is used for QA. The custom property `use: QA` then propagates to all MTS with that dimension value. 
	- You can also add custom properties to charts and detectors. In this case, the custom properties identify some aspect of the chart or detector that you can query.
	- **When do I apply custom properties?** When you have metadata that provides additional context for your metrics, but you don’t need the metadata for the MTS to be uniquely identifiable (unlike dimensions, 1 MTS isn't determined by a unique combination of custom properties). Or, when you have metadata you know you want to make changes to in the future (dimensions are immutable).
	- **How do I apply custom properties?** See [Search and edit metadata using the Metadata Catalog](https://docs.splunk.com/observability/metrics-and-metadata/metrics-finder-metadata-catalog.html#search-edit-metadata).
	- You can define up to 75 custom properties per dimension. See full list of custom properties criteria [here](https://docs.splunk.com/observability/metrics-and-metadata/metrics-dimensions-mts.html#custom-properties-criteria).

**Tags** = labels or keywords (not key-value pairs) applied to metrics, dimensions, detectors, and other objects **after ingest**
	- Examples: 
	- Use tags when you want to give the same searchable value to multiple dimensions/custom properties, or charts/detectors, for easy filtering.
	- You can apply custom properties to tags. When you do this, anything that has that tag inherits the properties associated with the tag. For example, if you associate the `"tier:web"` custom property with the `"apps-team"` tag, Observability Cloud attaches the `"tier:web"` custom property to any metric or dimension that has the `"apps-team"` tag. 
	- **When do I apply tags?** Use tags when there is a one-to-many relationship between the tag and the objects you are assigning it to (one tag can be applied to many different resources and is not a unique identifier).
	- **How do I apply tags?** See [Search and edit metadata using the Metadata Catalog](https://docs.splunk.com/observability/metrics-and-metadata/metrics-finder-metadata-catalog.html#search-edit-metadata).
	- You can have up to 50 tags per dimension/custom property/chart/detector. See full list of custom properties criteria [here](https://docs.splunk.com/observability/metrics-and-metadata/metrics-dimensions-mts.html#tags-criteria).

Sources:
- [Metrics, data points, and metric time series](https://docs.splunk.com/observability/metrics-and-metadata/metrics.html)
- [Dimensions, custom properties, and tags](https://docs.splunk.com/observability/metrics-and-metadata/metrics-dimensions-mts.html)

## cURL Ingestion Method

## Programmatic Ingestion Method
### Python

### Java

## Viewing Custom Metrics Usage
### Usage by Token

### Overall Usage