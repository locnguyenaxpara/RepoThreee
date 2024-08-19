import jwt
import time
import sys
import requests

keyPath = sys.argv[1]

# Load your GitHub App's private key
with open(keyPath, 'r') as f:
    private_key = f.read()

payload = {
    # Issued at time
    'iat': int(time.time()),
    # JWT expiration time (10 minute maximum)
    'exp': int(time.time()) + 600,
    # GitHub App's identifier
    'iss': '973261'
}

# Generate JWT
jwt_token = jwt.encode(payload, private_key, algorithm='RS256')

# Set up the headers and the URL
headers = {
    'Authorization': f'Bearer {jwt_token}',
    'Accept': 'application/vnd.github+json'
}

installation_id = '53911291'  # Replace with your installation ID
url = f'https://api.github.com/app/installations/{installation_id}/access_tokens'

# Make the POST request to get the installation access token
response = requests.post(url, headers=headers)

# Check if the request was successful
if response.status_code == 201:
    installation_access_token = response.json()['token']
    print(installation_access_token)
else:
    print(f'Failed to get installation access token: {response.status_code}')
    print(response.text)
    exit(1)
