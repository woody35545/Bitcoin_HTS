import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests
import data
access_key = data.access_key
secret_key = data.secret_key
server_url = "https://api.upbit.com"

def get_MyOrderByUuid(input_uuid): # Query Parma: uuid
    query = {
        'uuid': input_uuid,
    }
    query_string = urlencode(query).encode()
    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/order", params=query, headers=headers)

    print(res.json())
    return res.json


#