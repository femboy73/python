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
token = 'Z0FBQUFBQnBDTDd2VnRnUENFVEJRY2ItRk52dFY1cEdtZXNrUGJIZkhlSlZJNzRnbGozcEtWUjJwOF9pdUh0ZGZ2OGJTTkJRcHF0NUdRYTVHYmZFaW9FWGVTTmQ2QnhickVFd1p1bFU4cnlIOHgzT0N0cHZvcXVXcjh3X0hoRlAtaGZic196T3kxMEM='
user_id = 'Z0FBQUFBQnBDTDhLaGZPZEZrWEd1M2RwUTYzZWxiOGdnX19PLThLdlZ6cUEzMW1ZQzFNSzVpMms4Y1daOXVyNlg3cFlTMHVYQ0VkZFhhTmNlMDVzb195UDdmTzRyX0RyQ3c9PQ=='
# get pass
passw = 'secret password here (this isnt the actual password btw)'
b = "{}".format(passw).encode()

def decode(text,b):
    key = base64.urlsafe_b64encode(hashlib.sha256(b).digest())
    fernet = Fernet(key)
    encrypted_data = base64.urlsafe_b64decode(text.encode())
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data.decode()

f.tg('text',decode(token,b),decode(user_id, b))