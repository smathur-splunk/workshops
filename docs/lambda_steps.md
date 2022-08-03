### Create the microservices environment (GUI)
1. Download [this CloudFormation template](https://github.com/smathur-splunk/lambda-apm-workshop/blob/main/AlpacaTraderWorkshopIncomplete.template). This template contains all the objects (and code) that are needed for the microservices app that you will instrument.
2. Navigate to [CloudFormation in the AWS console](https://console.aws.amazon.com/cloudformation/home?region=us-east-1). **Make sure you are in the 'us-east-1' (N. Virginia) region!!! The CloudFormation template is written for that region ONLY.**
3. At the top-right, click `Create stack` > `With new resources (standard)`.
4. On the 'Create stack' page, select `Upload a template file`, and then `Choose file` to select the CloudFormation template you downloaded in Step 1. Click `Next`. <img src="https://smathur-splunk.github.io/workshops/images/step04.png" style="width:50%"/>
5. To complete the CloudFormation stack creation, give the stack a name (e.g. `lambda-stack`), and under 'Parameters', enter a name for the S3 bucket to be used by the microservices app. Click `Next`. Note that this name **must be unique across all of AWS**.
6. On the next page titled 'Configure stack options', scroll all the way down and click `Next`. Finally, on the 'Review' page, scroll to the bottom, and select the checkbox that says 'I acknowledge that AWS CloudFormation might create IAM resources with custom names.' Then click `Create stack`.
7. You should now see that your stack has a status of 'CREATE_IN_PROGRESS'. Wait until it says 'CREATE_COMPLETE' (or spam the refresh button, your choice). You now have a microservices app running on AWS Lambda!

### Create the microservices environment (CLI)
1. This CLI Command can be executed by either pointing the `--template-body` parameter to the local path of the Cloudformation template file, or passing `--template-url <An URL to an S3-based location of a template file>`
2. Execute the following AWS CLI Command:
```bash
aws cloudformation create-stack \
--stack-name <some-arbitrary-name> \
--template-body file://<local-path-to-'AlpacaTraderWorkshopIncomplete.template'> \
--region us-east-1 \
--parameters ParameterKey=bucketName,ParameterValue=<some-arbitrary-s3-bucket-name> \
--capabilities CAPABILITY_NAMED_IAM \
--role-arn <the-cfn-serivce-account-role-arn>
```
As an example:
```bash
aws cloudformation create-stack \
--stack-name lambda-demo-tsj-splunk-100 \
--template-body file:///Users/tjohander/splunk/projects/lambda-apm-workshop/AlpacaTraderWorkshopIncomplete.template \
--region us-east-1 \
--parameters ParameterKey=bucketName,ParameterValue=tsj-splunk-alpaca-bucket-100 \
--capabilities CAPABILITY_NAMED_IAM \
--role-arn arn:aws:iam::12345678:role/cloudformation-service-role
```

### Instrument the Lambda functions
8. Navigate to [AWS Lambda](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions) and take a moment to understand the functions in this app. There are 4 of them: 'watchlistUpdater', 'stockRanker', 'getFinancials', and 'buyStocks'. The architecture of these functions will become clear once you instrument them for APM.
9. Navigate to the Splunk O11y 'Data Setup' page, and search for `lambda` (you may have to click `Extend search across all integrations`). Select `AWS Lambda (Serverless instrumentation)`, and click `Add Integration`.
10. For 'Function name', enter the name of the first Lambda function you will instrument (e.g. `watchlistUpdater`). Select your Splunk access token (make sure it has the right permissions for APM), and enter a name for this app's environment (e.g. `lambda-app`). Click 'Next'. **Make sure the environment name is the same for all your functions in this app.**
11. On the 'Install Integration' page, select `Python`. Follow the steps on this page to add the Splunk OTel layer and set the environment variables. For the ARN, use `arn:aws:lambda:us-east-1:254067382080:layer:splunk-apm:51`. <img src="https://smathur-splunk.github.io/workshops/images/step11-1.png" style="width:50%"/> <img src="https://smathur-splunk.github.io/workshops/images/step11-2.png" style="width:50%"/> <img src="https://smathur-splunk.github.io/workshops/images/step11-3.png" style="width:80%"/> <img src="https://smathur-splunk.github.io/workshops/images/step11-4.png" style="width:50%"/> <img src="https://smathur-splunk.github.io/workshops/images/step11-5.png" style="width:80%"/> <img src="https://smathur-splunk.github.io/workshops/images/step11-6.png" style="width:50%"/>
12. Phew! That was a lot. Now repeat Step 11 for all 4 Lambda functions. (You do not need to go through the Splunk O11y GDI wizard again; simply make the changes necessary in AWS.)

### Run the app to generate APM data
13. Time to finally run the code and see some data! Manually run these 3 functions in order: 'watchlistUpdater', 'stockRanker', and 'buyStocks'. To run them, open up each function, and under the 'Function overview' section, click on the `Test` tab. Enter an event name (e.g. `test`), and at the top right, click the orange `Test` button. <img src="https://smathur-splunk.github.io/workshops/images/step13.png" style="width:50%"/>
14. If 'watchlistUpdater' and 'stockRanker' run as expected, you should see 'Execution result: succeeded'.
15. When running the 'buyStocks' function, you will get an error--**this is expected!** If you go into the service map in Splunk APM, you will now see that all 4 of our functions are there, as well as the S3 bucket that some of them are talking to. There will be a red circle for 'buyStocks', indicating that an error occurred! This is especially useful if Lambda functions are scheduled to run automatically, in which case errors won't be immediately apparent without APM. <img src="https://smathur-splunk.github.io/workshops/images/step18.png"/>
16. In the APM service map, click on `buyStocks` and select `Traces` on the right. Find the trace with the error we just saw, and see if you can find the issue. If not, go to the next step.
17. Go back to the AWS Lambda page for 'buyStocks' and in 'index.py', uncomment line 13. Click `Deploy` to save your changes.
```python
def lambda_handler(event, context):
    s3 = boto3.client('s3')
    alpaca_id = "PK6MU6XGW0KY0SSI402E"
    alpaca_secret = "ZBvSlwEB8mk1DnbFZHCm18mkmeYdxVLu5nw6c8cR"
    headers = {'APCA-API-KEY-ID':alpaca_id, 'APCA-API-SECRET-KEY':alpaca_secret}
  
    rankings_file = s3.get_object(Bucket=os.environ['BUCKET_NAME'], Key='rankings.txt')
    #stock_ranking = rankings_file['Body'].read().decode('utf-8').split(' ')
    # ^^^ UNCOMMENT THE LINE ABOVE
```
18. Go to the `Test` tab and run this function again. You should now see 'Execution result: succeeded', and another trace should pop up in Splunk APM as well (this time without any errors).

### [Optional] Add custom span tags for additional info
19. Custom span tags are already added for 3 of the functions. Let's take a look at how to add custom span tags in the 4th one, 'getFinancials'. Open up the 'getFinancials' Lambda function.
20. Under line 2, add a new line and write `from opentelemetry import trace`.  Under line 6, add **with proper indentation** 
```python
customizedSpan = trace.get_current_span()
customizedSpan.set_attribute("symbol", ticker);
customizedSpan.set_attribute("finnhub.token", "brqivm7rh5rc4v2pmq8g");
```
The final result should look like this:
```python
import json
import requests
from opentelemetry import trace

def lambda_handler(event, context):
    ticker = event['symbol']
    
    customizedSpan = trace.get_current_span()
    customizedSpan.set_attribute("symbol", ticker);
    customizedSpan.set_attribute("finnhub.token", "brqivm7rh5rc4v2pmq8g");
```
Source: [Instrument your application code to add tags to spans](https://docs.splunk.com/Observability/apm/span-tags/add-context-trace-span.html#instrument-your-application-code-to-add-tags-to-spans)

21. Click `Deploy` to save your changes. Now if you run 'stockRanker' and look at the traces for 'getFinancials' in Splunk APM, you'll see that each span has tags for the stock symbol being analyzed and the API token being used. This can help with troubleshooting, in case of any errors. <img src="https://smathur-splunk.github.io/workshops/images/step21.png"/>