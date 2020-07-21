from dynamo_connect import get_table


def put_data(customer_data):
    
    table = get_table('customers')
    
    customer = {
        'name' : customer_data['name'],
        'first_name' : customer_data['first_name'],
        'last_name' : customer_data['last_name'],
        'company_name' : customer_data['company_name'],
        'address' : customer_data['address'],
        'city' : customer_data['city'],
        'county' : customer_data['county'],
        'state' : customer_data['state'],
        'zip' : customer_data['zip'],
        'phone1' : customer_data['phone1'],
        'phone2' : customer_data['phone2'],
        'email' : customer_data['email'],
        'web' : customer_data['web']
    }
    
    response = table.put_item(Item=customer)
    
    return response
