At this point, you've created a microservices app in AWS using a CloudFormation template, and instrumented it for Splunk APM. As you probably noticed, the process of instrumenting Lambda functions for APM is simple, but tedious. This is where CloudFormation can help. For this workshop, the process of creating the app was automated, but the instrumentation can be automated too.

To see what the final result *should* look like if you did everything correctly (and how the instrumentation process can be automated), create a stack with [this CloudFormation template](https://github.com/smathur-splunk/lambda-apm-workshop/blob/main/AlpacaTraderWorkshop.template) and run the 3 functions in the same order: 'watchlistUpdater', 'stockRanker', and 'buyStocks'.

Alternatively, the final state can be deployed with the following AWS CLI Command, executed from the root of this project directory:
```bash
aws cloudformation create-stack \
--stack-name <some-arbitrary-name> \
--template-body <local-path-to-'AlpacaTraderWorkshop.template'> \
--region us-east-1 \
--parameters ParameterKey=bucketName,ParameterValue=<some-arbitrary-s3-bucket-name> \
--capabilities CAPABILITY_NAMED_IAM \
--role-arn <the-cfn-serivce-account-role-arn>
```