from controllers import c2b,lipaNaMpesa
from config.config import *

# create tables in our database
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def home():
    return "Hello World"


@app.route('/validate/c2b', methods=['GET', 'POST'])
def validate_c2b():
    c2b.validateC2B()
    return make_response(jsonify({"ResultCode": 0, "ResultDesc": "Confirmation Received Successfully"}), 200)


@app.route('/confirm/c2b', methods=['GET', 'POST'])
def confirm_c2b():
    c2b.confirmC2B()
    return make_response(jsonify({"ResultCode": 0, "ResultDesc": "Confirmation Received Successfully"}), 200)


@app.route('/stk/<string:phone>/<string:amount>', methods=['GET', 'POST'])
def stk(phone, amount):
    r = lipaNaMpesa.lipa_na_mpesa(stk_url, access_token, businessShortCode, decoded_password, formatted_time, phone,
                                  amount)
    return r


# @app.route('/balance', methods=['GET', 'POST'])
# def balance():
#     print("hhhhhh")
#
#     data = request.get_json(force=True)
#     print(data)
#     return make_response(jsonify({"ResultCode": 0, "ResultDesc": "Confirmation Received Successfully"}), 200)
#
#
# @app.route('/timeout', methods=['POST', 'GET'])
# def tm():
#     data = request.get_json(force=True)
#     print(data)
#     return make_response(jsonify({"ResultCode": 0, "ResultDesc": "Confirmation Received Successfully"}), 200)


if __name__ == '__main__':
    app.run()
