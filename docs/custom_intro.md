This workshop will give you a better understanding of how metrics work in Splunk Observability. It will guide you through the process of creating custom metrics (using multiple methods) and building custom dashboards.

## Requirements

- Terminal/Command line: for running cURL commands to send custom metrics
- Python 3: for generating data and sending custom metrics
	- You will need to have `pip` and the `requests` library installed. 
		- To install `pip`, follow the steps [here](https://pip.pypa.io/en/stable/installation).
		- To install `requests`, run `pip install requests`
- Access to a Splunk Observability org
	- You will need an **ingest** type access token (there should be a default that you can use)

## Key Assumptions

This workshop assumes that you have:

- Some Python experience (not needed but helpful to have)
- Some familiarity with building charts and dashboards in Splunk Observability