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