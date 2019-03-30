import json


def hellopost(event, context):

    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    if event['httpMethod'] == 'POST' and event['body'] != None:
        body['message'] = "Hi, I recevied a json object from you"
        response = {
            "statusCode": 200,
            "body": json.dumps(body)
        }
        return response
    
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
