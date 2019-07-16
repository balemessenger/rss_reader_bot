import json

import requests

from api.url import URL

from main_config import BotConfig


def is_admin(user_id, channel_user_name):
    data = {
        'group_id': str(channel_user_name),
        'user_id': str(user_id),
    }
    res = requests.post(URL.is_admin.format(BotConfig.token), data=data)
    text = res.text
    text = json.loads(text)
    print(text)
    if text.get('ok') and text.get('result'):
        return True
    else:
        return False
