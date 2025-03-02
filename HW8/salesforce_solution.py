import requests
import json
import configparser

config = configparser.ConfigParser()
config.read('salesforceconfig.ini')

grant_type = config.get('OAUTH', 'grant_type')
client_id = config.get('OAUTH', 'client_id')
client_secret = config.get('OAUTH', 'client_secret')
username = config.get('OAUTH', 'username')
password = config.get('OAUTH', 'password')
security_token = config.get('OAUTH', 'security_token')
base_url = config.get('OAUTH', 'base_url')

auth_url = f"{base_url}/services/oauth2/token"

payload = {
    'grant_type': grant_type,
    'client_id': client_id,
    'client_secret': client_secret,
    'username': username,
    'password': password + security_token
}

response = requests.post(auth_url, data=payload)
access_token = json.loads(response.text)['access_token']


api_url = f"{base_url}/services/data/v55.0/query/?q=SELECT+NAME+,+ID+,+BillingAddress+FROM+ACCOUNT"

headers = {
    'Authorization': 'Bearer ' + access_token
}


response = requests.get(api_url, headers=headers)
response.raise_for_status()
account_data = response.content

print(account_data)