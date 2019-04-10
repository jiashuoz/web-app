import json
import os
import time

from product_catalog_api import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

def purchase(event, context):
    product_table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    transaction_table =  dynamodb.Table(os.environ['TRANSACTION_TABLE'])

    # # fetch todo from the database
    # result = product_table.get_item(
    #     Key={
    #         'id': event['pathParameters']['id']
    #     }
    # )

    # create a response
    response = {
        "statusCode": 200,
        # "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
        "body": json.dumps(event)
    }

    return response