from dynamo_connect import get_table

def delete_customer(customer_name):
    
    table = get_table('customers')
    
    response = table.delete_item(
        Key={
            'name' : customer_name
        }
    )
