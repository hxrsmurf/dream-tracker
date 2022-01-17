# This gets the CloudFormation output.
import boto3

def get():
    client = boto3.client('cloudformation')

    response = client.describe_stacks(
            StackName='dream-tracker-sam'
    )

    output_keys = response['Stacks'][0]['Outputs']

    for output in output_keys:
        if output['OutputKey'] == 'Table':
            table_name = output['OutputValue']
        elif output['OutputKey'] == 'Topic':
            topic_arn = output['OutputValue']

    return table_name, topic_arn