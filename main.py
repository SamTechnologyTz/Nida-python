import requests
import json

nida = "Your nida"
api_key = "Your api key"  # not important
token = "Your token"       # not important
account_id = "Your account id"

url = 'https://kabukukidigitali.xyz/nida/api/index.php'
headers = {
    'api-key': api_key,
    'token': token,
    'account_id': account_id
}
payload = {'nida': nida}

try:
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()  # Raises an error for bad HTTP responses
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
