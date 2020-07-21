from dynamo_connect import get_table
from boto3.dynamodb.conditions import Key

def get_user_data(name):
    
    table = get_table('customers')
    
    response = table.query(
        KeyConditionExpression=Key('name').eq(name)
    )

    items = response['Items']
    
    return items
