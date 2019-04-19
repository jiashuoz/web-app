import os
import json
import time

import boto3
dynamodb = boto3.resource('dynamodb')


def delete(event, context):
    lambda_start = time.time()
    print(event)

    db_start = time.time()
    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    # delete the product from the database
    table.delete_item(
        Key={
            'id': event['pathParameters']['id']
        }
    )
    db_end = time.time()

    body = {
        "message": "deleted!",
        "id": event['pathParameters']['id']
    }

    run_time = {
        "message": "deleted!",
        "db_time": db_end - db_start,
        "lambda_time": time.time() - lambda_start
    }
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(run_time)
    }

    return response