# ⚠️ Under Construction ⚠️
## Finding Custom Metrics
### Query Metrics (API method)
[API Reference docs](https://dev.splunk.com/observability/reference/api/metrics_metadata/latest) 

You may refer to the following HTTP GET endpoints when doing this task:
 
- Query metric: `https://api.<realm>.signaflx.com/v2/metric/<metricname>`
- Query dimension:value `https://api.<realm>.signaflx.com/v2/dimension?query=<dim>:<val>`
- Check if property exists: `https://api.<realm>.signaflx.com/v2/dimension?query=_exists_:<prop>`

NOTE: The arguments that are passed in the cURL statement must be URL encoded. To find the correct URL encoding for the customer name, refer to [this guide](https://www.w3schools.com/tags/ref_urlencode.ASP). For example: `Zeus, Inc.` is encoded as `Zeus%2C%20Inc%2E`.

### Metric Finder (UI method)

## Customizing Charts
### Filters

### Analytic Functions

### Rollups

### SignalFlow

## Customizing Dashboards
### Dashboard Variables

### Text Notes (Markdown, HTML)

## Dashboard Permissions