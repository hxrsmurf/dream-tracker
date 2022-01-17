# This publishes to the SNS Topic.

import boto3

def publish(topic_arn, body, subject='Dream'):
    sns_client = boto3.client('sns')

    response = sns_client.publish(
        TargetArn=topic_arn,
        Message=body,
        Subject=subject
    )

    return response