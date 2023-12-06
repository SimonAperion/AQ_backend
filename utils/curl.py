# List of API URLs
import requests 
import json
api_endpoints = [
    '/api/change_mgmt',
]

# Set the base URL of your server
base_url = 'http://localhost:5000'  # Change this to your server's address

# Prepare the login data
login_data = {
    'email': 'super@aper.ion',
    'password': 'Aperion2023'
}

# Log in to get an access token
login_endpoint = '/login'
login_response = requests.post(base_url + login_endpoint, json=login_data)

if login_response.status_code == 200:
    access_token = login_response.json().get('access_token')

    # Prepare headers with the access token
    headers = {'Authorization': f'Bearer {access_token}'}
    data = json.dumps({'bewertung':"0"})
    for api_endpoint in api_endpoints:
        # Call each API endpoint
        api_response = requests.post(base_url + api_endpoint, headers=headers,json=json.loads(data))

        if api_response.status_code == 200:
            print(f"Data from {api_endpoint}:")
            print(api_response.json())
        else:
            print(f"Failed to call API endpoint {api_endpoint}: {api_response.status_code}")
else:
    print(f"Login failed: {login_response.status_code}")
