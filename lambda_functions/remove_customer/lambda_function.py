from remove_customer import delete_customer

def lambda_handler(event, context):
    delete_customer(event['name'])
