import requests


# create a lipa_na_mpesa stk push function
def lipa_na_mpesa(api_url, accessToken, businessShortCode, decoded_password, formatted_time, phonenumber, amount):

    headers = {"Authorization": "Bearer %s" % accessToken}

    request = {
        "BusinessShortCode": businessShortCode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phonenumber,
        "PartyB": businessShortCode,
        "PhoneNumber": phonenumber,
        "CallBackURL": "https://fullstack.com/lipa",
        "AccountReference": "ribiro1234",
        "TransactionDesc": " paying school fees"
    }

    response = requests.post(api_url, json = request, headers=headers)

    return response.text


# lipa_na_mpesa()