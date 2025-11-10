# REQUIRED
import requests
import time

# COLORS
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BLACK = '\033[30m'
    RESET = '\033[0m'

# SEND MESSAGE IN TELEGRAM USING A BOT
def tg(message, bot_token, id):
    message = str(message)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": id,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print(Color.GREEN + message + Color.RESET)
    elif response.status_code == 429:
        print(Color.RED + message + Color.RESET)
    else:
        print(f'{Color.YELLOW}({response.status_code}){message}{Color.RESET}')
while True:
    tg('привет', '8349787366:AAGDSq7zv9arAHAD6m94tClWRHcoW-75NO0', '7988581841')
    time.sleep(0.75)
