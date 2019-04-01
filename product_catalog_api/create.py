import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the product item.")
        return

    photographer_email = 'None' if 'photographer' not in data else data['photographer']

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': data['id'],
        'description': data['description'],
        'price': data['price'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
        'photographer': photographer_email
    }

    # write the todo to the dynamo database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response