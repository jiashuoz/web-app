import json
import os
import time
import datetime

from product_catalog_api import decimalencoder
import boto3

dynamodb = boto3.resource('dynamodb')

def purchase(event, context):
    product_table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
    credit_card_table = dynamodb.Table(os.environ['CREDITCARD_TABLE'])
    transaction_table =  dynamodb.Table(os.environ['TRANSACTION_TABLE'])

    data = json.loads(event['body'])

    # # fetch todo from the database
    credit_card_number = data['credit_card_number']
    credit_card_holder = data['credit_card_holder']

    credit_card_lookup_result = credit_card_table.get_item(
        Key={
            'credit_card_id': credit_card_number
        }
    )
    
    if 'Item' not in credit_card_lookup_result or credit_card_lookup_result['Item']['name'] != credit_card_holder:
        response = {
            "statusCode": 400,
            # "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
            "body": json.dumps({"error": "credit card info incorrect"})
        }
        return response
    print(credit_card_lookup_result)
    product = product_table.get_item(
        Key={
            'id': data['id']
        }
    )
    
    item = {
        'order_id': data['id'] + data['credit_card_number'],
        'time_created': str(datetime.datetime.utcnow())
    }

    transaction_table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        # "body": json.dumps(result['Items'], cls=decimalencoder.DecimalEncoder)
        "body": json.dumps(event)
    }

    return response