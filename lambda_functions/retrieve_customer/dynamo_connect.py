import boto3
from boto3.dynamodb.conditions import Key

def get_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
    return table
