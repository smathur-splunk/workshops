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