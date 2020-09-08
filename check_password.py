import requests
import hashlib
import argparse


def check_password(password: bytes):
    url = "https://api.pwnedpasswords.com/range/"
    hash_object = hashlib.sha1(password)
    hex_dig = hash_object.hexdigest().upper()

    prefix = hex_dig[0:5]
    suffix = hex_dig[5:]

    response = requests.get(f"{url}{prefix}")

    for item in response.iter_lines():
        if item.decode("utf-8")[0:35] == suffix:
            return True
    return False


password = input("Password: ")

if check_password(password.encode()):
    print("Your password has been found")
else:
    print("Your password has not been found")
