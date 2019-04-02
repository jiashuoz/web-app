import json
import time
import logging
import os

import boto3
from botocore.exceptions import ClientError

# Replace sender@example.com with your "From" address.
# This address must be verified with Amazon SES.
SENDER = "retail web <jiashuoz@outlook.com>"

# Replace recipient@example.com with a "To" address. If your account 
# is still in the sandbox, this address must be verified.
# RECIPIENT = "recipient@example.com"

# Specify a configuration set. If you do not want to use a configuration
# set, comment the following variable, and the 
# ConfigurationSetName=CONFIGURATION_SET argument below.
# CONFIGURATION_SET = "ConfigSet"

# If necessary, replace us-west-2 with the AWS Region you're using for Amazon SES.
AWS_REGION = "us-east-1"

# The subject line for the email.
SUBJECT = "Request for a photo for new products"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Request for a photo for new products\r\n")
            
# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Request for a photo for new products</h1>
  <p></p>
</body>
</html>
            """

# The character encoding for the email.
CHARSET = "UTF-8"

# Create a new SES resource and specify a region.
client = boto3.client('ses',region_name=AWS_REGION)

def request(event, context):
    for record in event['Records']:
        print(record['eventID'])
        print(record['eventName'])
        if record['eventName'] == 'INSERT':
            dynamoDB = record['dynamodb']
            if dynamoDB['NewImage']['photographer']['S'] != 'None':
                print(dynamoDB['NewImage']['photographer']['S'])
                RECIPIENT = dynamoDB['NewImage']['id']['S']
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
                # Display an error if something goes wrong.	
                except ClientError as e:
                    print(e.response['Error']['Message'])
                else:
                    print("Email sent! Message ID: " + response['MessageId'])
    print(event)