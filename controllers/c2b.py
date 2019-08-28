import requests
from config.config import *
from flask import request, json
from models.Payments import C2bPayment


# registering our url
def c2b_register_url():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": shortcode,
        "ResponseType": "completed",
        "ConfirmationURL": confirm_url,
        "ValidationURL": validate_url
    }

    response = requests.post(api_url, json=request, headers=headers)

    print("urls successfully registered: ", response.text)


c2b_register_url()


# simulate transaction
def c2b_simulate_transaction():

    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "ShortCode": shortcode,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "1",
        "Msisdn": test_msisdn,  # the phonenumber that is sending the transaction format 2547xxxxxxx
        "BillRefNumber": "1234"
    }

    response = requests.post(api_url, json=request, headers=headers)

    print ("simulate message" + response.text)


c2b_simulate_transaction()


def validateC2B():
    data = request.get_json(force=True)
    # data_dict = dict(eval(json.dumps(data)))
    try:
        with open('ValidateResponse.json', 'a') as outfile:
            json.dump(data, outfile)
        print('validate', data)
    except:
        print('No data sent to validate')


def confirmC2B():
    data = request.get_json(force=True)
    data_dict = dict(eval(json.dumps(data)))
    # print(type(data_dict))
    print(data_dict)
    TransactionType = data_dict['TransactionType']
    TransID = data_dict['TransID']
    TransTime = data_dict['TransTime']
    TransAmount = data_dict['TransAmount']
    BusinessShortCode = data_dict['BusinessShortCode']
    BillRefNumber = data_dict['BillRefNumber']
    InvoiceNumber = data_dict['InvoiceNumber']
    ThirdPartyTransID = data_dict['ThirdPartyTransID']
    MSISDN = data_dict['MSISDN']
    FirstName = data_dict['FirstName']
    MiddleName = data_dict['MiddleName']
    LastName = data_dict['LastName']
    OrgAccountBalance = data_dict['OrgAccountBalance']

    print(TransID)

    try:
        with open('ConfirmResponse.json', 'a') as outfile:
            json.dump(data, outfile)
        print('confirmed', data)
        print(OrgAccountBalance)

        transaction = C2bPayment(TransactionType=TransactionType, TransID=TransID, TransTime=TransTime, TransAmount=TransAmount,
                                 BusinessShortCode=BusinessShortCode, BillRefNumber=BillRefNumber, InvoiceNumber=InvoiceNumber,
                                 ThirdPartyTransID=ThirdPartyTransID, MSISDN=MSISDN, FirstName=FirstName, MiddleName=MiddleName,
                                 LastName=LastName, OrgAccountBalance=OrgAccountBalance)

        new = transaction.insert_transactions()


    except:
        print('No data sent for confirmation')

