

### Steps:
1. **Set up AWS EventBridge**:
   - Use EventBridge to trigger the Lambda function on a schedule using a cron expression.

2. **Install Required Libraries**:
   - Use the `paramiko` library to connect to the SFTP server.
   - Use the `boto3` library to interact with DynamoDB.

3. **Python Lambda Code**:

```python
import boto3
import paramiko
import datetime

# SFTP configuration
SFTP_HOST = 'sftp-server-host'
SFTP_PORT = 22
SFTP_USERNAME = 'your-username'
SFTP_PASSWORD = 'your-password'
REMOTE_DIR = '/remote/path/'  # Directory to monitor

# DynamoDB configuration
DYNAMODB_TABLE = 'YourDynamoDBTableName'

# Initialize DynamoDB client
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    # Initialize the SFTP connection
    try:
        transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
        transport.connect(username=SFTP_USERNAME, password=SFTP_PASSWORD)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # List files in the directory
        files = sftp.listdir_attr(REMOTE_DIR)

        for file_attr in files:
            file_name = file_attr.filename
            last_modified = datetime.datetime.fromtimestamp(file_attr.st_mtime).isoformat()

            # Update DynamoDB with file info
            dynamodb.update_item(
                TableName=DYNAMODB_TABLE,
                Key={'fileName': {'S': file_name}},
                UpdateExpression='SET lastUpdated = :time',
                ExpressionAttributeValues={
                    ':time': {'S': last_modified}
                }
            )
            print(f"Updated {file_name} in DynamoDB with last modified time {last_modified}.")

        # Close SFTP connection
        sftp.close()
        transport.close()

        return {'statusCode': 200, 'body': 'Files processed successfully.'}

    except Exception as e:
        print(f"Error: {e}")
        return {'statusCode': 500, 'body': str(e)}
```

---

### Key Components of the Code:
1. **SFTP Connection**:
   - Connect to the SFTP server using `paramiko`.
   - Use `listdir_attr()` to list files and fetch their metadata (e.g., `st_mtime` for last modified time).

2. **DynamoDB Update**:
   - Use `boto3.client('dynamodb')` to interact with DynamoDB.
   - The `update_item()` method updates or inserts records, using `fileName` as the primary key.

3. **Cron Job with EventBridge**:
   - Set up an EventBridge rule to trigger the Lambda function periodically using a cron expression (e.g., every 5 minutes).

4. **File Metadata**:
   - The file's last modified timestamp (`st_mtime`) is converted to ISO format and stored in DynamoDB.

---

### Advantages of this Approach:
- **Serverless**: No need for server management; AWS Lambda handles scaling.
- **Cost-Effective**: Pay only for execution time.
- **DynamoDB**: Scalable and efficient for storing file metadata.

Let me know if you want to dive deeper into EventBridge or need help deploying this Lambda function!