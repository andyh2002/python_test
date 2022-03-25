from datetime import datetime
import requests


def show_time():
    dt = datetime.now()
    print(dt.strftime("今天是:%Y年%m月%d日 %H:%M:%S"))


def tianqi(city):
    # print(f"{city}晴天！")
    url = 'https://tianqiapi.com/api'
    d = {"appid": "56446388", "appsecret": "YVH4UmE2", "version": "v6", "city": city}
    res = requests.get(url, d)
    print(res.json())


def ai_talk(question):
    return question.replace('你', '我').replace('不', '').replace('吗', '').replace('?', '!').replace('？', '！')
