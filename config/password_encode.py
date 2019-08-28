import base64


def generate_password(formatted_time, businessShortCode, lipa_na_mpesa_passkey):
    # timestamp is a combinationn of shortcode+passkey+time
    timestamp = businessShortCode + lipa_na_mpesa_passkey + formatted_time

    # encode to base64
    encode_password = base64.b64encode(timestamp.encode())

    # the result is in binary format but we need it as a string
    decoded_password = encode_password.decode('utf-8')
    print(decoded_password)

    return decoded_password

