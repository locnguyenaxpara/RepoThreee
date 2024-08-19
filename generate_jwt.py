import jwt
import time
import sys

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
print(jwt_token)