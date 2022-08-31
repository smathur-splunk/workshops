### [Optional] Add custom span tags for additional info
19. Custom span tags are already added for 3 of the functions. Let's take a look at how to add custom span tags in the 4th one, 'getFinancials'. Open up the 'getFinancials' Lambda function.
20. Under line 2, add a new line and write `from opentelemetry import trace`.  Under line 6, add **with proper indentation** 
```python
customizedSpan = trace.get_current_span()
customizedSpan.set_attribute("symbol", ticker)
customizedSpan.set_attribute("finnhub.token", "brqivm7rh5rc4v2pmq8g")
```
The final result should look like this:
```python
import json
import requests
from opentelemetry import trace

def lambda_handler(event, context):
    ticker = event['symbol']
    
    customizedSpan = trace.get_current_span()
    customizedSpan.set_attribute("symbol", ticker)
    customizedSpan.set_attribute("finnhub.token", "brqivm7rh5rc4v2pmq8g")
```
Source: [Instrument your application code to add tags to spans](https://docs.splunk.com/Observability/apm/span-tags/add-context-trace-span.html#instrument-your-application-code-to-add-tags-to-spans)

21. Click `Deploy` to save your changes. Now if you run 'stockRanker' and look at the traces for 'getFinancials' in Splunk APM, you'll see that each span has tags for the stock symbol being analyzed and the API token being used. This can help with troubleshooting, in case of any errors. <img src="https://smathur-splunk.github.io/workshops/images/step21.png"/>