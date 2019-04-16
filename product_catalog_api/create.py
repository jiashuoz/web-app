import json
import logging
import os
import time
import uuid

import boto3
dynamodb = boto3.resource('dynamodb')


def create(event, context):
    lambda_start = time.time()
    print(event)
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't create the product item.")
        return

    photographer_email = 'None' if 'photographer' not in data else data['photographer']

    db_start = time.time()
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': data['id'],
        'description': data['description'],
        'price': data['price'],
        'photographer': photographer_email
    }

    # write the todo to the dynamo database
    table.put_item(Item=item)
    db_end = time.time()

    run_time = {
        "db_time": db_end - db_start,
        "lambda_time": time.time() - lambda_start
    }
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(run_time)
    }
    return response