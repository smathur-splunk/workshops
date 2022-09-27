# ⚠️ Under Construction ⚠️
## Finding Custom Metrics
### Query Metrics (API method)

1. Review the table below for a quick guide on querying metrics and metric metadata via the API ([API Reference docs](https://dev.splunk.com/observability/reference/api/metrics_metadata/latest))
 
	| Query | URL |
	|---|---|
	| Query metric | `https://api.<realm>.signalfx.com/v2/metric?query=name:<metricname>` |
	| Query `dimension:value` pair | `https://api.<realm>.signalfx.com/v2/dimension?query=<dim>:<val>` |
	| Check if property exists | `https://api.<realm>.signalfx.com/v2/dimension?query=_exists_:<prop>` |

	*NOTE: The arguments that are passed in the cURL statement must be URL encoded. To find the correct URL encoding for the customer name, refer to [this guide](https://www.w3schools.com/tags/ref_urlencode.ASP). For example: `Buttercup, Inc.` is encoded as `Buttercup%2C%20Inc%2E`.*

2. As an example, try querying the custom metric that you created in the previous section.

	```bash
	curl -X GET "https://api.<realm>.signalfx.com/v2/metric?query=name:<metricname>" \
	    -H "Content-Type: application/json" \
	    -H "X-SF-TOKEN: <value>"
	```

### Metric Finder (UI method)

1. The other way to find metrics in Splunk Observability is using the Metric Finder. From the left sidebar, navigate to Metric Finder. You can view metrics across your various integrations here, and also search for custom metrics.

	![Metric Finder](images/custom_finder.png)

2. With the resulting metrics, you can inspect the related properties. Clicking on the metric name will open up a chart for the metric, which you can use to start building out some custom dashboards and alerts.

	![Metric Finder search results](images/custom_search.png)

## Customizing Charts

1. In Metric Finder, search for and click on the custom metric that you generated in the [previous section](https://smathur-splunk.github.io/workshops/custom_metr). This will open up a chart that we can modify and add to a custom dashboard.

![Custom metric default chart](images/custom_chart.png)

### Chart Types

2. Next, we'll explore each type of visualization with this custom metric. Source: [Chart types in Splunk Observability Cloud](https://docs.splunk.com/observability/data-visualization/charts/chart-types.html)

	- Line/area/column chart

		These 3 charts are similar in nature and display MTS values over time. 

		- Chart options:
			- Area and column charts can be stacked.
			- Color legend can be displayed for all 3 charts (useful when there are multiple MTS).
			- For the Y-axis, the label, min/max, units, and precision can be configured.

		| Line chart | Area chart | Column chart |
		|---|---|---|
		| ![Line chart](images/custom_line.png) | ![Area chart](images/custom_area.png) | ![Column chart](images/custom_column.png) |

	- Histogram

		Histograms will display MTS in a single color. 

		- Chart options:
			- For the Y-axis, the label, min/max, units, and precision can be configured.

		![Histogram chart](images/custom_histogram.png)

	- List

		Lists are useful for looking at the latest values of multiple MTS. 

		- Chart options:
			- Color by value to indicate severity. 
			- Refresh rate, sorting, and precision
			- Dimensions listed next to each value can be shown or hidden as needed (e.g. host name, environment, service name, etc.)
			- A secondary visualization can be enabled to display a sparkline with historical values, or a radial or linear scale for severity.

		![List view](images/custom_listview.png)

	- Single value

		The single value display behaves similarly to the list view. 

		- Chart options:
			- Color by scale
			- Precision, refresh rate
			- Secondary visualizations (sparkline, radial/linear scale)

		![Single value](images/custom_singlevalue.png)

	- Heatmap

		Heatmaps can be used to quickly identify severity across a number of MTS representing individual instances, services, hosts, functions, etc.

		- Chart options:
			- Refresh rate
			- Sorting, grouping by dimensions
			- Color by fixed or automatic scale

		| Heatmap (custom metric) | Heatmap (demo data) |
		|---|---|
		| ![Heatmap](images/custom_heatmap.png) | ![Demo heatmap](images/custom_demoheatmap.png) |

	- Text

		Splunk Observability supports creating "text" panels that support both Markdown and HTML. These panels also allow for adding images, which should be converted to base64. Text panels can be useful for dividing a dashboard into sections, making it easier to read.

	- Table

		Raw data can also be displayed along with its dimensions in the form of a data table. Precision and refresh rate can be customized.

		![Data table](images/custom_datatable.png)

3. After reviewing the various chart types and opening up your custom metric in a chart, select a chart type of your choice. Explore the "Chart Options" tab and customize the chart to your liking.

### Filters

### Analytic Functions

### Rollups

### SignalFlow

## Customizing Dashboards
### Dashboard Variables

### Text Notes (Markdown, HTML)

## Dashboard Permissions

Part of the strategy you may have with your dashboards is to align them to certain teams or audiences, so setting the right read/write permissions is key.