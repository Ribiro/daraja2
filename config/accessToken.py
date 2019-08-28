import requests
from requests.auth import HTTPBasicAuth


def generate_access_token(url, consumerkey, consumersecret):
    consumer_key = consumerkey
    consumer_secret = consumersecret
    api_URL = url

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # get the json response
    json_response = r.json()

    accessToken = json_response['access_token']

    return accessToken


