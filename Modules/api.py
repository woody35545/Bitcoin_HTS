import os
import jwt
import uuid
import hashlib
from urllib.parse import urlencode
import requests

access_key = data.access_key
secret_key = data.secret_key
server_url = "https://api.upbit.com"
def get_statusCode(response):
    return response.status_code
def isStatusOK(statusCode):
    if 200 <= statusCode < 400:
        return True
    else:
        print("REQUEST FAILED!")
        return False
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
    get_statusCode(res)
    return res.json

def order_limitType(ticker,price,volume):
    # order_limitType("BTC-ETC","100000","0.00005")
    # Testing 필요
    query = {
        'market': ticker,
        'side': 'bid',
        'volume': volume,
        'price': price,
        'ord_type': 'limit',
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

    res = requests.post(server_url + "/v1/orders", params=query, headers=headers)
    return res.json()

def get_myBalance():
    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    get_statusCode(res)

    print(res.json())
    return res.json