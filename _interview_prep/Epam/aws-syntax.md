CloudWatch 
->  cloudwatch.put_metric_data(
               Namespace='MyApp',
               MetricData=[
                   {
                       'MetricName': 'UsersCreated',
                       'Value': 1,
                       'Unit': 'Count'
                   },
               ]
           )

Lambda: 
->  lambda.invoke(
               FunctionName='MyFunction',
               InvocationType='Event',
               Payload=b'{}'
           )
        
           #before put item we need to convert to python dict
           data = json.loads(event['body'])
           item = {
               'PostID': "PostID",
               'Title': data['title'],
               'Content': data['content'],
               'Author': data['author'],
               'CreatedAt': data['created_at']
           }
           table.put_item(Item=item) 
           
sns = boto3.client('sns')

    def publish_order_confirmation(order_details):
        sns.publish(
            TopicArn='arn:aws:sns:region:account-id:OrderConfirmation',
            Message=json.dumps({'default': json.dumps(order_details)}),
            MessageStructure='json'
        )