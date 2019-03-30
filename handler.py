import json


def hello(event, context):

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    # if ('queryStringParameters' in event and 'name' in event['queryStringParameters']):
    #     body["message"] = "hello, " + event['queryStringParameters']['name'] + ", nice to meet you!"
    #     response = {
    #         "statusCode": 200,
    #         "body": json.dumps(body)
    #     }
    #     return response

    # if event['httpMethod'] == 'POST' and event['body'] != None:
    #     jsonObject = json.loads(event['body'])
    #     body['message'] = "Hi, I recevied a json object from you"
    #     body['input'] = jsonObject
    #     response = {
    #         "statusCode": 200,
    #         "body": json.dumps(body)
    #     }
    #     return response
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
