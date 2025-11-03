from cryptography.fernet import Fernet
import base64
import hashlib


def enc(text,bs):
    key = base64.urlsafe_b64encode(hashlib.sha256(bs).digest())
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode())
    return base64.urlsafe_b64encode(encrypted).decode()
name = input('PASSWORD:\n')
byte_string = "{}".format(name).encode()

text = input("\nTEXT:\n")
print(enc(text,byte_string))