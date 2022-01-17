# This writes to the DynamoDB.
import boto3

def write(timestamp, table_name, user, body):
    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName=table_name,
        Key={
            'id': {
                'S': timestamp
            }
        },
        AttributeUpdates={
            'user': {
                'Value': {
                    'S': user
                }
            },
            'body': {
                'Value': {
                    'S': body
                }
            }
        }
    )

    return response