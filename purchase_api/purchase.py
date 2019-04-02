import json
import os
import time

from product_catalog_api import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')

SENDER = "retail web <jiashuoz@outlook.com>"
AWS_REGION = "us-east-1"
SUBJECT = "Order complete"
BODY_TEXT = "Order information:\r\n"

BODY_HTML = """<html>
<head></head>
<body>
  <h1>Request for a photo for new products</h1>
  <p></p>
</body>
</html>
            """
CHARSET = "UTF-8"
client = boto3.client('ses',region_name=AWS_REGION)

def purchase(event, context):
    product_table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    transaction_table =  dynamodb.Table(os.environ['TRANSACTION_TABLE'])

    # fetch todo from the database
    result = product_table.get_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )

    BODY_TEXT = "Order information:\r\n" + result

    RECIPIENT = event['pathParameters']['email']

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
            # If you are not using a configuration set, comment or delete the
            # following line
            # ConfigurationSetName=CONFIGURATION_SET,
        )
        timestamp = int(time.time() * 1000)
        item = {
            'order_id': timestamp,
            'email': event['pathParameters']['email'],
            'product_id': event['pathParameters']['id']
        }
        transaction_table.put(Item=item)
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID: " + response['MessageId'])
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
    }

    return response