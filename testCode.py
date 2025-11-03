import femboy73lib as f
# Try importing
try:
    from cryptography.fernet import Fernet
    import base64
    import hashlib
except:
    print(f'{f.Color.CYAN}Wait... Installing libs')
    import os
    os.system("pip install cryptography")
    os.system("pip install hashlib")
    os.system("cls")
    print(f"{f.Color.GREEN}Installed needed libs!")

# secret info
token = 'Z0FBQUFBQnBDTzI4aTVZTF93aUJJV0t6dU4tYmpvbWZvdi1yLVNXb0I2WU85LWVmbGNIN0s1dDVrRkEzZnowN1dXMlZaTnlIRE12eWxpcUVRYXc2bU5wTEhLVWVObUtaVWxrRnF2LXEwN0FwcjJwSmFrOTlLdF9NVGt4LWRoMmcyRzhGS2M1N3pyckk='
user_id = 'Z0FBQUFBQnBDTzNuRUN5ZmhLQ0wzQUtTZE5yWGE2RzRTazlpejA3c0Uzelh0MXBodm9IUTRSM1VRWGg4Mkxzb1BOaWx0T284N2l5YUFNUHBBWEhBTWd1SmJQaWhCb3c2MWc9PQ=='
# get pass
passw = 'password should be here (im using github to share between 2 pcs) so no peeking :3'
b = "{}".format(passw).encode()

def decode(text,b):
    key = base64.urlsafe_b64encode(hashlib.sha256(b).digest())
    fernet = Fernet(key)
    encrypted_data = base64.urlsafe_b64decode(text.encode())
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()

f.tg('text',decode(token,b),decode(user_id, b))
