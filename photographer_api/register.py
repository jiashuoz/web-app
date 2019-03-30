import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def register(event, context):
    data = json.loads(event['body'])
    if 'email' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the product item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['PHOTOGRAPHER_TABLE'])

    item = {
        'email': data['email'],
        'password': data['password'],
        'name': data['name']
    }

    # write the todo to the dynamo database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response