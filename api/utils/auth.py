import jwt
import datetime
import os

PUBLIC_KEY ="""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAycQH1KXOJk1+gO3hMHyq
Fa0iLT9aidPX63XGi5UZ8+5IkKrSgzzzkaZtg1XlBvvtyasukepOeDK7UTLMrPUB
4T52jvueCaSjH+9O/eu6cve1tgRozUrCxC1IE4Xj6eJCejHfsvbdIrXfMKwi05pJ
YoU4ZHhn+CIoKFVGkiB436VT/wKGssv6Ai/qSximSRn6g8WWCIMQcHhSg10DOjyz
Ct3PtwZBlodWQf/Y2Rs2bjwPGNDAN1Nc5EFgzNnzLeaIjr4PCSup5QDaPJNGqmQA
iJ8+l4W1UxmdfZlpSX7CtGxJOBYX80K7Uf38YOXl5E2ese8FfIc21Az/nMAg2YqH
GQIDAQAB
-----END PUBLIC KEY-----"""
    # Load private key

private_key = os.environ.get("PRIVATE_KEY")
if private_key is None:
    with open("private.pem","+rb") as f:
        private_key=f.read()    

    # Secret key (keep this secret!)
# secret_key = "your-secret-key"

    # Payload data
payload = {
    "user_id": 123,
    "username": "testuser",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30), # Expiration time
    }


def encode():
    # Encode JWT
    # encoded_jwt = jwt.encode(payload, secret_key, algorithm="HS256")
    encoded_jwt = jwt.encode(payload,private_key,algorithm="RS256")
    # print("Encoded JWT:", encoded_jwt)
    return encoded_jwt

def decode(encoded_jwt):
    # Decode JWT
    try:
        # decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=["HS256"])
        decode_jwt = jwt.decode(encoded_jwt,PUBLIC_KEY,algorithms="RS256")
        return 0 #"Decoded JWT"
    except jwt.ExpiredSignatureError:
        return 1 #"Token has expired"
    except jwt.InvalidTokenError:
        return 2  #"Invalid token"