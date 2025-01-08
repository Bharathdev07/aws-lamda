import json

def lambda_handler(event, context):
    # Extract query parameters if available
    name = event.get('queryStringParameters', {}).get('name', 'World')
    
    # Response body
    response = {
        "message": f"Hello, {name}!",
        "input": event
    }
    
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response)
    }
