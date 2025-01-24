
#update dynamo db 
dynamodb.update_item(
        TableName=DYNAMODB_TABLE,
        Key={'fileName': {'S': file_name}},
        UpdateExpression='SET lastUpdated = :time',
        ExpressionAttributeValues={
            ':time': {'S': last_modified}
        }
    )