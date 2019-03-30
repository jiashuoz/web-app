import json
import time
import logging
import os

from product_catalog_api import decimalencoder
import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])
    if 'id' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the product item.")
        return

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the product's price in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#product_catalog_price': 'price',
        },
        ExpressionAttributeValues={
          ':price': data['price'],
          ':updatedAt': timestamp,
        },
        UpdateExpression='SET #product_catalog_price = :price, '
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'],
                           cls=decimalencoder.DecimalEncoder)
    }

    return response