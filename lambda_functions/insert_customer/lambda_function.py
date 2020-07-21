from put_customers import put_data

def lambda_handler(event, context):
    put_data(event)
