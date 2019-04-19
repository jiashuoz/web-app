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

    db_init_start = time.time()
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    db_init_end = time.time()

    item = {
        'id': data['id'],
        'description': data['description'],
        'price': data['price'],
        'photographer': photographer_email
    }

    # write the todo to the dynamo database
    db_put_start = time.time()
    table.put_item(Item=item)
    db_put_end = time.time()

    run_time = {
        "db_init_time": db_init_end - db_init_start,
        "db_put_time": db_put_end - db_put_start,
        "lambda_time": time.time() - lambda_start
    }
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(run_time)
    }
    return response