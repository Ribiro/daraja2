from flask import Flask, jsonify, make_response, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import accessToken, password_encode, utils
from templates import *

# create an instance of class Flask called app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@127.0.0.1:5432/payments'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '3b4c830cd7d88c05cfa5d6da59af4561'

db = SQLAlchemy(app)
CORS(app)



businessShortCode = "174379"  # lipa na mpesa shortcode
lipa_na_mpesa_passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
consumerkey = "eVVILnKlFCWHhparue4MpGQScG8ojR9e"
consumersecret = "a41YxsDFSHP8IfPx"
shortcode = "600407"  # Shortcode 1
test_msisdn = "254708374149"
confirm_url = "http://aa4d92dc.ngrok.io/confirm/c2b"
validate_url = "http://aa4d92dc.ngrok.io/validate/c2b"
# balance_url  = "http://a37471aa.ngrok.io/balance"
# timeout_url = "http://a37471aa.ngrok.io/timeout"
security_credential = "blgtvyneIatln/HsrCzTchmt9fzHPZQVU2eGlQTLpVCPwkM6yWfg8pNLcHhB4nobtPl+Umtn2JUwbBC2RxDiX+CIBTjcbAUGPxTjNTbVzxQhnBKK/KL0j2QBRUEeQBKxIeMGxL95GTSw41nNiWL7iPCSDGBR4s0Vv+NVjcxK5OMAY/ipbaAg0/PqLNNr9X0fMwdUny1HidBcaajjupgj+0TGDPOdrD0ple8z+sEhAHG30kPbNWEM1EQ44FsjZdg11fZENsRYbpXNhesZVPQ9dX+hEQTq9J51ojuPwGc0BQjL/mC3hDhEfQvLZd8bJ0Z9cjmdkCAqmHD/5pLZnf/nGg=="

token_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
stk_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

access_token = accessToken.generate_access_token(token_url, consumerkey, consumersecret)
print("acess token: ", access_token)
formatted_time = utils.get_timestamp()
decoded_password = password_encode.generate_password(formatted_time, businessShortCode, lipa_na_mpesa_passkey)







