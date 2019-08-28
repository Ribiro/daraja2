import requests
from config.config import *

from config.accessToken import access_token


def balance():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"

    headers = {"Authorization": "Bearer %s" % access_token}

    request = {"Initiator": "testapi",
               "SecurityCredential": security_credential,
               "CommandID": "AccountBalance",
               "PartyA": shortcode,
               "IdentifierType": "4",
               "Remarks": "this is my remark",
               # "QueueTimeOutURL": keys.timeout_url,
               # "ResultURL": keys.balance_url
               }

    response = requests.post(api_url, json=request, headers=headers)
    # data = request.get_json(force=True)
    print("This is the balance response: ", response.text)


print(balance())