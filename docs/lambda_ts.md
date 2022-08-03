### CloudFormation stack creation failed. Check the S3 bucket name.
S3 bucket names must be unique across the entirety of AWS, so make sure that when you create your CloudFormation stack, you enter a unique name in the 'bucketName' parameters field.

### Data is not being sent into Splunk Observability. Check your Splunk access token.
Ensure that the Splunk access token you have used has the right permissions for APM data.

### Lambda functions won't run. Check for indentation issues.
Don't forget to indent your code the proper amount when adding custom span tags, or the Python code won't be able to run.

### In the APM service map, services aren't connected to each other. Check the environment name.
Make sure the environment name (`OTEL_RESOURCE_ATTRIBUTES` environment variable in Lambda configuration) is the same for all your functions in this app.