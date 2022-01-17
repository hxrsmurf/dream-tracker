import json
import cloudformation as cloudformation
import twilio as twilio
import sns as sns
import dynamodb as dynamodb
import timestamp as timestamp
import base64

def handler(event, context):

    # I don't know why I have to do this, but it works to extract the API Gateway event.
    event = json.dumps(event)
    event = json.loads(event)

    # Get the CloudFormation Output values
    table_name, topic_arn = cloudformation.get()

    try:
        event_body = str((base64.b64decode(event['body'])), "utf-8")
        message = event_body.split("&")

        # Test Message
        # message = ['From=%2B555555' , 'Body=Test Message']
        user, body = twilio.parse(message)

        sns_result = sns.publish(topic_arn, body)['ResponseMetadata']['HTTPStatusCode']
        dynamodb_result = dynamodb.write(timestamp.get(), table_name, user, body)['ResponseMetadata']['HTTPStatusCode']

        if sns_result == 200 and dynamodb_result == 200:
            message = 'Save OK'
            print(message)

            # Twilio requires this so no error on their end and I don't want to send a text back.
            result = {
                "statusCode": 200
            }

            return result
        else:
            message = 'There was an error.'
            print(message)
            sns.publish(topic_arn, message, 'Error - Dream Function')
            return(message)
    except:
        message = 'Pretend error'
        sns.publish(topic_arn, message, 'Error - Dream Function')
        return(message)