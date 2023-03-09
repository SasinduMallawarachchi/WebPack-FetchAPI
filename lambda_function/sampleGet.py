import json

def lambda_handler(event, context):
    
    employees_list = [
    {
        'id': '1',
        'first_name': "Janith",
        'last_name': "Dilshan",
        'email': "dilshan@gmail.com"
    },
    {
        "id": '2',
        "first_name": "Anutha",
        "last_name": "Rathnayake",
        "email": "anuka@gmail.com"
    },
    {
        "id": '3',
        "first_name": "Ann",
        "last_name": "Perera",
        "email": "ann@gmail.com"
    }

    ]
    
    employee_id = event['queryStringParameters']['id']
    
    response = {}
    response['statusCode'] = 200
    response['headers'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    }
    
    for employee in employees_list:
        if employee['id'] == employee_id:
            response['body'] = json.dumps(employee)
            return response
    
    response['body'] = json.dumps("Employee Not Found")
    return response        
   

import json

def lambda_handler(event, context):
    
    employees_list = [
    {
        'id': '1',
        'first_name': "Janith",
        'last_name': "Dilshan",
        'email': "dilshan@gmail.com"
    },
    {
        "id": '2',
        "first_name": "Anutha",
        "last_name": "Rathnayake",
        "email": "anuka@gmail.com"
    },
    {
        "id": '3',
        "first_name": "Ann",
        "last_name": "Perera",
        "email": "ann@gmail.com"
    }

    ]
    
    employee_id = event['queryStringParameters']['id']
    
    response = {}
    response['statusCode'] = 200
    response['headers'] = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,GET'
    }
    
    for employee in employees_list:
        if employee['id'] == employee_id:
            response['body'] = json.dumps(employee)
            return response
    
    response['body'] = json.dumps("Employee Not Found")
    return response        
   

